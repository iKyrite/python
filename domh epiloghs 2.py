# coding= utf-8
print "ΠΡΩΤΗ ΑΣΚΗΣΗ"

age = input("Δώσε την ηλικία σου: ")
if age >= 18:
    print "Μπορείς να βγάλεις δίπλωμα οδήγησης."
else:
    print "Δεν μπορεις να βγάλεις δίπλωμα οδήγησης."
#---------------------------------------------------
print "ΔΕΥΤΕΡΗ ΑΣΚΗΣΗ"

parallelage = input("Δώσε την ηλικία σου: ")
if parallelage >= 18:
    print "Μπορείς να βγάλεις δίπλωμα οδήγησης."
else:
    leftage = 18 - parallelage
    print "Μπορείς να βγάλεις δίπλωμα οδήγησης σε", leftage, "χρόνια."
#---------------------------------------------------
print "ΤΡΙΤΗ ΑΣΚΗΣΗ"
grade = input("Δώσε τον πρώτο βαθμό: ")
grade1 = input("Δώσε τον δεύτερο βαθμό: ")
grade2 = input("Δώσε τον τρίτο βαθμό: ")
grade3 = input("Δώσε τον τέταρτο βαθμό: ")
finalgrade = (grade + grade1+ grade2 + grade3) / 4
if finalgrade >= 15:
    print "Επιτυχών"
else:
    print "Μη Επιτυχών"
#----------------------------------------------------
print "ΤΕΤΑΡΤΗ ΑΣΚΗΣΗ"
adult = 8
minor = 6
population = input("Πόσα άτομα ειστε; ")
populat = input("Πόσοι ειναι πάνω απο 18; ")
popu = input("Πόσοι ειναι κάτω απο 18; ")
if popu <= 18 > populat:
    finalpopu = popu * 6
    finalpopulat = populat * 8
    print "Θα πληρώσουν",finalpopulat,"ευρώ, Οι ενήλικοι."
    print "Θα πληρώσoyn",finalpopu,"ευρώ, οι ανήλικοι"
#----------------------------------------------------
print "ΠΕΜΠΤΗ ΑΣΚΗΣΗ"
num = input("Δώσε αριθμό: ")

if (num % 2) == 0:
    print "Ο αριθμός", num, "είναι ζυγός αριθμός."
else:
    print "Ο αριθμός", num, "είναι μονός αριθμός."
