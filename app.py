import streamlit as st
import configparser

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


