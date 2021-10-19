# EC601 Team 12 Project - Sprint 2
Zachary Halvorson, Boston University Fall 2021


## Plan for Sprint 2:

I will continue testing the Python and MATLAB programs in parallel on the same image sets for comparison, and will switch to a drone based series of aerial crop images for more specific testing and refinement of the models.

I'll also incorporate an open source plant health tool for post-processing instead of WebODM, as this relies on first stitching together a series of images before processing, and is not relevant for single image analysis.

Two simple options are NDVI and VARI:

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

Visible Atmospherically Resistant Index = (Green - Red) / (Green + Red - Blue)

Upon completition of Sprint 2, a user will be able to upload or input an image, and will receive a de-shadowed image, as well as plant health metrics on that image compared to the original image with shadows.


## [Shadow Detection and Removal Based on YCbCr Color Space](https://github.com/mykhailo-mostipan/shadow-removal)


## [Shadow Removal from RGB Images](https://github.com/jvalhondo/Shadow_Removal/blob/master/Shadow_Removal_VA_jvr.m)


## References

<a id="1">[1]</a> 
Earth Lab. (2018, April 14). Introduction to multispectral remote sensing data in Python.
Earth Data Science. Retrieved September 17, 2021
https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/
