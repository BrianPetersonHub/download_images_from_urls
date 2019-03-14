
"""
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
htpp://foobar.org/foobar.jpg
.
.
.

"""

import requests
import sys
import os

# check there are 3 arguments
if len(sys.argv) != 4:
    raise TypeError(os.path.basename(__file__) + ' take 3 arguments but ' + str(len(sys.argv) - 1) + ' given')

# parse arugments
input_file = sys.argv[1]
output_dir = sys.argv[2]
image_prefix = sys.argv[3]


with open(input_file, 'r') as datafile:
    count = 0
    for url in datafile:
        if url.strip()[-4:] == '.jpg':
            photoname = output_dir + '/' \
                + image_prefix \
                     + '_' \
                + str(count) \
                     + '.jpg'

            # if it takes too long to get a response
            # or the website is invalid
            # skip this image
            try:
                print(url)
                with open(photoname, 'wb') as f:
                    response = requests.get(url)
                    if response.status_code == 200:
                        f.write(response.content)
                        count += 1
            except:
                pass
