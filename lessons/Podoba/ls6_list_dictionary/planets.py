#initialize dictionary
planets = {}

#add new values
planets['Earth'] = 12756
planets['Mercury'] = 4880
planets['Jupiter'] = 142740
planets['Pluton'] = 5420

#function has_key()
if planets.has_key('Earth'):
    print u"Земля - частина нашої соонячної системи"
else:
    print u"Земля зникла?"

#try function keys()
print u"Наші планети:"
print planets.keys()

#make list of keys
keys = planets.keys()

#show values of dictionary
print u"Радіуси планет бувають:", planets.values()

#make list of values
values = planets.values()

#sort
print keys
keys.sort()
print keys

print values
values.sort()
print values

#count
print u"Кількість планет: ", len(planets)

