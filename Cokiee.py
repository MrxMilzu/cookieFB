#!/usr/bin/python
# -*- coding: utf-8 
#~═║CREATED2021║~═
#~═║CokieFB║~═
#~═║coding By Milzu.TC║~═

import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def yaya():
    os.system("git pull")
def ying():
    os.system("clear")
def gopal(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def adudu():
    time.sleep(0.3)
    gopal("""\033[96m
        ╔═╗╔═╗╦ ╦ ╦ ╔═╗ ╔═╗╔╗      
        ║  ║ ║║╣  ║ ║_  ║_ ╠╩╗           
        ║  ║ ║║║  ║ ║   ║  ║ ║
        ╚═╝╚═╝╩ ╩ ╩ ╚═╝ ╝  ╚═╝  By.Milzu """)

def fank():
    a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    gopal("\033[90m[\033[96m▪\033[90m]\033[97mIP ANDA\033[93m : " + ip)
Ussername = "FIQHI"

loop = 'true'
while (loop == 'true'):
    ussername = input("\n\033[93m[\033[92m🔒\033[93m] \033[95mLogin sebagai\033[93m:\033[93m ")
    if (ussername == Ussername):
            loop = 'false'
    else:
            gopal("[\033[91m!\033[93m]\033[93mSalah") 
            exit()
Password = "CYBERPUNK"

loop = 'true'
while (loop == 'true'):
    passcode = input("\033[1;93m[?] \033[92mPassword\033[95m:\033[93m ")
    if (passcode == Password):
            gopal("Login Suksesfully...")
            loop = 'false'
    else:
            gopal("[\033[91m!\033[93m]\033[93mSalah")
            exit()
def boboiboy():
    time.sleep(0.1)
    gopal("\033[92m╔════════════════════════════════╗")
    gopal("║ [1].cara mendapatkan cokie FB  ║")
    gopal("╚════════════════════════════════╝")
    gopal("╔════════════╗")
    gopal("║ [2].keluar ║")
    gopal("╚════════════╝")
    time.sleep(0.1)

    gopal("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    gopal ("\033[93m~")
    coco=input("\033[93m╰╼▪>   \033[96m")
    if coco == "1" or coco =="01":
       gopal("\033[93m download dulu kiwi browser.")
       os.system("xdg-open https://play.google.com/store/apps/details?id=com.kiwibrowser.browser")
       gopal("\033[92m Jika sudah ke tahap selanjutnya")
       helo()
    elif coco == "2" or coco =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

def helo():
    print("\033[93m Jika sudah download kiwi ke tahap selanjutnya")
    print("\033[92m╔════════════════════╗")
    print("║ [1].buka FB di kiwi║")
    print("╚════════════════════╝")
    print("╔════════════╗")
    print("║ [2].keluar ║")
    print("╚════════════╝")
    print("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    print ("\033[93m~")
    papazola=input("\033[93m╰╼▪>   \033[96m")
    if papazola == "1" or papazola =="01":
       gopal("\033[93m salin tautan dibawah ini...")
       gopal("\033[92m jangan lupa login FB Juga Di kiwi...")
       gopal("👉https://free.facebook.com/?_rdc=1&_rdr")
       gopal("\033[92m dan pastekan ke kiwi browser")
       laksamana()
    elif papazola == "2" or papazola =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

def laksamana():
    print("\033[93m Jika sudah buka facebook di kiwi ke tahap selanjutnya")
    print("\033[92m╔═══════════════════════════════════╗")
    print("║ [1].buka crome web store di kiwi  ║")
    print("╚═══════════════════════════════════╝")
    print("╔════════════╗")
    print("║ [2].keluar ║")
    print("╚════════════╝")
    print("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    print ("\033[93m~")
    ochobot=input("\033[93m╰╼▪>   \033[96m")
    if ochobot == "1" or ochobot =="01":
       gopal("\033[93m buka crome web store di kiwi...")
       gopal("\033[96m Salin lah tautan dibawah ini dan copy&paste")
       gopal("👉https://chrome.google.com/webstore/category/extensions")
       bagogo()
    elif ochobot == "2" or ochobot =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

def bagogo():
    print("\033[93m Jika sudah pastekan tautan di atas ke kiwi ke dan tekan enter")
    print("\033[92m Jika sudah ke tahap selanjutnya")
    print("\033[92m╔════════════════════════════╗")
    print("║ [1].cari CokieFB di kiwi   ║")
    print("╚════════════════════════════╝")
    print("╔═════════════╗")
    print("║ [2].keluar  ║")
    print("╚═════════════╝")
    print("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    print ("\033[93m~")
    megabot=input("\033[93m╰╼▪>   \033[96m")
    if megabot == "1" or megabot =="01":
       gopal("\033[93m cari di halaman [Telusuri TOKO!] crome web store ...")
       gopal("\033[96m dan Cari 👉FBCookie")
       gopal("\033[96m dan click [FBCookie]")
       gopal("\033[92m [Lalu click tambahkan ke crome]")
       atokaba()
    elif megabot == "2" or megabot =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

def atokaba():
    print("\033[93m Jika sudah tambahkan ke crome...")
    print("\033[92m╔══════════════════════════════════════════════╗")
    print("║[1].cari titik tiga di sebelah kanan apk kiwi dan (click)║")
    print("╚══════════════════════════════════════════════╝")
    print("╔═════════════╗")
    print("║ [2].keluar  ║")
    print("╚═════════════╝")
    print("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    print ("\033[93m~")
    atok=input("\033[93m╰╼▪>   \033[96m")
    if atok == "1" or atok =="01":
       gopal("\033[92m Jika sudah click geser ke bawah...")
       os.system("lalu [click] Yang kita tambahkan ke crome tadi")
       gopal("\033[96m Yaitu [FBCookie]")
       gopal("dan jangan lupa subscribe chanel saya...")
       powersvera()
    elif atok == "2" or atok =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

def powersvera():
    print("\033[93m menonton chanel saya...")
    print("\033[92m╔══════════════════════════════════════════════╗")
    print("║[1].bagi yang tidak mengerti tonton aja chanel saya║")
    print("╚══════════════════════════════════════════════╝")
    print("╔═════════════╗")
    print("║ [2].keluar  ║")
    print("╚═════════════╝")
    print("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    print ("\033[93m~")
    power=input("\033[93m╰╼▪>   \033[96m")
    if power == "1" or power =="01":
       gopal("\033[93m buka cookie di kiwi...")
       os.system("xdg-open https://youtu.be/QF0jMxC6CkE")
       gopal("\033[93m Terimakasih telah menggunakan tolls...")
       gopal("dan jangan lupa subscribe chanel saya...")
       sys.exit()
    elif power == "2" or power =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

if __name__=="__main__":
     ying()
     yaya()
     ying()
     adudu()
     fank()
     boboiboy()
