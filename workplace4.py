import warnings
import easyocr

warnings.filterwarnings('ignore')

reader = easyocr.Reader(['en'])
image = reader.readtext('Unsupervised_learning_clustering.png')

for detection in image:
    print(detection[1])