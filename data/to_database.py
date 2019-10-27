import json
with open("southwest_output_data.json", "r") as in_file:
    data = json.load(in_file)
result = [json.dumps(record) for record in data['items']]
with open("southwest_database_ready.txt", 'w') as out:
    for i in result:
        out.write(i+'\n')
