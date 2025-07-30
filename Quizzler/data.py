import requests

parameter={"amount":10,"type":"boolean","category":18}
responce=requests.get(url="https://opentdb.com/api.php",params=parameter)
question_data=responce.json()["results"]


