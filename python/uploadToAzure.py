import sys
import json
from requests import post

def sendFile(filePath, baseApiUrl, apiVersion, apiKey):

    params = {
        "includeTextDetails": True,
        "pages": "1-"
    }
    headers = {
        'Content-Type': 'application/pdf',
        'Ocp-Apim-Subscription-Key': apiKey,
    }

    try:
        with open(filePath, "rb") as file:
            fileByteArray = file.read()
    except IOError:
        print("Input file is not accessible!")
        sys.exit()

    try:
        response = post(url=baseApiUrl + apiVersion,
                                 params=params,
                                 headers=headers,
                                 data=fileByteArray)
        if response.status_code != 202:
            print(response.status_code)
            print("Post request has failed! \n" + str(json.dumps(response.json())))
            return str(json.dumps(response.json()))

        return str(response.headers.get("Operation-Location"))
    
    except Exception as exception:
        print("Post request has failed! \n Error: " + str(exception))
        return str(exception)