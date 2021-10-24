# EC601 Team 12 Project - Sprint 2
Zachary Halvorson, Boston University Fall 2021

## Sprint 2 Results:

User image selection pipeline, processing, displaying, and storing of results successfully implemented.
### RGB Image:
![RGB](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint2/DJI_0740.JPG)
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


NDVI and VARI both successfully implemented:

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

Visible Atmospherically Resistant Index = (Green - Red) / (Green + Red - Blue)

IMAGES HERE showing both methods

![VARI]()
![Normalized VARI]()
![NDVI]()
![Normalized NDVI]()


Upon completition of Sprint 2, a user will be able to upload or input an image, and will receive a de-shadowed image, as well as plant health metrics on that image compared to the original image with shadows.


### [Shadow Detection and Removal Based on YCbCr Color Space](https://github.com/mykhailo-mostipan/shadow-removal)

## Sprint 3 Plans:

Implement a shadow detection and elimination method that utilizes the multispectral data.

Determine if image alignment pre-processing step is necessary as the multispectral images do not overlap perfectly.

Create a more automatic pipeline for image selection based on file naming expectations for this specific dataset.

## References

<a id="1">[1]</a> 
Earth Lab. (2018, April 14). Introduction to multispectral remote sensing data in Python.
Earth Data Science. Retrieved September 17, 2021
https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/
