#This program defines a Binary class that supports fraction. Currently I only write the "add" function and "multiply" function. I may write more if I need more. 
num1 = input("Input first number: ")
num2 = input("Input second number: ")

def BinaryAdd(a,b):
	new_str = ''
	extra = 0
	n = max(len(a),len(b)) + 1
	for i in range(n):
		Sum = extra
		if len(a) - i > 0:
			Sum += int(a[len(a) - i - 1])
		if len(b) - i > 0:
			Sum += int(b[len(b) - i - 1])
		if Sum == 0:
			extra = 0
			new_str = '0' + new_str
		if Sum == 1:
			extra = 0
			new_str = '1' + new_str
		if Sum == 2:
			extra = 1
			new_str = '0' + new_str
		if Sum == 3:
			extra = 1
			new_str = '1' + new_str
	if new_str == '':
		return 0
	return int(new_str)
#print (BinaryAdd('11','11'))

class Binary:
	def __init__(self,int_part, dec_part):
		self.int_part = int_part
		self.dec_part = dec_part
	def add(self,x):   # x is a Binary class
		new_number = Binary('0','0')
		new_number.int_part = str(BinaryAdd(self.int_part,x.int_part))
		last = ''
		if len(x.dec_part) > len(self.dec_part):
			last = x.dec_part[len(self.dec_part):]
			new_number.dec_part = str(BinaryAdd(self.dec_part , x.dec_part[:len(self.dec_part)]))
			if len(new_number.dec_part) > len(self.dec_part):
				new_number.dec_part = new_number.dec_part[1:]
				new_number.int_part = str(BinaryAdd(new_number.int_part,'1'))
		else:
			last = self.dec_part[len(x.dec_part):]
			new_number.dec_part = str(BinaryAdd(x.dec_part , self.dec_part[:len(x.dec_part)]))
			if len(new_number.dec_part) > len(x.dec_part):
				new_number.dec_part = new_number.dec_part[1:]
				new_number.int_part = str(BinaryAdd(new_number.int_part, '1'))
		new_number.dec_part += last
		return new_number
	def Display(self):
		print(self.int_part+'.'+self.dec_part)
	def multiply(self,x):
		new_number = Binary('0','0')
		ldec = len(x.dec_part)
		lint = len(x.int_part)

		for i in range(lint):
			if(x.int_part[lint-i-1] == '1'):
				temp = Binary(self.int_part,self.dec_part)
				for j in range(i):
					temp.int_part += temp.dec_part[0]
					temp.dec_part = temp.dec_part[1:]
					if temp.dec_part == '':
						temp.dec_part = '0'
				new_number = new_number.add(temp)
		for i in range(ldec):
			if(x.dec_part[i] == '1'):
				temp = Binary(self.int_part,self.dec_part)
				for j in range(i+1):
					temp.dec_part = temp.int_part[-1] + temp.dec_part
					temp.int_part = temp.int_part[:-1]
					if temp.int_part == '':
						temp.int_part = '0'

				new_number = new_number.add(temp)
		return new_number
	def Display_Decimal(self):
		int_part = 0
		for i in self.int_part:
			int_part = int_part * 2 + int(i)
		dec_part = 0
		number = 5
		for i in self.dec_part:
			dec_part += number * int(i)
			number *= 5
			dec_part*=10
		print(str(int_part)+'.'+str(dec_part))


a = Binary(num1.split('.')[0],num1.split('.')[1])
b = Binary(num2.split('.')[0],num2.split('.')[1])
c = a.multiply(b)
c.Display_Decimal()