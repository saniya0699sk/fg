 #-*- coding: utf-8 -*-
print u"Введите число"
i = int(raw_input("> "))
while i != 0:
    if i < 0:
        print u"Введите положительное число"
        break
    elif i > 0:
    	print u"Введите второе число"
    	s = int(raw_input ("> "))
    	while int(i+s) <=14:
    	   	print (i+s)
    	s = s+1