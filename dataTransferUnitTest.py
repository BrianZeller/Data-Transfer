import pytest
import contact_updated as dt
from datetime import date

from logHandler import LogHandler

json_dict2 = {}

def test_getNum():
    count = dt.getNum("qualtrics_survey.csv")
    assert count == 111

def test_getMotivations():
    motivations = [0,0,0,0,0]
    assert dt.getMotivations(motivations, json_dict2) == [{"FIELD_NAME":"CONTACT_FIELD_92","FIELD_VALUE":0.0,"CUSTOM_FIELD_ID":"CONTACT_FIELD_92"},{"FIELD_NAME":"CONTACT_FIELD_93","FIELD_VALUE":0.0,"CUSTOM_FIELD_ID":"CONTACT_FIELD_93"},{"FIELD_NAME":"CONTACT_FIELD_94","FIELD_VALUE":0.0,"CUSTOM_FIELD_ID":"CONTACT_FIELD_94"},{"FIELD_NAME":"CONTACT_FIELD_95","FIELD_VALUE":0.0,"CUSTOM_FIELD_ID":"CONTACT_FIELD_95"},{"FIELD_NAME":"CONTACT_FIELD_96","FIELD_VALUE":0.0,"CUSTOM_FIELD_ID":"CONTACT_FIELD_96"}]

def test_getUCIAffiliation():
    noAffiliation = "9"
    student = "1"
    alum = "2"
    faculty = "3"
    staff = "4"
    community = "5"
    for dtfields, testfields in zip(dt.getUCIAffiliation(noAffiliation, json_dict2),[{"FIELD_NAME":"CONTACT_FIELD_154","FIELD_VALUE":"na","CUSTOM_FIELD_ID":"CONTACT_FIELD_154"}, {"FIELD_NAME":"CONTACT_FIELD_133","FIELD_VALUE":"na","CUSTOM_FIELD_ID":"CONTACT_FIELD_133"},{"FIELD_NAME":"CONTACT_FIELD_82","FIELD_VALUE":"na","CUSTOM_FIELD_ID":"CONTACT_FIELD_82"},{"FIELD_NAME":"CONTACT_FIELD_142","FIELD_VALUE":"na","CUSTOM_FIELD_ID":"CONTACT_FIELD_142"}, {"FIELD_NAME":"CONTACT_FIELD_18","FIELD_VALUE":"na","CUSTOM_FIELD_ID":"CONTACT_FIELD_18"}, {"FIELD_NAME":"UCI_unit__c","FIELD_VALUE":None,"CUSTOM_FIELD_ID":"UCI_unit__c"}]):
        assert dtfields == testfields
    for dtfields, testfields in zip(dt.getUCIAffiliation(student, json_dict2), [{"FIELD_NAME":"CONTACT_FIELD_154","FIELD_VALUE":"UCI student","CUSTOM_FIELD_ID":"CONTACT_FIELD_154"}]):
        assert dtfields == testfields
    for dtfields, testfields in zip(dt.getUCIAffiliation(alum, json_dict2), [{"FIELD_NAME":"CONTACT_FIELD_133","FIELD_VALUE":"UCI student alum","CUSTOM_FIELD_ID":"CONTACT_FIELD_133"}]):
        assert dtfields == testfields
    for dtfields, testfields in zip(dt.getUCIAffiliation(faculty, json_dict2), [{"FIELD_NAME":"CONTACT_FIELD_82","FIELD_VALUE":"Current","CUSTOM_FIELD_ID":"CONTACT_FIELD_82"}]):
        assert dtfields == testfields
    for dtfields, testfields in zip(dt.getUCIAffiliation(staff, json_dict2), [{"FIELD_NAME":"CONTACT_FIELD_23","FIELD_VALUE": True,"CUSTOM_FIELD_ID":"CONTACT_FIELD_23"}]):
        assert dtfields == testfields
    for dtfields, testfields in zip(dt.getUCIAffiliation(community, json_dict2), [{"FIELD_NAME":"CONTACT_FIELD_132","FIELD_VALUE": True,"CUSTOM_FIELD_ID":"CONTACT_FIELD_132"}]):
        assert dtfields == testfields

def test_academicDecoder():
    academic_area = [13]
    assert dt.academicDecoder(academic_area, json_dict2) == {'FIELD_NAME': 'UCI_unit__c', 'FIELD_VALUE': ';School of Physical Sciences', 'CUSTOM_FIELD_ID': 'UCI_unit__c'}

def test_getOrganization():
    pod = pod = 'na1'
    key = "2749c36f-192d-423b-ab08-e9b793299427"
    url = "https://api.{}.insightly.com/v3.1".format(pod)

    assert dt.getOrganization(url, key, "Western Digital", 40) == 98140657

def test_getIndustryEiR():
    industry = ["3,9,14", "", "", "3,6", "", "", "", "", "", "1,8,11", "", "", "", "", "2,3,12", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    assert dt.getIndustryEiR(industry, json_dict2) == {"FIELD_NAME":"CONTACT_FIELD_127","FIELD_VALUE":"05'01'00 Computer Hardware, 05'03'00 Consumer Electronics, 05'05'00 Telecommunications Equipment, 06'01'00 Additive Manufacturing, 06'06'00 Paints and Coatings, 06'12'00 Steel and Aluminum, 12'03'00 Consumer Electronics, 12'08'00 Personal & Household Goods","CUSTOM_FIELD_ID":"CONTACT_FIELD_127"}

def test_getSkillEiR():
    skills = ["7", "", "", "", "", "", "", "1,3,5,6", "", "", ""]
    assert dt.getSkillEiR(skills, json_dict2) == {"FIELD_NAME":"CONTACT_FIELD_128","FIELD_VALUE":"03|01 Focus Groups and Interviews, 03|04 Industrial Design, 03|07 Prototyping, 03|10 3D printing","CUSTOM_FIELD_ID":"CONTACT_FIELD_128"}

def test_getGender():
    assert dt.getGender(4, json_dict2) == {"FIELD_NAME":"Gender__c","FIELD_VALUE":"Prefer Not to Say","CUSTOM_FIELD_ID":"Gender__c"}

def test_getEthnicity():
    ethnicity = "8"
    assert dt.getEthnicity(ethnicity, json_dict2) == {"FIELD_NAME":"Ethnicity__c","FIELD_VALUE":";Prefer not to Say","CUSTOM_FIELD_ID":"Ethnicity__c"}

def test_getAcademicOther():
    testStr = "academic other testing"
    assert dt.getAcademicOther(testStr, json_dict2) == {"FIELD_NAME":"CONTACT_FIELD_151","FIELD_VALUE":"academic other testing","CUSTOM_FIELD_ID":"CONTACT_FIELD_151"}

def test_getAcademicBackground():
    testBackground = ["BS","Product Design","Stanford University","BS","Product Design","Stanford University","BS","Product Design","Stanford University","BS","Product Design","Stanford University"]
    assert dt.getAcademicBackground(testBackground, json_dict2) == {"FIELD_NAME":"CONTACT_FIELD_129","FIELD_VALUE":"BS - Product Design - Stanford University; BS - Product Design - Stanford University; BS - Product Design - Stanford University; BS - Product Design - Stanford University","CUSTOM_FIELD_ID":"CONTACT_FIELD_129"}

def test_getAdditionalContactInfo():
    testAdd =  ["google.com","google.com","google.com"]
    for testField, outField in zip(dt.getAdditionalContactInfo(testAdd, json_dict2), [{"FIELD_NAME":"CONTACT_FIELD_143","FIELD_VALUE":"google.com","CUSTOM_FIELD_ID":"CONTACT_FIELD_143"},{"FIELD_NAME":"CONTACT_FIELD_144","FIELD_VALUE":"google.com","CUSTOM_FIELD_ID":"CONTACT_FIELD_144"},{"FIELD_NAME":"CONTACT_FIELD_145","FIELD_VALUE":"google.com","CUSTOM_FIELD_ID":"CONTACT_FIELD_145"}]):
        assert testField == outField
        
def test_getUCIStaff():
    testStaff = "Division of Continuing Education"
    assert dt.getUCIStaff(testStaff, json_dict2) == {"FIELD_NAME":"CONTACT_FIELD_142","FIELD_VALUE":"Division of Continuing Education","CUSTOM_FIELD_ID":"CONTACT_FIELD_142"}

def test_getWorkshop():
    testWorkshop = ["1,2","other"] 
    testField = dt.getWorkshop(testWorkshop, json_dict2)
    #[{"FIELD_NAME":"CONTACT_FIELD_126","FIELD_VALUE":"other","CUSTOM_FIELD_ID":"CONTACT_FIELD_126"}, {"FIELD_NAME":"EiR_Potential_Workshop_Presenter__c","FIELD_VALUE":";Finance and accounting fundamentals;Legal basics","CUSTOM_FIELD_ID":"EiR_Potential_Workshop_Presenter__c"}]
    outField = [{"FIELD_NAME":"EiR_Potential_Workshop_Presenter__c","FIELD_VALUE":";Finance and accounting fundamentals;Legal basics","CUSTOM_FIELD_ID":"EiR_Potential_Workshop_Presenter__c"},{"FIELD_NAME":"CONTACT_FIELD_126","FIELD_VALUE":"other","CUSTOM_FIELD_ID":"CONTACT_FIELD_126"}]
    for test, out in zip(testField, outField):
        keysList = test.keys()
        for k in keysList:
            if k == "FIELD_VALUE":
                tempTest = test["FIELD_VALUE"].split(";")
                tempOut = out["FIELD_VALUE"].split(";")
                for i in tempTest:
                    assert i in tempOut
            else:
                assert test[k] == out[k]

def test_getLL():
    testLL = "I could focus on marketing strategies"
    assert dt.getLL(testLL, json_dict2) == {"FIELD_NAME":"CONTACT_FIELD_146","FIELD_VALUE":"I could focus on marketing strategies","CUSTOM_FIELD_ID":"CONTACT_FIELD_146"}

def test_getAIOpps():
    testAI = ["1,2,6,7,8","2,4,6"]
    testField = dt.getAIOpp(testAI, json_dict2)
    outField = {"FIELD_NAME":"EiR_Desired_Role_From_Survey__c","FIELD_VALUE":";Competition judge;Campus team mentor;General coach;Wayfinder advisor;Wayfinder contributor;Wayfinder reviewer;Wayfinder orientation leader","CUSTOM_FIELD_ID":"EiR_Desired_Role_From_Survey__c"}
    keysList = outField.keys()
    for k in keysList:
        if k == "FIELD_VALUE":
            tempTest = testField["FIELD_VALUE"].split(";")
            tempOut = outField["FIELD_VALUE"].split(";")
            for i in tempTest:
                assert i in tempOut
        else:
            assert testField[k] == outField[k]

def test_DataTransfer():
    for i in range(2,68):
        dt.main("qualtrics_survey.csv", i, "2019-12-31 23:59:59","2021-11-29 11:58:00")


def test_FaultyCSV():
    dt.main("qualtriocs_survey.csv", 10, "2019-12-31 23:59:59","2021-11-29 11:58:00")

def test_logHandler():
    testLog = LogHandler()
    testLog.writeError(100, str(ValueError), "Test")
    testLog.writeIncompleteResponse(101, 50)
    testLog.writeNotification(102, "This is a Test")
    testLog.writeNotInDateRange(103)
    testLog.writePostFailure(104, 404)
    testLog.writePostSuccess(105)
    
