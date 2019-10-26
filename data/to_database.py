import json
with open("data/jetblue_parsed copy.json", "r") as in_file:
    data = json.load(in_file)
result = [json.dumps(record) for record in data]
with open("data/database_ready.txt", 'w') as out:
    for i in result:
        out.write(i+'\n')
