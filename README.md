# Radiative-trigger-thresholds-of-pigment-based-photoprotection
This repository provides Python codes to estimate the radiative trigger threshold for plant pigment photoprotection based on the chlorophyll ratio index (Rchl) and short-wave radiation (SWR) time series.   

Rchl data can be obtained based on the moderate resolution imaging spectroradiometer (MODIS) products following Wu et al 2021 (https://iopscience.iop.org/article/10.1088/1748-9326/abf3dc).  

SWR data can be aquired from the version 2.1 dataset of global land data assimilation system (GLDAS).  

Two examples are provided with input data included in "/datasample" and expected outputs included in "/fig". In the output figures, blue points denote SWR-Rchl scatters with binned Rchl and black lines show smoothed SWR-Rchl curves. In example "test1", an obvious pigment-based photoprotection can be observed from the parabolic relationship between SWR and Rchl variations, and the threshold is detected and marked with a red spot. In example "test2", no pigment-based photoprotection is found as Rchl increases with SWR linearly and thus the threshold is undetected.
