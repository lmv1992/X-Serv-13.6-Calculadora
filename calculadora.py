#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

comand_line = sys.argv

if len(comand_line) != 4:
	sys.exit("ha introducido mal el nro de argumentos") 

n1 = comand_line[2]
n2 = comand_line[3]
operator = comand_line[1]

if operator == "suma":
	print n1 + "+" +n2+ "=" + str(int(comand_line [2])+int(comand_line[3])),
if operator == "resta": 
	print n1+" - "+ n2+" = "+str(int(comand_line [2])-int(comand_line[3])),
if operator == "multiplicar":
	print n1+" * "+n2+" = "+ str(int(comand_line [2])*int(comand_line[3])),
if operator == "dividir":
	print n1+" / "+n2+" = "+str(float(comand_line [2])/float(comand_line[3])),
	
