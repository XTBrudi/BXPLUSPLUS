E=print
from colorama import Fore as C,Style as D,init
init()
from load import load
import subprocess as F,os,sys,base64 as A
G='RW50ZXIgdGhlIHBhc3N3b3JkLg=='
H='V3JvbmcgcGFzc3dvcmQu'
I='QkhVQktFWV9xdXppcjFjMnRiaHJPQjU2RzMwYnJzalV0NmI3QVI4VnQ0YkpOYnNl'
def B():
	B='utf-8';E(f"{C.RED}{A.b64decode(G).decode(B)}{D.RESET_ALL}\n");J=input('>> ');F.call('clear'if os.name=='posix'else'cls',shell=True)
	if J==A.b64decode(I).decode(B):load()
	else:E(f"{C.RED}{A.b64decode(H).decode(B)}{D.RESET_ALL}");sys.exit()