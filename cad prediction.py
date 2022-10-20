# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:55:05 2022

@author: DELL
"""

import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu


heart_disease_model = pickle.load(open('C:/Users/DELL/Desktop/disease prediction/saved models/heart_disease_model.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          
                          ['About CAD prediction','CAD Disease Prediction'],
                          icons=['person','heart'],
                          default_index=0)
    
    
  
if (selected == 'About CAD prediction'):
    
    # page title
    st.title('Coronary Artery Disease')  
     
    st.header('TO KNOW MORE...')
    
    st.button('CLICK HERE')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if (selected == 'CAD Disease Prediction'):
    
    # page title
    st.title('Coronary Artery Disease Prediction ')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    lst = [[int(i) for i in [age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]]]
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    #b = np.array(a, dtype=float) #  convert using numpy
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(lst)                          
        print(heart_prediction)
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
    