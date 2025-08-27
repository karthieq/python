import json

people = '''
{
  "people": [
    {
      "name": "Karthik",
      "phone": "1234",
      "emails": ["a@com", "b@com"],
      "has_license": false
    },
    {
      "name": "Keyan",
      "phone": "5678",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

print(type(people))
data = json.loads(people)
print(type(data))
for person in data['people']:
    print(person['name'])
for person in data['people']:
    del person['phone']

new_people = json.dumps(data, indent=2, sort_keys=True)
print(type(new_people))
print(new_people)

with open('sample.json', 'r') as f:
    data = json.load(f)

print(type(data))

data['Source'] = 'EMCC'
with open('sample_mod.json', 'w') as f:
    json.dump(data, f, indent=2)
