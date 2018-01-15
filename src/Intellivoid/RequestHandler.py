import requests
import json

class RequestError(Exception):
	"""Handles any Request errors
	"""

	pass

class RequestHandler:
	"""Sends and handles requests
	"""

	def __init__(self, Host):
		"""Public Consturctor
		
		Arguments:
			Host {[type]} -- The API endpoint to send the requests to
		"""

		self.Host = Host

	def sendRequest(self, Data, HandleError = False):
		"""Sends a request using the requests library
		
		Arguments:
			Data {[type]} -- Post data to send with the request
		
		Keyword Arguments:
			HandleError {[type]} -- If the response indicates that the request failed, It will handle the error. (default: {False})
		
		Raises:
			RequestError -- If the response from the server failed, The error will be handled
			RequestError -- If the response from the server failed, The error will be handled
		"""

		Request = requests.post(self.Host, data=Data)
		RequestData = None

		try:
			RequestData = json.loads(Request.text)
		except ValueError:
			raise RequestError('Server returned an unknown response: %s' % (Request.text))

		if(HandleError == True):
			if(Request.status_code == 200):
				return(Request)
			else:
				ErrorCode = Request.status_code
				Reason = RequestData['text']
				Message = RequestData['message']
				raise RequestError('Error Code: %s (%s) %s' % (ErrorCode, Reason, Message))
		else:
			return(Request)