import numpy as np
import argparse
from keygen import keygen
from encrypt import encrypt,decrypt

def main():
	parser=argparse.ArgumentParser()
	parser.add_argument('action',help='encrypt or decrypt?',choices=['encrypt','decrypt'])
	parser.add_argument('ipfile')
	parser.add_argument('opfile')
	args=parser.parse_args()
	
	with open(args.ipfile,'rb') as f:
		inp=np.fromfile(f,dtype=np.uint8)
	
	k1,k2=keygen()

	if args.action=='encrypt':
		op=encrypt(inp,k1,k2)
	else:
		op=decrypt(inp,k1,k2)
	
	with open(args.opfilie,'wb') as f:
		op.tofile(f)
		
if __name__=='__main__':
	main()
		
