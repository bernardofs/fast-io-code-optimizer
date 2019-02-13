import re

def removeSpacesFromVar(name):
	
	i = 0
	while name[i] in ['\t', ' ', '\n']:
		i += 1

	j = len(name) - 1
	while name[j] in ['\t', ' ', '\n']:
		j -= 1

	return name[i : j + 1]	

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
			aux += 'readVar(' + removeSpacesFromVar(y) + ')' + ', '
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
			aux += 'writeVar(' + removeSpacesFromVar(y) + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(entry, aux)

	return text

inp = (open("input.txt", "r")).read()

x = getCinEntries(inp)
inp = (replaceInput(inp, x))

x = getCoutEntries(inp)
inp = (replaceOutput(inp, x))

print (inp)
