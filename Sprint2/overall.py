# Pulled from https://github.com/mykhailo-mostipan/shadow-removal
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
import os.path


def folder_selection():
	root = tk.Tk()
	root.withdraw()
	folder_path = filedialog.askdirectory()

	return folder_path

def file_selection():
	ftypes = [
	('JPG image files', '*.jpg'),
	('PNG image files', '*.png'),
	('TIF image files', '*.TIF')
	]
	root = tk.Tk()
	root.withdraw()
	file_list = filedialog.askopenfiles(filetypes=ftypes)

	return file_list

def ycbcr_removal(or_img):

	# Pulled from https://github.com/mykhailo-mostipan/shadow-removal

	# read an image with shadow...
	# and it converts to BGR color space automatically
	# or_img = cv2.imread('test3.jpg')

	# covert the BGR image to an YCbCr image
	y_cb_cr_img = cv2.cvtColor(or_img, cv2.COLOR_BGR2YCrCb)

	# copy the image to create a binary mask later
	binary_mask = np.copy(y_cb_cr_img)

	# get mean value of the pixels in Y plane
	y_mean = np.mean(cv2.split(y_cb_cr_img)[0])

	# get standard deviation of channel in Y plane
	y_std = np.std(cv2.split(y_cb_cr_img)[0])

	# classify pixels as shadow and non-shadow pixels
	for i in range(y_cb_cr_img.shape[0]):
	    for j in range(y_cb_cr_img.shape[1]):

	        if y_cb_cr_img[i, j, 0] < y_mean - (y_std / 3):
	            # paint it white (shadow)
	            binary_mask[i, j] = [255, 255, 255]
	        else:
	            # paint it black (non-shadow)
	            binary_mask[i, j] = [0, 0, 0]

	# Using morphological operation
	# The misclassified pixels are
	# removed using dilation followed by erosion.
	kernel = np.ones((3, 3), np.uint8)
	erosion = cv2.erode(binary_mask, kernel, iterations=1)

	# sum of pixel intensities in the lit areas
	spi_la = 0

	# sum of pixel intensities in the shadow
	spi_s = 0

	# number of pixels in the lit areas
	n_la = 0

	# number of pixels in the shadow
	n_s = 0

	# get sum of pixel intensities in the lit areas
	# and sum of pixel intensities in the shadow
	for i in range(y_cb_cr_img.shape[0]):
	    for j in range(y_cb_cr_img.shape[1]):
	        if erosion[i, j, 0] == 0 and erosion[i, j, 1] == 0 and erosion[i, j, 2] == 0:
	            spi_la = spi_la + y_cb_cr_img[i, j, 0]
	            n_la += 1
	        else:
	            spi_s = spi_s + y_cb_cr_img[i, j, 0]
	            n_s += 1

	# get the average pixel intensities in the lit areas
	average_ld = spi_la / n_la

	# get the average pixel intensities in the shadow
	average_le = spi_s / n_s

	# difference of the pixel intensities in the shadow and lit areas
	i_diff = average_ld - average_le

	# get the ratio between average shadow pixels and average lit pixels
	ratio_as_al = average_ld / average_le

	# added these difference
	for i in range(y_cb_cr_img.shape[0]):
	    for j in range(y_cb_cr_img.shape[1]):
	        if erosion[i, j, 0] == 255 and erosion[i, j, 1] == 255 and erosion[i, j, 2] == 255:

	            y_cb_cr_img[i, j] = [y_cb_cr_img[i, j, 0] + i_diff, y_cb_cr_img[i, j, 1] + ratio_as_al,
	                                 y_cb_cr_img[i, j, 2] + ratio_as_al]

	# covert the YCbCr image to the BGR image
	final_image = cv2.cvtColor(y_cb_cr_img, cv2.COLOR_YCR_CB2BGR)

	#cv2.imshow("im1", or_img)
	#cv2.imshow("im2", final_image)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	return binary_mask, final_image

def multispectral_algorithm(image_list):

	# Possibly need to first align multiple photos as slight variation exists

	# Open and load image into file
	red_original = cv2.imread(image.name)
	nir_original = cv2.imread(image.name)

	# Image A being RGB

	# Image B being NIR bands, they do not overlap perfectly, so this will cause issues
	# if evaluating pixel intensities directly assuming they overlap perfectly



	return binary_mask, final_image

def vari_plant(image):

	x_dim, y_dim = image.shape[:2]
	plant_health_image = np.zeros((x_dim, y_dim))
	result_image = np.zeros((x_dim, y_dim))

	max_vari = 0
	min_vari = 0
	vari_list = []

	for x in range(0, x_dim):
		for y in range(0, y_dim):
			# Visible Atmospherically Resistant Index = (Green - Red) / (Green + Red - Blue)
			color = image[x, y]
			b = int(color[0])
			g = int(color[1])
			r = int(color[2])
			if ((g+r-b) <= 0):
				vari = 0
			elif ((g-r) < 0):
				vari = 0
			else:
				vari = (g-r)/(g+r-b)
			if vari > max_vari:
				max_vari = vari
			if vari < min_vari:
				min_vari = vari
			vari_list.append(vari)
			plant_health_image[x, y] = vari

	print(max_vari)
	print(min_vari)

	cv2.imshow("VARI Plant Health Index", plant_health_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# Normalize image to 0,1 or 0, 255 for display
	norm_plant_health_image = plant_health_image
	for x in range(0, x_dim):
		for y in range(0, y_dim):
			norm_plant_health_image[x, y] = 255*((norm_plant_health_image[x, y] - min_vari)/(max_vari - min_vari))

	cv2.imshow("Normalized VARI Plant Health Index", norm_plant_health_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return norm_plant_health_image

def ndvi_plant(red_image, nir_image):

	# Need to ensure images are the same size and are aligned as the index is done on a per pixel basis blindly

	x_dim, y_dim = red_image.shape[:2]
	plant_health_image = np.zeros((x_dim, y_dim))
	result_image = np.zeros((x_dim, y_dim))

	max_ndvi = 0
	min_ndvi = 100
	ndvi_list = []

	for x in range(0, x_dim):
		for y in range(0, y_dim):
			# Normalized Difference Vegetation Index = (NIR - Red) / (NIR + Red)
			red = int(red_image[x, y][1])
			nir = int(nir_image[x, y][1])
			ndvi = (nir-red)/(nir+red)
			if ndvi > max_ndvi:
				max_ndvi = ndvi
			if ndvi < min_ndvi:
				min_ndvi = ndvi
			ndvi_list.append(ndvi)
			plant_health_image[x, y] = ndvi

	cv2.imshow("NDVI Plant Health Index", plant_health_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# Normalize image
	norm_plant_health_image = plant_health_image
	for x in range(0, x_dim):
		for y in range(0, y_dim): 
			# use max_ndvi and min_ndvi to normalize between -1 and 1
			#norm_plant_health_image[x, y] = 2*((norm_plant_health_image[x, y] - min_ndvi)/(max_ndvi - min_ndvi))-1
			norm_plant_health_image[x, y] = ((norm_plant_health_image[x, y] - min_ndvi)/(max_ndvi - min_ndvi))

	cv2.imshow("Normalized NDVI Plant Health Index", norm_plant_health_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return norm_plant_health_image

def nir_coordination_function():

	# Call file selection function to get specific images
	rgb_file = file_selection()
	red_file = file_selection()
	nir_file = file_selection()
	for image in rgb_file:
		rgb_image = cv2.imread(image.name)
	for image in red_file:
		red_image = cv2.imread(image.name)
	for image in nir_file:
		nir_image = cv2.imread(image.name)

	cv2.imshow("RGB Image", rgb_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imshow("Red Image", red_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imshow("NIR Image", nir_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
		

	# # Select from list the proper bands - develop later for automatic image selection given a large folder of sets of images
	# 0510 is RGB
	# 0511 is Blue
	# 0512 is Green
	# 0513 is Red
	# 0514 is RedEdge
	# 0515 is NIR
	# for image in image_list:
	# 	if image.name contains 000...
	# 		rgb_image = image
	# 	if image.name contains 001...
	# 		red_image = image
	# 	if image.name contains 005...
	# 		nir_image = image

	# Process set of images in selected algorithm - to be developed
	# red_mask, red_processed, nir_mask, nir_processed = multispectral_algorithm(red_image, nir_image)

	# Save masks and processed images
	# cv2.imwrite('mask_'+os.path.basename(red_image.name), red_mask)
	# cv2.imwrite('mask_'+os.path.basename(nir_image.name), nir_mask)
	# cv2.imwrite('processed_'+os.path.basename(red_image.name), red_processed)
	# cv2.imwrite('processed_'+os.path.basename(nir_image.name), nir_processed)

	# Run and save plant health algorithm on original and de-shadowed images
	original_ph_image = ndvi_plant(red_image, nir_image)
	# improved_ph_image = ndvi_plant(red_processed, nir_processed)
	cv2.imwrite('ndvi_original_'+os.path.basename(rgb_file[0].name), original_ph_image)
	# cv2.imwrite('ph_processed_'+os.path.basename(rgb_image.name), improved_ph_image)

	# Create and save image showing differences
	# cv2.imwrite('ph_original_'+os.path.basename(rgb_image.name), original_ph_image-improved_ph_image)
	# need to correct this for negative

	return

def rgb_coordination_function():

	# Call file selection function to get list of images
	image_list = file_selection()

	# Process each of the images in selected algorithm - for RGB single based image
	for image in image_list:
		# Open and load image into file
		image_mat = cv2.imread(image.name)
		
		mask, processed = ycbcr_removal(image_mat)

		# Save masks and processed images
		cv2.imwrite('mask_'+os.path.basename(image.name), mask)
		cv2.imwrite('processed_'+os.path.basename(image.name), processed)

		# Run and save plant health algorithm on original and de-shadowed image
		original_ph_image = vari_plant(image_mat)
		improved_ph_image = vari_plant(processed)
		cv2.imwrite('ph_original_'+os.path.basename(image.name), original_ph_image)
		cv2.imwrite('ph_improved_'+os.path.basename(image.name), improved_ph_image)


		# Create and save image showing differences
		cv2.imwrite('ph_difference_'+os.path.basename(image.name), original_ph_image-improved_ph_image)
		# need to correct this for negative

	return

if __name__ == "__main__":


	# For RGB function, select a series of photos for sequential processing - performs shadow detection and elimination followed by VARI analysis on a per image basis
	rgb_coordination_function()

	# For NIR function, select the specific photos for the Red and then NIR image
	nir_coordination_function()

