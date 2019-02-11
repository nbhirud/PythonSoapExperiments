# from zeep import Client
#
# client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
# result = client.service.ConvertSpeed(
#     100, 'kilometersPerhour', 'milesPerhour')
#
# assert result == 62.137


import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))