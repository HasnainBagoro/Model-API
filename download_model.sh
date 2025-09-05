import requests

url = "https://github.com/HasnainBagoro/Model-API/releases/download/Model/rf_url_model.pkl"
print("Downloading model...")
r = requests.get(url)
with open("rf_url_model.pkl", "wb") as f:
    f.write(r.content)
print("Model downloaded!")
