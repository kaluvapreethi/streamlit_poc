import pandas as pd
import streamlit as st
import configparser
from utility_functions import databricks_connection

def fetch_data_from_db(config_file):
  connection = databricks_connection(config_file)
  with connection.cursor() as cursor:
    res = cursor.execute("select first_name, last_name, JobTitle, Salary from (SELECT * , ROW_NUMBER() over (partition by JobTitle order by Salary desc) as rank FROM member_data ) where rank==1 order by JobTitle")

    df = pd.DataFrame(res.fetchall())
    df.columns=[x[0] for x in res.description]
    st.dataframe(df)


if __name__=="__main__": 
  st.set_page_config(page_title="DB data", layout="wide")
  config_file = configparser.ConfigParser()
  config_file.read("configurations.ini")

  with st.container():
      st.subheader("Employees with Top salary in every Department")
      st.title("Fetching data from DB tables")
      
      fetch_data_from_db(config_file)

  

