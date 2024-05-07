import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is available.")
        else:
            print(f"Website {url} is not available. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to website {url}")

if __name__ == "__main__":
    website_url = "https://www.example.com"
    while True:
        check_website(website_url)
        time.sleep(60)  # Verifică site-ul la fiecare 60 de secunde
