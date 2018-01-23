# post-it
a clumsily-written program to pixelize photographs. uses [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to determine the most common color from image regions and pixelizes image based on this information.


<img src="sunset-original.jpg?raw=true" width="400">  <img src="sunset-final.jpg?raw=true" width="400">

## user's guide
This program works best with simple images that are often already cartoonized or reduced to 3 or 4 colors, like [this one](https://upload.wikimedia.org/wikipedia/en/5/55/Barack_Obama_Hope_poster.jpg), so don't get too salty if it doesn't work with your huge landscape.

Also, it's really freaking slow right now, so don't get impatient. There's a lot going on behind the scenes (and I have no idea how to optimize anything).

1. install [python 2.7](https://www.python.org/download/releases/2.7/), [pillow](http://pillow.readthedocs.io/en/latest/installation.html), and [numpy and scipy](https://datahub.packtpub.com/tutorials/installing-numpy-scipy-matplotlib-ipython/).
2. download or clone this repository.
3. put the image you want to convert in the repository folder.
4. open pixelize.py, edit the img_src variable, and run the program.
5. complain when it doesn't work because i'm incompetent.

## to do
1. compare color of box to predefined post it note colors and change the box to that color
2. provide the user with a way to see how many post it notes they're gonna need (and also halt the program if they don't want to put 8112 post its up on the window)

## special thanks
* to [this](https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image) github contributor for implementing k-means clustering in a way I could use, because I'm probably never going to understand how this works.
* to macgregor d entry for inspiring a more intense post it note window drawing
