# Dictionaries that map the industry responses from Qualtrics to the EiR decoder
industry = {1:8, 2:2, 3:12, 4:13, 5:1, 6:3, 7:4, 8:15, 9:6, 10:11, 11:9, 12:14, 13:10, 14:5, 15:7}
indAgriculture = {1:(1, "Agricultural Production & Policy") , 2:(4, "Animal Husbandry"), 3:(8, "Desalination"), 4:(7, "Drought Management"), 5:(9, "Environmental Protection"), 6:(11, "Forestry"), 7:(2, "Genetically Modified Crops"), 8:(3, "Green Biotechnology"), 9:(5, "Veterinary Services"), 10:(10, "Waste Management & Recycling"), 11:(6, "Water Management")}
indCleantech = {1:(12, "Air & Carbon Capture"), 2:(5, "Bioenergy"), 3:(13, "Construction"), 4:(11, "Electric Motors"), 5:(8, "Energy Storage"), 6:(6, "Geothermal"), 7:(10, "Greywater"),  8:(3, "Hydropower"), 9:(9, "Lighting"), 10:(7, "Recycling"), 11:(1, "Renewables"), 12:(4, "Solar Energy"), 13:(2, "Wind Energy")}
indConsGds = {1:(1, "Automobiles & Parts"), 2:(6, "Clothing & Accessories"), 3:(3, "Consumer Electronics"), 4:(2, "Food & Beverages"), 5:(7, "Footwear"), 6:(8, "Personal & Household Goods"), 7:(4, "Recreational Products"), 8:(5, "Toys")}
indConsServ = {1:2, 2:1, 3:3}
indEnergy = {1:(1, "Equipment"), 2:(2, "Generation & Storage"), 3:(5, "Mining"), 4:(3, "Services"), 5:(4, "Utilities")}
indHlthcare = {1:3, 2:4, 3:5, 4:1, 5:2, 6:6}
indIT = {1:1, 2:2, 3:3, 4:4}
indLaw = {1:(4, "Business Law"), 2:(3, "Contract Law"), 3:(7, "Formation & Ownership"), 4:(9, "Intellectual Property"), 5:(1, "Labor Law"), 6:(8, "Liability and Insurance"), 7:(10, "Licensing"), 8:(11, "Privacy & Data Security"), 9:(5, "Private Equity Financing"), 10:(2, "Property Law"), 11:(6, "Term Sheets & Valuations")}
indManufact = {1:(1, "Additive Manufacturing"), 2:(9, "Chemicals"), 3:(5, "Food and Beverage"), 4:(2, "Industrial Supplies"), 5:(3, "Machinery"), 6:(4, "Nanotechnology"), 7:(7, "Nutraceuticals"), 8:(6, "Paints and Coatings"), 9:(8, "Pharmaceuticals"), 10:(11, "Semiconductor"), 11:(12, "Steel and Aluminum"), 12:(10, "Textiles")}
indMaterials = {1:(10, "Advanced Materials"), 2:(12, "Biomaterials"), 3:(3, "Ceramic and Glasses"), 4:(1, "Chemical and Gases"), 5:(4, "Composites"), 6:(9, "Construction Materials"), 7:(13, "Forestry and Paper"), 8:(2, "Metals"), 9:(11, "Nanomaterials"), 10:(8, "Packaging"), 11:(5, "Polymers"), 12:(6, "Semiconductors"), 13:(7, "Textiles")}
indMonetary = {1:(7, "Accounting"), 2:(8, "Alternative Financial Services"), 3:(2, "Angel Investment"), 4:(9, "Audit & Tax Services"), 5:(5, "Commercial Banking"), 6:(10, "FinTech"), 7:(6, "Insurance"), 8:(4, "Investment Banking"), 9:(1, "Private Equity"), 10:(3, "Venture Capital")}
indPubServ = {1:(1, "Education & Training Services"), 2:(2, "Emergency Services"), 3:(12, "Energy"), 4:(7, "Environmental Protection"), 5:(3, "Government"), 6:(8, "Military and Public Security"), 7:(4, "Non-Profit"), 8:(9, "Telecommunications"), 9:(6, "Transportation"), 10:(5, "Urban Planning"), 11:(10, "Waste Management"), 12:(11, "Water Supply")}
indRealEst = {1:(5, "Building Materials"), 2:(4, "Construction Management and Procurement"), 3:(6, "Construction Techniques and Sustainability"), 4:(10, "Critical Infrastructure"), 5:(9, "Green Infrastructure"), 6:(11, "Infrastructure Maintenance"), 7:(2, "Property Management"), 8:(1, "Real Estate Services"), 9:(3, "Real State Financing"), 10:(8, "Urban Infrastructure"), 11:(7, "Urban Planning")}
indTechHard = {1:(10, "Advance Systems"), 2:(1, "Computer Hardware"), 3:(3, "Consumer Electronics"), 4:(9, "Containers and Packaging"), 5:(12, "Drones"), 6:(2, "Electronic Office Equipment"), 7:(8, "Industrial Machinery"), 8:(6, "Instrumentation"), 9:(11, "Robotics"), 10:(4, "Semiconductors"), 11:(7, "Sensors and Wearables"), 12:(5, "Telecommunications Equipment")}
indTransport = {1:(9, "Aeronautics"), 2:(10, "Astronautics"), 3:(2, "Autonomous vehicles"), 4:(4, "Cargo"), 5:(1, "Commercial & Industrial Transportation"), 6:(11, "Drones"), 7:(8, "Manufacturing"), 8:(4, "Mass Transit"), 9:(5, "Mobility as a Service"), 10:(7, "Safety"), 11:(6, "Traffic Management")}
subIndMedia = {1:(11, "Arts"), 2:(8, "Audio"), 3:(1, "Broadcasting and Entertainment"), 4:(3, "Electronic and Digital Media"), 5:(6, "Gaming"), 6:(5, "Journalism"), 7:(2, "Media Agency"), 8:(9, "Photography"), 9:(10, "Print"), 10:(4, "Publishing"), 11:(7, "Video and Film")}
subIndRetail = {1:(2, "Apparel"), 2:(4, "Broadline"), 3:(6, "E-commerce"), 4:(1, "Food and Drug"), 5:(3, "Home Improvement"), 6:(5, "Specialty")}
subIndTravel = {1:(3, "Accommodations"), 2:(5, "Passenger Transportation"), 3:(1, "Recreational Services"), 4:(4, "Restaurants and Bars"), 5:(2, "Travel & Tourism")}
subIndBiotech = {1:(2, "Bioinformatics"), 2:(3, "Green Biotechnology"), 3:(4, "Red Biotechnology"), 4:(1, "Regulations")}
subIndHlthServ = {1:(2, "Clinic/Outpatient Services"), 2:(4, "Elder and Disable Care"), 3:(1, "Hospital/ Inpatient Services"), 4:(5, "Insurance"), 5:(3, "Laboratory Services")}
subIndHlthTech = {1:(2, "Decision/ Risk Analysis"), 2:(5, "Diagnostic Equipment"), 3:(8, "Digital Health"), 4:(4, "Enterprise Systems"), 5:(1, "Medical Records"), 6:(6, "Monitoring Equipment"), 7:(3, "Practice Management"), 8:(7, "Sensors & Instrumentation")}
subIndMedDev = {1:(4, "Cybersecurity"), 2:(2, "Manufacturing"), 3:(1, "R&D"), 4:(3, "Standards and Regulations")}
subIndPharm = {1:(3,  "Approval & Regulations"), 2:(1, "Discovery, R&D"), 3:(4, "Distribution"), 4:(2, "Manufacturing")}
subIndWellness = {1:(2, "Mental Fitness"), 2:(1, "Physical Fitness")}
subIndComputing = {1:(1, "Software"), 2:(2, "Artificial Intelligence"), 3:(3, "Virtual Reality"), 4:(4, "Augmented Reality"), 5:(5, "IaaS"), 6:(6, "SaaS"), 7:(7, "PaaS"), 8:(8, "IT services")}
subIndConnectiv = {1:(1, "Internet"), 2:(2, "Networking"), 3:(3, "Internet of Things"), 4:(4, "Wireless- Mobile")}
subIndDataCapt = {1:(1, "Data Analytics"), 2:(2, "Big Data"), 3:(3, "Bioinformatics"), 4:(4, "Sensors"), 5:(5, "Wearables"), 6:(6, "Imaging"), 7:(7, "Data Storage and Retrieval"), 8:(8, "Cybersecurity"), 9:(9, "Surveillance & Biometrics")}
subIndTelecomm = {1:(1, "Internet"), 2:(2, "Radio"), 3:(3, "Television"), 4:(4, "Telephony"), 5:(5, "Satellite")}
indCategory = {1:indEnergy, 2:indCleantech, 3:indHlthcare, 4:indIT, 5:indTechHard, 6:indManufact, 7:indTransport, 8:indAgriculture, 9:indMonetary, 10:indRealEst, 11:indMaterials, 12:indConsGds, 13:indConsServ, 14:indPubServ, 15:indLaw}
indHlthcareSubs = {1:subIndMedDev, 2:subIndPharm, 3:subIndBiotech, 4:subIndHlthServ, 5:subIndHlthTech, 6:subIndWellness}
indITSubs = {1:subIndComputing, 2:subIndConnectiv, 3:subIndDataCapt, 4:subIndTelecomm}
indConsServSubs = {1:subIndRetail, 2:subIndMedia, 3:subIndTravel}

# Dictionaries that map the skill responses from Qualtrics to the EiR decoder
skill = {1:8, 2:2, 3:7, 4:6, 5:1, 6:9, 7:3, 8:5, 9:10, 10:4}
businessLaw = {1:(5, "Board & Advisors"), 2:(6, "Contracts"), 3:(1, "Formation & Ownership"), 4:(2, "IP Strategy"), 5:(3, "Private Equity"), 6:(4, "Term Sheets & Valuations")}
bizModel = {1:(1, "Business Model Canvas"), 2:(4, "Customer Discovery and Validation"), 3:(3, "Revenue Models"), 4:(2, "Value Proposition")}
finMgmt = {1:(2, "Accounting"), 2:(3, "Compensation & Payroll"), 3:(10, "Exit Strategy"), 4:(1, "Financial Forecasting"), 5:(4, "Fundraising Strategy"), 6:(8, "Grants"), 7:(9, "Insurance"), 8:(5, "Private Equity"), 9:(6, "SBIR &STTR"), 10:(7, "Term Sheets & Valuations")}
mgmtHR = {1:(7, "Compensation & Payroll"), 2:(4, "Governance, Boards & Advisors"), 3:(5, "HR Management"), 4:(3, "Partnerships & Negotiations"), 5:(2, "Project Management"), 6:(6, "Recruiting & Team Building"), 7:(1, "Strategic Planning")}
marketing = {1:(4, "A/B Testing"), 2:(9, "Channels and Distribution") , 3:(3, "Consumer Behavior"), 4:(10,"Digital Marketing"), 5:(1, "Market Research and Strategy"), 6:(2, "Market Segmentation"), 7:(5, "Marketing Mix"), 8:(7, "Pricing"), 9:(11, "Product Development"), 10:(8, "Promotion"), 11:(6, "Value Proposition")}
medDev = {1:(3, "Device Design & Development"), 2:(4, "Device Production"), 3:(1, "Regulatory Strategy"), 4:(2, "Reimbursement Strategy"), 5:(5, "Wearables")}
MVPDesign = {1:(10, "3D printing"), 2:(9, "Electronic Prototyping"), 3:(1, "Focus Groups and Interviews"), 4:(3, "Graphic Design"), 5:(4, "Industrial Design"), 6:(7, "Prototyping"), 7:(11, "Recruitment of Software Developers"), 8:(2, "Survey Design"), 9:(6, "UI/UX Design"), 10:(5, "Web & Mobile Prototyping"), 11:(8, "Wire Frame Modeling")}
operations = {1:(10, "Customer Support & Call Centers"), 2:(11, "Import/ Exports"), 3:(6, "IT Management"), 4:(1, "Manufacturing Systems and Automation"), 5:(8, "Order Processing"), 6:(9, "Outsourcing"), 7:(2, "Production Control & Analysis"), 8:(3, "Safety Risk & Maintenance"), 9:(4, "Supply Chain"), 10:(7, "Transportation"), 11:(5, "Warehouse and Inventory")}
pharma = {1:(3, "Good Manufacturing Practices"), 2:(2, "Pre-Clinical Development"), 3:(1, "Regulatory Strategy")}
sales = {1:(8, "Brand Strategy"), 2:(1, "Business Development"), 3:(2, "Customer Acquisition"), 4:(6, "E-Commerce"), 5:(4, "Mobile Advertisement"), 6:(7, "Online Transaction Processing"), 7:(12, "Pitch Development"), 8:(3, "Product Launch"), 9:(10, "Promotions and Pricing"), 10:(5, "Search Engine Optimization"), 11:(9, "Social Media"), 12:(11, "Web Analytics & Metrics")}
skillDict = {1:marketing, 2: bizModel, 3:MVPDesign, 4:sales, 5:operations, 6:mgmtHR, 7:finMgmt, 8:businessLaw, 9:medDev, 10:pharma}


def decodeIndustry(rawresponses):
    responses = []

    # Converts the response fields into integer values
    for r in rawresponses:
        if r != '':
            responses.append(list(map(int, r.split(','))))
        else:
            responses.append([])

    industryEiR = []

    # Loops through all of the industry categories that were selected
    for r in responses[0]:
        categoryCode = 0
        industryCode = 0
        subIndustryCode = 0
        industryName = ''
        
        # Index to map
        i = r

        categoryCode = industry[r]
        
        # Loops through each category selected for their industries
        for industryR in responses[i]:

            # Filters out the responses for Healthcare, Information Management, and Consumer Services as they need to be handled differently due to Sub-Industries
            if categoryCode not in [3, 4, 13]:
                industryCode = indCategory[categoryCode][industryR][0]
                industryName = indCategory[categoryCode][industryR][1]
                industryEiR.append("{:02d}'{:02d}'{:02d} {}".format(categoryCode, industryCode, subIndustryCode, industryName))
            else:

                industryCode = indCategory[categoryCode][industryR]
                if categoryCode == 3:
                    # Sets the index for the responses for the given Industry to where it is in the Qualtrics data
                    subindex = 18 + industryR
                    for subIndustryR in responses[subindex]:
                        subIndustryCode = indHlthcareSubs[industryCode][subIndustryR][0]
                        industryName =  indHlthcareSubs[industryCode][subIndustryR][1]
                        industryEiR.append("{:02d}'{:02d}'{:02d} {}".format(categoryCode, industryCode, subIndustryCode, industryName))

                elif categoryCode == 4:
                    # Sets the index for the responses for the given Industry to where it is in the Qualtrics data
                    subindex = 24 + industryR
                    for subIndustryR in responses[subindex]:
                        subIndustryCode = indITSubs[industryCode][subIndustryR][0]
                        industryName =  indITSubs[industryCode][subIndustryR][1]
                        industryEiR.append("{:02d}'{:02d}'{:02d} {}".format(categoryCode, industryCode, subIndustryCode, industryName))

                elif categoryCode == 13:
                    # Sets the index for the responses for the given Industry to where it is in the Qualtrics data
                    subindex = 15 + industryR
                    for subIndustryR in responses[subindex]:
                        subIndustryCode = indConsServSubs[industryCode][subIndustryR][0]
                        industryName =  indConsServSubs[industryCode][subIndustryR][1]
                        industryEiR.append("{:02d}'{:02d}'{:02d} {}".format(categoryCode, industryCode, subIndustryCode, industryName)) 
    industryEiR = sorted(industryEiR, key=lambda x:x[:8])
    # Combines all of the EiR strings created into one singular string that is returned
    return ', '.join(industryEiR)

def decodeSkills(rawresponses):
    responses = []

    # Converts the response fields into integer values
    for r in rawresponses:
        if r != '':
            responses.append(list(map(int, r.split(','))))
        else:
            responses.append([])
    skillEiR = []

    # Loops through the selected skill categories
    for r in responses[0]:
        categoryCode = 0
        skillCode = 0
        skillName = ''

        i = r
        categoryCode = skill[r]

        # Loops through the selected skills within a given category
        for skillR in responses[i]:
            skillCode = skillDict[categoryCode][skillR][0]
            skillName = skillDict[categoryCode][skillR][1]
            skillEiR.append("{:02d}|{:02d} {}".format(categoryCode, skillCode, skillName))
    skillEiR = sorted(skillEiR, key=lambda x:x[:5])
    # Combines all of the EiR strings created into one singular string that is returned
    return ', '.join(skillEiR)
  
