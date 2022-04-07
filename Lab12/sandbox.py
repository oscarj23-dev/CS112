from PIL import Image
import os
img = Image.open("/Users/oscarmaldonado/Downloads/cwu logo/cwu_logo0.jpg") 
print(img.size)

width, height = img.size
newImg = img.resize((width//2, height//2))
print(newImg.size)
img.show()
newImg.show()
greyImage = newImg.convert('L')
greyImage.show()