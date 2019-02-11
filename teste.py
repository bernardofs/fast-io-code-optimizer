import re

def getCinEntries(text):
	r = re.findall(r'cin[\s\t]*>>[^;,]*[;,]', text)
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
			aux += y + ' = ' + 'readVar(' + y + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(entry, aux)
	return text

def getCoutEntries(text):
	r = re.findall(r'cout[\s\t]*<<[^;,]*[;,]', text)
	return r

def replaceOutput(text, coutEntries):
	for entry in coutEntries:
		print (entry)
		aux = ''
		last = entry[-1]
		# delete semicolon (;) or comma (,) from line
		x = entry[:-1]
		l = x.split('<<')
		# delete cout from list
		l.pop(0)
		print (l)
		for y in l:
			aux += 'writeVar(' + y + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(entry, aux)

	return text

table = {}
typeOfVar = {}
invalidVar = []
usedTypes = []

readFunctionOfType = {
	'int': 'readSInt()',
	'string': 'readString()',
	'char': 'readChar()',
	'bool': 'readBool()',
	'short int': 'readSInt()',
	'long int': 'readSInt()',
	'long long': 'readSInt()',
	'long long int': 'readSInt()',
	'double': 'readFloating()',
	'float': 'readFloating()',
	'long double': 'readFloating()',
}

typeNames = ['int', 'string', 'char', 'bool', \
			'short int', 'long int', 'long long', \
			'long long int', 'double', 'float', 'long double']

inp = (open("input.txt", "r")).read()


x = getCinEntries(inp)
inp = (replaceInput(inp, x))

x = getCoutEntries(inp)
inp = (replaceOutput(inp, x))

print (inp)
