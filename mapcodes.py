import csv



with open('journal-map.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    journalMap = {rows['TITLE']:rows['CODE'] for rows in reader}

with open('example.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(journalMap[row['TITLE']])