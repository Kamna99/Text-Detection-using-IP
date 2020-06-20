from pytesseract import Output
import pytesseract
import argparse
import cv2
image = cv2.imread('apple_support.png')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
for i in range(0, len(results["text"])):

	x = results["left"][i]
	y = results["top"][i]
	w = results["width"][i]
	h = results["height"][i]

	text = results["text"][i]
	conf = int(results["conf"][i])

	
	if conf > 0:
		print("Confidence: {}".format(conf))
		print("Text: {}".format(text))
		print("")
		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			1.2, (0, 0, 255), 3)


cv2.imshow("Image", image)
cv2.waitKey(0)
