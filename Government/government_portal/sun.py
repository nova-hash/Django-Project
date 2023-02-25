

# /**API to verify Degree/ Diploma Certificate.**/

import requests

url = "https://apisetu.gov.in/certificate/v3/gtu/dgcer"

payload = {
    "txnId": "f7f1469c-29b0-4325-9dfc-c567200a70f7",
    "format": "pdf",
    "certificateParameters": {
        "RROLL": "12345",
        "REGNO": "AC-XX12",
        "YEAR": "2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021",
        "FullName": "Sunil Kumar",
        "DOB": "31-12-1980"
    },
    "consentArtifact": {
        "consent": {
            "consentId": "ea9c43aa-7f5a-4bf3-a0be-e1caa24737ba",
            "timestamp": "2019-08-24T14:15:22Z",
            "dataConsumer": {"id": "string"},
            "dataProvider": {"id": "string"},
            "purpose": {"description": "string"},
            "user": {
                "idType": "string",
                "idNumber": "string",
                "mobile": "string",
                "email": "string"
            },
            "data": {"id": "string"},
            "permission": {
                "access": "string",
                "dateRange": {
                    "from": "2019-08-24T14:15:22Z",
                    "to": "2019-08-24T14:15:22Z"
                },
                "frequency": {
                    "unit": "string",
                    "value": 0,
                    "repeats": 0
                }
            }
        },
        "signature": {"signature": "string"}
    }
}
headers = {
    "X-APISETU-CLIENTID": "REPLACE_KEY_VALUE",
    "content-type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)