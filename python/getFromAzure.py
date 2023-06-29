import sys
from requests import get

# retrieves processed invoice from Azure as JSON from given url
def retrieveFileFromAzure(url, apiKey):

    response = get(url = url, headers={"Ocp-Apim-Subscription-Key": apiKey})

    if response.status_code >= 400:
        print(response.status_code)
        print(str(response.json()))
        sys.exit()

    if response.status_code == 200:
        print(response.status_code)
        print(response.encoding)
        data = response.text
        
        data.replace("'","\"") 
        data.replace("True","true")
        data.replace("False","false")

        return data