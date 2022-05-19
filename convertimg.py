import PIL
from PIL import Image

# ascii, you can change it
ASCII_CHARS = ["⢀","⡀","⢠","⢰","⡇","⣼","⣿","⣧","⣆","⡄","⠠","","⢿","⣸","⢾","⠹","⢻","⠳","⠻","⠈","⠘","⠇","⠿","⠙","⠉","⠁","⢠","⢈","⣄","⢨","⠐","⠆"]

def resize_image(image,new_height, new_width):
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//40] for pixel in pixels])
    return(characters)    

def unicode_img(path,width,height,h_limit=60,w_limit=35):
    # attempt to open image from user-input
    new_width=width
    new_height=height
    try:
        image = PIL.Image.open(path)
    except:
        print("Error, path file is not valid. Source:", path)
        return
    i = 1
    while True:
        i = i+1
        if new_height <= h_limit and new_width <= w_limit:
            break
        else:
            new_height = height / i
            new_width = width / i
    ratio = i * 0.1
    alt_new_height = int(new_height)
    alt_new_width = int(new_width/ratio)
    #print("h:",new_height,"/","w:",new_width)
    new_height = alt_new_width
    new_width = alt_new_height
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image,new_height,new_width)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # return ascii_img
    return ascii_image
    
    # save result to txt (opcionally)
    # with open("ascii_image.txt", "w",encoding="utf-8") as f:
    #     f.write(ascii_image)
 
#THIS IS A FORK / ORIGINAL: https://github.com/kiteco/python-youtube-code/blob/master/ascii/ascii_convert.py
