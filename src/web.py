import json
import random
from flask import Flask
app = Flask('app')
# Opening JSON file
f = open('quotes.json',)
 
# returns JSON object as a dict
data = json.load(f)
all_quotes=[]
#iterating through the json, making the dict into a list
for i in data['quotes']:
  all_quotes.append(i)
  pass

randquote = random.choice(all_quotes)

@app.route('/')
def return_quote():
  return randquote

app.run(host='0.0.0.0', port=8080)
