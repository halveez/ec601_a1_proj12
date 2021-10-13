# EC601 Team 12 Project - Sprint 1
Zachary Halvorson, Boston University Fall 2021

## Product Mission, MVP Definition, and User Stories

As an agricultural manager (farmer, rancher, etc.), I want to improve the accuracy of my image-based plant health detection systems, by using additional algorithms to detect and remove shadows from acquired images before processing into plant health metrics.

The MVP will be defined as a program that effectively eliminates shadows from drone based aerial images (top down, minimal imaging angle) of crops, initially focusing on a specific crop such as maize, barley, or soybeans.

Some additional user stories include:

As a user, I need to upload or input images into this tool, and receive a set of output images with shadwos removed that can be used for additional processing.

As a user, I need to easily refine this program with manual or automatic thresholds to optimize the results for my specific use case (farm, region, crop, etc.).


## Reproduction of Open Source Products

### NAIP Cold Springs Fire

For Sprint 1, I attempted to reproduce the results in [[1]](#1), first by downloading the Cold Springs Fire data from the National Agriculture Imagery Program (NAIP) and following their guide to establishing a working environment in Python.

First, I needed to install Microsoft Visual C++ 14.0 tools. I then ran into some Python issues, and was advised to reinstall using Anacadona, additionally for troubleshooting Rasterio package installation.

Ran into some additional issues with Anaconda and gdal, rasterio, and rioaxxary installation, and was ultimately unable to follow the guide to completion. This will be revisited in future sprints to test their datasets.


### OpenDroneMap WebODM

Next, I set up OpenDroneMap's WebODM system, and downloaded some shared multi-spectral datasets from their user forums, and set out to extract some 3D models from these aerial images. Sourced from https://community.opendronemap.org/t/xmission-multispectral/7524. I first processed folders 01 and 03 separately, which consisted of a Green, Red, Red edge, NIR, and NDVI image for each position (5 bands). The data also included a 6th RGB image, however this was excluded as it was of different dimensions and WebODM failed processing when it was included.

![Image 1](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/textured_model_test1/original/XAG001_0037.JPG)

This was quite effective in demonstrating some multi-spectral image analysis, as using the WebODM interface, it was possible to analyze the combined scene and use some of their preset algorithms to determine "Plant Health", generally based on various values or red, green, and blue in order to characterize plant health.

![Image 2](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/textured_model_test1/capture1.PNG)
![Image 3](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/textured_model_test1/capture2.PNG)

I tested two sets of photos from this dataset, and included the first set of reports in this repository, under textured_model_test1. This folder includes PDF reports of the entire image set, and some rendered photos showing the Plant Health results, as well as a 3D object for interactive exploration.

### OS GitHub 

After forming teams, I focused more specifically on shadow detection and removal in single images, without requiring stitching of multiple images together to create 3D reconstructions from aerial shots. This was much faster to test and implement, and to do this, I tested the following programs to first reproduce their results and system, which I plan to later improve upon.

I continued using the same set of images from WebODM, but also tested separately a set of images provided by Ece Sureyya Birol, who is also working on this project, although not through the class. This set of images was acquired from a DJI FC330, and has accompanying GPS coordinates for each image. This would be helpful for 3D scene reconstructions, but is not used in more simple image colorspace processing algorithms.


#### [Near Real - Time Shadow Detection and Removal in Aerial Motion Imagery Application](https://github.com/ThomasWangWeiHong/Shadow-Detection-Algorithm-for-Aerial-and-Satellite-Images)


Rasterio installation issues, same as before in individual work. Need to troubleshoot for future testing.

#### [Shadow Detection and Removal Based on YCbCr Color Space](https://github.com/mykhailo-mostipan/shadow-removal)


![Test Image 1](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test1.JPG)
![Test Image 1 - Masks](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test1_mask.jpg)
![Test Image 1 - Output](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test1_output.jpg)


![Test Image 2](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test2.JPG)
![Test Image 2 - Masks](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test2_mask.jpg)
![Test Image 2 - Output](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test2_output.jpg)


![Test Image 3](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test3.JPG)
![Test Image 3 - Masks](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test3_mask.jpg)
![Test Image 3 - Output](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program2/test3_output.jpg)



#### [Shadow Removal from RGB Images](https://github.com/jvalhondo/Shadow_Removal/blob/master/Shadow_Removal_VA_jvr.m)

Testing 3 specific images from the farm house set, the results are as follows:

![Test Image 1](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test1input.jpg)
![Test Image 1 - Masks](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test1mask.jpg)
![Test Image 1 - Output](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test1output.jpg)


![Test Image 2](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test2input.jpg)
![Test Image 2 - Masks](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test2mask.jpg)
![Test Image 2 - Output](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test2output.jpg)


![Test Image 3](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test3input.jpg)
![Test Image 3 - Masks](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test3mask.jpg)
![Test Image 3 - Output](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint1/program3/test3output.jpg)



## Plan for Sprint 2:

I will continue testing the Python and MATLAB programs in parallel on the same image sets for comparison, and will switch to a drone based series of aerial crop images for more specific testing and refinement of the models.

I'll also incorporate an open source plant health tool for post-processing instead of WebODM, as this relies on first stitching together a series of images before processing, and is not relevant for single image analysis.

Two simple options are NDVI and VARI:

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

Visible Atmospherically Resistant Index = (Green - Red) / (Green + Red - Blue)

Upon completition of Sprint 2, a user will be able to upload or input an image, and will receive a de-shadowed image, as well as plant health metrics on that image compared to the original image with shadows.


## References

<a id="1">[1]</a> 
Earth Lab. (2018, April 14). Introduction to multispectral remote sensing data in Python.
Earth Data Science. Retrieved September 17, 2021
https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/
