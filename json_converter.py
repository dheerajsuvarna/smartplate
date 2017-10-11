from nutrition import nutrition
import json

scanned_food="apple"

json_string = json.dumps(nutrition[scanned_food])

print json_string
