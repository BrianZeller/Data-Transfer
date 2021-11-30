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
For example: 'CONTACT_FIELD_92' (Motivation_1), 'CONTACT_FIELD_93' (Motivation_2)
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
```

```
9. Skills EiR
```

```
### Miscellaneous
- The last updated date time is saved in savedData.txt
- Local Business Executive and Local Service Provider place holders are in the getUCIAffiliation function of contact_updated.py
