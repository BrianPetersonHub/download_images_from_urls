# download_images_from_urls


this script downloads JPG images from a URLs.

This script takes 3 arguments:
    [1] the file location of the dataset of urls
    [2] the directory you want to save the images to
    [3] the "class" of the images - used for naming the images


To run:

python download_images_from_urls.py ./input_file ./output_dir class_name

Ex. to download dog images:

python download_images_from_urls.py ./dog_urls.txt ./rawImages/main_dog dog 

input data should be a text file of URLs seperated by newlines as seen below:

	https://foo.com/bar/foo.jpg
	http://bar.org/foo/bar.jpg
	https://foobar.org/foobar.jpg
	.
	.
	.
