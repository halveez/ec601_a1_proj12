# EC601 Team 12 Project - Sprint 2
Zachary Halvorson, Boston University Fall 2021

## Sprint 2 Results:

User image selection pipeline, processing, displaying, and storing of results successfully implemented.
### Blue Image:
![Blue](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0741.TIF.jpg)
### Green Image:
![Green](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0742.TIF.jpg)
### Red Image:
![Red](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0743.TIF.jpg)
### RedEdge Image:
![RedEdge](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0744.TIF.jpg)
### NIR Image:
![NIR](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0745.TIF.jpg)

## RGB Shadow Removal Results

### RGB Original
![RGB Original](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0740.JPG)
### RGB Mask
![RGB Mask](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/mask_DJI_0740.JPG)
### RGB De-Shadowed
![RGB De-Shadowed](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/processed_DJI_0740.JPG)

## Plant Health Results

NDVI and VARI both successfully implemented:

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

Visible Atmospherically Resistant Index = (Green - Red) / (Green + Red - Blue)

### VARI on RGB Original
![Original VARI](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/ph_original_DJI_0740.JPG)
### VARI on RGB De-Shadowed
![Deshadowed VARI](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/ph_improved_DJI_0740.JPG)
### Difference in VARI 
![Difference in VARI](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/ph_difference_DJI_0740.JPG)

### NDVI on Original Red and NIR
![Original NDVI](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/ndvi_original_DJI_0740_save.JPG)


## Sprint 3 Plans:

Implement a shadow detection and elimination method that utilizes the multispectral data.

Determine if image alignment pre-processing step is necessary as the multispectral images do not overlap perfectly.

Create a more automatic pipeline for image selection based on file naming expectations for this specific dataset.

### [Shadow Detection and Removal Based on YCbCr Color Space](https://github.com/mykhailo-mostipan/shadow-removal)