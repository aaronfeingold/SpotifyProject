import os
import json
from main import Main


def lambda_handler(event, context):
   main = Main(cache_path='../cache.txt')
   response = main.run_main()

   return response

