import requests

def test_jenkins_connection(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Connection successful! Jenkins is reachable.")
        else:
            print(f"Failed to connect to Jenkins. Status code: {response.status_code}")
    except requests.ConnectionError:
        print("Failed to connect to Jenkins. Check the URL and try again.")

if __name__ == "__main__":
    jenkins_url = "http://192.168.233.130:8080" 
    test_jenkins_connection(jenkins_url)
