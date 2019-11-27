import json
import re
x = '{"Satarday": "1", "Sunday": 2,"Monday": "3","Thursday":"4","Wednesday":"5","Tursday":"6""Friday":"7"}'

print(json.dumps(x,indent=4))


RegEX = "data is the new oil"

y = re.search("data",RegEX)
print(y)
