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

model=load_model('model.h5')
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
    image_placeholder.image(gray_img,channels="RGB",use_column_width=True)
    gray_img=cv2.resize(gray_img,(64,64))
    img_pixels=image.img_to_array(gray_img)
    img_pixels=np.expand_dims(img_pixels,axis=0)
    img_pixels/=255
    predictions=model.predict(img_pixels)    
    max_index=np.argmax(predictions[0])
    emotions=('angry','disgusted','fear','happy','sad','surprise','neutral')
    predicted_emotion=emotions[max_index]
    text_placeholder.empty()    
    text_placeholder.text('Predicted Emotion: {}'.format(predicted_emotion))
    resized_img=cv2.resize(test_img,(1000,700))
    if (iterations==1):
        if st.button('Stop'):
            break
cap.release()
cv2.destroyAllWindows