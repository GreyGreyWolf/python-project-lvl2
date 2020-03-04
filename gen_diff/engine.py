import json
f1 ={"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22"}
f2 = {"timeout": 20, "verbose": 'true', "host": "hexlet.io"}
status = {'any': '+', 'removed': '-', 'unchanged': ' '}


def parser(to_file):
    data = json.load(open(to_file))
    return data


def differ(f1, f2):
    x = f1.keys()
    y = f2.keys()
    result = list()
    for elem in x & y:
        result.extend(make_choice(elem, f1[elem], f2[elem]))
    for elem in x - y:
        result.append(select_removed(elem, f1[elem]))
    for elem in y - x:
        result.append(select_added(elem, f2[elem]))
    return result


def make_choice(elem, f1, f2):
    new_dict = {}
    if f1 == f2:
        new_dict = (assign_status(status['unchanged'], elem, f1), )
    elif f1 != f2:
       new_dict = (assign_status(status['removed'], elem, f1), assign_status(status['any'], elem, f2))
    return new_dict


def select_removed(elem, f1):
    return assign_status(status['removed'], elem, f1)


def select_added(elem, f2):
    return assign_status(status['any'], elem, f2)


def assign_status(status, key, value):
    return (status, key), value


def convert(data):
    result_dict = {}
    for i in data:
        s_tuple = i[0]
        s_string = ' ' + s_tuple[0] + ' ' + s_tuple[1]
        result_dict.update(dict([(s_string, i[1])]))
    return result_dict
    
def engine_diff(f1, f2):
    file1 = parser(f1)
    file2 = parser(f2)
    diff = differ(file1, file2)
    diff = convert(diff)
    diff = json.dumps(diff, indent=1, separators=(" ", ":"))
    return diff

#op = differ(f1, f2)
#print(len(op))
#print(op[0])
#for i in op:
    #a = i[0]
    #b = a[0] + ' ' + a[1]
    #print(a[0])
    #print(a[1])
    #print(b)
    #print(type(b))
#    print(i[0])
#   print(i[1])
#p = convert(op)
#print(p)