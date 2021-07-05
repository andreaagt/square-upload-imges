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

You need cloudinary credentials to upload the images


### Installing

You can install the libraries used by running:

    $ pipenv shell
    
    $ pipenv install -r requirements.txt

To square all the images in ./images run:

    $ python resize_images.py

To upload the new images created in ./new_images, you need to create a config.py with the cloudinary credentials as follow:

    config = { 
      "cloud_name" : "874837483274837", 
      "api_key" : "a676b67565c6767a6767d6767f676fe1",
      "api_secret" : "your api_secret"
    }

    $ python upload_img_for_cloudinary.py
