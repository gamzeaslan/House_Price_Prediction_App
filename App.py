#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import Module
import numpy as np
import pickle
import base64


# In[2]:


#modelin yüklenmesi
loaded_model=pickle.load(open("model.pickle","rb"))

#standard scaler yüklenmesi
standard_scaler=pickle.load(open("standard_scaler.pkl","rb"))


# In[3]:


def house_price_prediction(input_data):
    input_data = np.asarray(input_data)
    input_data_reshape = input_data.reshape(1, -1)
    input_data_reshape = standard_scaler.transform(input_data_reshape)
    prediction = loaded_model.predict(input_data_reshape)
    return int(prediction[0])


# In[4]:


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# In[5]:


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


# In[6]:


def main():
    OverallQual=(st.number_input("OverallQual", min_value=0, max_value=20, value=5, step=1))
    YearBuilt=(st.number_input("YearBuilt", min_value=1870, max_value=2022, value=2015, step=1))
    YearRemodAdd=(st.number_input("YearRemodAdd", min_value=1870, max_value=2022, value=2015, step=1))
    TotalBsmtSF=(st.number_input("TotalBsmtSF", min_value=30, max_value=3000, value=100, step=50))
    _1stFlrSF=(st.number_input("1stFlrSF", min_value=100, max_value=3000, value=200, step=50))
    GrLivArea=(st.number_input("GrLivArea", min_value=0, max_value=3000, value=100, step=50))
    FullBath=(st.number_input("FullBath", min_value=0, max_value=10, value=5, step=1))
    TotRmsAbvGrd=(st.number_input("TotRmsAbvGrd", min_value=0, max_value=20, value=10, step=1))
    GarageCars=(st.number_input("GarageCars", min_value=0, max_value=8, value=4, step=1))
    GarageArea=(st.number_input("GarageArea", min_value=0, max_value=2000, value=200, step=50))
    
    select_ExterQual=["ExterQual_TA","ExterQual_Ex","other"]
    exter=st.selectbox("Exter Qual",select_ExterQual)
    ExterQual_TA=Module.ExterQual_TA(exter)
    ExterQual_Ex=Module.ExterQual_Ex(exter)
    
    
    
    select_BsmtQual=["BsmtQual_TA","BsmtQual_Ex","other"]
    bsmt=st.selectbox("Bsmt Qual",select_BsmtQual)
    BsmtQual_TA=Module.BsmtQual_TA(bsmt)
    BsmtQual_Ex=Module.BsmtQual_Ex(bsmt)
    
    
    select_KitchenQual=["KitchenQual_TA","KitchenQual_Ex","other"]
    kitchen=st.selectbox("Kitchen Qual",select_KitchenQual)
    KitchenQual_TA=Module.KitchenQual_TA(kitchen)
    KitchenQual_Ex=Module.KitchenQual_Ex(kitchen)
    
    set_background("C:/Users/Gamze/House Price Prediction/image.jpg")
    
    diagnosis = ""
    
    
    
    
    if st.button("House Price Prediction Result"):
        diagnosis = house_price_prediction([OverallQual,YearBuilt,YearRemodAdd,
                                     TotalBsmtSF,_1stFlrSF,GrLivArea,FullBath,
                                     TotRmsAbvGrd,GarageCars,GarageArea,
                                     ExterQual_TA,BsmtQual_Ex,KitchenQual_Ex,
                                     KitchenQual_TA,ExterQual_Ex,BsmtQual_TA])
        
        
        
    st.success(diagnosis)



if __name__ == '__main__':
    main() 

    


# In[ ]:




