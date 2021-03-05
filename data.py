# https://opentdb.com/api_config.php

import  requests

parameters = {
    "amount":10,
    "type":"boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
