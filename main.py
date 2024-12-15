import requests
from datetime import datetime

APP_ID = YOUR_API_ID
API_KEY = YOUR_API_KEY

GENDER = "Female"
YOUR_WEIGHT = WEIGHT_KG
YOUR_HEIGHT = HEIGHT_CM
YOUR_AGE = 19
YOUR_USERNAME = USERNAME
YOUR_PASSWORD = PASSWORD
YOUR_TOKEN = YOUR_SECRET_TOKEN

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = YOUR_EXERCISE_ENDPOINT
sheet_endpoint = YOUR_SHEET_ENDPOINT

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": YOUR_WEIGHT,
    "height_cm": YOUR_HEIGHT,
    "age": YOUR_AGE,
}

response = requests.post(exercise_endpoint, json= parameters, headers=headers)
result = response.json()
print(result)

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%H:%M:%S")

if "exercises" in result:
    for exercise in result["exercises"]:
        sheet_parameters = {
            "workout": {
                "date": today_date,
                "time": current_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
    }
    
    #Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {YOUR_TOKEN}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_parameters, 
        headers=bearer_headers
    )

    print(sheet_response.text)