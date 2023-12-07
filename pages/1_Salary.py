import pandas as pd
from databricks import sql
import streamlit as st
import configparser
from utility_functions import authenticate_azure

def fetch_data_from_db(config):
   client = authenticate_azure(config)
   http_path = client.get_secret("http-path").value
   server_hostname = client.get_secret("server-hostname").value
   access_token = client.get_secret("access-token").value

   with sql.connect(server_hostname = server_hostname,
                      http_path       = http_path,
                      access_token    = access_token) as connection:

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
      if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
        st.session_state.placeholder = "This is a Place Holder"
      
      fetch_data_from_db(config_file)

  

