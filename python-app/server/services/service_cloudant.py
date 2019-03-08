from ibmcloudenv import IBMCloudEnv
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

username = "7f3532b0-d678-4936-a89f-25a7f0c5090d-bluemix"
password = "ab46de8f3c69f883a405118d65d49800a6fd6b05c93c40409fa32f5cc78fd3f8"
url = "https://7f3532b0-d678-4936-a89f-25a7f0c5090d-bluemix:ab46de8f3c69f883a405118d65d49800a6fd6b05c93c40409fa32f5cc78fd3f8@7f3532b0-d678-4936-a89f-25a7f0c5090d-bluemix.cloudantnosqldb.test.appdomain.cloud"

client = Cloudant(username, password, url=url, connect=True, auto_renew=True)
client.connect()

databaseName = "db"
myDatabase = client.create_database(databaseName)

if myDatabase.exists():
   print("successfully created")





def getService(app):
    return 'cloudant', cloudant
