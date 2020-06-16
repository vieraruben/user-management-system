import json

def sava_data(filepath, data):
  with open(filepath, 'w') as outfile:
    json.dump(data, outfile)

def load_data(filepath):
  with open(filepath, 'r') as file:
    return json.load(file)
