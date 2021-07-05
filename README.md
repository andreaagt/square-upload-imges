# square-upload-tool
Python scripts to square and upload the new images to cloudinary

## Getting Started

This code resize the images to fit in a square, it use the shorter side of the image.
It take all the images in ./images, this images are named in a enumerate way  as 'img1', 'img2' ...

The code to upload images in cloudinary, return a csv file of all urls of this images.
 
Python 3

### Prerequisites

python version 3.9.5
Version of the libraries are in Requirements.txt


### Installing

You can install the libraries used by running:

    $ pipenv shell
    
    $ pipenv install -r requirements.txt

To square all the images in ./images run:

    $ python resize_images.py

To upload the new images created in ./new_images

    $ python upload_img_for_cloudinary.py
