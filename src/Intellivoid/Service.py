import json
from Intellivoid.RequestHandler import RequestHandler

class Service:
	"""A class to handle the Service API for Intellivoid API
	"""

	def __init__(self, EndPoint, ServiceAuthKey):
		"""Public Constructor
		
		Arguments:
			EndPoint {[type]} -- The Service API Endpoint
			ServiceAuthKey {[type]} -- Your service Auth key
		"""

		self.RequestHandler = RequestHandler(EndPoint)
		self.ServiceAuthKey = ServiceAuthKey

	def disableService(self, Reason):
		"""Disables the service, Followed by a reason
		
		Arguments:
			Reason {[type]} -- The reason why the service is disabled
		"""

		self.RequestHandler.sendRequest({'action': 'disableService', 'service_authkey': self.ServiceAuthKey, 'reason': Reason}, True)
		return(True)

	def enableService(self):
		"""Enables the service if it's disabled
		"""

		self.RequestHandler.sendRequest({'action': 'enableService', 'service_authkey': self.ServiceAuthKey}, True)
		return(True)

	def generateKey(self, Quota = 500):
		"""Generates a API Key for the consumer to use, Followed by a starting quota
		
		Keyword Arguments:
			Quota {[type]} -- The quota amount that this key should start with once it's activated (default: {500})
		"""

		Response = self.RequestHandler.sendRequest({'action': 'generateKey', 'service_authkey': self.ServiceAuthKey, 'quota': Quota}, True)
		ResponseData = json.loads(Response.text)
		return(ResponseData['response'])

	def getKey(self, APIKey):
		"""Returns information about a API Key
		
		Arguments:
			APIKey {[type]} -- The public API Key from the consumer
		"""

		Response = self.RequestHandler.sendRequest({'action': 'getKey', 'service_authkey': self.ServiceAuthKey, 'apiKey': APIKey}, True)
		ResponseData = json.loads(Response.text)
		return(ResponseData['response'])

	def suspendKey(self, APIKey):
		"""Suspends a API Key
		
		Arguments:
			APIKey {[type]} -- The public API Key from the consumer
		"""

		self.RequestHandler.sendRequest({'action': 'suspendKey', 'service_authkey': self.ServiceAuthKey, 'apiKey': APIKey}, True)
		return(True)

	def reinstateKey(self, APIKey):
		"""Reinstates a suspended API Key
		
		Arguments:
			APIKey {[type]} -- The public API Key from the consumer
		"""

		self.RequestHandler.sendRequest({'action': 'reinstateKey', 'service_authkey': self.ServiceAuthKey, 'apiKey': APIKey}, True)
		return(True)

	def fetchKeys(self):
		"""Fetches all API keys associated with your service
		"""

		Response = self.RequestHandler.sendRequest({'action': 'fetchKeys', 'service_authkey': self.ServiceAuthKey}, True)
		ResponseData = json.loads(Response.text)
		return(ResponseData['response'])

	def increaseQuota(self, APIKey, Quota = 500):
		"""Increases the quota of a API Key
		
		Arguments:
			APIKey {[type]} -- The public API Key from the consumer
		
		Keyword Arguments:
			Quota {[type]} -- The amount of quota to increase to the key (default: {500})
		"""

		self.RequestHandler.sendRequest({'action': 'increaseQuota', 'service_authkey': self.ServiceAuthKey, 'apiKey': APIKey, 'quota': Quota}, True)
		return(True)
