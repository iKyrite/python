print "����� ������"
for i in range (1):
    grade = input("���� �����: ")
    if grade >= 9 and grade <= 20:
     print "������������"
    else:
     print "������������"
#----------------------------------------
print "������� ������"

for i in range(-10, 101, 1):
    print i,
#---------------------------------------
print ""
print "����� ������"

for i in range (100, -2, -1):
    print i,
#---------------------------------------
print ""
print "������� ������"

for i in range (0, 91, 3):
    print i,    
#---------------------------------------
print ""
print ("������ ������")

numlst = []
num = 35
for i in range(num):
    numinput = input("���� ������: ")
    numlst.append(numinput)
    total = sum(numlst)

total = total / 35
print float(total)
#---------------------------------------
print ""
print ("���� ������")

for i in range (0, 88, 8):
    print i, 

#---------------------------------------
print ""
print ("������ ������")

sum = 0 
for i in range(1,101): 
	sum += i 
print(sum)
#---------------------------------------
print ""
print ("����� ������")

sum = 0 
for i in range(3,303,3): 
	sum += i 
print(sum)
#---------------------------------------
print ""
print ("������ ������")

sum = 1 
for i in range(1,101,1): 
	sum *= i 
print(sum) 
#---------------------------------------
print ""
print "������ ������"

sum = 1 
for i in range(3,33,3): 
	sum *= i 
print(sum)
#---------------------------------------
print ""
print "�������� ������"

spending = input("���� ������� ����������; ")
price = 8
people = input("���� ����� ����; ")
city = raw_input("����� �����: ")
problem = raw_input("������� ����������; (y/n) ")
peopleprice = people * price
profitprice = spending - peopleprice
lossprice = peopleprice - spending
if profitprice > peopleprice and problem.lower() == 'n ':
    print "����� ������:", profitprice
elif lossprice < peopleprice and problem.lower() == 'y ':
    print "K�����:", "-" + str(lossprice),"�� ��� ����������� � �������� �� ������� ���������"
elif lossprice < peopleprice and problem.lower() == 'n ':
    print "K�����:", "-" + str(lossprice)
elif lossprice > peopleprice and problem.lower() == 'y ':
    print "K�����:", profitprice,"�� ��� ����������� � �������� �� ������� ���������"
else:
    print "��� �����������"
