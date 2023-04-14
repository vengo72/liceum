import json
import datetime as dt

system = input()
date = input()
a1 = int(date[:4])
b1 = int(date[5:7])
c1 = int(date[8:])
sdate = dt.date(a1, b1, c1)
d = set()
with open('light.json') as cat_file:
    f = cat_file.read()
    data = json.loads(f)
    for item in data:
        for value in data[item]:
            a = int(item[:4])
            b = int(item[5:7])
            c = int(item[8:])
            if value['type'] == 'bar':
                my_date = dt.date(a, b, c)
                if my_date < sdate:
                    d.add(value['galaxy'])
print(', '.join(sorted(d)))
