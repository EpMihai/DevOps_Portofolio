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
# În acest script, folosim biblioteca requests pentru a face o cerere HTTP GET către un site web dat. 
# Dacă site-ul returnează un cod de stare HTTP 200, atunci considerăm că site-ul este disponibil. 
# În caz contrar, afișăm un mesaj că site-ul nu este disponibil împreună cu codul de stare HTTP returnat.
# Scriptul este apoi rulat într-o buclă infinită folosind while True, astfel încât să verifice site-ul la intervale regulate de timp (în acest caz, la fiecare 60 de secunde)
# Aceasta ar putea fi o modalitate simplă de a monitoriza disponibilitatea unui site web și de a primi notificări în cazul în care acesta nu este disponibil.
