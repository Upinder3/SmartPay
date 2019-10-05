from fpt import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils
from PIL import Image,ImageEnhance,ImageFilter
import PIL.Image
from pytesseract import image_to_string
import pytesseract
import json
import re
from card_identifier.cardutils import format_card
from card_identifier.cardutils import validate_card
from card_identifier.card_type import identify_card_type
from card_identifier.card_issuer import identify_card_issuer
import json


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)
 
# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
 
# show the original image and the edge detected image
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
 
# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	print(len(approx))
 
	# our approximated contour shold have four points
	if len(approx) == 4:
		screenCnt = approx
		break
 
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
 
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255
 
# show the scanned image and save one copy in out folder
print("STEP 3: Apply perspective transform")

imS = cv2.resize(warped, (650, 650))
cv2.imwrite('out/'+'Output Image.PNG', imS)

output = pytesseract.image_to_string(PIL.Image.open('out/'+ 'Output Image.PNG'),lang='eng')

numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', output)


card="5401683100112371"

a=identify_card_issuer(card)

result={'card_type':a['type'],'card_scheme':a['scheme'],'country':a['country']['name'],'bank_name':a['bank']['name']}
f = open('details.json','w')
f.write(json.dumps(result))
f.close()


