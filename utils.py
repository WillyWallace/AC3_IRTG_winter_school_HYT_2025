"""
utils.py
===============
Basic utility functions used for apply-virga-sniffer.ipynb
"""

from typing import Optional, Union, Tuple, Any

import xarray as xr
import numpy as np
import os
import requests
import pandas as pd
import datetime
import json
import glob


def download_cloudnet_categorize(date_start, date_end, paths):
    """
    download cloudnet categorize file for the given date range

    Parameters
    ----------
    date_start: datetime object (yyyy-mm-dd)
    date_end: datetime object (yyyy-mm-dd)
    paths: dict containing the path of the categorize file
    
    Returns
    -------

    """
    url = 'https://cloudnet.fmi.fi/api/files/'
    payload = {
        #'date': '2024-02-04',
        'dateFrom': date_start,
        'dateTo': date_end,
        'site': 'hyytiala',
        'product': 'categorize',
    }
    
    metadata = requests.get(url, payload).json()
    
    outpath = paths['categorize']
    
    for row in metadata:
        res = requests.get(row['downloadUrl'])
        filepath = os.path.join(outpath, row['filename'])
        with open(filepath, 'wb') as f:
            f.write(res.content)


def proc_categ(date, paths) -> xr.core.dataset.Dataset:
    """
    read cloudnet categorize file

    Parameters
    ----------
    date: datetime object (yyyy-mm-dd)
    path: dict containing the path of the categorize file
    
    Returns
    -------
    xarray.Dataset

    """
    year, month, day = date2filestring(date)
    
    categ_file = paths['categorize'] + year + month + day +'_hyytiala_categorize.nc'
    #print(categ_file)
    categ = xr.open_dataset(categ_file)

    if "Z" not in categ:
        raise Exception("categorize file missing 'Z' variable.")
    if "v" not in categ:
        raise Exception("categorize file missing 'v' variable.")
    if "rain_detected" not in categ:
        raise Exception("categorize file missing 'rain_detected' variable.")
    if "category_bits" not in categ:
        raise Exception("categorize file missing 'category_bits' variable.")
    if "time" not in categ:
        raise Exception("categorize file missing 'time' variable.")
    if "height" not in categ:
        raise Exception("categorize file missing 'height' variable.")
    
    return categ


def proc_class(date, paths) -> xr.core.dataset.Dataset:
    """
    read cloudnet classification file

    Parameters
    ----------
    date: datetime object (yyyy-mm-dd)
    path: dict containing the path of the categorize file
    
    Returns
    -------
    xarray.Dataset

    """
    year, month, day = date2filestring(date)
    
    class_file = paths['classification'] + year + month + day +'_hyytiala_classification.nc'
    #print(class_file)
    classi = xr.open_dataset(class_file)

    if "time" not in classi:
        raise Exception("classification file missing 'time' variable.")
    if "height" not in classi:
        raise Exception("classification file missing 'height' variable.")
    if "target_classification" not in classi:
        raise Exception("classification file missing 'target_classification' variable.")
        
    return classi


def date2filestring(date) -> Tuple[str, str, str]:
    """
    converts date (yyyy-mm-dd) into strings of year (yyyy), month (mm) and day (dd)

    Parameters
    ----------
    date: datetime object (yyyy-mm-dd)
    
    Returns
    -------
    str
        year string (yyyy)
    str
        month string (mm)
    str
        day string (dd)

    """
    
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date}. Expected format: YYYY-MM-DD")

    date = str(date)
    year = str(date.split('-')[0])
    month = str(date.split('-')[1])
    day = str(date.split('-')[2].split(' ')[0])
    
    return year, month, day


#def find_lowest_liquid_containing_layer_height(data):
#   mask = data["target_classification"].isin([1, 3, 5, 7])
#    return data["height"].where(mask).min(dim="height")


def find_lowest_liquid_containing_layer_height(data)-> xr.Dataset:
    """
    finds lowest height bin where liquid bit in 'category bits' is set 

    Parameters
    ----------
    data: xarray.Dataset
        cloudnet categorize data
    
    Returns
    -------
    xarray.Dataset

    """
    mask = isbit(data["category_bits"], 0)
    return data["height"].where(mask).min(dim="height")


def isbit(array: np.ndarray, nth_bit: int) -> np.ndarray:
    """Tests if nth bit (0,1,2,...) is set.

    Args:
        array: Integer array.
        nth_bit: Investigated bit.

    Returns:
        Boolean array denoting values where nth_bit is set.

    Raises:
        ValueError: negative bit as input.

    Examples:
        >>> isbit(4, 1)
            False
        >>> isbit(4, 2)
            True

    See Also:
        utils.setbit()

    """
    if nth_bit < 0:
        msg = "Negative bit number"
        raise ValueError(msg)
    mask = 1 << nth_bit
    return array & mask > 0

def prepare_and_save_config(name, config, paths) -> dict:
    """
    Prepare and save the config. Preparation means adding the name of the 
    investigator and converting the cbh_processing array into a string to 
    have it later easier in the dataframe.

    Parameters
    ----------
    name: string
    config: dict
    paths: dict
    
    Returns
    -------
    dict
    
    """
    keys = []
    for key in config:
        #print(key)
        if key != "cbh_processing":
            keys.append(key)            
    
    dict_config = {key: config[key] for key in keys if key in config}
    dict_config["cbh_processing"] =  str(config["cbh_processing"])
    dict_config['name'] = name

    # safe config file as json
    save_config_as_json(name, dict_config, paths)
    
    return dict_config


def save_config_as_json(name, config, paths):
    """
    save config as json

    Parameters
    ----------
    name: string
    config: dict
    paths: dict
    
    Returns
    -------
    
    """
    with open(f'{paths['data_collection']}{name}_config.json', 'w') as f:
        json.dump(config, f, indent=4)  # `indent=4` makes it human-readable


def load_json_config(file) -> dict:
    """
    load json containing the config

    Parameters
    ----------
    file: string
    
    Returns
    -------
    json
    
    """
    with open(file, 'r') as f:
        return json.load(f)


def load_all_json_configs(paths) -> list: 
    """
    loaf all json files with the configs

    Parameters
    ----------
    paths: dict
    
    Returns
    -------
    list
    
    """
    json_file_list = glob.glob(paths['data_collection'] + '*_config.json')
    #print(json_file)
    
    df_config_list = []
    for file in json_file_list:
        df_config_list.append(pd.DataFrame([load_json_config(file)]))
        
    return df_config_list
