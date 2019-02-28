import converter
import sys

# if you do not want to print the code in terminal set 
# the variable to false
printInTerminal = True

# if you do not want to print the code in a new file
# set the variable below to false
printInFile = True

fileName = ''
if len(sys.argv) == 2:
	fileName = sys.argv[1]
else:
	fileName = input('Type the name of the file\n')

while True:
	try:
		code = open(fileName, "r").read()
		break
	except:	
		fileName = input('File not found, try again\n')

code = converter.convertToFastIO(code)

if printInFile:
	r = fileName.split('/')
	newName = 'FastIO - ' + r[-1]
	file = open(newName, 'w')
	file.write(code)
	file.close()

if printInTerminal:
	print (code)