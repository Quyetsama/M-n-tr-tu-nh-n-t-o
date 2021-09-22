import cv2
import numpy as np
import sqlite3
import os
import pyodbc

id = 0

def inseretOrUpdate(name):
    global id
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-EBVUMV9\MSSQLSERVER01;'
                      'Database=Face;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    query = "SELECT TOP 1 * FROM Face ORDER BY id DESC"
    cursor.execute(query)



    for row in cursor:
        id = int(row[0]) + 1
        print(row)
        print(row[0])
        print(id)



    query = "INSERT INTO face(name) VALUES('" +str(name)+ "')"
    conn.execute(query)
    conn.commit()
    conn.close()

# inseretOrUpdate(2, 'Quyet2')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# id = int(input("Enter your ID:"))
name = input("Enter your name:")
inseretOrUpdate(name)

sampleNum = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')
        sampleNum +=1
        cv2.imwrite('dataSet/User.'+str(id)+'.'+ str(sampleNum)+'.jpg', gray[y: y+h , x: x+w])

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

    if sampleNum > 300:
        break
cap.release()
cv2.destroyAllWindows()
