input_list = [1,4,5,6,23,54,34,212]

def div_by_two(num):
	if num % 2 ==0:
		return True
	else:
		return False


abc = (i for i in input_list if div_by_two(i))
[print(i) for i in abc]
print(abc)
print("*********************")

abc = (i for i in input_list if div_by_two(i))
print(abc)
print("*********************")

abc = [i for i in input_list if div_by_two(i)]
print(abc)
print("*********************")


[print(i) for i in abc]	 
print("*********************")

[[print(i,ii) for ii in range(5)] for i in range(5)] 
print("*********************")

xyz = ([[i,ii] for ii in range(5) for i in range(5)])
print(xyz)


