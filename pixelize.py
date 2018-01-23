from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

img_src = "che.jpg"
postit_width = 10
postit_height = 10

img = Image.open(img_src).convert("RGB")

img.show()

img_width = img.size[0]
img_height = img.size[1]

horizontal_boxes = int(img_width / postit_width)
vertical_boxes = int(img_height / postit_height)

NUM_CLUSTERS = 5

def get_box_color(region):
    ar = np.asarray(region)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    # finds clusters
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent

    peak = []
    for code in codes[index_max]:
        peak.append(int(code))

    peak = tuple(peak)

    region.paste(peak, [0,0,region.size[0],region.size[1]])
    return region

for w in range(0, horizontal_boxes):
    for h in range(0, vertical_boxes):
        left_corner = postit_width * w
        right_corner = left_corner + postit_width
        upper = postit_height * h
        lower = upper + postit_height

        box = (left_corner, upper, right_corner, lower)
        region = img.crop(box)

        colorized_region = get_box_color(region)
        img.paste(colorized_region, box)

img.show()

print(img.format, img.size, img.mode)
