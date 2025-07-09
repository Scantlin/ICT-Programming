'''import warnings
import easyocr

warnings.filterwarnings('ignore')

reader = easyocr.Reader(['en'])
image = reader.readtext('Unsupervised_learning_clustering.png')

for detection in image:
    print(detection[1])'''

'''
import cv2
import pytesseract

image = cv2.imread('workplace.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresholding = cv2.threshold(gray, 0, 25, 5, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#perform OCR
text = pytesseract.image_to_string(thresholding)
print(text)'''

import easyocr

reader = easyocr.Reader(['en'])
results = reader.readtext('workplace.png', paragraph=False)  # paragraph=False helps preserve lines

# Dictionary to store text by line (y-coordinate)
lines = {}

for detection in results:
    text = detection[1]
    bbox = detection[0]
    # Use the top y-coordinate as line identifier
    y = int(min(bbox[0][1], bbox[1][1], bbox[2][1], bbox[3][1]))
    if y not in lines:
        lines[y] = []
    lines[y].append((bbox[0][0], text))  # Store with x-coordinate for ordering

# Sort lines by y-coordinate and words by x-coordinate
for y in sorted(lines.keys()):
    line_text = ' '.join([text for x, text in sorted(lines[y], key=lambda x: x[0])])
    print(line_text)