from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from databricks import sql

def authenticate_azure(config_file):
  TENANT = config_file["AzureServicePrinciple"]["TENANT"]
  CLIENT_ID = config_file["AzureServicePrinciple"]["CLIENT_ID"]
  CLIENT_SECRET = config_file["AzureServicePrinciple"]["CLIENT_SECRET"]
  VAULT_URL = config_file["AzureServicePrinciple"]["VAULT_URL"]

  credential = ClientSecretCredential(TENANT,CLIENT_ID,CLIENT_SECRET)
  client = SecretClient(vault_url=VAULT_URL, credential=credential)
  return client

def databricks_connection(config_file):
  client = authenticate_azure(config_file)
  http_path = client.get_secret("http-path").value
  server_hostname = client.get_secret("server-hostname").value
  access_token = client.get_secret("access-token").value

  connection= sql.connect(server_hostname = server_hostname,
                    http_path       = http_path,
                    access_token    = access_token) 

  return connection