# coding=utf-8
from base64 import *
import os,sys,time


def logo():
    os.system('clear')
    print '          \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x90\xe2\x95\x97 \xe2\x95\xa6\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\n          \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\xa3 \xe2\x95\x91   \xe2\x95\x91 \xe2\x95\x91\xe2\x95\xa3 \xe2\x95\x94\xe2\x95\xa9\xe2\x95\xa6\xe2\x95\x9d \xe2\x95\x91\n          \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90 \xe2\x95\xa9\n               Secret Your Text with base64'


def polo(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.5 / 100)

def pilihan():
    try:
        logo()
        print '\n\n     1). Secret\n     2). UnSecret'
        pil = raw_input('\n     Pilih : ')
        if pil == '1':
          polo('     ════════════════════════[Secret]>')
          enc = raw_input('     [+] Text  : ')
          b = b64encode(enc)
          print '     [+] Hasil : ' +str(b) + '\n\n\n     Copyright© 2020 sCuby07 | Cyber Ghost Indonesia'
        elif pil == '2':
            polo('     ════════════════════════[UnSecret]>')
            dec = raw_input('     [+] Text  : ')
            c = b64decode(dec)
    	    print '     [+] Hasil : ' +str(c) + '\n\n\n     Copyright© 2020 sCuby07 | Cyber Ghost Indonesia'
	else:
	     print '     Masukan Input Yang Benar!'
  	     time.sleep(3)
	     pilihan()
    except TypeError:
	  print '     Text Bukan Type base64'
          time.sleep(3)
	  pilihan()



if __name__ == '__main__':
     pilihan()
