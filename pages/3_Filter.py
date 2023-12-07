import pandas as pd
import streamlit as st
import configparser
from utility_functions import databricks_connection

def fetch_data_from_db(config_file,gender):
  connection = databricks_connection(config_file)
  with connection.cursor() as cursor:
    print("SELECT * FROM member_data where gender == {}".format(gender))
    print("=======================================")

    res = cursor.execute("SELECT * FROM member_data where gender == '{}'".format(gender))

    df = pd.DataFrame(res.fetchall())
    df.columns=[x[0] for x in res.description]
    st.dataframe(df)


if __name__=="__main__": 
    st.set_page_config(page_title="DB data", layout="wide")
    config_file = configparser.ConfigParser()
    config_file.read("configurations.ini")

    with st.container():
        st.subheader("Gender based display of Data")
        st.title("Fetching data from DB tables")
        gender = st.selectbox('Select the gender?',('Male', 'Female'), index=None)
        st.write('You selected:', gender)

        if gender:
          fetch_data_from_db(config_file,gender)


  

