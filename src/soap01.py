import zeep
# import datetime

wsdl = 'http://currencyconverter.kowabunga.net/converter.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
curr1 = 'USD'
curr2 = 'INR'
lastUpdateDate = client.service.GetLastUpdateDate()
# print lastUpdateDate
print 'Conversation rate from %s to %s is: %s as of %s' %(curr1, curr2, client.service.GetConversionRate(curr1, curr2, lastUpdateDate), lastUpdateDate)
