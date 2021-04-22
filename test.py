import json
from lambda_function import lambda_handler

with open('data.json') as json_file:
  data = json.load(json_file)
  trigger = data["dev_cloudwatch_trigger"]

lh = lambda_handler(event=trigger, context=None)

print(lh)