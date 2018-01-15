from Intellivoid.Service import Service

API = Service('http://example.com/v1/api_service', 'SERVICE_AUTH_KEY')
GeneratedKey = API.generateKey(1000)

print('Public Key: %s' %(GeneratedKey['PublicKey']))
print('Auth Key: %s' %(GeneratedKey['AuthKey']))