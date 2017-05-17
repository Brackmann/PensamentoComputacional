z=1
while z<=10:
	print(z, "elefantes incomodam muita gente")
	z = z+1
	print (z , "elefantes ",  end='')
	for x in range(z):
		print ('incomodam, ', end='')
	print ('muito mais')
	z = z+1

# 1 elefantes incomodam muita gente
# 2 elefantes incomodam, incomodam, muito mais
# 3 elefantes incomodam muita gente
# 4 elefantes incomodam, incomodam, incomodam, incomodam, muito mais
# 5 elefantes incomodam muita gente
# 6 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, muito mais
# 7 elefantes incomodam muita gente
# 8 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, muito mais
# 9 elefantes incomodam muita gente
# 10 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, incomodam, muito mais
