for i in range (0, 31, 3):
    print i,

numbers = [100,15,20,8,7]
sortednums = sorted(numbers)
print numbers , sortednums
print len(sortednums)

cities=["city0","city1","city2","city3","city4","city5","city6"]
even = []
odd = []
#i = 0
for i in range(0, len(cities), 2):
    if i % 2 == 0:
        even.append(cities[i])
        
    else:
        odd.append(cities[i])
    
print "even: ", even        


numlist = []

amount = input("Dwse plhthos listas: ")
for i in range (amount):
    nums = input("Dwse arithmo: ")
    numlist.append(nums)

numlist.sort()
print numlist
