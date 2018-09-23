"""
Encrypt and decrypt using caesar cipher for English alphabet
"""
import sys
import argparse
from nltk.corpus import wordnet

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--e", help="enter string to be encrypted")
ap.add_argument("-d", "--d", help="enter string to be decrypted")
ap.add_argument("-k", "--k", help="enter shift key to encrypt")

if len(sys.argv) > 1:
    args = ap.parse_args()
    print(args)
    avalues = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    # Encrypt
    if args.e:
        k = int(args.k)
        if k > 25 or k < 1:
            print("enter a key between 1 and 25")
        istr = args.e.lower()
        o = ''
        for v in istr.split():
            o += ''.join([chr(ord('a') + ((ord(x) + k)%26)) for x in v]) + ' '
        print(o.strip().upper())
    elif args.d:
        # Decrypt
        istr = args.d.lower()
        maxscore = 0
        maxa = 0
        maxb = 0
        for k in range(1, 26):
            score = 0
            o = ''
            for v in istr.split():
                o = ''.join([chr(ord('a') + ((ord(x) - k)%26)) for x in v])
                if len(o) > 2:
                    if len(wordnet.synsets(o)) > 0:
                        score += 1
            if score > maxscore:
                maxscore = score
                maxk = k
        o = ''
        for v in istr.split():
            o += ''.join([chr(ord('a') + ((ord(x) - maxk)%26)) for x in v]) + ' '
        print(o.strip().upper())
        print('k={k}'.format(k=maxk))
    else:
        print('Enter a string to encrypt or decrypt')
        ap.print_help()
else:
    ap.print_help()
