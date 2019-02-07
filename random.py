import csv

creaturelist={}
creaturetable=[]

with open('D&D 5e Monster List with Ability Scores.csv', encoding = "ISO-8859-1") as csvfile:
    table = csv.DictReader(csvfile)
    for row in table:
        creaturelist[str(row['Name'])] = [row['Type'], row['ALIGNMENT'],
                                          row['Size'], row['CR'], row['AC'], row['HP'],
                                          row['STR'], row['DEX'], row['CON'], row['INT'],
                                          row['WIS'], row['CHA'], row['Total Points (sum of ability scores)'],
                                          row['Arctic'], row['Coast'], row['Desert'], row['Forest'],
                                          row['Grassland'], row['Hill'], row['Mountain'], row['Swamp'],
                                          row['Underdark'], row['Underwater'], row['Urban']]

        creaturetable.append(row['Name'])

creaturetable.sort()

print(creaturetable)