# Data-Transfer

### Authors
Kai Li Tan, Jing Wu, Justin Yoo, Brian Zeller, Yuan Wang

### Usage
Transfers the Qualtrics Innovation Advisor Profile Survey data in a CSV file into the Insightly Contacts database.

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

### Miscellaneous
- The last updated date time is saved in savedData.txt
- Local Business Executive and Local Service Provider place holders are in the UCI Affiliation section of contact_updated.py
