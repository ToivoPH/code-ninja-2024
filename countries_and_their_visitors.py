#exercise 1
'''
while True:
  line = input('> ')
  if line[0] == '#':
    continue
  if line.startswith('#'):
    line = 'done'
  if line == 'done':
    break
  print(line)
print('Done!')
'''
#exercise 2
'''
str = 'avg_session_duration: 211.90007144372942'
slice = slice(21, 39)
num = str[slice]
print(float(num))
'''
#note 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels') 'In 3 years I have spotted 0.1 camels.'
#useful items
'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits
to the right of the dot.
'''
#exercise 3
'''
strip will remove the trailing spaces on the left and right of the string.
replace will replace the first argument with the second.
'''
#exercise 4-5
'''
Python f-strings provide a quick way to interpolate and format strings. They're readable, concise, and less prone to error.
'''
import os
import glob
import json

fname = glob.glob("./**/countries.txt")
#get to the local files
# if len(local_list) < 1:
  # print('query is wrong. no files being extracted. Rerun code.')

file = open(fname[0]).readlines()
# with open(fname[0]) as file:
  # for line in file.readlines()

# countryVisitorDict = {
#   'country': [],
#   'visitors': [],
  
# }


country = []
visitors = []
main_output = []
uppercase_country = []

for x in file:
  if x.find('"country"') >= 0:
    country.append(x[18:-4])
    
for x in country:
  uppercase_country = [word.upper() for word in country]

for x in file:    
  if x.find('"active_visitors"') >= 1:
    visitors.append(x[26:-3])

x = zip(uppercase_country, visitors)

with open('results/countries_and_visitors.txt', 'w') as f:
  #sent to the results folder
  for (u, v) in x:
    content = f"{u} {v}\n"
    #f string as learnt in class
    #curly brackets are for telling what is going to be 
    #the string
    f.write(content)#write the formatted string in

# quicker way using dict()   :-)
countryVisitorDict = dict(zip(uppercase_country, visitors))
# turn it into JSON format

visitorDictJson = json.dumps(countryVisitorDict) # the string to write to the file
print(visitorDictJson)

# write to the file
f = open("results/countries_and_visitors.json", "a")
f.write(visitorDictJson)
f.close()

#get the total number of countries, the total number of visitors
total_countries = len(country)

total_visitors_per_country = 0
for i in range(len(visitors)):
  total_visitors_per_country += i
total_visitors = total_visitors_per_country

#csv formatting
#use the dictionary that is on line 87
import csv


 
# name of csv file
filename = "results/visitors_countries_csvfile.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['country_name', 'nr_visitors'])
    writer.writeheader()

    for c, v in countryVisitorDict.items():
      # print({ 'country_name': c, 'nr_visitors': v })
      writer.writerow({ 'country_name': c, 'nr_visitors': v })