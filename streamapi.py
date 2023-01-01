import pickle
import streamlit as st

model = pickle.load(open('C:/Users/Asus/Desktop/respaldo/Desktop/Proyectos/Proyecto API/model.pkl', 'rb'))


def main():
    st.title("Diabetes data classification")

    # Input variables
    preg = st.text_input('preg')
    plas = st.text_input('plas')
    pres = st.text_input('pres')
    skin = st.text_input('skin')
    test = st.text_input('test')
    mass = st.text_input('mass')
    pedi = st.text_input('pedi')
    age = st.text_input('age')

    # Prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

        output = makeprediction


if __name__ == '__main__':
    main()
