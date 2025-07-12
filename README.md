# SAR ARD open source comparison
[![DOI](https://img.shields.io/badge/DOI-FAB70C.svg?style=for-the-badge&logo=DOI&logoColor=black)](https://www.mdpi.com/2072-4292/15/21/5110)

**Description**: Scripts for time series analysis of five Analysis Ready Data (ARD) synthetic aperture radar (SAR) products 

## 📢 Add this repo to [Google Earth Engine](https://code.earthengine.google.com/) 🌐 (GEE) 📢
To add the code repository 💾 directly to your GEE account, use the following 🔗: https://code.earthengine.google.com/?accept_repo=users/helenbluebaldwin/SAR_ARD_TimeSeries.

## Functions
i. Geocode RTC dataset produced by ISCE-2 (code from Simon Kraatz)

1. Generate samples 
- for CoV time series comparison
- for RMSE time series comparison
2. Compute CoV (on a monthly basis):
- for ISCE 2
- for GRD
- for GTC (Andreas Vollrath et al)
- for Gamma
- for SNAP 8
3. Compute RMSE, R2 (over forest land cover class):
- for Gamma to ISCE 2
- for Gamma to GRD
- for Gamma to GTC (Andreas Vollrath et al)
- for Gamma to SNAP 8
4. Create figures & calculate CoV ranges

## Citation

If this code is used in publications, presentations, or other venues, please cite 📝 the following:

Flores, A., Parache, H.B., Martin Arias, V., Jimenez, S., Herndon, K., Mehlich, S., Meyer, F., Agarwal, S., Ilushchenko, S., Agarwal, M., Puzzi Nicolau, A., Markert, A., Saah, D., Cherrington, E.A. 2023. Evaluating SAR Radiometric Terrain Correction Products: Analysis-Ready Data for Users. *Remote Sensing*, 15 (5110): 1-19. DOI: 128098. https://www.mdpi.com/2072-4292/15/21/5110
