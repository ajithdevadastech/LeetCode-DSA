import requests

url = 'https://updapidev.beaconhealthoptions.com/PhaseII/api/getproviders'

data = '''{"benefitPlanID":"449","zipCode":"78641","radius":"30","name":"","npi":"","taxid":"","networkFlag":1}'''

header = {'Content-Type': 'application/json'}

response = requests.post(url, data=data, headers=header)

print (response.status_code)


