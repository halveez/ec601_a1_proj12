# EC601 Team Project - Sprint 1
Zachary Halvorson, Boston University Fall 2021

Items to cover:
Define your product mission
Comprehensive literature review (build on project 1)
Define MVP and MVP user stories
Technologies to evaluate and reason for choosing them
Setup of development environment


## Reproduction of OS Results

### NAIP Cold Springs Fire

For Sprint 1, I attempted to reproduce the results in [[1]](#1), first by downloading the Cold Springs Fire data from the NAIP and following their guide to establishing a working environment in Python.

First, I needed to install Microsoft Visual C++ 14.0 tools. I then ran into some Python issues, and was advised to reinstall using Anacadona, additionally for troubleshooting Rasterio package installation.

Ran into some additional issues with Anaconda and gdal, rasterio, and rioaxxary installation, and was ultimately unable to follow the guide to completion.


### OpenDroneMap WebODM

Instead, I set up OpenDroneMap's WebODM system, and downloaded some shared multi-spectral datasets from their user forums, and set out to extract some 3D models from these aerial images. Sourced from https://community.opendronemap.org/t/xmission-multispectral/7524. I first processed folders 01 and 03 separately, which consisted of a Green, Red, Red edge, NIR, and NDVI image for each position (5 bands). The data also included a 6th RGB image, however this was excluded as it was of different dimensions and WebODM failed processing when it was included.

This was quite effective in demonstrating some multi-spectral image analysis, as using the WebODM interface, it was possible to analyze the combined scene and use some of their preset algorithms to determine "Plant Health", generally based on various values or red, green, and blue in order to characterize plant health.

I tested two sets of photos from this dataset, and included the first set of reports in this repository, under textured_model_test1. This folder includes PDF reports of the entire image set, and some rendered photos showing the Plant Health results, as well as a 3D object for interactive exploration.

### OS GitHub 

After forming teams, I focused more specifically on shadow detection and removal in single images, without requiring stitching of multiple images together to create 3D reconstructions from aerial shots. This was much faster to test and attempt to implement, and to do this, I tested a set from the following list of GitHub links to first reproduce their results and system, which I plan to later improve upon:

https://github.com/ThomasWangWeiHong/Shadow-Detection-Algorithm-for-Aerial-and-Satellite-Images
https://github.com/tsingqguo/exposure-fusion-shadow-removal
https://github.com/mykhailo-mostipan/shadow-removal
https://github.com/jvalhondo/Shadow_Removal/blob/master/Shadow_Removal_VA_jvr.m
https://github.com/kittenish/Image-Shadow-Detection-and-Removal
https://github.com/ceciliavision/perceptual-reflection-removal#conda-environment

Describe images used here - from who and what study group

Describe Drone image acquisition next - camera specifics, etc.

Describe specific links from above that were tested - pipeline, pre-processing, etc.

Before and after results

Next steps

Plan for Sprint 2:

Definition of architecture
Technology Selection and justification
Functional demonstration of major user story



## References

<a id="1">[1]</a> 
Earth Lab. (2018, April 14). Introduction to multispectral remote sensing data in Python.
Earth Data Science. Retrieved September 17, 2021
https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/
