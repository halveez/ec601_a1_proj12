# EC601 Team 12 Project - Sprint 4
Zachary Halvorson, Boston University Fall 2021


## Sprint 4 Results

Compared multispectral methods for shadow detection and removal through batch processing, selecting one for final sprint.

Implemented image alignment pre-processing step as the multispectral images do not overlap perfectly.

## [Image Alignment Methods](https://github.com/khufkens/align_images)

The script includes the following methods, with different capabilities for each:
FFT phase correlation
Enhanced Correlation Coefficient (ECC) maximization
Feature based registration

The images include offsets in both the x and y axis, as well as minimal rotations.

## Multispectral Shadow Removal Results

### [Based on Shadow Detection on Multispectral Images Thesis by Hazan Sevim](https://etd.lib.metu.edu.tr/upload/12619166/index.pdf)

Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)

For the final sprint, the program utilizes the following for the shadow detection method:

	# Create composition image of R,G,B and R,G,NIR
	rgb_composed = cv2.merge([red_vals, green_vals, blue_vals])
	rgnir_composed = cv2.merge([red_vals, green_vals, nir_vals])

	# Convert to HSV
	rgb_hsv = cv2.cvtColor(rgb_composed, cv2.COLOR_RGB2HSV)
	rgnir_hsv = cv2.cvtColor(rgnir_composed, cv2.COLOR_RGB2HSV)
	
	# Ratiomap = (Sat - Val) / (Sat + Val)
	ratiomap_image[x, y] = abs((rgnir_hsv[x,y,1] - rgnir_hsv[x,y,2]) / (rgnir_hsv[x,y,1] + rgnir_hsv[x,y,2]))

	# Thresholding for mask creation
	ratiomap_blurred = cv2.blur(ratiomap_image, (5, 5))
	ret, r_difference_mask = cv2.threshold(difference_gray_blurred, 127, 255, cv2.THRESH_BINARY)

And an accompanying shadow removal method based on the mask:

	# Adjust value here for shadow removal method
	adjustment = 50
	deshadowed_red_vals[x, y] = deshadowed_red_vals[x, y] + adjustment
	deshadowed_nir_vals[x, y] = deshadowed_nir_vals[x, y] + adjustment


## Sprint 4 Image Alignment Results

### Collage A GIF (500 iterations, 500 max features)
![A](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint4/alignment_testA.gif)

Row 1: Red Image, NIR Image
Row 2: Red Image, NIR Feature Aligned Image
Row 3: Red Image, NIR ECC Aligned Image

### Collage B GIF (5000 iterations, 5000 max features)
![B](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint4/alignment_testB.gif)

Row 1: Red Image, NIR Image
Row 2: Red Image, NIR Feature Aligned Image
Row 3: Red Image, NIR ECC Aligned Image

## Sprint 4 Shadow Removal Results

### Aligned Images:
![aligned](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint4/aligned.gif)

Row 1: Red, NIR, NDVI
Row 2: Red, NIR, NDVI

### Un-Aligned Images:
![unaligned](https://github.com/halveez/ec601_a1_proj12/blob/main/Sprint4/unaligned.gif)

Row 1: Red, NIR, NDVI
Row 2: Red, NIR, NDVI


## Final Plans and Next Steps:

Allow for multiple function selection and automated batch testing of selected algorithms for manual optimization (eventually perform mathematical comparisons on the images for automatic optimization).

Test with additional image datasets to validate and strengthen overall system.

Documentation on GitHub, modularize the overall program, installation and other instructions.