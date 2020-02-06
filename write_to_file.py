import json

def prep_contents_for_json(contents):
    new_contents = dict()
    new_contents['data'] = contents
    return json.dumps(new_contents)

def write_to_json_file(filename, contents):
    try:
        content_json = prep_contents_for_json(contents)
        with open(filename, 'w') as file:
            file.write(content_json)
    except:
        print('failed to write ' + filename)
        print(contents)