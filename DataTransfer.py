import requests
import json
import csv
import tkinter as tk
import decoderDicts
from tkinter import filedialog

pod = 'na1'
insightlyAPIkey = "2749c36f-192d-423b-ab08-e9b793299427"
insightlyAPIurl = "https://api.{}.insightly.com".format(pod)

def getCSVresponses(filepath):
    responses = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        next(reader, None)
        next(reader, None)
        for row in reader:
            responses.append(row)
    return responses

class response:
    def __init__(self, rawResponse) -> None:
        self.response = self.parseResponse(rawResponse)
        
    def decodeIndustryEiR(self, industryResponses):
        
        industryEiR = []
        for industry in industryResponses[0]:
            industryCode = decoderDicts.industry[industry]
            
            #subIndustryCode
            subSubIndustryCode = 0
            industryEiR.append("{:02d}'{:02d}'{:02d} {}".format(industryCode, subIndustryCode, subSubIndustryCode, subIndustry))
        indEir = ", ".join(industryEiR)

    def decodeSkillsEiR(self, skillResponses):
        skillEiR = []
        for skill in skillResponses[0]:
            categoryCode = decoderDicts.skill[skill]
            skilltuple = decoderDicts.skillDict[categoryCode]

    def parseResponse(self, rawResponse):
        self.decodeIndustryEiR(rawResponse[27:56])
        self.decodeSkillsEiR(rawResponse[56:67])
        return

class qualtrics:
    pass

class insightly:
    def __init__(self, responseList) -> None:
        self.pod = 'na1'
        self.insightlyAPIkey = "2749c36f-192d-423b-ab08-e9b793299427"
        self.insightlyAPIurl = "https://api.{}.insightly.com".format(pod)
        self.contacts = responseList

    def postContacts(self):
        pass
    #    postURL = self.insightlyAPIurl + '/Contacts'
    #    for contact in self.contacts:

root = tk.Tk()
root.withdraw()

filepath = filedialog.askopenfilename(filetypes=[("CSV","*.csv")])

responses = getCSVresponses(filepath)
print()
print(responses)
print()
#print(len(responses[0]))