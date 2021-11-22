import requests
import json
import csv
import tkinter as tk
# import decoderDicts
from tkinter import filedialog
from os import system

def getNum(file_path):
    # file_name = '/Users/joviwyel/UCI/2021_Fall/INF117/qualtrics_survey.csv'
    print("getNum is being called")
    file_name = file_path
    print("file_path pass in:" , file_path)
    print("file_name got:" , file_name)
    count = 0
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            count+= 1
    print(count)
    return count

def main(file_path):
    message = ""
    # Insightly API Key
    pod = 'na1'
    insightlyAPIkey = "2749c36f-192d-423b-ab08-e9b793299427"
    insightlyAPIurl = "https://api.{}.insightly.com/v3.1".format(pod)
    try:
        # CSV Source
        # file_name = '/Users/joviwyel/UCI/2021_Fall/INF117/qualtrics_survey.csv'
        file_name = file_path
        num = 0
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            count = 0

            for row in reader:
                if (count >= 2):  # row 0-1 are headers
                    num += 1
                    json_dict = {"CONTACT_ID": None, "FIRST_NAME": row['Contact_1']}
                    json_dict['CUSTOMFIELDS'] = []
                    json_dict2 = {}
                    json_dict2['CUSTOMFIELDS'] = {}

                    if (row['Contact_2']):
                        json_dict['LAST_NAME'] = row['Contact_2']
                    if (row['Contact_4']):
                        json_dict['PHONE'] = row['Contact_4']
                    if (row['Contact_3']):
                        json_dict['EMAIL_ADDRESS'] = row['Contact_3']
                    if (row['Contact_5']):
                        json_dict['ADDRESS_MAIL_STREET'] = row['Contact_5']
                    if (row['Contact_6']):
                        json_dict['ADDRESS_MAIL_CITY'] = row['Contact_6']
                    if (row['Contact_7']):
                        json_dict['ADDRESS_MAIL_STATE'] = row['Contact_7']
                    if (row['Contact_8']):
                        json_dict['ADDRESS_MAIL_POSTCODE'] = row['Contact_8']
                    if (row['Contact_9']):
                        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_143'
                        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Contact_9']
                        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_143'
                        json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                    if (row['Contact_10']):
                        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_144'
                        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Contact_10']
                        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_144'
                        json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                    if (row['Contact_11']):
                        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_145'
                        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Contact_11']
                        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_145'
                        json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])

                    # POST CSV data to Insightly

                    # comment for test UI
                    # r = requests.post(insightlyAPIurl + '/Contacts', json=json_dict, auth=(insightlyAPIkey, ''))
                    # print(r)

                    break;  # get first row of dummy data only
                count += 1

            count -= count
            # print(count, "rows of data has been transferred successfully.")


    except (csv.Error, FileNotFoundError) as e:  # display error
        if type(e) is FileNotFoundError:
            message = "The file inputted into the program can not be found within the path"
        else:
            message = "There has been a CSV error"
        # system.exit('file {}, line {}: {}'.format(file_name, reader.line_num, e))

    return message, num
