import sys
import random
import hashlib

#Calculate SHA256 and get file size
def Pack(fname):
	fin = open(fname, "rb")
	buff = fin.read()
	size = len(buff)
	MSN = hashlib.sha256(buff).hexdigest()
	fin.close()
	fout = open(fname+".np","w")
	fout.write(str(size)+"\n"+str(MSN))
	fout.close()

#Create random file and calculate SHA256 if equally write data
def UnPack(fname):
	fin = open(fname, "r")
	size = int(fin.readline())
	MSN = fin.readline()
	MSN1 = 0
	fin.close()
	while(MSN1 != MSN):
		buff = []
		MSN1 = r = 0
		while(r < size):
			buff.append(chr(random.randint(0, 255)))
			r += 1
		buff = str(''.join(buff))
		buff = buff.encode()
		MSN1 = hashlib.sha256(buff).hexdigest()
	fout=open(fname+".up", "w")
	fout.write(buff.decode())
	fout.close() 
