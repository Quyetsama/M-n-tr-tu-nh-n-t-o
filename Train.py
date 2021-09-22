import cv2
import numpy as np
import os
from PIL import Image
# pip install Pillow


recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataSet'
def getImagewithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    print(imagePaths)
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImage, 'uint8')
        print(faceNp)
        Id = int(imagePath.split('\\')[1].split('.')[1])
        faces.append(faceNp)
        IDs.append(Id)
        cv2.imshow('tranning', faceNp)
        cv2.waitKey(10)
    return faces, IDs

faces, Ids = getImagewithId(path)

recognizer.train(faces, np.array(Ids))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()


