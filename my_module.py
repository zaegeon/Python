def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

class Test:
	def __init__(self, name):
		self.name = name
	
	def hello(self):
		print(f'안녕하세요, {self.name}님!')