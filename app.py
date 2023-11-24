import pandas as pd
from databricks import sql
import streamlit as st

if __name__=="__main__": 
  st.set_page_config(page_title="DB data", layout="wide")

  with st.container():
      st.subheader("DB POC")
      st.title("Fetching data from DB tables")
      st.write("POC")

  with sql.connect(server_hostname = "adb-7768825380979695.15.azuredatabricks.net",
                      http_path       = "sql/protocolv1/o/7768825380979695/1122-181140-8sw75rhq",
                      access_token    = "dapie3faf7033e886034eba03f7f1c0c0f19-3") as connection:

      with connection.cursor() as cursor:
        res = cursor.execute("SELECT * FROM member_data LIMIT 10")

        df = pd.DataFrame(res.fetchall())
        df.columns=[x[0] for x in res.description]
        print(df)
        st.dataframe(df)
        st.write("Displaying only top 10 rows")


