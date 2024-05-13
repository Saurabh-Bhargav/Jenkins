# connectiontest.py

import requests

def test_connection(url):
    try:
        response = requests.head(url, timeout=10)
        if response.status_code == 200:
            print(f"Connection to {url} successful!")
        else:
            print(f"Failed to connect to {url}. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}. Connection error.")
    except requests.Timeout:
        print(f"Connection to {url} timed out.")

if __name__ == "__main__":
    website_url = input("Enter the URL to test connection: ")
    test_connection(website_url)
