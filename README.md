# Data-Transfer

### Authors
Kai Li Tan, Jing Wu, Justin Yoo, Brian Zeller, Yuan Wang

### Usage
Transfers the Innovation Advisor Profile Survey data in a CSV file exported from Qualtrics into the Insightly Contacts database.

### How-to-Use
1. Run prototype.py 
2. Select time range of data to transfer: 
    - Default time would transfer data after the last updated date time
    - Customize start and end date time would transfer data within that specific time range
3. Click on "Choose CSV File" to specify the file path
4. Click on "Start Transfer" to start the transferring process
5. An uploading process bar will appear
6. Once transfer is done, a successful message will appear
7. New Contact objects will be created in Insightly

### Adding New Fields
1. Use the suitable templates below to add new fields into contact_updated according to the value's data type.
2. Replace FIELD_NAME_IN_CSV with the field name in the CSV file which is located at the first row such as 'Degree 1_1' and 'Contact_2'. 
3. Replace FIELD_NAME_IN_INSIGHTLY with the corresponding field name in Insightly such as 'CONTACT_FIELD_129' and 'LAST_NAME'.
4. Replace the function name getField into something more relevant such as getAcademicBackground and getOrganization.

### Templates for Different Data Types in Insightly
1. Text (Insightly Built-In Fields)
- For example: 'LAST_NAME', 'PHONE', 'ADDRESS_MAIL_CITY'
```
if (row['FIELD_NAME_IN_CSV']):
    json_dict['FIELD_NAME_IN_INSIGHTLY'] = row['FIELD_NAME_IN_CSV']
```
2. Text (Custom Fields) 
- For example: 'CONTACT_FIELD_92', 'Ethnicity__c', 'UCI_unit__c'
```
def getField(field_value, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'FIELD_NAME_IN_INSIGHTLY'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = field_value
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'FIELD_NAME_IN_INSIGHTLY'
    return json_dict2['CUSTOMFIELDS']

if (row['FIELD_NAME_IN_CSV']):
    json_dict['CUSTOMFIELDS'].append(getField(row['FIELD_NAME_IN_CSV'], json_dict2))
```
3. Integer 
- For example: 'CONTACT_FIELD_92' (Motivation_1), 'CONTACT_FIELD_93' (Motivation_2)
```
def getField(field_value, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'FIELD_NAME_IN_INSIGHTLY'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(field_value)
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'FIELD_NAME_IN_INSIGHTLY'
    return json_dict2['CUSTOMFIELDS']

if (row['FIELD_NAME_IN_CSV']):
    json_dict['CUSTOMFIELDS'].append(getField(row['FIELD_NAME_IN_CSV'], json_dict2))
```
4. Single Choice in Dropdown
- For example: 'Gender__c'
```
def getField(field_value, json_dict2):
    field_decoder = {
        1: "Option A"
        , 2: "Option B"
        , 3: "Option C"
    }
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'FIELD_NAME_IN_INSIGHTLY'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = field_decoder[int(field_value)]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'FIELD_NAME_IN_INSIGHTLY'
    return json_dict2['CUSTOMFIELDS']

if (row['FIELD_NAME_IN_CSV']):
    json_dict['CUSTOMFIELDS'].append(getField(row['FIELD_NAME_IN_CSV'], json_dict2))
```
5. Multiple Choice in Dropdown
- For example: 'Ethnicity__c', 'EiR_Potential_Workshop_Presenter__c', 'EiR_Desired_Role_From_Survey__c'
```
def getField(field_value, json_dict2):
    field_list = []
    field_list.extend(field_value.split(","))
    field_list = list(set(ethnicity))  # remove duplicated
    field_decoder = {
        1: ";Option A"
        , 2: ";Option B"
        , 3: ";Option C"
    }
    str1 = ""
    for i in field_list:
        str1 += field_decoder[int(i)]
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'FIELD_NAME_IN_INSIGHTLY'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = str1
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'FIELD_NAME_IN_INSIGHTLY'
    return json_dict2['CUSTOMFIELDS']

if (row['FIELD_NAME_IN_CSV']):
    json_dict['CUSTOMFIELDS'].append(getField(row['FIELD_NAME_IN_CSV'], json_dict2))
```
6. Checkbox
- For example: 'CONTACT_FIELD_154' (UCI student), 'CONTACT_FIELD_133' (UCI Alumni)
```
def getField(field_value, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'FIELD_NAME_IN_INSIGHTLY'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = True
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'FIELD_NAME_IN_INSIGHTLY'
    return json_dict2['CUSTOMFIELDS']

if (row['FIELD_NAME_IN_CSV']):
    json_dict['CUSTOMFIELDS'].append(getField(row['FIELD_NAME_IN_CSV'], json_dict2))
```
7. Organization Name
- For example: 'ORGANISATION_ID'
- An organization name will be passed in into the function. 
- It will be used to lookup the organization ID in Insightly's Organisation database. 
- The organization ID would be used to link the Contact object to the Organisation.
- If organization name from Qualtrics is not found in the Organisation database in Insightly, it would not transfer because it needs to link to an existing ORGANISATION_ID.
```
def getOrganization(insightlyAPIurl, insightlyAPIkey, organizationResponses, rownum):
    organization_id = None
    r = requests.get(
        insightlyAPIurl + '/Organisations/Search?field_name=ORGANISATION_NAME&field_value=' + organizationResponses + '&brief=false&count_total=false', auth=(insightlyAPIkey, ''))
    organization_json = r.json()
    if (organization_json): # if list is  not empty, it means ORGANISATION_ID exists
        organization_json = organization_json[0]  # first item in list is the organization dict
        organization_id = int(organization_json['ORGANISATION_ID'])
    else:
        logObject.writeNotification(rownum, "Organization name is not found in Insightly Organisation database")
        # Print log statement that Organization does not exist in Insightly
    return organization_id

if (row['FIELD_NAME_IN_CSV']):
    json_dict['ORGANISATION_ID'] = getOrganization(insightlyAPIurl, insightlyAPIkey, row['FIELD_NAME_IN_CSV'], rownum)
```
8. Industry EiR

The Industry EiR is obtained through passing a list of the industry responses into a decoder. The decoder is organized by dictionaries that pertain to the Industry Category, Industry, and the Sub-Industry.
```
industry = {1:8, 2:2, 3:12, 4:13, 5:1, 6:3, 7:4, 8:15, 9:6, 10:11, 11:9, 12:14, 13:10, 14:5, 15:7}
```
The dictionary above relates the response number of the given Industry Category in the survey to the value that it has for the Category section of the EiR code. The obtained value is then given to the following dictionary.
```
indCategory = {1:indEnergy, 2:indCleantech, 3:indHlthcare, 4:indIT, 5:indTechHard, 6:indManufact, 7:indTransport, 8:indAgriculture, 9:indMonetary, 10:indRealEst, 11:indMaterials, 12:indConsGds, 13:indConsServ, 14:indPubServ, 15:indLaw}
```
This dictionary then, based on the given code section, accesses another dictionary for the given Industry Category. For example, if the survey response had a value of 6, it would then get 3 from the industry dictionary, which then accesses the indHlthcare dictionary which corresponds to the Healthcare & Patient Services Industry Category. The decoder then goes to the list index that corresponds with that Category and obtains the responses for the Industry. Industries that do not have Sub-Industries takes the response values and returns the Industry section EiR code along with the Industry name. This is done through a dictionary such as indAgriculture shown below.
```
indAgriculture = {1:(1, "Agricultural Production & Policy") , 2:(4, "Animal Husbandry"), 3:(8, "Desalination"), 4:(7, "Drought Management"), 5:(9, "Environmental Protection"), 6:(11, "Forestry"), 7:(2, "Genetically Modified Crops"), 8:(3, "Green Biotechnology"), 9:(5, "Veterinary Services"), 10:(10, "Waste Management & Recycling"), 11:(6, "Water Management")}
```
Industries that do have Sub-Industries however, have an additional dictionary for determining the Industry prior to the Sub-Industry as seen below.
```
indHlthcareSubs = {1:subIndMedDev, 2:subIndPharm, 3:subIndBiotech, 4:subIndHlthServ, 5:subIndHlthTech, 6:subIndWellness}
```
After determining the Industry through this additional dictionary, it goes to a Sub-Industry dictionary for that given Category, as can be seen below.
```
subIndMedDev = {1:(4, "Cybersecurity"), 2:(2, "Manufacturing"), 3:(1, "R&D"), 4:(3, "Standards and Regulations")}
```
This dictionary works in the same manner that the typical Industry dictionary does as seen with indAgriculture.

#### How to modify Industry EiR decoder
In order to update the decoder, if the order of questions in the survey have been changed, first determine the indexes that comprise the survey responses pertaining to the Industry EiR questions and change it the decodeIndustry argument to the slice of indexes.

#### To update the industry dictionary
The key values are the response number in the survey. Change the value for the given key to that industry's corresponding EiR code.

#### To update the indCategory diction
If the EiR codes changed order, change the industry category to match the corresponding key value.

#### To update an industry dictionary
The key values are again the response number for the given industry in the survey. Change the values of the tuple which is comprised of
```
(EiRsection, "Industry Name")
```
to match the new survey answer order.

#### To update a industry that has sub-industries
The key values are the corresponding section of the EiR code, change the dictionary to correspond to the new EiR code.
In decodeIndustry there is the section
```
if categoryCode not in [3, 4, 13]:
```
change the values in [] to match the EiR codes for the Industry Categories that have Sub-Industries. Following this there an else statement that leads to a couple of sections of code that looks like this
```
if categoryCode == 3:
                    subindex = 18 + industryR
                    for subIndustryR in responses[subindex]:
                        subIndustryCode = indHlthcareSubs[industryCode][subIndustryR][0]
                        industryName =  indHlthcareSubs[industryCode][subIndustryR][1]
                        industryEiR.append("{:02d}'{:02d}'{:02d} {}".format(categoryCode, industryCode, subIndustryCode, industryName))
```
First change the if statment to match the new EiR code value here
```
if categoryCode == newEir:
```
If the order of questions in the survey changed, or a new industry with sub-industries was added change the subindex offset to match where the new section of sub-industries begins in the list. For example, here the offset is 18 due to the Healthcare Sub-Industries survey responses starting in the 19th index of the sliced list, so the previous index is used as a starting location.
```
subindex = offset + industryR
```
Next change the sub-industry dictionary to match the new industry category being used.
```
subIndustryCode = indNewIndustrySubs[industryCode][subIndustryR][0]
industryName =  indNewIndustrySubs[industryCode][subIndustryR][1]
```
#### To update a subInd dictionary
Refer to "To update an industry dictionary"

9. Skills EiR
```

```
### Miscellaneous
- The last updated date time is saved in savedData.txt
- Local Business Executive and Local Service Provider place holders are in the getUCIAffiliation function of contact_updated.py
