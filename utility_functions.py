from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

def authenticate_azure(config_file):
  TENANT = config_file["AzureServicePrinciple"]["TENANT"]
  CLIENT_ID = config_file["AzureServicePrinciple"]["CLIENT_ID"]
  CLIENT_SECRET = config_file["AzureServicePrinciple"]["CLIENT_SECRET"]
  VAULT_URL = config_file["AzureServicePrinciple"]["VAULT_URL"]

  credential = ClientSecretCredential(TENANT,CLIENT_ID,CLIENT_SECRET)
  client = SecretClient(vault_url=VAULT_URL, credential=credential)
  return client