import json
with open("sent_python/newout.json", "r", encoding='utf-8') as in_file:
    data = json.load(in_file)
result = [json.dumps(record) for record in data['items']]
with open("data/database_ready.txt", 'w', encoding="utf-8") as out:
    for i in result:
        out.write(i+'\n')
