import requests
import json



# plans =['BEAU',
# 'BRHC',
# 'CHV',
# 'DAC',
# 'DED',
# 'DIA',
# 'EGHI',
# 'EHCO',
# 'ESG',
# 'FEL',
# 'GBHC',
# 'GMC',
# 'HNEC',
# 'ICS',
# 'KADB',
# 'KAHN',
# 'KAHP',
# 'KANC',
# 'KASC',
# 'KNSF',
# 'LCO',
# 'NIS',
# 'NYS',
# 'OEF',
# 'OWC',
# 'PGE',
# 'PPPC',
# 'SABC',
# 'SAG',
# 'SHL',
# 'SMW',
# 'SUF',
# 'TRH',
# 'UFC',
# 'UFL',
# 'UICO',
# 'UPS']


plans = ['CHV']
zipcode = '79705'
serviceType = ''

CAurl = 'https://jarvisdev.beaconhealthoptions.com/services/client-contract/details.service?token=cHJpY2luZ3Rvb2wg'
#updurl = 'https://updapidev.beaconhealthoptions.com/api/getproviders'
updurl = 'https://updapi.beaconhealthoptions.com/api/getproviders'
header = {'Content-Type': 'application/json'}

CAarr = []

for plan in plans:
    data = '''{
    "parentCode":"'''+ plan + '''",
    "clientLibrary":"O" 
}'''
    responseCA = requests.post(CAurl, data=data, headers=header, timeout=10)
    print (responseCA.json())
    CAjson = responseCA.json()
    contractCode = CAjson['clientContract']['contractCode']
    associationCodes = CAjson['clientContract']['associationCodes']
    benefitPlanArr = ""
    for ac in associationCodes:
        benefitPlan = contractCode + "-" + ac
        benefitPlanArr = benefitPlanArr + benefitPlan.strip() + ","
    #remove the last comma
    benefitPlanArr = benefitPlanArr[:-1]

    data = '''{"benefitPlanID":"''' + benefitPlanArr + '''","zipCode":"''' + zipcode + '''","serviceType":"''' + serviceType + '''","radius":"30","name":"","npi":"","taxid":"","networkFlag":1, "sourceApp":"CAS"}'''
    response = requests.post(updurl, data=data, headers=header, timeout=60)
    UPDjson = response.json()
    print(UPDjson)
    npi = []
    for i in UPDjson:
        npi.append(i['npi'])
    print (benefitPlanArr + " : " + str(response.status_code))
    print (npi)


# for plan in plans:
#     data = '''{"benefitPlanID":"''' + plan + ''''","zipCode":"78641","radius":"30","name":"","npi":"","taxid":"","networkFlag":1}'''
#     response = requests.post(url, data=data, headers=header)
#     print (plan, response.status_code)
