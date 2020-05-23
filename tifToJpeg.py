from PIL import Image
import glob
import os
currentDirPath = os.path.abspath(os.getcwd())
outputPath = os.path.join(currentDirPath, "output")
os.mkdir(outputPath)

Image.MAX_IMAGE_PIXELS = None

for file in glob.glob("*.tif"):
	print(file)
	im = Image.open(file)
 	#im.mode = 'I'
 	i#m = im.point(lambda i:i*(1./256)).convert('L')
 	im.save(os.path.join(outputPath, file.replace("tif", "jpg")), quality=90)
