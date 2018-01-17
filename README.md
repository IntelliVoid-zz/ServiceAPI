# ServiceAPI
A Python class for interacting with the Service API for Intellivoid API, This class basically sends `POST` requests to the provided endpoint and reads the response using `json`

# Introduction
This API allows you to interact with your service without the need of logging into the control panel, granted not all features are available such as the ability to view the request log. This API is designed as a way for your server to determine the state and status of your service easily, while giving the ability to properly setup your server to work with Intellivoid API

# Making requests
You can either use a `POST` or `GET` via HTTP as a request method to make calls to the service API, However each request requires the following parameters: `action` and `service_authkey`

`service_authkey` is where you provide your service auth key in order to prove you have the permissions to make changes. And `action` is what you will provide to specify the action you want to take, below you can see all the available actions you can use

The examples shown in this documentation will be using a python class that will handle both sending the request and understanding the response, Alternatively this can easily be achieved with just POST Requests followed by the required parameters that will also be shown in the documentation

---
## Examples


### Disable Service
This action will disable your service, when a consumer makes a request with a valid API key they will be blocked from accomplishing a successful request followed by the reason you specify. This is useful if your server is undergoing updates and cannot handle requests for the time being.
```python
from Intellivoid.Service import Service
API = Service('API_ENDPOINT_URL', 'SERVICE_AUTHKEY')
API.disableService('Undergoing server updates')
```
---

### Enable Service
Once you are ready to make your service available again, using the enableService action will enable your service again

```python
from Intellivoid.Service import Service
API = Service('API_ENDPOINT_URL', 'SERVICE_AUTHKEY')
API.disableService('Undergoing server updates')
```
---

### Generate Key
This will allow you to generate a key for a consumer to use, Followed by the amount of quota it should start with once the key is activated by the consumer. In response you will get basic information about the key such as the `PublicKey`, `AuthKey` and `Quota`

```python
from Intellivoid.Service import Service
API = Service('API_ENDPOINT_URL', 'SERVICE_AUTHKEY')
Response = API.generateKey(500)

print("Public Key: %s" %(Response['PublicKey']))
print("Auth Key: %s" %(Response['AuthKey']))
print("Quota: %s" %(str(Response['Quota'])))
```
---
### Get API Key information
This allows you to retrieve basic information about a API Key by the consumer’s Public Key

```python
from Intellivoid.Service import Service
API = Service('API_ENDPOINT_URL', 'SERVICE_AUTHKEY')
Response = API.getKey('- The public API Key of the consumer -')

print("Public Key: %s" %(Response['PublicKey']))
print("Auth Key: %s" %(Response['AuthKey']))
print("Quota: %s" %(str(Response['Quota'])))
print("Status: %s" %(str(Response['Status'])))
print("Registered Username: %s" %(str(Response['RegisteredUsername'])))
```
---
### Suspend Key
This action will suspend the API Key using the public api key from being further used, The consumer will no longer be able to successfully send requests without being stopped with the message saying that the key has been suspended, And the consumer will no longer be able to access the control panel and will be logged out if the consumer is already logged in

```python
from Intellivoid.Service import Service
API = Service('API_ENDPOINT_URL', 'SERVICE_AUTHKEY')
API.suspendKey('- The public API Key of the consumer -')
```
---
### Reinstate API Key
If a key was previously suspended, This suspension can be lifted by using the reinstate key action which will restore the key to it’s previous state

```python
from Intellivoid.Service import Service
API = Service('API_ENDPOINT_URL', 'SERVICE_AUTHKEY')
API.reinstateKey('- The public API Key of the consumer -')
```
---
### Fetch all keys
This will retrieve all the API Keys that are associated with your service, followed by the associated information for each key

```python
from Intellivoid.Service import Service
API = Service('http://localhost/intellivoid-systems/v1/api_service.php', '588edf4d7402fa7486bb029be9ff85ba13f8ee1df9922338c71307595143216d')
for Key in API.fetchKeys():
    print("Public Key: %s" %(Key['PublicKey']))
    print("Auth Key: %s" %(Key['AuthKey']))
    print("Quota: %s" %(str(Key['Quota'])))
    print("Status: %s" %(str(Key['Status'])))
    print("Registered Username: %s" %(str(Key['RegisteredUsername'])))
```
---
### Increase Quota
This action will allow you to increase the quota of a activated API Key

```python
from Intellivoid.Service import Service
API = Service('http://localhost/intellivoid-systems/v1/api_service.php', '588edf4d7402fa7486bb029be9ff85ba13f8ee1df9922338c71307595143216d')
API.addQuota('- The public API Key of the consumer -', 500):
```
---
## Documentation notice
A further detailed version of this documentation can be found on the control panel (service) followed by the examples being prefixed with the appropriate information such as your service auth key and the api endpoint url, including the document being available in other languages that the control panel has available 


---
# License
MIT License

Copyright (c) 2018 Intellivoid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
