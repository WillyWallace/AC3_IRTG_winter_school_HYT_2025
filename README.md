<a name="top"></a>

<!--[![Python package](https://github.com/remsens-lim/pyMakeRetrieval/actions/workflows/python-package.yml/badge.svg)](https://github.com/remsens-lim/pyMakeRetrieval/actions/workflows/python-package.yml) -->
<!--[![Pylint](https://github.com/remsens-lim/pyMakeRetrieval/actions/workflows/pylint.yml/badge.svg)](https://github.com/remsens-lim/pyMakeRetrieval/actions/workflows/pylint.yml) -->
<!--[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10014291.svg)](https://doi.org/10.5281/zenodo.10014291) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://github.com/WillyWallace/winter_school_HYT_2025/releases/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/WillyWallace/winter_school_HYT_2025/graphs/commit-activity)
![Mastodon Follow](https://img.shields.io/mastodon/follow/109461236453474330?domain=https%3A%2F%2Fmeteo.social&logoColor=%230066cc&style=social)

# Winter school in Hyytälä 2025 - Seminar on the application of the Virga Sniffer

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Introduction">Introduction</a></li>
    <!-- <li><a href="#Installation">Installation</a></li>    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#roadmap">Program</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Introduction

The Virga-Sniffer is a tool to detect virga (precipitation which completely evaporates before reaching the surface). As input source radar reflectivity and ceilometer cloud-base height observations are mandatory. Optionally but highly recommended are the additional information of radar mean Doppler velocity, lifting condensation level and surface rain detection.

Virga sniffer documentation: https://virga-sniffer.readthedocs.io/en/latest/index.html

Virga sniffer code on github: https://github.com/remsens-lim/virga_sniffer/tree/main

Virga sniffer paper: https://amt.copernicus.org/articles/16/1683/2023/amt-16-1683-2023.html

<!-- USAGE -->
## Usage

Just go through the ipython notebook 'apply_virga-sniffer.ipynb' and follow the instructions

<!-- Program -->
## Program

### Working group 1:
Lead by Andreas Foth, Leipzig Institute for Meteorology, Leipzig University, Leipzig Germany
### Title:
„Application of the Virga-Sniffer tool for the detection of virga based on ground-based remote sensing data”

### Audience:
PhD students with an interest in ground-based remote sensing (5–8 participants). **Basic python skills are required.**

### Focus:
The Virga-Sniffer is a tool for detecting virga from ground-based remote sensing measurements. In the simplest approach, it detects virga from time–height fields of cloud radar reflectivity and time series of ceilometer cloud base height. In addition, optional parameters like lifting condensation level, a surface rain flag, and time-height fields of cloud radar mean Doppler velocity can be added to refine virga event identifications. The Virga-Sniffer Python package is highly modular and configurable and can be applied to multilayer cloud situations. It is therefore to be expected that different users will come to slightly different results, which is probably due to different settings. In this work program, the variability of the results is to be estimated.

### Goal:
The goal is for each participant to apply the virga sniffer tool to one week of the given datasets from Hyytiälä provided by the Cloudnet data portal, and produces statistical results about geometrical cloud and virga properties as well as statistics about classified targets from the Cloudnet target classification within detected virga. We will create a synopsis of the statistical results of each participant to determine the variability between the participants and to finally estimate a quantification of uncertainty of the Virga-Sniffer output.

### Preliminary schedule:

|          |   Mon             |   Tue           | Wed             |  Thu           |  Fri            |
+:--------:+:-----------------:+:---------------:+:---------------:+:--------------:+:---------------:+
| 12:00    | Introduction to   | Data analysis & | Data analysis & | Statistical    | Presentation of |
| --       | the Virga-        | processing      | processing      | analysis over  | single results  |
| 13:30    | Sniffer tool      |                 |                 | single results | and discussions |
+:--------:+:-----------------:+:---------------:+:---------------:+:--------------:+:---------------:+
| 15:30    | Installation of   | Data analysis & | Data analysis & | Preparing      | Presentation of |
| --       | the Virga-Sniffer | processing      | processing      | presentations  | single results  |
| 16:30    | python package    |                 |                 |                | and discussions |
+:--------:+:-----------------:+:---------------:+:---------------:+:--------------:+:---------------:+
| 18:00    | Data              | Data analysis & | Discussing and  | Wrap up &      | Presentation of |
| --       | familiarization   | processing      | interpreting the| feedback       | single results  |
| EOD      | & Q&A             |                 | single results  |                | and discussions |


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p text-align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

[Andreas Foth](https://www.uni-leipzig.de/personenprofil/mitarbeiter/dr-andreas-foth)


<p text-align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Special thanks for templates and help during implementation.

* [Readme Template](https://github.com/othneildrew/Best-README-Template)
* [remsens-lim](https://github.com/remsens-lim/virga_sniffer)

<p text-align="right">(<a href="#top">back to top</a>)</p>

