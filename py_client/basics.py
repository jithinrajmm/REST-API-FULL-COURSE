
from urllib import response
import requests


end_point = 'https://httpbin.org/'


get_response = requests.get(end_point)
print(get_response.text)
# the get_response.text return the all code related to the webpage as in the form of html
# this is like a sorce code of a web site

#______________________________________________________________________________________________________

end_point = 'https://httpbin.org/anything'
get_response = requests.get(end_point)
print(get_response.text)
''' THIS CODE RETURN THE JSON RESPONSE '''
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.28.1", 
#     "X-Amzn-Trace-Id": "Root=1-6333c8d6-03dc7fb754dd7b7e646c50ae"
#   }, 
#   "json": null, 
#   "method": "GET", 
#   "origin": "122.164.10.72", 
#   "url": "https://httpbin.org/anything"
# }


# HTTP REQUEST => RETURNING html
# REST API HTTP REQUEST RETURNING => JSON 
# JAVASCRIPT OBJECT NOTATION IS ALMOST SAME AS DICTIONARY IN PYTHON

print(get_response.json())
# {'args': {}, 'data': '', 
# 'files': {}, 
# 'form': {}, 
# 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-6333ca6d-61500ca1717db2112d471638'}, 
# 'json': None, 'method': 'GET', 'origin': '122.164.10.72', 'url': 'https://httpbin.org/anything'}
'''now this is completely python dictionary , notice that the 'json': Null value changed to None, .json() returning the actual python 
dictionary '''

# SENDING DATA 
end_point = 'https://httpbin.org/anything'
get_response = requests.get(end_point,json={'name': 'jithin raj mm','designation': 'software Engineer'})
print(get_response.json())

# {'args': {}, 'data': '{"name": "jithin raj mm", "designation": "software Engineer"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 
# 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '61', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-6333cbd4-6cbeebb951b85af058c2e267'}, 
# 'json': {'designation': 'software Engineer', 'name': 'jithin raj mm'},
#  'method': 'GET', 'origin': '122.164.10.72', 'url': 'https://httpbin.org/anything'}

''' Here we can see that the data feild is filled with our data that send through the json key in request.get() '''

# also we can pass the data ,changed the json to data 
get_response = requests.get(end_point,data={'name': 'jithin raj mm','designation': 'software Engineer'})
print(get_response.json())

# Output

# {'args': {}, 'data': '', 'files': {}, 'form': {'designation': 'software Engineer', 'name': 'jithin raj mm'}, 
# 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '48', 
# 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 
# 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-6333cc76-07e7a7296c0d8f730b73a3d4'}, 
# 'json': None, 'method': 'GET', 'origin': '122.164.10.72', 'url': 'https://httpbin.org/anything'}

''' Notice the output of this file , the earliest code the json data send throug the data part, but now that sending the 
data throug form part '''

# ALSO WE CAN SHOW THE STATUS CODE ALSO

print(get_response.status_code)
# the output is 200

