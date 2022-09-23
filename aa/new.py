import json
a_file = open("sample_file.json", "r")
json_object = json.load(a_file)
a_file.close()

for item in json_object:
    item['fields'] = 
    
print(type(json_object))
print(json_object[0])
a_file = open("sample_file.json", "w")
json.dump(json_object, a_file)
a_file.close()
