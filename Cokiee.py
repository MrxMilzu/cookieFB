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
    print("""\033[96m
        ╔═╗╔═╗╦ ╦ ╦ ╔═╗ ╔═╗╔╗      
        ║  ║ ║║╣  ║ ║_  ║_ ╠╩╗           
        ║  ║ ║║║  ║ ║   ║  ║ ║
        ╚═╝╚═╝╩ ╩ ╩ ╚═╝ ╝  ╚═╝  By.Milzu-TC """)

def fank():
    a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    print("\033[90m[\033[96m▪\033[90m]\033[97mIP ANDA\033[93m : " + ip)
def boboiboy():
    print("\033[92m╔════════════════════════════════╗")
    print("║ [1].cara mendapatkan cokie FB  ║")
    print("╚════════════════════════════════╝")
    print("╔════════════╗")
    print("║ [2].keluar ║")
    print("╚════════════╝")
    print("\033[93m╭╼[Mrx.Milzu]─[cokieFB]")
    print ("\033[93m~")
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
       gopal("\033[93m buka facebook di kiwi...")
       gopal("\033[92m jangan lupa login FB Juga Di kiwi...")
       os.system("xdg-open https://free.facebook.com/?_rdc=1&_rdr")
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
    print("\033[93m Jika sudah buka crome web store di kiwi ke tahap selanjutnya")
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
       gopal("\033[93m cari di crome web store ...")
       gopal("xdg-open https://chrome.google.com/webstore/detail/fb-cookie/nkjaphaegknhjpjhgnigaofonibmbmom")
       gopal("\033[93m jika sudah ke tahap selanjutnya")
       powersvera()
    elif megabot == "2" or megabot =="02":
         print("\033[92m Subscribe dulu chanel saya...")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         sys.exit()

def powersvera():
    print("\033[93m menonton chanel saya...")
    print("\033[92m╔══════════════════════════════════════════════╗")
    print("║[1].di bagian akir anda tonton aja chanel saya║")
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
