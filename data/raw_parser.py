import json

input_file = 'data/southwestair.json'
output_file = 'data/southwestair_parsed.json'

new_data = {'items': []}


with open(input_file, encoding='utf-8', mode='r') as in_file:
    data = json.load(in_file)

for gimage in data['GraphImages']:
    caption = {}
    overcaption = gimage['edge_media_to_caption']['edges']
    caption['text'] = overcaption[0]['node']['text']
    caption['time'] = gimage['taken_at_timestamp']
    new_data['items'].append(caption)
    for comment in gimage['edge_media_to_comment']['data']:
        obj = {}
        obj['time'] = comment['created_at']
        obj['text'] = comment['text']
        new_data['items'].append(obj)

print(new_data)

with open(output_file, 'w') as out_file:
    json.dump(new_data, out_file)
