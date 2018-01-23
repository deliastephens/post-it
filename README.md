# post-it
a clumsily-written program to pixelize photographs. uses [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to determine the most common color from image regions and pixelizes image based on this information.

## user's guide
1. install [python 2.7](https://www.python.org/download/releases/2.7/), [pillow](http://pillow.readthedocs.io/en/latest/installation.html), and [numpy and scipy](https://datahub.packtpub.com/tutorials/installing-numpy-scipy-matplotlib-ipython/).
2. download or clone this repository.
3. put the image you want to convert in the repository folder.
4. open pixelize.py, edit the img_src variable, and run the program.
5. complain when it doesn't work because i'm incompetent.

## special thanks
* to [this](https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image) github contributor for implementing k-means clustering in a way I could use, because I'm probably never going to understand how this works.
* to macgregor d entry for inspiring a more intense post it note window drawing