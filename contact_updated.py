from tkinter.constants import TRUE, FALSE
import requests
import json
import csv
import tkinter as tk
import Decoder
from tkinter import filedialog
import sys

# Insightly API Key
pod = 'na1'
insightlyAPIkey = "2749c36f-192d-423b-ab08-e9b793299427"
insightlyAPIurl = "https://api.{}.insightly.com/v3.1".format(pod)

# CSV Source
file_name = 'qualtrics_survey.csv'

with open(file_name, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    count = 0
    imported_count = 0
    try:
        for row in reader:
            if (count >= 2):  # row 0-1 are headers
                
                json_dict = {"CONTACT_ID":None,"FIRST_NAME":row['Contact_1']}
                json_dict['CUSTOMFIELDS'] = []
                json_dict2 = {}
                
                # AREA 1: CONTACTS
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
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_143'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Contact_9']
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_143'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Contact_10']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_144'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Contact_10']
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_144'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Contact_11']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_145'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Contact_11']
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_145'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                    
                # AREA 2: DEGREE
                if (row['Degree 1_1']):
                    str1 = row['Degree 1_1'] + ' - ' + row['Degree 1_2'] + ' - ' + row['Degree 1_3']
                    if (row['Degree 2_1']):
                        str1 += '; ' + row['Degree 2_1'] + ' - ' + row['Degree 2_2'] + ' - ' + row['Degree 2_3']
                        if (row['Degree 3_1']):
                            str1 += '; ' + row['Degree 3_1'] + ' - ' + row['Degree 3_2'] + ' - ' + row['Degree 3_3']
                            if (row['Degree 4_1']):
                                str1 += '; ' + row['Degree 4_1'] + ' - ' + row['Degree 4_2'] + ' - ' + row['Degree 4_3']
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_129'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = str1
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_129'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Academic - Other']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_151'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = row['Academic - Other']
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_151'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                
                # AREA 3: INDUSTRY
                if (row['Industry']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_127'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = Decoder.decodeIndustry(list(row.values())[27:56])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_127'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                
                # AREA 4: SKILLS
                if (row['Skills']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_128'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = Decoder.decodeSkills(list(row.values())[56:67])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_128'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                    
                # AREA 5: MOTIVATION
                if (row['Motivations_1']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_92'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(row['Motivations_1'])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_92'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Motivations_2']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_93'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(row['Motivations_2'])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_93'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Motivations_3']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_94'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(row['Motivations_3'])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_94'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Motivations_4']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_95'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(row['Motivations_4'])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_95'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                if (row['Motivations_5']):
                    json_dict2['CUSTOMFIELDS'] = {}
                    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_96'
                    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(row['Motivations_5'])
                    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_96'
                    json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                                        
                # AREA 6: UCI AFFILIATIONS
                # if (row['UCI Staff']):
                #     json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_23'
                #     if (row['UCI Staff'] == 1):
                #         json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = TRUE
                #     if (row['UCI Staff'] == 0):
                #         json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = FALSE
                #     json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_23'
                #     json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
                   
                # POST CSV data to Insightly   
                #r = requests.get(insightlyAPIurl + '/Contacts/333962025', auth=(insightlyAPIkey, ''))   
                r = requests.post(insightlyAPIurl + '/Contacts', json=json_dict, auth=(insightlyAPIkey, ''))
                print(r.text)
                imported_count += 1
                
                break  # get first row of dummy data only
            count += 1

        print(imported_count, "row(s) of data has been transferred successfully.")
        
    except csv.Error as e:  # display error
        sys.exit('file {}, line {}: {}'.format(file_name, reader.line_num, e))
