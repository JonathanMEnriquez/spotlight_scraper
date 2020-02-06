import json

with open('contents.json', 'r') as j:
    d = j.read()
    data = json.loads(d)
data = data['data']

ids_seen = dict()
i = 0

print('before cleanup: {}'.format(len(data)))

while i < len(data):
    if not ids_seen.get(data[i]['id']):
        ids_seen[data[i]['id']] = 1
        img_src = str(data[i]['img_src'])
        data[i]['img_src'] = img_src.replace('-1024x576', '')
        i = i + 1
    else:
        data.pop(i)


res = json.dumps({'data': data})

with open('contents_cleaned.json', 'w') as file:
    file.write(res)

print('after cleanup: {}'.format(len(data)))