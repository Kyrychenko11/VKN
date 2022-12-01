A = set() 
B = set() 
C = set() 

def mult(multNum, multSet):
	for i in range(100):
		i += 1
		if(i%multNum == 0):
			multSet.add(i)


mult(2, A)
mult(3, B)
mult(5, C)

print(A&B&C) 
print((B&C)-A)
print((C-A)-B) 


