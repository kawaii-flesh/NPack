#   NPack - file compression program
#   Copyright (C) 2019  kawaii-flesh

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
