import json
import random
from flask import Flask
app = Flask('app')
# Opening JSON file
f = open('quotes.json',)
 
# returns JSON object as a dict
data = json.load(f)
# I already made a list in json called "quotes" so why am I making another list out of that list iterating through the same list? So inefficient. just going to choose a random
#quote from the list i already made in quotes.json
randquote = random.choice(data['quotes'])

@app.route('/')
def return_quote():
  return randquote

app.run(host='0.0.0.0', port=8080)
