from dbg import dbg


if __name__ == '__main__':
	
	@dbg
	def f():
		a = 1
		@dbg
		def f1():
			a = 0
		f1()
		
		for i in range(10):
			a+=i

	f()
