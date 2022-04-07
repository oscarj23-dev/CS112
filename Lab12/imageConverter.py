#Oscar Maldonado
#11/2/2021  
#imageConverter.py

from PIL import Image
import os
#import os to iterate over files in a directory
for filename in os.listdir("/Users/oscarmaldonado/Downloads/cwu logo"):
    img = Image.open("/Users/oscarmaldonado/Downloads/cwu logo/" + filename) 
    #resize the images, convert them to greyscale and save them to the new folder.
    width, height = img.size
    newImg = img.resize((width//2, height//2))
    greyImage = newImg.convert('L')
    greyImage.save("/Users/oscarmaldonado/Desktop/py4e/CS112/Lab12/grey_resized_logos" + filename)



