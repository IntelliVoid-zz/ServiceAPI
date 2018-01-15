# ServiceAPI
A Python class for interacting with the Service API for Intellivoid API, This class basically sends `POST` requests to the provided endpoint and reads the response using `json`

---
## Examples

- Disable Service
```python
from Intellivoid.Service import Service

API = Service('http://example.com/v1/api_service', 'SERVICE_AUTH_KEY')
API.disableService('Undergoing Updates')
```

- Generate Key
```python
from Intellivoid.Service import Service

API = Service('http://example.com/v1/api_service', 'SERVICE_AUTH_KEY')
GeneratedKey = API.generateKey(1000)

print('Public Key: %s' %(GeneratedKey['PublicKey']))
print('Auth Key: %s' %(GeneratedKey['AuthKey']))
```

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
