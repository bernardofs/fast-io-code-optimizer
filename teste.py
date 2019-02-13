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
	r = re.findall(r'cin[\s\t\n]*>>[^;,]*[;,]', text)
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
	r = re.findall(r'cout[\s\t\n]*<<[^;,]*[;,]', text)
	return r

def removeDeSync(text):
	r = []
	r += re.findall(r'[{;,][^{;,]*sync_with_stdio[^;,]*[;,]', text)
	r += re.findall(r'[{;,][^{;,]*cin[\s\t\n]*.[\s\t\n]*tie[^;,]*[;,]', text)
	r += re.findall(r'[{;,][^{;,]*cout[\s\t\n]*.[\s\t\n]*tie[^;,]*[;,]', text)

	for entry in r:
		entry = entry[1:]
		text = text.replace(entry, '')

	return text


def replaceOutput(text, coutEntries):
	for entry in coutEntries:
		aux = ''
		last = entry[-1]
		# delete semicolon (;) or comma (,) from line
		x = entry[:-1]
		l = x.split('<<')
		# delete cout from list
		l.pop(0)
		for y in l:
			aux += 'writeVar(' + removeSpacesFromVar(y) + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(entry, aux)

	return text

inp = (open("input.txt", "r")).read()
inp = removeDeSync(inp)

x = getCinEntries(inp)
inp = (replaceInput(inp, x))

x = getCoutEntries(inp)
inp = (replaceOutput(inp, x))

print (inp)
