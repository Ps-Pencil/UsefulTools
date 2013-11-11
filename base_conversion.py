#Base conversions. Up to base 35. (Above base 35, I do not know how to represent the numbers.)
def convert(number,base_from, base_to):
	num_dec=0
	power=0
	number=number.upper()
	while number!="":
		digit=0
		if(number[-1].isdigit()):
			digit=int(number[-1])
		else:
			digit=ord(number[-1])-ord('A')+10
		num_dec+=digit*(base_from**power)
		power+=1
		number=number[:-1]
	res_list=[]
	while num_dec!=0:
		digit=num_dec%base_to
		if(digit>9):
			digit=chr(ord('A')+digit-10)
		num_dec//=base_to
		res_list=[str(digit)]+res_list
	return "".join(res_list)

#for test purposes. Enter EOF (Ctrl+C on linux, Ctrl+D on Windows) to end
while True:
	number=input("Enter the number you want to convert: ")
	fro=input("Base the number is in (eg. 2,8,10,16...): ")
	to=input("Base to convert to(eg. 2,8,10,16...): ")
	print(convert(number,int(fro),int(to)))
	print()