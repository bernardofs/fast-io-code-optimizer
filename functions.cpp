

// read two consecutive char
// char READ_CHARACTER; bool REMAINING_CHARACTER = false;

template <typename T>
bool READ_INT(T &x) {
  x = 0; T sig = 1;
  if(!REMAINING_CHARACTER) READ_CHARACTER = getchar(), REMAINING_CHARACTER = true; else REMAINING_CHARACTER = false;
  while (!isdigit(READ_CHARACTER) && READ_CHARACTER != EOF) sig = (READ_CHARACTER == '-' ? -sig : sig), READ_CHARACTER = getchar();
  if(READ_CHARACTER == EOF) return REMAINING_CHARACTER = false, false;
  while (isdigit(READ_CHARACTER)) x = x * 10 + READ_CHARACTER - '0', READ_CHARACTER = getchar();
  x *= sig; REMAINING_CHARACTER = true;
  return true;
}

template <typename T>
bool READ_STRING(T &x) {
  x = "";
  if(!REMAINING_CHARACTER) READ_CHARACTER = getchar(), REMAINING_CHARACTER = true; else REMAINING_CHARACTER = false;
  while ((READ_CHARACTER == '\n' || READ_CHARACTER == '\t' || READ_CHARACTER == ' ')) READ_CHARACTER = getchar();
  if(READ_CHARACTER == EOF) return REMAINING_CHARACTER = false, false;
  while ((READ_CHARACTER != '\n' && READ_CHARACTER != '\t' && READ_CHARACTER != ' ' && READ_CHARACTER != EOF)) x += READ_CHARACTER, READ_CHARACTER = getchar();
  REMAINING_CHARACTER = true;
  return true;
}

bool READ_GETLINE(std::string &x) {
  x = "";
  if(!REMAINING_CHARACTER) READ_CHARACTER = getchar(), REMAINING_CHARACTER = true; else REMAINING_CHARACTER = false;
  if(READ_CHARACTER == EOF) return REMAINING_CHARACTER = false, false;
  while ((READ_CHARACTER != '\n' && READ_CHARACTER != EOF)) x += READ_CHARACTER, READ_CHARACTER = getchar();
  REMAINING_CHARACTER = false;
  return true;
}

template <typename T>
bool READ_CHAR(T &x) {
  if(!REMAINING_CHARACTER) READ_CHARACTER = getchar(), REMAINING_CHARACTER = true; else REMAINING_CHARACTER = false;
  if(READ_CHARACTER == EOF) return REMAINING_CHARACTER = false, false;
  while ((READ_CHARACTER == '\n' || READ_CHARACTER == '\t' || READ_CHARACTER == ' ')) READ_CHARACTER = getchar();
  x = READ_CHARACTER; REMAINING_CHARACTER = false;
  return true;
}

template<size_t N>
bool READ_CHAR_ARRAY(char (&x)[N]) {
  if(!REMAINING_CHARACTER) READ_CHARACTER = getchar(), REMAINING_CHARACTER = true; else REMAINING_CHARACTER = false;
  while ((READ_CHARACTER == '\n' || READ_CHARACTER == '\t' || READ_CHARACTER == ' ')) READ_CHARACTER = getchar();
  if(READ_CHARACTER == EOF) return REMAINING_CHARACTER = false, false;
  char *ptr = &x[0];
  while ((READ_CHARACTER != '\n' && READ_CHARACTER != '\t' && READ_CHARACTER != ' ' && READ_CHARACTER != EOF)) *ptr++ = READ_CHARACTER, READ_CHARACTER = getchar();
  *ptr = '\0', REMAINING_CHARACTER = true;
  return true;
}

bool READ_CHAR_ARRAY(char*& x) {
  std::string y;
  if(READ_STRING(y) == false)
    return false;
  x = new char[(int)y.size() + 1];
  strcpy(x, y.c_str());
  return true;
}

template <typename T>
bool READ_FLOAT(T &x) {
  return (scanf("%f", &x) != EOF);
}

template <typename T>
bool READ_DOUBLE(T &x) {
  double y;
  if(scanf("%lf", &y) == EOF) return false;
  x = y;
  return true;
}

bool READ_VAR(bool &x) {
  int aux; bool ret = READ_INT(aux);
  x = (aux != 0);
  return ret;
}

template<std::size_t N>
bool READ_BITSET(std::bitset<N> &x) {
  if(!REMAINING_CHARACTER) READ_CHARACTER = getchar(), REMAINING_CHARACTER = true; else REMAINING_CHARACTER = false;
  while ((READ_CHARACTER == '\n' || READ_CHARACTER == '\t' || READ_CHARACTER == ' ')) READ_CHARACTER = getchar();
  if(READ_CHARACTER == EOF) return REMAINING_CHARACTER = false, false;
  int i = 0; REMAINING_CHARACTER = true;
  while (READ_CHARACTER == '0' || READ_CHARACTER == '1') x[i++] = READ_CHARACTER - '0', READ_CHARACTER = getchar();
  return true;
}


bool READ_VAR(short int &x) {
  return READ_INT(x);    
}

bool READ_VAR(int &x) {
  return READ_INT(x);    
}

bool READ_VAR(long int &x) {
  return READ_INT(x);    
}

bool READ_VAR(long long int &x) {
  return READ_INT(x);    
}

bool READ_VAR(unsigned short int &x) {
  return READ_INT(x);    
}

bool READ_VAR(unsigned int &x) {
  return READ_INT(x);    
}

bool READ_VAR(unsigned long &x) {
  return READ_INT(x);    
}

bool READ_VAR(unsigned long long &x) {
  return READ_INT(x);    
}

bool READ_VAR(std::string &x) {
  return READ_STRING(x);    
}

bool READ_VAR(char &x) {
  return READ_CHAR(x);
}

template<size_t N>
bool READ_VAR(char (&x)[N]) {
  return READ_CHAR_ARRAY(x);
}

bool READ_VAR(char*& x) {
  return READ_CHAR_ARRAY(x);
}

bool READ_VAR(float &x) {
  return READ_FLOAT(x);
}

bool READ_VAR(double &x) {
  return READ_DOUBLE(x);
}

bool READ_VAR(long double &x) {
  return READ_DOUBLE(x);
}

template<std::size_t N>
bool READ_VAR(std::bitset<N> &x) {
  return READ_BITSET(x);
}

template <typename T>
void WRITE_INT(T x) {
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

void WRITE_CHAR(char x) {
  putchar(x);
}

void WRITE_CHAR_ARRAY(const char *x) {
  while(*x != '\0')
    putchar(*x++);
}

void WRITE_STRING(std::string &x) {
  for(char c: x) 
    putchar(c);
}

void WRITE_FLOAT(float x) {
  printf("%f", x);
}

template <typename T>
void WRITE_DOUBLE(T x) {
  printf("%lf", (double)x);
}

template<std::size_t N>
void WRITE_BITSET(std::bitset<N> &x) {
  for(int i = (int)x.size() - 1; i >= 0; i--)
    putchar(x[i] + 48);
}

void WRITE_VAR(bool x) {
  WRITE_INT(x);
}

void WRITE_VAR(short int x) {
  WRITE_INT(x);    
}

void WRITE_VAR(int x) {
  WRITE_INT(x);    
}

void WRITE_VAR(long int x) {
  WRITE_INT(x);    
}

void WRITE_VAR(long long int x) {
  WRITE_INT(x);    
}

void WRITE_VAR(unsigned short int x) {
  WRITE_INT(x);    
}

void WRITE_VAR(unsigned int x) {
  WRITE_INT(x);    
}

void WRITE_VAR(unsigned long x) {
  WRITE_INT(x);    
}

void WRITE_VAR(unsigned long long x) {
  WRITE_INT(x);    
}

void WRITE_VAR(std::string &x) {
  WRITE_STRING(x);    
}

void WRITE_VAR(char x) {
  WRITE_CHAR(x);
}

void WRITE_VAR(const char *x) {
  WRITE_CHAR_ARRAY(x);
}

void WRITE_VAR(float x) {
  WRITE_FLOAT(x);
}

void WRITE_VAR(double x) {
  WRITE_DOUBLE(x);
}

void WRITE_VAR(long double x) {
  WRITE_DOUBLE(x);
}

template<std::size_t N>
void WRITE_VAR(std::bitset<N> &x) {
  WRITE_BITSET(x);
}

