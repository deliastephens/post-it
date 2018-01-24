# post-it
a clumsily-written program to pixelize photographs. uses [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to determine the most common color from image regions and pixelizes image based on this information.


<img src="sunset-original.jpg?raw=true" width="400">  <img src="sunset-final.jpg?raw=true" width="400">

*side note: this image has 8112 post its* 

## user's guide
this program works best with simple images that are often already cartoonized or reduced to 3 or 4 colors, like [this one](https://upload.wikimedia.org/wikipedia/en/5/55/Barack_Obama_Hope_poster.jpg), so don't get too salty if it doesn't work with your huge landscape.

while the program is no longer slower than me running a timed mile, it doesn't work with non-square post it note shapes. to those of you who want non square post its, I want to know where the heck you got these post it notes and why you are using them. 
1. install [python 2.7](https://www.python.org/download/releases/2.7/), [pillow](http://pillow.readthedocs.io/en/latest/installation.html), and [numpy and scipy](https://datahub.packtpub.com/tutorials/installing-numpy-scipy-matplotlib-ipython/).
2. download or clone this repository.
3. put the image you want to convert in the repository folder.
4. open pixelize.py, edit the  variable, and run the program.
5. complain when it doesn't work because i'm incompetent.

## to do
* ~~provide the user with a way to see how many post it notes they're gonna need (and also halt the program if they don't want to put 8112 post its up on the window)~~
* provide user with an option to save image
* specify a color palette for quantization, so you can get custom post it note colors

## special thanks
* to [this](https://gist.github.com/danyshaanan/6754465) github contributor, who basically wrote the exact program that I was trying to write in a much better way (turns out pillow has k-means clustering built in, so you don't have to do it yourself!)
* macgregor house for fostering a friendly but competitive post-it-note environment