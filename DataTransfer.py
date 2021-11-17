import requests
import json
import csv
import tkinter as tk
import Decoder
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
        self.industryEiR = Decoder.decodeIndustry(rawResponse[27:56])
        self.skillEiR = Decoder.decodeSkills(rawResponse[56:67])
        #self.response = self.parseResponse(rawResponse)

    def printEiR(self):
        print(self.industryEiR)
        print(self.skillEiR)

    # def parseResponse(self, rawResponse):
    #     Decoder.decodeIndustry(rawResponse[27:56])
    #     Decoder.decodeSkills(rawResponse[56:67])
    #     return

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
example = response(responses[0])
example.printEiR()
