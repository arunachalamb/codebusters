"""
Encrypt and decrypt using Hill cipher for English alphabet
"""
import sys
import argparse
import numpy as np
from numpy import matrix

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--k", help="enter a key of length 4 or 9")
ap.add_argument("-e", "--e", help="enter string to be encrypted")
ap.add_argument("-d", "--d", help="enter string to be decrypted")

if len(sys.argv) > 1:
    args = ap.parse_args()
    print(args)
    k = args.k.lower()
    lk = len(k)
    s = int(lk**0.5)
    if not (lk == 4 or lk == 9):
        print('k needs to be a key of length 4 or 9')
        quit()
    if args.e:
        istr = args.e.lower()
        ci = istr.replace(' ', '') # concatenated input string
        if len(ci) % s != 0:
            ci += 'z'*(s - (len(ci)%s)) # Pad with z
        km = matrix(np.array([ord(x) - ord('a') for x in k]).reshape(s, s))
        print('Key matrix: ', km.getA1())
        o = ''
        for i in range(len(ci)//s):
            m = matrix(np.array([ord(x) - ord('a') for x in ci[i*s:i*s+s]]).reshape(s,1))
            o += ''.join([chr(x + ord('a')) for x in ((km*m)%26).getA1()])
        x = 0
        for i in istr.split():
            print(o[x:x+len(i)].upper(), end=' ')
            x += len(i)
        print('')
    elif args.d:
        print('Decrypt')
    else:
        print('Enter a string to encrypt or decrypt')
        ap.print_help()
else:
    ap.print_help()
