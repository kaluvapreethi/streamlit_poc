import pandas as pd
from databricks import sql
import streamlit as st
import configparser
from utility_functions import authenticate_azure
# from azure.identity import ClientSecretCredential
# from azure.keyvault.secrets import SecretClient


# def authenticate_azure(config):
#   TENANT = config_file["AzureServicePrinciple"]["TENANT"]
#   CLIENT_ID = config_file["AzureServicePrinciple"]["CLIENT_ID"]
#   CLIENT_SECRET = config_file["AzureServicePrinciple"]["CLIENT_SECRET"]
#   VAULT_URL = config_file["AzureServicePrinciple"]["VAULT_URL"]

#   credential = ClientSecretCredential(TENANT,CLIENT_ID,CLIENT_SECRET)
#   client = SecretClient(vault_url=VAULT_URL, credential=credential)
#   return client


def fetch_data_from_db(config_file,gender):
  
  client = authenticate_azure(config_file)
  http_path = client.get_secret("http-path").value
  server_hostname = client.get_secret("server-hostname").value
  access_token = client.get_secret("access-token").value

  with sql.connect(server_hostname = server_hostname,
                    http_path       = http_path,
                    access_token    = access_token) as connection:

    with connection.cursor() as cursor:
      res = cursor.execute("SELECT * FROM member_data where gender=='{}'".format(gender))

      df = pd.DataFrame(res.fetchall())
      df.columns=[x[0] for x in res.description]
      # print(df)
      st.dataframe(df)
      st.write("Displaying {} members".format(gender))


if __name__=="__main__": 
  st.set_page_config(page_title="DB data", layout="wide")
  config_file = configparser.ConfigParser()
  config_file.read("configurations.ini")

  with st.container():
      st.subheader("DB POC")
      st.title("Fetching data from DB tables")
      st.write("POC")

      if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
        st.session_state.placeholder = "This is a Place Holder"

      f_name = st.text_input(
        "First Name",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
      )

      l_name = st.text_input(
        "Last Name",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
      )

      if l_name and f_name:
          st.write("Welcome: ", f_name, " ", l_name)

      gender = st.selectbox('Select the gender?',('Male', 'Female'), index=None)
      st.write('You selected:', gender)

      if gender:
        fetch_data_from_db(config_file,gender)
  
  # fetch_data_from_db(config_file)



