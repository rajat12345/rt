 from sys import argv
 script , file=argv
def rajat_fun(f):
	print f.read()
	f.seek(0)
	current_file=open(file)
	rajat_fun(current_file)