
import requests

end_point = 'http://127.0.0.1:8000/api/'

# sending th json data from frontend

# response = requests.get(end_point,json={'data':'this data from frontend json'})
# print(response.json())
# print(response.status_code)

# QUERY PARAMETERS THAT PASSED THROUGH THE http://127.0.0.1:8000/api/?category=mobile 

# response = requests.get(end_point,params={'category':'mobile'})
# print(response.json())
# print(response.status_code)

# GETTING THE MODELS DATA'S
# response = requests.get('http://127.0.0.1:8000/api/products/')
# print(response.json())


# REST API FUNCTION CALL
response = requests.get('http://127.0.0.1:8000/api/rest_fun/')
print(response.json())