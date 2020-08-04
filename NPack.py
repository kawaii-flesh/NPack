import sys
import npp

#Check args if not print help
if(len(sys.argv)<3 or sys.argv[1]=="-h" or sys.argv[1]=="--help"):
	print("NPack.py [param] [file]")
	print("-p - pack file")
	print("-u - unpack file")
	print("-h - show help")
#Check args if -p pack file
elif(sys.argv[1]=="-p"):
	npp.Pack(sys.argv[2])
#Check args if -u unpack file	
elif(sys.argv[1]=="-u"):
	npp.UnPack(sys.argv[2])
