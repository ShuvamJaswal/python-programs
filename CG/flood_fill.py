
from PIL import Image,ImageDraw
img=Image.new('RGBA',(100,100),color=(0,0,0))
ImageDraw.floodfill(img,(50,50),(0,255,0),thresh=0)
img.save('a.png')