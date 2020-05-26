import numpy as np

def accept_ip():
	text=input('enter 10  bit key')
	if(len(text)!=10):
		print('invalid length')
		exit(1)
	bitlist=[int(text1,2) for text1 in text ]
	npbits=np.array(bitlist,dtype=np.uint8)
	return npbits
	
def P10(text):
	P10hash=[2,4,1,6,3,9,0,8,7,5]
	text=text[P10hash]
	return text
	
def P8(text):
	P8hash=[0,1,5,2,6,3,7,4,9,8]
	text=text[P8hash]
	return text[2:]

def ls1(text):
	ls1hash=[1,2,3,4,0,6,7,8,9,5]
	text=text[ls1hash]
	return text

def ls2(text):
	ls2hash=[2,3,4,0,1,7,8,9,5,6]
	text=text[ls2hash]
	return text
	
	
	
	
def keygen():
	temp=accept_ip()
	p10op=P10(temp)
	ls1op=ls1(p10op)
	k1=P8(ls1op)
	ls2op=ls2(ls1op)
	k2=P8(ls2op)
	return k1,k2

#print(keygen())	
