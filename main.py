import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        print("Weather:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    city = input("Enter a city: ")
    get_weather(city)
