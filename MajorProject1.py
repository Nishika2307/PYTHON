cities=eval(input("enter a list"))
cleaned_cities=list()
for i in l:
    i=i.capitalize()
    if i not in cleaned_cities:
        cleaned_cities.append(i)

cleaned_cities.sort()
print(cleaned_cities)

#i/p:-['Kyiv', 'Kharkiv', 'Odessa', 'Kyiv', 'Lviv', 'Kharkiv', 'Dnipro']


 #mission2:
cleaned_citiess=set(cleaned_cities)
#print(cleaned_citiess)

previous_intel=eval(input("enter previous intel"))
print(cleaned_citiess.union(previous_intel))
print(previous_intel.symmetric_difference(cleaned_citiess))
high_alert_cities=cleaned_citiess.intersection(previous_intel)
print(high_alert_cities)

#i/p:- {'Kyiv', 'Mariupol', 'Lviv', 'Donetsk'}

city_data=eval(input("enter city data in a tuple inside list form:"))
high_alert_cities_info=dict()
population=0
aid_request=0
for  i in city_data:
    if i[0] in high_alert_cities:
       high_alert_cities_info[i[0]]=i
       population+=i[1]
       aid_request+=i[2]

print(high_alert_cities_info)
print("population sum:",population)
print("total aid number:",aid_request)

#i/p:-[('Kyiv', 2800000, 250), ('Kharkiv', 1431000, 180), ('Lviv',721301, 90), ('Odessa', 1029049, 120)]

#mission4:
supplies=eval(input("enter supplies"))
dsupplies=dict()
for i in supplies:
    dsupplies[i[0]]=dict({i[1]:i[2]})

print(dsupplies)

#i/p:- [('Kyiv', 'Food', 500), ('Moscow', 'Medicines', 200), ('Lviv', 'Water', 300), ('Saint Petersburg', 'Blankets', 100), ('Kharkiv', 'Food', 150)]
