import pandas as pd
import streamlit as st
import configparser
from utility_functions import databricks_connection

def fetch_data_from_db(config_file):
  connection = databricks_connection(config_file)
  with connection.cursor() as cursor:
    res = cursor.execute("SELECT JobTitle, count(*) as employees_count FROM member_data group by JobTitle order by employees_count desc ")

    df = pd.DataFrame(res.fetchall())
    df.columns=[x[0] for x in res.description]
    st.dataframe(df)
    st.bar_chart(df, x="JobTitle", y="employees_count")



if __name__=="__main__": 
  st.set_page_config(page_title="DB data", layout="wide")
  config_file = configparser.ConfigParser()
  config_file.read("configurations.ini")

  with st.container():
      st.subheader("Job title employee count")
      st.title("Fetching data from DB tables")

      fetch_data_from_db(config_file)

  

