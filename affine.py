"""
Encrypt and decrypt using affine cipher for English alphabet
"""
import sys
import argparse
from nltk.corpus import wordnet

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--a", help="enter a coprime integer to 26 as parameter a")
ap.add_argument("-b", "--b", help="enter the shift used as parameter b")
ap.add_argument("-e", "--e", help="enter string to be encrypted")
ap.add_argument("-d", "--d", help="enter string to be decrypted")

if len(sys.argv) > 1:
    args = ap.parse_args()
    print(args)
    avalues = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    # Encrypt
    if args.e:
        a = int(args.a)
        b = int(args.b)
        if a not in avalues:
            print("enter a value for a that is coprime to 26")
        istr = args.e.lower()
        o = ''
        for v in istr.split():
            oi = [chr(ord('a') + ((a*(ord(x) - ord('a')) + b)%26)) for x in v]
            o += ''.join(oi) + ' '
        print(o.strip().upper())
    elif args.d:
        # Decrypt
        istr = args.d.lower()
        maxscore = 0
        maxa = 0
        maxb = 0
        for a in avalues:
            for b in range(0, 26):
                score = 0
                o = ''
                for v in istr.split():
                    o = ''.join([chr(ord('a') + ((a*((ord(x) - ord('a')) - b))%26)) for x in v])
                    if len(o) > 2:
                        if len(wordnet.synsets(o)) > 0:
                            score += 1
                if score > maxscore:
                    maxscore = score
                    maxa, maxb = a, b
        o = ''
        for v in istr.split():
            o += ''.join([chr(ord('a') + ((maxa*((ord(x) - ord('a')) - maxb))%26)) for x in v]) + ' '
        print(o.strip().upper())
        print('a={a}'.format(a=maxa), 'b={b}'.format(b=maxb))
    else:
        print('Enter a string to encrypt or decrypt')
        ap.print_help()
else:
    ap.print_help()
