import re

def findType(type, text):
	# find all declarations of type
	r = re.findall(r''+type+' [^;]*;', text)
	var = []
	for i in range(len(r)):
		r[i] = re.sub(type + ' ', '', r[i])
		l = r[i].split(',')
		for x in l:
			x = re.sub(" ", "", x)
			ls = re.findall(r'[a-z|A-Z|_][a-z|A-Z|_|0-9]*', x)
			y = ls[0]
			# if it was declared as other type it is invalid
			if y in typeOfVar and typeOfVar[y] != type:
				invalidVar.append(y) 
			typeOfVar[y] = type
			var.append(y)
	return var

def getCinEntries(text):
	# check comma
	r = re.findall(r'cin[\s]*>>[^;,]*[;,]', text)
	print ('r = ' , r)
	return r

def replaceInput(text, cinEntries):
	for entry in cinEntries:
		aux = ''
		last = entry[-1]
		# delete semicolon (;) or comma (,) from line
		x = entry[:-1]
		l = x.split('>>')
		# delete cin from list
		l.pop(0)
		for y in l:
			# remove all unuseful spaces
			y = re.sub(' ', '', y)
			# if it was declared as two different types the program stops
			if y in invalidVar:
				assert False
			aux += y + ' = ' + 'readType' + ', '
		aux = aux[:-2] + last
		text = re.sub(entry, aux, text)
	return text


table = {}
typeOfVar = {}
invalidVar = []

typeNames = ['int', 'string', 'char', 'bool', \
			'short int', 'long int', 'long long', \
			'long long int', 'double', 'float', 'long double']

inp = input("Type line\n")

for type in typeNames:
	table[type] = findType(type, inp)

x = getCinEntries(inp)
print (replaceInput(inp, x))

print (table)
print(invalidVar)