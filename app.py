import requests
import streamlit as st

st.title('IRCTC TRAIN SEEKER :train:')
st.header('An appliaction to extract train station details')
st.subheader('built by Author')
st.sidebar.title('Irctc Train Details :train:')

class IRCTC:

    def __init__(self):

        user_input=st.sidebar.text_input("""
        How would you like to proceed?
          Enter start to return station name and code
        """,key=0)

        if user_input=="start":
            while True:
                self.fetch_data()

    def fetch_data(self):

        train_name=st.sidebar.text_input("Enter train name :",key=1)
        data=self.get_api(train_name)
        for i in data["stations"]:
            st.write(i["stationName"]+"/"+i["stationCode"])

    def get_api(self,train_name):

        url = "https://indianrailways.p.rapidapi.com/findstations.php"
        querystring = {"station": "{}".format(train_name)}
        headers = {
            "X-RapidAPI-Key": "Modify in accordance",
            "X-RapidAPI-Host": "Modify in accordance"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return (response.json())
object=IRCTC()
