first_value = input('Enter the first value: ')
second_value = input('Enter the second value: ')
operation = input('Operation: ')


# Первое Значение


if len(first_value) == 1:
	n1 = (ord(first_value[0])-48) * 1
	n0 = n1
if len(first_value) == 2:
	n1 = (ord(first_value[0])-48) * 10
	n2 = (ord(first_value[1])-48) * 1
	n0 = n1+n2
if len(first_value) == 3:
	n1 = (ord(first_value[0])-48) * 100
	n2 = (ord(first_value[1])-48) * 10
	n3 = (ord(first_value[2])-48) * 1
	n0 = n1+n2+n3
if len(first_value) == 4:
	n1 = (ord(first_value[0])-48) * 1000
	n2 = (ord(first_value[1])-48) * 100
	n3 = (ord(first_value[2])-48) * 10
	n4 = (ord(first_value[3])-48) * 1
	n0 = n1+n2+n3+n4
if len(first_value) == 5:
	n1 = (ord(first_value[0])-48) * 10000
	n2 = (ord(first_value[1])-48) * 1000
	n3 = (ord(first_value[2])-48) * 100
	n4 = (ord(first_value[3])-48) * 10
	n5 = (ord(first_value[4])-48) * 1
	n0 = n1+n2+n3+n4+n5
if len(first_value) == 6:
	n1 = (ord(first_value[0])-48) * 100000
	n2 = (ord(first_value[1])-48) * 10000
	n3 = (ord(first_value[2])-48) * 1000
	n4 = (ord(first_value[3])-48) * 100
	n5 = (ord(first_value[4])-48) * 10
	n6 = (ord(first_value[5])-48) * 1
	n0 = n1+n2+n3+n4+n5+n6
if len(first_value) == 7:
	n1 = (ord(first_value[0])-48) * 1000000
	n2 = (ord(first_value[1])-48) * 100000
	n3 = (ord(first_value[2])-48) * 10000
	n4 = (ord(first_value[3])-48) * 1000
	n5 = (ord(first_value[4])-48) * 100
	n6 = (ord(first_value[5])-48) * 10
	n7 = (ord(first_value[6])-48) * 1
	n0 = n1+n2+n3+n4+n5+n6+n7
if len(first_value) == 8:
	n1 = (ord(first_value[0])-48) * 10000000
	n2 = (ord(first_value[1])-48) * 1000000
	n3 = (ord(first_value[2])-48) * 100000
	n4 = (ord(first_value[3])-48) * 10000
	n5 = (ord(first_value[4])-48) * 1000
	n6 = (ord(first_value[5])-48) * 100
	n7 = (ord(first_value[6])-48) * 10
	n8 = (ord(first_value[7])-48) * 1
	n0 = n1+n2+n3+n4+n5+n6+n7+n8


# Второе Значение


if len(second_value) == 1:
	n1 = (ord(second_value[0])-48) * 1
	n00 = n1
if len(second_value) == 2:
	n1 = (ord(second_value[0])-48) * 10
	n2 = (ord(second_value[1])-48) * 1
	n00 = n1+n2
if len(second_value) == 3:
	n1 = (ord(second_value[0])-48) * 100
	n2 = (ord(second_value[1])-48) * 10
	n3 = (ord(second_value[2])-48) * 1
	n00 = n1+n2+n3
if len(second_value) == 4:
	n1 = (ord(second_value[0])-48) * 1000
	n2 = (ord(second_value[1])-48) * 100
	n3 = (ord(second_value[2])-48) * 10
	n4 = (ord(second_value[3])-48) * 1
	n00 = n1+n2+n3+n4
if len(second_value) == 5:
	n1 = (ord(second_value[0])-48) * 10000
	n2 = (ord(second_value[1])-48) * 1000
	n3 = (ord(second_value[2])-48) * 100
	n4 = (ord(second_value[3])-48) * 10
	n5 = (ord(second_value[4])-48) * 1
	n00 = n1+n2+n3+n4+n5
if len(second_value) == 6:
	n1 = (ord(second_value[0])-48) * 100000
	n2 = (ord(second_value[1])-48) * 10000
	n3 = (ord(second_value[2])-48) * 1000
	n4 = (ord(second_value[3])-48) * 100
	n5 = (ord(second_value[4])-48) * 10
	n6 = (ord(second_value[5])-48) * 1
	n00 = n1+n2+n3+n4+n5+n6
if len(second_value) == 7:
	n1 = (ord(second_value[0])-48) * 1000000
	n2 = (ord(second_value[1])-48) * 100000
	n3 = (ord(second_value[2])-48) * 10000
	n4 = (ord(second_value[3])-48) * 1000
	n5 = (ord(second_value[4])-48) * 100
	n6 = (ord(second_value[5])-48) * 10
	n7 = (ord(second_value[6])-48) * 1
	n00 = n1+n2+n3+n4+n5+n6+n7
if len(second_value) == 8:
	n1 = (ord(second_value[0])-48) * 10000000
	n2 = (ord(second_value[1])-48) * 1000000
	n3 = (ord(second_value[2])-48) * 100000
	n4 = (ord(second_value[3])-48) * 10000
	n5 = (ord(second_value[4])-48) * 1000
	n6 = (ord(second_value[5])-48) * 100
	n7 = (ord(second_value[6])-48) * 10
	n8 = (ord(second_value[7])-48) * 1
	n00 = n1+n2+n3+n4+n5+n6+n7+n8

#Операция

if operation == '+':
	answer = n0 + n00
if operation == '-':
	answer = n0 - n00
if operation == '*':
	answer = n0 * n00
if operation == '/':
	answer = n0 / n00

#Ответ
print('Answer: ' + '%s %s %s = %s' %(first_value, operation, second_value, answer))
