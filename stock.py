import requests
stocks = input("Enter the stock  Name:")
url = "https://api.api-ninjas.com/v1/stockprice?ticker=AAPL"

payload = ""
headers = {
  'X-Api-Key': 'a4f6SlPqvwrWa/xRiW1sGg==L32QYXtSlyISzGk3'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    stock_price = data['price']
    print("The price of the stock is:", stock_price)
    
result = response.json()
    