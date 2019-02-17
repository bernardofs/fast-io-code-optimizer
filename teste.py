import re

prototypes = (open("prototypes.cpp", "r")).read()

auxVariablesToRead = 'char readCharacter; bool remaining = false;'

warningBackslashMessage = '''
/*
....................... WARNING .......................
.. It was found a \\ (Backslash) symbol in your file ...
.... This software doesn\'t support multiline code .....
............. and may not work as expected ............
.......................................................
*\\

'''  

definedStrings = {}

def joinTuple(tuple):
	return ''.join(tuple)

def coverStrings(text):
	r = []
	r += re.findall(r'[^\\]\"(?:(?![^\\]\").)*[^\\]\"', text)
	r += re.findall(r'[^\\]\'(?:(?![^\\]\').)*[^\\]\'', text)
	for i in range(len(r)):
		r[i] = r[i][1:]
		definedStrings[i] = r[i]
		text = text.replace(r[i], '¿¿¿¿¿' + str(i) + '¿¿¿¿¿')

	return text

def uncoverStrings(text):
	for key, value in definedStrings.items():
		text = text.replace('¿¿¿¿¿' + str(key) + '¿¿¿¿¿', value)

	return text

def removeSpacesFromVar(name):
	
	i = 0
	while name[i] in ['\t', ' ', '\n']:
		i += 1

	j = len(name) - 1
	while name[j] in ['\t', ' ', '\n']:
		j -= 1

	return name[i : j + 1]

def getCinEntries(text):
	r = re.findall(r'[\s\t\n,;()]*(std[\s\t]*::[\s\t]*|)(cin[\s\t\n]*>>[^;{}\n]*[;{}\n])', text)
	ret = []
	for entry in r:
		entry = joinTuple(entry)
		iter = re.finditer(r"([\s\t\n,;()]*)(std[\s\t]*::[\s\t]*|)(cin)", entry)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while entry[i] != 'c' and entry[i] != 's':
				i += 1
			s = entry[i]
			# variable to check if brackets are balanced at that moment	
			bra = 0
			# variable to check if parenthesis are balanced at that moment	
			par = 0
			while (not entry[i] in [',', ';', '&', '|', '\n']) or (par != 0) or (bra != 0):
				if entry[i] == '(':
					par += 1
				elif entry[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif entry[i] == '[':
					bra += 1
				elif entry[i] == ']':  		
					bra -= 1
					if bra < 0:
						break

				i += 1
				s += entry[i]
			ret.append(s)				
	return ret

def replaceInput(text, cinEntries):
	for entry in cinEntries:
		aux = ''
		last = entry[-1]
		# delete special characters like semicolon (;) or comma (,) from line
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
	r = re.findall(r'[\s\t\n,;()]*(std[\s\t]*::[\s\t]*|)(cout[\s\t\n]*<<[^;{}\n]*[;{}\n])', text)
	ret = []
	for entry in r:
		entry = joinTuple(entry)
		iter = re.finditer(r"([\s\t\n,;()]*)(std[\s\t]*::[\s\t]*|)(cout)", entry)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while entry[i] != 'c' and entry[i] != 's':
				i += 1
			s = entry[i]
			# variable to check if brackets are balanced at that moment	
			bra = 0
			# variable to check if parenthesis are balanced at that moment	
			par = 0
			while (not entry[i] in [',', ';', '&', '|', '\n']) or (par != 0) or (bra != 0):
				if entry[i] == '(':
					par += 1
				elif entry[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif entry[i] == '[':
					bra += 1
				elif entry[i] == ']':  		
					bra -= 1
					if bra < 0:
						break

				i += 1
				s += entry[i]
			ret.append(s)				
	return ret


def removeDeSync(text):
	r = []
	# remove all desync
	r += re.findall(r'(std[\s\t]*::[\s\t]*|)(ios[\t\s]*::|ios_base[\t\s]*::)([\t\s]*sync_with_stdio[\t\s]*\([\t\s]*)([^\)]*)([\t\s]*\)[\t\s]*[,;\n])', text)
	r += re.findall(r'(std[\s\t]*::[\s\t]*|)(cin|cout)([\s\t]*\.[\s\t]*tie[\s\t]*\([\s\t]*)([^\)]*)([\s\t]*\)[\s\t]*[;,\n])', text)

	# replace desync with 0
	for entry in r:
		entry = joinTuple(entry)
		last = entry[-1]
		entry = entry[:-1]
		text = text.replace(entry + last, '0' + last)

	# remove all define endl	
	r = re.findall(r'[\n]#[\s\t]*define[\s\t]*endl', text)
	for entry in r:
		entry = entry[1:]
		text = text.replace(entry, '#define jlakjasdhfheyhidfkjvcbhd')


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
		# print (entry)
		for y in l:
			aux += 'writeVar(' + removeSpacesFromVar(y) + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(entry, aux)

	return text

def getGetlineEntriesAndReplace(text):
	r = re.findall(r'getline[\s\t]*\([^;{}\n]*[;{}\n]', text)
	for entry in r:
		iter = re.finditer(r"[\s\t\n,;()]*getline", entry)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while entry[i] != 'g':
				i += 1
			i += 8
			s = 'getline('
			# variable to check if brackets are balanced at that moment	
			bra = 0
			# variable to check if parenthesis are balanced at that moment	
			par = 0
			while (entry[i] != ',') or (par != 0) or (bra != 0):
				if entry[i] == '(':
					par += 1
				elif entry[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif entry[i] == '[':
					bra += 1
				elif entry[i] == ']':  		
					bra -= 1
					if bra < 0:
						break
				s += entry[i];
				i += 1
			s += ',';
			i += 1	
			var = ''
			while (entry[i] != ')') or (par != 0) or (bra != 0):
				if entry[i] == '(':
					par += 1
				elif entry[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif entry[i] == '[':
					bra += 1
				elif entry[i] == ']':  		
					bra -= 1
					if bra < 0:
						break

				s += entry[i]
				var += entry[i]
				i += 1
			s += ')'
			var = re.sub(' ', '', var)
			text = text.replace(s, 'readGetline(' + var + ')')		
	return text

def undefMacros(text):

	r = []
	r += re.findall(r'#[\s\t]*define[\s\t]+[^\s\t]+\([^\n\)]*\)', text)
	r += re.findall(r'#[\s\t]*define[\s\t]+[^\s\t\(]*', text)

	undefs = '\n\n'
	for entry in r:
		entry = re.sub(r'#[\s\t]*define', '#undef', entry)
		entry = re.sub(r'\([^\)]*\)', '', entry)
		entry += '\n'
		undefs += entry

	text += undefs

	return text

def replaceCinIgnore(text):
	r = re.findall(r'(std[\s\t]*::[\s\t]*|)(cin[\s\t]*\.[\s\t]*ignore[\s\t]*\([\s\t]*\))', text)
	for entry in r:
		text = text.replace(entry, 'if(remaining == true) remaining = false; else readCharacter = getchar()')
	return text

def replaceOstream(text):
	# replace cout.flush()
	text = re.sub(r'(std[\s\t]*::[\s\t]*|)(cout[\s\t]*\.[\s\t]*flush[\s\t]*\([\s\t]*\))', 'fflush(stdout)', text)

	#replace cout << flush
	text = re.sub(r'(writeVar\()(std[\s\t]*::[\s\t]*|)(flush\))', 'fflush(stdout)', text)

	#replace cout << endl
	text = re.sub(r'(writeVar\()(std[\s\t]*::[\s\t]*|)(endl\))', "writeVar(endl)", text)
	text = text.replace('writeVar(endl)', "putchar('\\n')")

	return text

def getAndSetPrecision(text):

	# remove cout << fixed
	text = re.sub(r'(writeVar\()(std[\s\t]*::[\s\t]*|)([\s\t]*fixed[\s\t]*)(\))', '0', text)

	r = re.findall(r'(writeVar\()(std[\s\t]*::[\s\t]*|)([\s\t]*setprecision[\s\t]*\([\s\t]*)([0-9]*)([\s\t]*\)\))', text)
	precision = ''
	entry = ''
	if r:
		entry = joinTuple(r[0])
		precision = r[0][3]
		text = text.replace(entry, '0')
		text = text.replace('printf(\"%f\", x);', 'printf(\"%.' + precision +'f\", x);')
		text = text.replace('printf(\"%lf\", (double)x);', 'printf(\"%.' + precision + 'lf\", (double)x);')


	return text

def findBackslash(text):
	r = re.findall(r'[\s\n\t]\\[\s\n\t]', text)
	if r:
		text = warningBackslashMessage + text + warningBackslashMessage

	return text

inp = (open("input.txt", "r")).read()
inp = coverStrings(inp)
inp = removeDeSync(inp)
inp = undefMacros(inp)
inp = getGetlineEntriesAndReplace(inp)
inp = replaceCinIgnore(inp)

x = getCinEntries(inp)
inp = (replaceInput(inp, x))

x = getCoutEntries(inp)
inp = (replaceOutput(inp, x))

inp = replaceOstream(inp)

inp = prototypes + inp
inp = auxVariablesToRead + inp
inp = "#include <bits/stdc++.h>\n\n" + inp
inp += (open("functions.cpp", "r")).read()

inp = findBackslash(inp)

inp = getAndSetPrecision(inp)
inp = uncoverStrings(inp)


print (inp)
