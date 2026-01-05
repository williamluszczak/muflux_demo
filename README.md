# README
This repository contains scripts and notebooks demoing some tools for atmospheric muon flux simulation for numerical weather prediction. The requirements for running these materials are:

- MCEq: https://github.com/mceq-project/MCEq
- Pandas (for pickle file management): https://pandas.pydata.org/
- numpy/scipy (I think any version will do. We're not doing anything too fancy)
- geopy (for calculating distances): https://geopy.readthedocs.io/en/stable/

## musim_demo.ipynb
This notebook demonstrates how to use MCEq to calculate the atmospheric muon flux under various atmospheric conditions, including how to feed it atmospheric density information from an external file.

## compute_mass_densities.py
This file interprets the netCDF files that are output by Joseph's WRF simulations, reducing them down to just the relevant variables (pressure, temperature, location, density) and writing this information out to a pkl file. While not strictly necessary for this tutorial, it will be needed to tie muon simulations to the data assimilation framework. 

