import requests
import base64
import json

def ocr(IMAGE_PATH):
        try:
                with open(IMAGE_PATH, 'rb') as fp:
                    response = requests.post(
                        'https://api.platerecognizer.com/v1/plate-reader/',
                        files=dict(upload=fp),
                        headers={'Authorization': 'Token 6e4cf241a2942991d08a2f444cdb6946fc61429e'})
                results = response.json()
                return results['results'][0]['plate']
        except:
                print("No number plate found")
