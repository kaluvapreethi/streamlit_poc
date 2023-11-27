import pandas as pd
from databricks import sql
import streamlit as st
from pyspark.sql import SparkSession

def fetch_data_from_db():
   with sql.connect(server_hostname = "adb-7768825380979695.15.azuredatabricks.net",
                      http_path       = "sql/protocolv1/o/7768825380979695/1122-181140-8sw75rhq",
                      access_token    = "dapie3faf7033e886034eba03f7f1c0c0f19-3") as connection:

      with connection.cursor() as cursor:
        res = cursor.execute("SELECT * FROM member_data LIMIT 10")

        column_names=[x[0] for x in res.description]
        df = spark.createDataFrame(res.fetchall(),column_names)
        st.dataframe(df)
        st.write("Displaying first ten 10 rows")


if __name__=="__main__": 
  spark = SparkSession.builder.master("local[1]").appName("streamlit_spark").getOrCreate()

  st.set_page_config(page_title="DB data", layout="wide")

  with st.container():
      st.subheader("DB POC")
      st.title("Fetching data from DB tables using spark")
      st.write("POC")

  fetch_data_from_db()

  

