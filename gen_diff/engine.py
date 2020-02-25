#import json


#def parser(file):
    #data = json.load(open(file))
    #return data


def differ(f1, f2):
    new_dict = {}
    for key, value in f1.items():
        if key in f2 and f1[key] == f2[key]:
            print(key, f1[key])   
        elif key not in f2:
            print(key, f1[key])
        elif key in f2 and f1[key] != f2[key]:
            print(key, f1[key])
    for key, value in f2.items():
        if key not in f1:
            print(key, f2[key])
    return new_dict
    
#def engine_diff(f1, f2):
    #file1 = parser(f1)
    #file2 = parser(f2)
    #diff = differ(file1, file2)
    #return diff

dict1 = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22"}
dict2 = {"timeout": 20,"verbose": 'true',"host": "hexlet.io"}
print(differ(dict1, dict2))