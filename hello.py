import requests

# Transaction hash
tx_hash = '77ef13bf55da97330bbccabed5508c965ecb235daa9de7f53de8b5c141efa447'

# BlockCypher API endpoint for Bitcoin mainnet transaction details
url = f'https://api.blockcypher.com/v1/btc/main/txs/{tx_hash}'

# Optional: If you have an API key, you can include it in the query parameters (not required for basic usage)
# api_key = 'your_api_key_here'
# response = requests.get(url, params={'token': api_key})

# Sending the GET request
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Printing the response as JSON
    tx_data = response.json()
    print(tx_data)
else:
    print(f"Error: Unable to fetch data, received status code {response.status_code}")

