__author__ = 'PyBeaner'

basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None

import json

with open("basic.json",mode="w",encoding="utf-8") as f:
    json.dump(basic_entry,f,indent=2)



# byte,tuple are not serializable by json
basic_entry['internal_id'] = b'\xDE\xD5\xB4\xF8' # not JSON serializable
with open("basic.json",mode="w",encoding="utf-8") as f:
    # json.dump(basic_entry,f,indent=2)
    import custom_to_json
    json.dump(basic_entry,f,default=custom_to_json.to_json)