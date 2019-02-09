import re

def findType(type, text):
	r = re.findall(r''+type+' [^;]*;', text)
	var = []
	for i in range(len(r)):
		r[i] = re.sub(type + ' ', '', r[i])
		l = r[i].split(',')
		for x in l:
			x = re.sub(" ", "", x)
			ls = re.findall(r'[a-z|A-z|_][a-z|A-z|_|0-9]*', x)
			y = ls[0]
			if y in typeOfVar and typeOfVar[y] != type:
				invalidVar.append(y) 
			typeOfVar[y] = type
			var.append(y)

	return var

typeNames = ['int', 'string', 'char', 'bool', \
			'short int', 'long int', 'long long', \
			'long long int', 'double', 'float', 'long double']
			
def getCinEntries(text): 
	r = re.findall(r'cin[\s]*>>[^;]*;', text)
	return r
	
def replaceInput(text, cinEntries):
	for x in cinEntries:
		aux = ''
		x = x[:-1]
		l = x.split('>>')
		for y in l:
			re.sub(' ', '', y)
			if y == 'cin'
				continue
			if y in invalidVar:
				assert False
			aux += y + ' = ' + 'readType'		
			
	
			
table = {}
typeOfVar = {}
invalidVar = []

inp = input("Type line\n")

'''
for type in typeNames:
	table[type] = findType(type, inp)
	'''
getCinEntries(inp)

print (table)
print(invalidVar)