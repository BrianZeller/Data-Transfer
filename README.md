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
Data Types in Insightly:
1. Text (Insightly Built-In Fields)
```
if (row['FIELD_NAME_IN_CSV']):
    json_dict['FIELD_NAME_IN_INSIGHTLY'] = row['FIELD_NAME_IN_CSV']
```
2. Text (Custom Fields) 
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
6. Checkbox
7. Organization related

### Miscellaneous
- The last updated date time is saved in savedData.txt
- Local Business Executive and Local Service Provider place holders are in the getUCIAffiliation function of contact_updated.py
- If organization name from Qualtrics is not found in the Organisation database in Insightly, it would not transfer because it needs to link to an existing ORGANISATION_ID.
