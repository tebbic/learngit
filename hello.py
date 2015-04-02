#this is a hello.py
class Student(object):
	def __init__(self,name,age):
		self.__name=name
		self.__age=age
	def print(self):
		print 'name:%s,age:%d'%(self.__name,self.age)

