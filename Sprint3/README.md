# EC601 Team 12 Project - Sprint 3
Zachary Halvorson, Boston University Fall 2021


## Sprint 3 Results

Implemented a shadow detection and elimination method that utilizes the multispectral data.

Automated batch testing for additional sets of images from provided dataset


## Multispectral Shadow Removal Results

### [Based on Shadow Detection on Multispectral Images Thesis by Hazan Sevim](https://etd.lib.metu.edu.tr/upload/12619166/index.pdf)

Chapter 4 describes various methods, including Polidorio’s difference, and an enhanced ratio between the saturation and intensity values. Other methods are based on Hue and Intensity, as shadow regions compared to non-shadow regions are generally of a higher hue. This varies between bands of multipsectral images, so there are many options to choose from for implementation.

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

Ratiomap = Saturation - Intensity / Saturation + Intensity

Ratiomap(HSI) = Hue + Intensity / Intensity + 1

Ratiomap(HCV) = Hue + 1 / Value + 1

Otsu's method is often used for automatic thresholding based on the ratiomaps and comparisons between images in order to create a shadow mask.


## Sprint 3 Plant Health Results

### Collage GIF
![CollageGIF](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0741.TIF.jpg)
Original: Red, NIR, NDVI
De-shadowed: Red, NIR, NDVI

### Example NDVI Image:
![NDVI](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint3/ndvi_23.jpg)

### Example De-shadowed NDVI Image:
![De-shadowedNDVI](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint3/deshadowed_ndvi_23.jpg)


## Sprint 4 Plans:

Compare multiple multispectral methods for shadow detection through batch processing, select one for final sprint.

Determine if image alignment pre-processing step is necessary as the multispectral images do not overlap perfectly.

