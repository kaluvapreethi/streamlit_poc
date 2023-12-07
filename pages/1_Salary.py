import pandas as pd
import streamlit as st
import configparser
from utility_functions import databricks_connection

def fetch_data_from_db(config_file):
  connection = databricks_connection(config_file)
  with connection.cursor() as cursor:
    res = cursor.execute("SELECT * FROM member_data order by Salary limit 10")

    df = pd.DataFrame(res.fetchall())
    df.columns=[x[0] for x in res.description]
    st.dataframe(df)


if __name__=="__main__": 
  st.set_page_config(page_title="DB data", layout="wide")
  config_file = configparser.ConfigParser()
  config_file.read("configurations.ini")

  with st.container():
      st.subheader("Top 10 salaried employees")
      st.title("Fetching data from DB tables")
      
      fetch_data_from_db(config_file)

  

