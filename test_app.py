import requests
import time

def test_api():
    max_retries = 3
    wait_time = 2  # seconds
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                'http://localhost:5000/predict',
                data={
                    'Age': 35,
                    'Gender': 'Male',
                    'Vehicle_Age': '1-2',
                    'Vehicle_Damage': 'Yes',
                    'Annual_Premium': 50000,
                    'Vintage': 200
                },
                timeout=5
            )
            print("Test Successful!")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
            return
            
        except requests.exceptions.ConnectionError:
            if attempt < max_retries - 1:
                print(f"Connection failed - retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            print("\nERROR: Could not connect to the server.")
            print("Make sure 'python app.py' is running in another terminal!")
        except Exception as e:
            print("Unexpected error:", str(e))
            break

if __name__ == "__main__":
    test_api()