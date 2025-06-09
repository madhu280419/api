import requests

model = input("Enter the car model: ")
url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
payload = ""
headers = {
  'X-Api-Key': 'a4f6SlPqvwrWa/xRiW1sGg==L32QYXtSlyISzGk3',  
  
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    make = data[0]['make']
    print(make)
    

result = response.json()

