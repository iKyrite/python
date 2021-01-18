students = 8
grades = []
for i in range (students):
    grade = input("Bathmos: ")
    grades.append(grade)
    
total = int(sum(grades))
average = total / 8
print "xamhloteros bathmos: ", min(grades)
print "megistos mathmos: ",max (grades)
print "mesos oros: ", average
