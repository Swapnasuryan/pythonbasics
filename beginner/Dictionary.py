#dictonary = a changeble, unorderd collection of unique key:value pairs
#               fast because they use hashing, allow us to access a vlue quickly

capitals = {'USA':'Washington', 'INDIA':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
#print(capitals)
#for key,value in capitals.items():
 #   print(key,value)

#print(capitals['Germany'])
#print(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las vegas'})
capitals.pop('China')
capitals.clear()
for key,value in capitals.items():
    print(key,value)
