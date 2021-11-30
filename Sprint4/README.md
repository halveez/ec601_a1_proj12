# EC601 Team 12 Project - Sprint 4
Zachary Halvorson, Boston University Fall 2021


## Sprint 4 TO-DO / Results

Compare multiple multispectral methods for shadow detection and REMOVAL through batch processing, select one for final sprint.

Implement image alignment pre-processing step is necessary as the multispectral images do not overlap perfectly.


## Multispectral Shadow Removal Results

### [Based on Shadow Detection on Multispectral Images Thesis by Hazan Sevim](https://etd.lib.metu.edu.tr/upload/12619166/index.pdf)

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

For the final sprint, the program utilizes the following for the shadow detection method:

CODE

And an accompanying shadow removal method based on the mask:

CODE

## Sprint 4 Plant Health Results

### Collage GIF
![]()

Original: Red, NIR, NDVI

De-shadowed: Red, NIR, NDVI

### Example NDVI Image:
![]()

### Example De-shadowed NDVI Image:
![]()


## Final Plans:

Documentation on GitHub, modularize the overall program, 