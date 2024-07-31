import streamlit as st
import pickle
import numpy as np
pipe=pickle.load(open(r"C:\Users\HP\OneDrive\Desktop\Artificial Intellegence\Machine learning\titanic\pipe.pkl","rb"))

st.title("Check if person is Dead or Alive")
st.write("fill the details")
p_class=st.selectbox("select passanger class",[1,2,3])
sex=st.selectbox("select gender",["Male","Female"])
age=st.slider("Age",0,100)
sibsp=st.selectbox("select sibsp",[0,1,2,3,4])
parch=st.selectbox("slect parch",[0,1,2,3])
embarked=st.selectbox("select embarked point",["S","C","Q"])

predict=st.button("predict")
x=np.array([p_class,sex,age,sibsp,parch,embarked],dtype=object).reshape(1,6)
if predict:
    predicted=pipe.predict(x)
    if predicted[0]==1:
        st.write("guess what! person is alive")
    else:
        st.write("Sorry to say but person is Dead ")