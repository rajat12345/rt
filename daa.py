from sys import argv
script , file_new=argv
def print_all(f):
	print f.read()	
	
def rewind(f):
	 print f.seek(2)
	
current_file=open(file_new)
print_all(current_file)
rewind(current_file)
print_all(current_file)
