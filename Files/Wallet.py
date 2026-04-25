# Yeh bina entity secret ke - old API use karta hai

import requests
import uuid

API_KEY = "TEST_API_KEY:b1beeb711246a7b7206dcaf9c16d92fe:fb82a6566d5d81123f3cad2094f8cff1"

# Try old endpoint
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Direct wallet create (without wallet set)
resp = requests.post(
    "https://api-sandbox.circle.com/v1/wallets",  # Old endpoint
    headers=headers,
    json={
        "idempotencyKey": str(uuid.uuid4()),
        "blockchain": "MATIC-AMOY"
    }
)

print(f"Old API Status: {resp.status_code}")
print(resp.text[:500])
