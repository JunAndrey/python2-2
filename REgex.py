from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',')
    data_list = list(data)

pattern = r"(\+7|8)?\s*(\(?(\d{3})\)?)[-\s]?(\d{3})-?(\d{2})-?(\d{2})\s?\(?(доб.)?\s*(\d{4})?\)?"
pattern1 = r"+7(\3)\4-\5-\6 \7\8"

new_line = []

for row in data_list:
    index = 1
    new_line.append([])
    for row_1 in row:

        if ' ' in row_1 and index < 3:
            datt = row_1.split(' ')
            datt_num = 0
            for bio in datt:
                new_line[-1].append(datt[datt_num])
                datt_num += 1
            passlen = len(datt) - 1
        elif index == 6:
            new_line[-1].append(re.sub(pattern, pattern1, row_1))
        elif index < 4 and row_1 == '' and passlen != 0:
            passlen -= 1
            pass
        elif index > 7:
            pass
        else:
            new_line[-1].append(row_1)
        index += 1

iop = []
for index, item in enumerate(new_line[1:]):
    for index_1, item_1 in enumerate(new_line[1:]):
        if index != index_1 and item[0] == item_1[0]:
            zipped_file = zip(item, item_1)
            iop.append([])
            for i, j in list(zipped_file):
                if i == j:
                    iop[-1].append(i)
                elif i == '' and j != '':
                    iop[-1].append(j)
                else:
                    iop[-1].append(i)

new_iop = []
[new_iop.append(item) for item in iop if item not in new_iop]
new_line_fin = []
for line in new_iop: new_line_fin.append(line)

for line in new_line[::-1]:
    for line_1 in new_line_fin:
        if line[0] == line_1[0]:
            new_line.remove(line)

for line in new_line_fin:
    new_line.append(line)
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    ddd = datawriter.writerows(new_line)
