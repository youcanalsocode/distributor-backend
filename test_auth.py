import requests
import time

def test():
    print("Testing Registration...")
    res = requests.post("http://localhost:8000/restaurant/register", json={
        "mobile": "9988776655",
        "password": "securepassword",
        "name": "Gourmet Kitchen",
        "address": "456 Food Ave"
    })
    print("Register Response:", res.status_code, res.json())

    print("\nTesting Login...")
    res2 = requests.post("http://localhost:8000/restaurant/login", json={
        "mobile": "9988776655",
        "password": "securepassword"
    })
    print("Login Response:", res2.status_code, res2.json())

if __name__ == "__main__":
    time.sleep(2) # wait for server
    test()
