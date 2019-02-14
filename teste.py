import re

prototypes = '''template <typename T> bool readInt(T &x); template <typename T> bool readString(T &x);
template <typename T> bool readChar(T &x); bool readCharArray(char*& x);
template <typename T> bool readFloat(T &x); template <typename T> bool readDouble(T &x);
bool readVar(bool &x); bool readVar(short int &x); bool readVar(int &x);
bool readVar(long int &x); bool readVar(long long int &x); bool readVar(unsigned short int &x);
bool readVar(unsigned int &x); bool readVar(unsigned long &x); bool readVar(unsigned long long &x);
bool readVar(std::string &x); bool readVar(char &x); bool readVar(char*& x); bool readVar(float &x);
bool readVar(double &x); bool readVar(long double &x); template <typename T> void writeInt(T x);
void writeString(std::string x); void writeChar(char x); void writeCharArray(char *x);
void writeFloat(float x); template <typename T> void writeDouble(T x); void writeVar(bool x);
void writeVar(short int x); void writeVar(int x); void writeVar(long int x); void writeVar(long long int x);
void writeVar(unsigned short int x); void writeVar(unsigned int x); void writeVar(unsigned long x);
void writeVar(unsigned long long x); void writeVar(char x); void writeVar(char *x); 
void writeVar(std::string x); void writeVar(float x); void writeVar(double x); void writeVar(long double x);\n\n'''

auxVariablesToRead = 'char readCharacter; bool remaining = false;\n'

def removeSpacesFromVar(name):
	
	i = 0
	while name[i] in ['\t', ' ', '\n']:
		i += 1

	j = len(name) - 1
	while name[j] in ['\t', ' ', '\n']:
		j -= 1

	return name[i : j + 1]	

def getCinEntries(text):
	r = re.findall(r'[\s\t\n,;()]*cin[\s\t\n]*>>[^;]*;', text)
	ret = []
	for entry in r:
		iter = re.finditer(r"[\s\t\n,;()]*cin", entry)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while entry[i] != 'c':
				i += 1
			s = 'c'	
			# variable to check if parenthesis is balanced at that moment	
			par = 0
			while (not entry[i] in [',', ';']) or (par != 0):
				if entry[i] == '(':
					par += 1
				elif entry[i] == ')':  		
					par -= 1
				i += 1
				s += entry[i]
			ret.append(s)				
	return ret

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
	r = re.findall(r'cout[\s\t\n]*<<[^;]*;', text)
	ret = []
	for entry in r:
		iter = re.finditer(r"[\s\t\n,;]*cout", entry)
		indices = [m.start(0) for m in iter]
		for i in indices:
			while entry[i] != 'c':
				i += 1
			s = 'c'	
			# variable to check if parenthesis is balanced at that moment	
			par = 0
			while (not entry[i] in [',', ';']) or (par != 0):
				if entry[i] == '(':
					par += 1
				elif entry[i] == ')':  		
					par -= 1
				i += 1
				s += entry[i]
			ret.append(s)				
	return ret

def removeDeSync(text):
	r = []
	r += re.findall(r'[\n{;,][^\n{;,]*sync_with_stdio[^;,\n]*[;,\n]', text)
	r += re.findall(r'[\n{;,][^\n{;,]*cin[\s\t]*.[\s\t]*tie[^;,\n]*[;,\n]', text)
	r += re.findall(r'[\n{;,][^\n{;,]*cout[\s\t]*.[\s\t]*tie[^;,\n]*[;,\n]', text)

	for entry in r:
		entry = entry[1:]
		text = text.replace(entry, '')

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

def undefMacros(text):

	r = []
	r += re.findall(r'#[\s\t]*define[\s\t]+[^\s\t]+\([^\n)]*\)', text)
	r += re.findall(r'#[\s\t]*define[\s\t]+[^\s\t]*', text)

	undefs = '\n\n'
	for entry in r:
		entry = re.sub(r'#[\s\t]*define', '#undef', entry)
		entry = re.sub(r'\(.*\)', '', entry)
		entry += '\n'
		undefs += entry

	text += undefs

	return text

inp = (open("input.txt", "r")).read()
inp = removeDeSync(inp)
inp = undefMacros(inp)

x = getCinEntries(inp)
inp = (replaceInput(inp, x))

x = getCoutEntries(inp)
inp = (replaceOutput(inp, x))

inp = prototypes + inp
inp = auxVariablesToRead + inp
inp = "#define endl '\\n'\n" + inp
inp = "#include <bits/stdc++.h>\n" + inp
inp += '''

template <typename T>
bool readInt(T &x) {
  x = 0; T sig = 1;
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  while (!isdigit(readCharacter) && readCharacter != EOF) sig = (readCharacter == '-' ? -sig : sig), readCharacter = getchar();
  if(readCharacter == EOF) return remaining = false, false;
  while (isdigit(readCharacter) && readCharacter != EOF) x = x * 10 + readCharacter - '0', readCharacter = getchar();
  x *= sig;
  return true;
}

template <typename T>
bool readString(T &x) {
  x = "";
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  while ((readCharacter == '\\n' || readCharacter == '\\t' || readCharacter == ' ')) readCharacter = getchar();
  if(readCharacter == EOF) return remaining = false, false;
  while ((readCharacter != '\\n' && readCharacter != '\\t' && readCharacter != ' ' && readCharacter != EOF)) x += readCharacter, readCharacter = getchar();
  return true;
}

template <typename T>
bool readChar(T &x) {
  if(!remaining) readCharacter = getchar(); else remaining = false;
  if(readCharacter == EOF) return remaining = false, false;
  while ((readCharacter == '\\n' || readCharacter == '\\t' || readCharacter == ' ')) readCharacter = getchar();
  remaining = false;
  x = readCharacter;
  return true;
}

bool readCharArray(char*& x) {
  std::string y;
  if(readString(y) == false)
    return false;
  x = new char[(int)y.size() + 1];
  strcpy(x, y.c_str());
  return true;
}

template <typename T>
bool readFloat(T &x) {
  return (scanf("%f", &x) != EOF);
}

template <typename T>
bool readDouble(T &x) {
  double y;
  if(scanf("%lf", &y) == EOF) return false;
  x = y;
  return true;
}

bool readVar(bool &x) {
  int aux; bool ret = readInt(aux);
  x = (aux != 0);
  return ret;
}


bool readVar(short int &x) {
  return readInt(x);    
}

bool readVar(int &x) {
  return readInt(x);    
}

bool readVar(long int &x) {
  return readInt(x);    
}

bool readVar(long long int &x) {
  return readInt(x);    
}

bool readVar(unsigned short int &x) {
  return readInt(x);    
}

bool readVar(unsigned int &x) {
  return readInt(x);    
}

bool readVar(unsigned long &x) {
  return readInt(x);    
}

bool readVar(unsigned long long &x) {
  return readInt(x);    
}

bool readVar(std::string &x) {
  return readString(x);    
}

bool readVar(char &x) {
  return readChar(x);
}

bool readVar(char*& x) {
  return readCharArray(x);
}

bool readVar(float &x) {
  return readFloat(x);
}

bool readVar(double &x) {
  return readDouble(x);
}

bool readVar(long double &x) {
  return readDouble(x);
}

template <typename T>
void writeInt(T x) {
  if (x < 0) {putchar('-'); x = -x; }
  char writeBuffer[20], *writePtr = writeBuffer;
  do {
    *writePtr++ = '0' + x % 10;
    x /= 10;
  }
  while (x);
  do  { putchar(*--writePtr); }
  while (writePtr > writeBuffer);
}

void writeChar(char x) {
  putchar(x);
}

void writeCharArray(char *x) {
  while(*x != '\\0')
    putchar(*x++);
}

void writeString(std::string x) {
  for(char c: x) 
    putchar(c);
}

void writeFloat(float x) {
  printf("%f", x);
}

template <typename T>
void writeDouble(T x) {
  printf("%lf", (double)x);
}

void writeVar(bool x) {
  writeInt(x);
}

void writeVar(short int x) {
  writeInt(x);    
}

void writeVar(int x) {
  writeInt(x);    
}

void writeVar(long int x) {
  writeInt(x);    
}

void writeVar(long long int x) {
  writeInt(x);    
}

void writeVar(unsigned short int x) {
  writeInt(x);    
}

void writeVar(unsigned int x) {
  writeInt(x);    
}

void writeVar(unsigned long x) {
  writeInt(x);    
}

void writeVar(unsigned long long x) {
  writeInt(x);    
}

void writeVar(std::string x) {
  writeString(x);    
}

void writeVar(char x) {
  writeChar(x);
}

void writeVar(char *x) {
  writeCharArray(x);
}

void writeVar(float x) {
  writeFloat(x);
}

void writeVar(double x) {
  writeDouble(x);
}

void writeVar(long double x) {
  writeDouble(x);
}
'''

print (inp)
