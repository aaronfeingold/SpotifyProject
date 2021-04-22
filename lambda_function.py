import os
import json
from main import Main

###For dev purposes
# with open('data.json') as json_file:
#   data = json.load(json_file)
#   trigger = data["dev_cloudwatch_trigger"]

def lambda_handler(event, context):
   main = Main()
   response = main.run_main()

   return response



###Dev tests
# lh = lambda_handler(event=trigger, context=None)

# print(lh)