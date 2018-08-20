def func(level):
	test  = {
		'test':'perfect!',
		'test2':'A',
		'test3':'B',
	 	'test4':'C',
	 	'test5':'D'
	}
	return test.get(level, 'E')

def switchfun(level):
	print("switchfun:",level)
	test = level {
		'test':lambda:func('test'),
		'test1':lambda:func('test1'),
		'test2':lambda:func('test2'),
		'test3':lambda:func('level4'),ㄢ
		}.get(level, lambda:func('test4'))

print(func('test'))
print(func('test2'))
print(func('test6'))
switchfun('test3')

