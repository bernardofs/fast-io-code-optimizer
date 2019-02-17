

template <typename T> bool READ_INT(T &x); template <typename T> bool READ_STRING(T &x); 
template<size_t N> bool READ_CHAR_ARRAY(char (&x)[N]); template<size_t N> bool READ_VAR(char (&x)[N]);
template <typename T> bool READ_CHAR(T &x); bool READ_CHAR_ARRAY(char*& x); bool READ_GETLINE(std::string &x);
template <typename T> bool READ_FLOAT(T &x); template <typename T> bool READ_DOUBLE(T &x);
template<std::size_t N> bool READ_BITSET(std::bitset<N> &bit); template<std::size_t N> bool READ_VAR(std::bitset<N> &bit);
bool READ_VAR(bool &x); bool READ_VAR(short int &x); bool READ_VAR(int &x); 
bool READ_VAR(long int &x); bool READ_VAR(long long int &x); bool READ_VAR(unsigned short int &x);
bool READ_VAR(unsigned int &x); bool READ_VAR(unsigned long &x); bool READ_VAR(unsigned long long &x);
bool READ_VAR(std::string &x); bool READ_VAR(char &x); bool READ_VAR(char*& x); bool READ_VAR(float &x);
bool READ_VAR(double &x); bool READ_VAR(long double &x); template <typename T> void WRITE_INT(T x);
void WRITE_STRING(std::string &x); void WRITE_CHAR(char x); void WRITE_CHAR_ARRAY(const char *x);
void WRITE_FLOAT(float x); template <typename T> void WRITE_DOUBLE(T x); void WRITE_VAR(bool x);
void WRITE_VAR(short int x); void WRITE_VAR(int x); void WRITE_VAR(long int x); void WRITE_VAR(long long int x);
void WRITE_VAR(unsigned short int x); void WRITE_VAR(unsigned int x); void WRITE_VAR(unsigned long x);
void WRITE_VAR(unsigned long long x); void WRITE_VAR(char x); void WRITE_VAR(const char *x); 
void WRITE_VAR(std::string &x); void WRITE_VAR(float x); void WRITE_VAR(double x); void WRITE_VAR(long double x);
template<std::size_t N> void WRITE_VAR(std::bitset<N> &bit); template<std::size_t N> void WRITE_BITSET(std::bitset<N> &bit);
