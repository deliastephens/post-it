from PIL import Image
import PIL

borderColor = (0, 0, 0) # RGB values for post-it border colors
cardSize = 9 # How big you want your "cards" (post it notes) to be
img_src = 'sunset-original.jpg' # Input file. Make sure to save in same directory as pixelize. 

image = Image.open(img_src)
image = image.convert('RGB')


def pixelize_image(image, cardSize):
    # Uses the resize function to pixelize the image.
    # dangerops!! black magic spookery ahead!!
    image = image.resize((image.size[0]/cardSize, image.size[1]/cardSize), Image.NEAREST)
    image = image.resize((image.size[0]*cardSize, image.size[1]*cardSize), Image.NEAREST)

    return image

def add_borders(image, borderColor):
    image = image.convert('RGB')
    pixel = image.load() # Loads image as series of pixels
    
    # Adds borders of specified color to image
    for i in range(0, image.size[0], cardSize):
        for j in range(0, image.size[1], cardSize):
            for r in range(cardSize):
                pixel[i+r, j] = borderColor
                pixel[i, j+r] = borderColor

    return image

def modify_image(image, cardSize):
    image = pixelize_image(image, cardSize)

    image = image.quantize(5, 1, 5) # Reduces colors of image

    image = add_borders(image, borderColor)
    image.show()

def num_cards(image, cardSize):
    # Get the total number of post-its required
    horizontal_cards = image.size[0] / cardSize
    vertical_cards = image.size[1] / cardSize
    total_cards = horizontal_cards * vertical_cards

    # Wait for user input to proceed
    print("These settings require " + str(total_cards) + " post its.")
    decision = raw_input("Do you want to proceed? y/n: ")
    if decision == 'y':
        modify_image(image, cardSize)
    else:
        print("Quitting program. Try resizing your input image or making cards larger.")
        pass
    
num_cards(image, cardSize)
