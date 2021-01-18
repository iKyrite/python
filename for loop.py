print "ΠΡΩΤΗ ΑΣΚΗΣΗ"
for i in range (1):
    grade = input("Δώσε βαθμό: ")
    if grade >= 9 and grade <= 20:
     print "Προβιβάζεται"
    else:
     print "Απορρίπτεται"
#----------------------------------------
print "ΔΕΥΤΕΡΗ ΑΣΚΗΣΗ"

for i in range(-10, 101, 1):
    print i,
#---------------------------------------
print ""
print "ΤΡΙΤΗ ΑΣΚΗΣΗ"

for i in range (100, -2, -1):
    print i,
#---------------------------------------
print ""
print "ΤΕΤΑΡΤΗ ΑΣΚΗΣΗ"

for i in range (0, 91, 3):
    print i,    
#---------------------------------------
print ""
print ("ΠΕΜΠΤΗ ΑΣΚΗΣΗ")

numlst = []
num = 35
for i in range(num):
    numinput = input("Δώσε αριθμό: ")
    numlst.append(numinput)
    total = sum(numlst)

total = total / 35
print float(total)
#---------------------------------------
print ""
print ("ΕΚΤΗ ΑΣΚΗΣΗ")

for i in range (0, 88, 8):
    print i, 

#---------------------------------------
print ""
print ("ΕΒΔΟΜΗ ΑΣΚΗΣΗ")

sum = 0 
for i in range(1,101): 
	sum += i 
print(sum)
#---------------------------------------
print ""
print ("ΟΓΔΟΗ ΑΣΚΗΣΗ")

sum = 0 
for i in range(3,303,3): 
	sum += i 
print(sum)
#---------------------------------------
print ""
print ("ΕΝΝΑΤΗ ΑΣΚΗΣΗ")

sum = 1 
for i in range(1,101,1): 
	sum *= i 
print(sum) 
#---------------------------------------
print ""
print "ΔΕΚΑΤΗ ΑΣΚΗΣΗ"

sum = 1 
for i in range(3,33,3): 
	sum *= i 
print(sum)
#---------------------------------------
print ""
print "ΕΝΤΕΚΑΤΗ ΑΣΚΗΣΗ"

spending = input("Πόσα χρήματα ξοδεύτηκαν; ")
price = 8
people = input("Πόσα άτομα ήταν; ")
city = raw_input("Όνομα πόλης: ")
problem = raw_input("Υπήρχαν προβλήματα; (y/n) ")
peopleprice = people * price
profitprice = spending - peopleprice
lossprice = peopleprice - spending
if profitprice > peopleprice and problem.lower() == 'n ':
    print "Έχεις κέρδος:", profitprice
elif lossprice < peopleprice and problem.lower() == 'y ':
    print "Kέρδος:", "-" + str(lossprice),"Να μην επαναληφθεί η συναυλία το επόμενο καλοκαίρι"
elif lossprice < peopleprice and problem.lower() == 'n ':
    print "Kέρδος:", "-" + str(lossprice)
elif lossprice > peopleprice and problem.lower() == 'y ':
    print "Kέρδος:", profitprice,"Να μην επαναληφθεί η συναυλία το επόμενο καλοκαίρι"
else:
    print "Δεν καταλαβαινω"
