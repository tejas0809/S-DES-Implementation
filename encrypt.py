import numpy as np
s0=np.array([
			[[0,1],[0,0],[1,1],[1,0]],
			[[1,1],[1,0],[0,1],[0,0]],
			[[0,0],[1,0],[0,1],[1,1]],
			[[1,1],[0,1],[1,1],[1,0]]
			],dtype=np.uint8)

s1=np.array([
			[[0,0],[0,1],[1,0],[1,1]],
			[[1,0],[0,0],[0,1],[1,1]],
			[[1,1],[0,0],[0,1],[0,0]],
			[[1,0],[0,1],[0,0],[1,1]]
			],dtype=np.uint8)			
def applyIP(text):
	IPhash=[1,5,2,0,3,7,4,6]
	temp=np.unpackbits(text)
	temp1=temp[IPhash]
	del temp
	return temp1

def applyIIP(text):
	IIPhash=[3,0,2,4,6,1,7,5]
	temp=text[IIPhash]
	temp1=np.packbits(temp)
	del temp
	return temp1
def mangle_left4(text,key):
	EPhash=[3,0,1,2,1,2,3,0]
	print(np.shape(text))
	temp=text[:,4:]
	temp=temp[:,EPhash]
	temp=temp^key
	return sbox(temp)

def sbox(text):
	P4hash=[1,3,2,0]
	r1,c1=text[:,0]*2+text[:,3],text[:,1]*2+text[:,2]
	r2,c2=text[:,4]*2+text[:,7],text[:,5]*2+text[:,6]
	op=np.c_[s0[r1,c1],s1[r1,c1]]
	op=op[P4hash]
	return op
	
	
def encrypt(text,k1,k2):
	ip=applyIP(np.reshape(text,[-1,1]))
	newu4=mangle_left4(ip,k1)
	ip[:,:4]=ip[:,:4]^newu4
	ip=ip[[4,5,6,7,0,1,2,3]]
	newl4=mangle_left4(ip,k2)
	ip[:,:4]=ip[:,:4]^newl4
	cpt=np.reshape((applyIIP(ip)),[-1])
	return cpt
	
def decrypt(text,k1,k2):
	ip=applyIP(np.reshape(text,[-1,1]))
	print(np.shape(ip))
	newu4=mangle_left4(ip,k2)
	ip[:,:4]=ip[:,:4]^newu4
	ip=ip[[4,5,6,7,0,1,2,3]]
	newl4=mangle_left4(ip,k1)
	ip[:,:4]=ip[:,:4]^newl4
	cpt=np.reshape((applyIIP(ip)),[-1])
	return cpt
