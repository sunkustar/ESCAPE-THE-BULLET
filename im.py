from PIL import Image 


im = Image.open(r"bullet1.png") 

newsize = (64, 64)

im1 = im.resize(newsize)

im1.save("1.png")