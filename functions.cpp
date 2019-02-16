

// read two consecutive char
// char readCharacter; bool remaining = false;

template <typename T>
bool readInt(T &x) {
  x = 0; T sig = 1;
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  while (!isdigit(readCharacter) && readCharacter != EOF) sig = (readCharacter == '-' ? -sig : sig), readCharacter = getchar();
  if(readCharacter == EOF) return remaining = false, false;
  while (isdigit(readCharacter)) x = x * 10 + readCharacter - '0', readCharacter = getchar();
  x *= sig; remaining = true;
  return true;
}

template <typename T>
bool readString(T &x) {
  x = "";
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  while ((readCharacter == '\n' || readCharacter == '\t' || readCharacter == ' ')) readCharacter = getchar();
  if(readCharacter == EOF) return remaining = false, false;
  while ((readCharacter != '\n' && readCharacter != '\t' && readCharacter != ' ' && readCharacter != EOF)) x += readCharacter, readCharacter = getchar();
  remaining = true;
  return true;
}

bool readGetline(std::string &x) {
  x = "";
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  if(readCharacter == EOF) return remaining = false, false;
  while ((readCharacter != '\n' && readCharacter != EOF)) x += readCharacter, readCharacter = getchar();
  remaining = false;
  return true;
}

template <typename T>
bool readChar(T &x) {
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  if(readCharacter == EOF) return remaining = false, false;
  while ((readCharacter == '\n' || readCharacter == '\t' || readCharacter == ' ')) readCharacter = getchar();
  x = readCharacter; remaining = false;
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

template<std::size_t N>
bool readBitset(std::bitset<N> &bit) {
  if(!remaining) readCharacter = getchar(), remaining = true; else remaining = false;
  while ((readCharacter == '\n' || readCharacter == '\t' || readCharacter == ' ')) readCharacter = getchar();
  if(readCharacter == EOF) return remaining = false, false;
  int i = 0; bit[i++] = readCharacter - '0';
  while (readCharacter == '0' || readCharacter == '1') bit[i++] = readCharacter - '0', readCharacter = getchar();
  remaining = true;
  return true;
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

template<std::size_t N>
bool readVar(std::bitset<N> &bit) {
  return readBitset(bit);
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

void writeCharArray(const char *x) {
  while(*x != '\0')
    putchar(*x++);
}

void writeString(std::string &x) {
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

template<std::size_t N>
void writeBitset(std::bitset<N> &bit) {
  for(int i = (int)bit.size() - 1; i >= 0; i--)
    putchar(bit[i] + 48);
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

void writeVar(std::string &x) {
  writeString(x);    
}

void writeVar(char x) {
  writeChar(x);
}

void writeVar(const char *x) {
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

template<std::size_t N>
void writeVar(std::bitset<N> &bit) {
  writeBitset(bit);
}

