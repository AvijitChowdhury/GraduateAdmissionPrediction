import pickle

import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

st.title('Graduate Admission Prediction')
d1=st.number_input('GRE Score')
d2=st.number_input('TOEFL Score')
d3=st.number_input('University Rating')
d4=st.number_input('SOP')
d5=st.number_input('LOR ') 
d6=st.number_input('CGPA')
d7=st.number_input('Research')

data = pd.read_csv('Admission_Predict.csv')
data = data.drop('Serial No.',axis=1)
X = data.drop('Chance of Admit ',axis=1) 
y = data['Chance of Admit ']
y  = [1 if value>0.8 else 0 for value in y]
y = np.array(y)
sc=StandardScaler()
X = sc.fit_transform(X)
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=.2, random_state=42)

#Fit the model, you should involve the required hyper parameters, here I left blank to use defaults
model = GradientBoostingClassifier().fit(X_train,y_train)
#Then evaluate that model with test data, once satisfied with accu
pickle.dump(model, open('model.pkl', 'wb'))
pickled_model = pickle.load(open('model.pkl', 'rb'))
if st.button('Predict'):
    
    
    # try:
       
        preds= pickled_model.predict(np.array([[d1,d2,d3,d4,d5,d6,d7]]))
        print(preds)
        if(preds==1):
            st.success('Congratulations!')
            st.write('High chance of getting admission')
        else:
            st.write('Low chance of getting admission')
    # except:
    #     st.write('Something is wrong')
