import re

warningBackslashMessage = '''
/*
....................... WARNING .......................
.. It was found a \\ (Backslash) symbol in your file ...
.... This software doesn\'t support multiline code .....
............. and may not work as expected ............
.......................................................
*/

'''  
# if you do not want to print backslash warning in code 
# uncomment the line below
# warningBackslashMessage = ''

warningSetPrecisionMessage = '''
/*
....................... WARNING ........................
.. It was found multiple setprecision occurrences in ...
.. your code. This software doesn\'t support multiple ...
....... occurrences and may not work as expected .......
........................................................
*/

'''

# if you do not want to print setprecision warning in code 
# uncomment the line below
# warningSetPrecisionMessage = ''



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

def removeEnter(text):
	s = str(chr(13))
	text = text.replace(s, '')
	return text

def customSplit(text, div):
	l = []
	bra, par = 0, 0
	acc, i = '', 0
	while i < len(text):
		if i + len(div) <= len(text):
			if text[i : i + len(div)] == div and par == 0 and bra == 0:
				l.append(acc)
				acc = ''
				i += len(div)
				continue
		if text[i] == '(':
			par += 1
		elif text[i] == ')':
			par -= 1
		elif text[i] == '[':
			bra += 1
		elif text[i] == ']':
			bra -= 1
		acc += text[i]
		i += 1
	l.append(acc)
	return l


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
	for pattern in r:
		pattern = joinTuple(pattern)
		iter = re.finditer(r"([\s\t\n,;()]*)(std[\s\t]*::[\s\t]*|)(cin)", pattern)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while pattern[i] != 'c' and pattern[i] != 's':
				i += 1
			s = pattern[i]
			# variable to check if brackets are balanced at that moment	
			bra = 0
			# variable to check if parenthesis are balanced at that moment	
			par = 0
			while (not pattern[i] in [',', ';', '&', '|', '\n']) or (par != 0) or (bra != 0):
				if pattern[i] == '(':
					par += 1
				elif pattern[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif pattern[i] == '[':
					bra += 1
				elif pattern[i] == ']':  		
					bra -= 1
					if bra < 0:
						break

				i += 1
				s += pattern[i]
			ret.append(s)				
	return ret

def replaceInput(text, cinEntries):
	for pattern in cinEntries:
		aux = ''
		last = pattern[-1]
		# delete special characters like semicolon (;) or comma (,) from line
		x = pattern[:-1]
		l = x.split('>>')
		# delete cin from list
		l.pop(0)
		for y in l:
			aux += '__FIO__.READ_VAR(' + removeSpacesFromVar(y) + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(pattern, aux)
	return text

def getCoutEntries(text):
	r = re.findall(r'[\s\t\n,;()]*(std[\s\t]*::[\s\t]*|)(cout[\s\t\n]*<<[^;{}\n]*[;{}\n])', text)
	ret = []
	for pattern in r:
		pattern = joinTuple(pattern)
		iter = re.finditer(r"([\s\t\n,;()]*)(std[\s\t]*::[\s\t]*|)(cout)", pattern)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while pattern[i] != 'c' and pattern[i] != 's':
				i += 1
			s = pattern[i]
			# variable to check if brackets are balanced at that moment	
			bra = 0
			# variable to check if parenthesis are balanced at that moment	
			par = 0
			while (not pattern[i] in [',', ';', '&', '|', '\n']) or (par != 0) or (bra != 0):
				if pattern[i] == '(':
					par += 1
				elif pattern[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif pattern[i] == '[':
					bra += 1
				elif pattern[i] == ']':  		
					bra -= 1
					if bra < 0:
						break

				i += 1
				s += pattern[i]
			ret.append(s)				
	return ret

def replaceOutput(text, coutEntries):
	for pattern in coutEntries:
		aux = ''
		last = pattern[-1]
		# delete semicolon (;) or comma (,) from line
		x = pattern[:-1]
		l = customSplit(x, '<<')
		# delete cout from list
		l.pop(0)
		# print (pattern)
		for y in l:
			aux += '__FIO__.WRITE_VAR(' + removeSpacesFromVar(y) + ')' + ', '
		aux = aux[:-2] + last
		text = text.replace(pattern, aux)

	return text


def removeDeSync(text):
	r = []
	# remove all desync
	r += re.findall(r'(std[\s\t]*::[\s\t]*|)(ios[\t\s]*::|ios_base[\t\s]*::)([\t\s]*sync_with_stdio[\t\s]*\([\t\s]*)([^\)]*)([\t\s]*\)[\t\s]*[,;\n])', text)
	r += re.findall(r'(std[\s\t]*::[\s\t]*|)(cin|cout)([\s\t]*\.[\s\t]*tie[\s\t]*\([\s\t]*)([^\)]*)([\s\t]*\)[\s\t]*[;,\n])', text)

	# replace desync with 0
	for pattern in r:
		pattern = joinTuple(pattern)
		last = pattern[-1]
		pattern = pattern[:-1]
		text = text.replace(pattern + last, '0' + last)

	return text


def getGetlineEntriesAndReplace(text):
	r = re.findall(r'getline[\s\t]*\([^;{}\n]*[;{}\n]', text)
	for pattern in r:
		iter = re.finditer(r"[\s\t\n,;()]*getline", pattern)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while pattern[i] != 'g':
				i += 1
			i += 8
			s = 'getline('
			# variable to check if brackets are balanced at that moment	
			bra = 0
			# variable to check if parenthesis are balanced at that moment	
			par = 0
			while (pattern[i] != ',') or (par != 0) or (bra != 0):
				if pattern[i] == '(':
					par += 1
				elif pattern[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif pattern[i] == '[':
					bra += 1
				elif pattern[i] == ']':  		
					bra -= 1
					if bra < 0:
						break
				s += pattern[i];
				i += 1
			s += ',';
			i += 1	
			var = ''
			while (pattern[i] != ')') or (par != 0) or (bra != 0):
				if pattern[i] == '(':
					par += 1
				elif pattern[i] == ')':  		
					par -= 1
					if par < 0:
						break
				elif pattern[i] == '[':
					bra += 1
				elif pattern[i] == ']':  		
					bra -= 1
					if bra < 0:
						break

				s += pattern[i]
				var += pattern[i]
				i += 1
			s += ')'
			var = re.sub(' ', '', var)
			text = text.replace(s, '__FIO__.READ_GETLINE(' + var + ')')		
	return text

def undefMacros(text):

	r = []
	r += re.findall(r'#[\s\t]*define[\s\t]+[^\s\t]+\([^\n\)]*\)', text)
	r += re.findall(r'#[\s\t]*define[\s\t]+[^\s\t\(]*', text)

	undefs = '\n\n'
	for pattern in r:
		pattern = re.sub(r'#[\s\t]*define', '#undef', pattern)
		pattern = re.sub(r'\([^\)]*\)', '', pattern)
		pattern += '\n'
		undefs += pattern

	text += undefs

	return text

def replaceCinIgnore(text):
	r = re.findall(r'(std[\s\t]*::[\s\t]*|)(cin[\s\t]*\.[\s\t]*ignore[\s\t]*\([\s\t]*\))', text)
	for pattern in r:
		pattern = joinTuple(pattern)
		text = text.replace(pattern, '__FIO__.ignore()')
	return text

def replaceOstream(text):
	# replace cout.flush()
	text = re.sub(r'(std[\s\t]*::[\s\t]*|)(cout[\s\t]*\.[\s\t]*flush[\s\t]*\([\s\t]*\))', '__FIO__.flush()', text)

	#replace cout << flush
	text = re.sub(r'(__FIO__.WRITE_VAR\()(std[\s\t]*::[\s\t]*|)(flush\))', '__FIO__.flush()', text)

	#replace cout << endl
	text = re.sub(r'(__FIO__.WRITE_VAR\()(std[\s\t]*::[\s\t]*|)(endl\))', "__FIO__.WRITE_VAR(endl)", text)
	text = text.replace('__FIO__.WRITE_VAR(endl)', "putchar('\\n')")

	return text

def getAndSetPrecision(text):

	# remove cout << fixed
	text = re.sub(r'(__FIO__.WRITE_VAR\()(std[\s\t]*::[\s\t]*|)([\s\t]*fixed[\s\t]*)(\))', '0', text)

	r = re.findall(r'(__FIO__.WRITE_VAR\()(std[\s\t]*::[\s\t]*|)([\s\t]*setprecision[\s\t]*\([\s\t]*)([0-9]*)([\s\t]*\)\))', text)
	precision = ''
	pattern = ''
	if r:
		pattern = joinTuple(r[0])
		precision = r[0][3]
		text = text.replace(pattern, '0')
		text = text.replace('printf(\"%f\", x);', 'printf(\"%.' + precision +'f\", x);')
		text = text.replace('printf(\"%lf\", (double)x);', 'printf(\"%.' + precision + 'lf\", (double)x);')

	if len(r) > 1:
		text = warningSetPrecisionMessage + text + warningSetPrecisionMessage 

	return text

def findBackslash(text):
	r = re.findall(r'[\s\n\t]\\[\s\n\t]', text)
	if r:
		text = warningBackslashMessage + text + warningBackslashMessage

	return text


def convertToFastIO(code):

	code = removeEnter(code)
	code = coverStrings(code)
	code = removeDeSync(code)
	code = undefMacros(code)
	code = getGetlineEntriesAndReplace(code)
	code = replaceCinIgnore(code)

	x = getCinEntries(code)
	code = (replaceInput(code, x))

	x = getCoutEntries(code)
	code = (replaceOutput(code, x))

	code = replaceOstream(code)

	struct = (open("struct.cpp", "r")).read()
	code = struct + code
	code = "#include <bits/stdc++.h>\n" + code
	code += (open("functions.cpp", "r")).read()

	code = findBackslash(code)
	code = getAndSetPrecision(code)

	code = uncoverStrings(code)

	return code

