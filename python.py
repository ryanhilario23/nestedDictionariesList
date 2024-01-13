"""
x = [
    [5,2,3],
    [10,8,9]
    ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [
    {'x': 10, 'y': 20}
    ]

#change value from 10 to 15 in x
x[1][0] = 15
print(x)

#change name to Bryant
students[0]['last_name'] = "Bryant"
print(students[0]['last_name'])
#change name from Messi to Andres
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])
#change 10 to 15 in 'z'
z[0]['y'] = 30
print(z)

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python
print('----------')


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#print the dictionary list
def iterateDictionary(someList):
    for i in range(len(someList)):
        print('first_name - ' + someList[i]['first_name']+"," +' last_name - ' + someList[i]['last_name'])
#Print the dictionary
iterateDictionary(students)
print('----------')

def iterateDictionary(key,someList):
    for i in range(len(someList)):
        print(someList[i][key])

print("First Name:")
iterateDictionary('first_name',students)

print("Last Name:")
iterateDictionary('last_name',students)
print('----------')

"""
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(dojo)
def printinfo(some_dict):
    print('----------')
    #Locations
    print(str(len(some_dict['locations'])) + ' LOCATIONS')

    for i in range(len(some_dict['locations'])):
        print(some_dict['locations'][i])
    #instructors
    print('----------')
    print(str(len(some_dict['instructors'])) + ' INSTRUCTORS')

    for i in range(len(some_dict['instructors'])):
        print(some_dict['instructors'][i])
    

printinfo(dojo)
"""
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""
