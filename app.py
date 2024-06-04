import streamlit as st
import pickle
from PIL import Image

def main() :

    st.title ("Video Games sales 2024 :computer:")
    image=Image.open("image.jpg")
    st.image(image,width=700)

    critic=st.text_input("critic score :1234:","type here")
    na=st.text_input("north america sales :foggy:","type here")
    jp=st.text_input("Japan sales :japanese_castle:","type here")
    pal=st.text_input("Europe/Africa sales :european_castle:","type here")
    other=st.text_input("other sales :chart_with_upwards_trend:","type here")

    features=[critic,na,jp,pal,other]

    model=pickle.load(open("model game","rb"))
    scaler=pickle.load(open("scaler game","rb"))

    predicts=st.button("predict the Sales :sparkles:")

    if predicts :

        prediction=model.predict(scaler.transform([features]))
        st.caption("Your sales :bar_chart:")
        st.write("From the Details of the Game :bookmark_tabs: the total Sales of the Game is :star:",prediction)
        st.caption("Thankyouuuu, Enjoy the time mate :heart:")

main()








