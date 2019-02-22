# Fast I/O Code Optimizer
A tool developed in Python to optimize execution time of C++ codes by replacing methods of reading and writing variables. The program is focused on Competitive Programming and could be used to help to solve problems with a tight time limit. This optimizer replaces all cin/cout methods to faster approaches which can optimize until 90% the execution time of the code.

## Motivation
Some competitive programming problems have a tight time limit.  Then, when someone submits a solution, even with the expected complexity, it may get a time limit exceeded verdict. Occasionally, the problem requires Fast I/O methods to speed up the execution time and is very hard to get accepted verdict without making this type of optimization. Consequently, it is needed to replace all default C++ reading and writing methods (cin/cout) to faster approaches.  This tool makes very easy the task of replacing the way of reading and writing variables, and it uses very fast methods which would take very long to type and wouldn't be so efficient.

## Functions and Commands

### To Be Replaced 
* cin
* cout
* cin.ignore() - 0 parameter
* getline() - Any number of parameters
* cout << setpresision() - 1 parameter and at most 1 call

### To Be Deleted
* cout << fixed
* ios_base::sync_with_stdio()
* ios::sync_with_stdio()

## Implementation
In order to optimize the code performance, text replacing was the approach chosen. This tool finds all occurrences of cin/cout commands and replaces them with functions. Important auxiliaries commands also are supported and will be described later. Most of the implementation consists of finding patterns in text using regular expressions, and this is very useful to avoid blank characters. Because of the best compatibility with methods applied, Python was the language chosen. There are other approaches available to make the same optimization, but this one was chosen by reason of it is possible to modify easier all commands without creating some specific modification to a certain command. Besides that, it is possible to add support to a big range of things like the use of different namespaces.

### Reading Variables

#### Reading Integers
Cin is replaced by getchar() function which is responsible to read each number as a character and convert it to a number.

#### Reading Strings and Characters 
Cin is replaced by getchar() function which is responsible to read the string char by char.

#### Reading floating numbers
Cin is replaced by a scanf function.

#### Reading bool and bitset
Cin is replaced by getchar() function which is responsible to read each bit as a character and convert it to a bit.

### Writing Variables

#### Writing Integers
Cout is replaced by putchar() function which is responsible to write each number as a character.

#### Writing Strings and Characters
Cout is replaced by putchar() function which is responsible to write each character char by char.

#### Writing floating numbers
Cout is replaced by a printf function. If setprecision(number) method, is called all floating numbers will be written with "number" decimal places. However, this tool only supports one call of setprecision method.  

#### Writing bool and bitset
Cout is replaced by putchar() function which is responsible to write each bit as a character.

The use of std:: before a call and the use of blank characters like tabs and spaces are supported.

## Important restrictions 
* This tool doesn't work with multiple calls of setprecision function.
* Multiline statements are not supported.








