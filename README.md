# README
This repository contains scripts and notebooks demoing some tools for atmospheric muon flux simulation for numerical weather prediction. The requirements for running these materials are:

- MCEq: https://github.com/mceq-project/MCEq
- Pandas (for pickle file management): https://pandas.pydata.org/
- numpy/scipy (I think any version will do. We're not doing anything too fancy)
- geopy (for calculating distances): https://geopy.readthedocs.io/en/stable/

## musim_demo.ipynb
This notebook demonstrates how to use MCEq to calculate the atmospheric muon flux under various atmospheric conditions, including how to feed it atmospheric density information from an external file. You will need to download one additional file (that was too large to store on github) and place it in this directory prior to running this notebook. The file (`reduced_prior_00001.pkl`) is an example file containing the density field information for one of our TC Freddy ensemble members and can be found on a google drive [here](https://drive.google.com/drive/folders/1QqqeUvInxiVASqWUYmnAB5hPwBP9x654?usp=sharing).

## compute_mass_densities.py
This file interprets the netCDF files that are output by Joseph's WRF simulations, reducing them down to just the relevant variables (pressure, temperature, location, density) and writing this information out to a pkl file. As part of this tutorial, this script doesn't really do anything (as it requires an input netCDF file to interpret, which is not included here), butt it will be needed to tie muon simulations to the data assimilation framework. 

