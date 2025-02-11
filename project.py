import pickle as p
from sklearn.linear_model import LogisticRegression
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
st.title("Mini_Project")
st.write("enter the Mail :")
i = st.text_input("write here", key="input")
with open("mini_project_vectorizer.plk",'rb') as f:
    tf = p.load(f)
print(tf)
input_values = tf.transform([i])
print(input_values)
with open("mini_project.plk",'rb') as f:
    model = p.load(f)
predict_ = model.predict(input_values) 
st.write(predict_)
