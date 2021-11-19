import requests
import json

def main():
    json_dict = {"CONTACT_ID":None,"FIRST_NAME":"TestUI","LAST_NAME":"AA"}

    # Task: Post into Insightly Contacts
    pod = 'na1'
    insightlyAPIkey = "2749c36f-192d-423b-ab08-e9b793299427"
    insightlyAPIurl = "https://api.{}.insightly.com/v3.1".format(pod)

    json_data = json.dumps(json_dict)

    r = requests.post(insightlyAPIurl + '/Contacts', json_data, auth=(insightlyAPIkey, ''))
    print(r)

