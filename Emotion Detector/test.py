import os
import cv2
import numpy as np
from keras.preprocessing import image
import warnings 
warnings.filterwarnings("ignore")
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import streamlit as st
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
model=load_model('model.h5')
emotion = {
    0: "angry",
    1: "disgusted",
    2: "fearful",
    3: "happy",
    4: "neutral",
    5: "sad",
    6: "surprised"
}
st.title('Emotion Detection')
cap=cv2.VideoCapture(0)
image_placeholder = st.empty()
text_placeholder = st.empty()
iterations=0
while True:
    iterations=iterations+1
    ret, test_img=cap.read()
    if not ret:
        continue
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2RGB)
    face_rects = face_cascade.detectMultiScale(gray_img)
    image_placeholder.image(gray_img,channels="RGB",use_column_width=True)
    for (x,y,w,h) in face_rects:
        roi_gray=gray_img[y:y+h,x:x+h]
        roi_color=test_img[y:y+h,x:x+h]
        roi=cv2.resize(roi_color,(48,48))
        roi=image.img_to_array(roi)
        roi=np.expand_dims(roi,axis=0)
        pred = model.predict(roi)
        pred = np.argmax(pred)
        predicted_emotion=emotion[pred]
        text_placeholder.empty()    
        text_placeholder.text('Predicted Emotion: {}'.format(predicted_emotion))
        resized_img=cv2.resize(test_img,(1000,700))
cap.release()
cv2.destroyAllWindows