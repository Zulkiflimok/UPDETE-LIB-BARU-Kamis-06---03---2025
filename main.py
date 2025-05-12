#lib nya
#[9/5 8.04 PM] Noz As: line://app/1654421336-LVE6z591

#line://app/1603103514-p5KLLVQW

#line://app/1647207293-rNJ7MlJm

#line://app/1603968955-ORWb9RdY

#line://app/1653635854-BmgzeMGk

#line://app/1623679774-k9nBDB6b

#line://app/1655722995-58MG7mN0
#[9/5 8.05 PM] Noz As: Berikut Data Liffmu Majikanku

#Liff [ 01 ]
#https://liff.line.me/2000602682-YP5KArqL

#Liff [ 02 ]
#https://liff.line.me/2000602728-ZB8DrLMB

#Liff [ 03 ]
#https://liff.line.me/2000602744-qe53a4vv
#
#
from Zul import *
from ZulBots.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffNoneContext, LiffViewRequest
from ZulBots.ttypes import ContentType as Type
from ZulBots.ttypes import TalkException
from justgood import imjustgood
from datetime import datetime
import humanize
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback, livejson
from threading import Thread,Event
from subprocess import check_output
from Naked.toolshed.shell import execute_js
import sys,traceback
_session = requests.session()
botStart = time.time()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2 
#=========================================================
cl = LINE("imel@gmail.com","katasandi",appName="DESKTOPWIN\t9.8.0.3597\tWINDOWS\t10.0.{randomName};SECONDARY") #taru imel sma sandi mu di sini
#=========================================================

oepoll = OEPoll(cl)
#=========================================================
clProfile = cl.getProfile()
clSettings = cl.getSettings()
#=========================================================
clMID = cl.profile.mid
mid = cl.getProfile().mid
creator = ["clMID","u9b0ae88d7cf669da9a8416bd4c765cd1","u9bef22a6f6ee633bdf4dddd6572dcd3f","ub3a4144fd62686316824b3e1c39a5f04"]
owner = ["clMID","u9b0ae88d7cf669da9a8416bd4c765cd1","u9bef22a6f6ee633bdf4dddd6572dcd3f","ub3a4144fd62686316824b3e1c39a5f04"]
admin = ["clMID","u9b0ae88d7cf669da9a8416bd4c765cd1","u9bef22a6f6ee633bdf4dddd6572dcd3f","ub3a4144fd62686316824b3e1c39a5f04"]
staff = ["clMID","u9b0ae88d7cf669da9a8416bd4c765cd1","u9bef22a6f6ee633bdf4dddd6572dcd3f","ub3a4144fd62686316824b3e1c39a5f04"]
Bots = [mid]
ZulBots = creator + owner+ admin + staff
#=========================================================
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
invitemember = []
targets = []
welcome = []
leave = []
msg_dict = {}
msg_dict1 = {}
temp_flood = {}
try:
    with open("quisdata.json", "r", encoding="utf_8_sig") as fp:
        quisdata = json.loads(fp.read())
except:
    print ("data file not found, data dict default will used")
    quisdata = {}

with open("quest.txt", "r") as file:
     blist = file.readlines()
     quest = [x.strip() for x in blist]
file.close()
group = cl.getAllChatIds()

for g in group:
  quisdata[g]={'point':{}}
  quisdata[g]['saklar']=False
  quisdata[g]['quest']=''
  quisdata[g]['asw']=[]
  quisdata[g]['tmp']=[]
#=========================================================
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changevp": False,
    "changeCover":{},
    "autoJoinTicket":True,
    "readerPesan": "Gw @!, Kang Sider",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
cctv4 = {"cyduk":{},"point":{},"sidermem":{}}
tailah = {
    "siderTemp": {},
    "siderPesan": "You can join chat?",
}

read = { 
    "readMember": {},
    "readPoint": {}
}

tes = {
    "Message": {},
    "msg": {},
}

tes2 = {
    "Message2": {},
    "msg2": {},
}
wait = {
    "Limit": 3,
    "owner":{},
    "admin":{},
    "detectvp":True,
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "invite":False,
    "Invi":False,
    "quis": True,
    "autoJoinquis":True,
    "checkPost":True,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "puskun":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    'autoBlock':False,
    "respontag":True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":5},
    'autotext':True,
    'autoLeave':False,
    'Timeline':False,
    "detectMention":False,
    "detectMention1":False,
    "Mentionkick":False,
    "welcomemsgOn":True,
    "welcomeOn":True,
    "stickerOn":False,
    "sticker":False,
    "rsmule": True,
    "tiktok": True,
    "ytube": True,
    "welcomemsg": True,
    "changevp": False,
    "changeFoto": {},
    "likeOn": True,
    "stickers": {},
    "apikey" : "amdbots",
    "dark" : True,
    "nganu" : False,
    "apkTikel": True,
    "AddstickerSider": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerPesan": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerWelcome": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerLeave": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "stk":{},
    "selfbot":True,
    "token":True,
    "responGc":True,
    "respontag":True,
    "Images":{},
    "Img":{},
    "Addimage":{},
    "Videos":{},
    "Video":{},
    "Addvideo":{},
    "laranganOn":True,
    "responsalam":True,
    "liff": "2000602682-YP5KArqL",
    "liff1": "2000602682-YP5KArqL",
    "liff2": "2000602728-ZB8DrLMB",
    "liff3": "2000602744-qe53a4vv",
    "anu": "2000602682",
    "anu1": "2000602682",
    "anu2": "2000602728",
    "anu3": "2000602744",
    "saat": "Data Liff Kamu Saat Ini [ 1 ]\n━━━━━━━━━━━━━━━━━━━\n",
    "saat1": "Data Liff Kamu Saat Ini [ 1 ]\n━━━━━━━━━━━━━━━━━━━\n",
    "saat2": "Data Liff Kamu Saat Ini [ 2 ]\n━━━━━━━━━━━━━━━━━━━\n",
    "saat3": "Data Liff Kamu Saat Ini [ 3 ]\n━━━━━━━━━━━━━━━━━━━\n",
    "link":"https://i.gifer.com/7CJk.gif",
    "link":"https://www.smule.com",
    "amdb":"#1zul",
    "amda":"nukeall",
    "balasan": "ngetag bae tandane jomblo",
    "siderMsg": "suka ngintip sini msk kk",
    "mention1":"hai kk",
    "mention":"Terciduk kau tukang ngintip dasar😎 ",
    "Tag":"Ada apa sayang 🥰",
    "leave":"Selamat Tinggal Kak ",
    "welcome":"sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ɢᴀᴇᴢ\nᴊᴀɴɢᴀɴ ɴᴀᴋᴀʟ ʏᴀ ᴅɪ ᴍᴀʀɪ",
#    "welcome":"Selamat Datang Kk !!",
    "noTiFcall1":"  Ya udh turun aja",
    "noTiFcall":"  Naik yuk Kk",
    "order":"""
╭────────────────
│• OPEN  BOTS TEAM TERMUX
├────────────────
├ ▣ https://wa.me/message/ANCIF474MS6OL1
├ ▣
├ ▣ BOT GOLANG 1 BULAN 10K
├ ▣
├ ▣7 ASIS 2 AJS 10 RIBUH
├ ▣
├ ▣ BOT SB GRATIS
├ ▣
├ ▣ BOT KUIS GRATIS
├ ▣
├ ▣ BOT PUBLIK GRATIS
├ ▣
├ ▣ https://wa.me/message/ANCIF474MS6OL1
├ ▣
├ ▣ Wa 0857-5707-6639
├ ▣
├ ▣ https://youtube.com/@zulkiflimokoagow7511?si=8s6uELcJd__b_Fjb
╰────────────────
    """,
    "comment":"""
▣ TEAM TERMUX ▣
▣ Done Like
▣ Done Comment
▣ Add Owner kami
▣ https://wa.me/message/ANCIF474MS6OL1""",
    "message":"""
╭────────────────
│• OPEN  BOTS TEAM TERMUX
├────────────────
├ ▣ https://wa.me/message/ANCIF474MS6OL1
├ ▣
├ ▣ BOT GOLANG 1 BULAN 10K
├ ▣
├ ▣7 ASIS 2 AJS 10 RIBUH
├ ▣
├ ▣ BOT SB GRATIS
├ ▣
├ ▣ BOT KUIS GRATIS
├ ▣
├ ▣ BOT PUBLIK GRATIS
├ ▣
├ ▣ https://wa.me/message/ANCIF474MS6OL1
├ ▣
├ ▣ Wa 0857-5707-6639
├ ▣
├ ▣ https://youtube.com/@zulkiflimokoagow7511?si=8s6uELcJd__b_Fjb
╰────────────────
▣ Langsung gasken link bawah ini
▣ https://wa.me/message/ANCIF474MS6OL1
▣ Wa 0857-5707-6639""", 
    "unsend":False,
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

comd = {
    "help": "help",
    ".help": ".help",
    "/help": "/help",
    "zhelp": "zhelp",
    ",help": ",help",
    "help ": "help ",
    "1help": "1help",
    "ช่วย": "ช่วย",
    "يساعد": "يساعد",
    "speed": "speed",
    "tagall": "hay",
    "aping": "aping",
    "cban": "cban",
    "yasinon": "yasin on",
    "yasinoff": "yasin off",
    "sider1On": "sider1 on",
    "sider1Off": "sider1 off",
    "siderOn": "sider on",
    "siderOff": "sider off",
    "ซีรอน": "ไซเดอร์บน",
    "ไซด์โรฟ": "ไซเดอร์ออก",
    "bye": "@bye",
    "unsend": "unsend"
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
cctv1 = {
    "cyduk1":{},
    "point1":{},
    "sidermem1":{}
}

temptag = {
    "stealtag":False
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('sticker.json', 'r') as fp:
    stickers = json.load(fp)
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)

mulai = time.time()
def bypassJS(aping):
    ktl = cl.getChats([aping]).chats[0]
    if ktl.extra.groupExtra.inviteeMids == None:pends = []
    else:pends = ktl.extra.groupExtra.inviteeMids
    pending = []
    for x in pends:
        if x not in Bots and x not in admin and x not in clMID:pending.append(x)
    member = []
    for x in ktl.extra.groupExtra.memberMids:
        if x not in admin and x not in Bots and x not in clMID:member.append(x)
    cm = 'kickall.js gid={} type=dual token={} {}'.format(aping, cl.authToken, "app=desktopwin")
    for x in pending:
        cm += ' uik={}'.format(x)
    for x in member:
        cm += ' uid={}'.format(x)
    success = execute_js(cm)
    return success    
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
def backupquisData():
    with open("quisdata.json", "w", encoding="utf8") as f:
        json.dump(quisdata, f, ensure_ascii=False, indent=4, separators=(',', ': '))
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "BOT ACTIVE AGAIN"
                        cl.sendMessage(tmp, veza, {'AGENT_LINK': "https://https://wa.me/message/ANCIF474MS6OL1", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def helpvirus():
    helpKvirus2 = """
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
"""
    return helpKvirus2

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "ProTection\n\n" + \
                  "." + key + "Priall on\n" + \
                  "." + key + "Remotepro [Numbr]\n" + \
                  "." + key + "Protectqr On\n" + \
                  "." + key + "Protectjoin On\n" + \
                  "." + key + "Protectkick On\n" + \
                  "." + key + "Protectcancel On\n" + \
                  "." + key + "• ➥Next Key[ Token ]\n" + \
                  "." + key + "•────────•\n" + \
                  "." + key + "「 Thanks to :↘TEAM TERMUX V 16\n"                 
    return helpMessage1

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "BOT ACTIVE AGAIN"
                        cl.sendMessage(tmp, veza, {'AGENT_LINK': "https://https://wa.me/message/ANCIF474MS6OL1", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)
def helpquis():
    helpMessagequis = "[ Daftar Perintah ]" + "\n" + \
                  "zulkifli QUIS /mulai" + "\n" + \
                  "zulkifli QUIS rek" + "\n" + \
                  "zulkifli QUIS /next" + "\n" + \
                  "zulkifli QUIS /nyerah" + "\n" + \
                  "zulkifli QUIS dana" + "\n" + \
                  "zulkifli QUIS laporkan" + "\n" + \
                  "[ TEAM TERMUX ]"
    return helpMessagequis
def getQuest(to):
	try:
			quisdata[to]['quest'] = ''
			quisdata[to]['asw'] = []
			quisdata[to]['tmp'] = []
			a = random.choice(quest)
			a = a.split('*')
			quisdata[to]['quest'] = a[0]
			for i in range(len(a)):
				quisdata[to]['asw'] += [a[i]]
			quisdata[to]['asw'].remove(a[0])
			for j in range(len(quisdata[to]['asw'])):
				quisdata[to]['tmp'] += [str(j+1)+'. _________']
	except Exception as e:
		print(e)
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)
def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': cl.authToken,
        'X-Line-Application': cl.server.APP_NAME,
        'X-Line-ChannelId': wait["anu"],
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

def sendFlexAudio(to, link):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest(wait["liff"], xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {
        'messages': [{
            'type': 'audio',
            'originalContentUrl': link,
            'duration': 250000
        }]
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    return res

def sendFlexVid2024(to, vid_url, img_url):
    #img_url = "https://i.ibb.co.com/YFgMQKXz/a97bfba3168f331db7ddbf5e3cebd240.jpg"
    data = {
      "type": "bubble",
      "size": "hecto",
      "hero": {
        "type": "video",
        "url": vid_url,
        "altContent": {
          "type": "box",
          "layout": "vertical",
          "contents": []
        },
        "previewUrl": img_url,
        "aspectRatio": "2:2"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#FFFFFF"
        }
      }
    }
    sendTemplate(to, {"type": "flex", "altText": "TEAM TERMUX", "contents": data})

def sendFlexVid2025(to, vid_url, img_url):
    #img_url = "https://i.ibb.co.com/7tWL3r2z/61c5d7029d173fe0ae816aa67c79532a.jpg"
    data = {
      "type": "bubble",
      "size": "hecto",
      "hero": {
        "type": "video",
        "url": vid_url,
        "altContent": {
          "type": "box",
          "layout": "vertical",
          "contents": []
        },
        "previewUrl": img_url,
        "aspectRatio": "2:2"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#FFFFFF"
        }
      }
    }
    sendTemplate(to, {"type": "flex", "altText": "TEAM TERMUX", "contents": data})


def sendFlexVid2026(to, vid_url, img_url):
    #img_url = "https://i.ibb.co.com/pB4rwmGR/c587e77101042b11485dd465bfe6df38.jpg"
    data = {
      "type": "bubble",
      "size": "hecto",
      "hero": {
        "type": "video",
        "url": vid_url,
        "altContent": {
          "type": "box",
          "layout": "vertical",
          "contents": []
        },
        "previewUrl": img_url,
        "aspectRatio": "2:2"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#FFFFFF"
        }
      }
    }
    sendTemplate(to, {"type": "flex", "altText": "TEAM TERMUX", "contents": data})    

def sendFlexVideo(to, videoUrl, thumbnail='dark'):
    main = ["dark","red","cyan","yellow","green","white"]
    if thumbnail in main:
       thumbnail = "https://i.ibb.co.com/mRBRg3m/Whats-App-Image-2024-01-30-at-12-47-27.jpg"
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest(wait["liff"], xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {
        'messages': [{
            'type': 'video',
            'originalContentUrl': videoUrl,
            'previewImageUrl': thumbnail,
        }]
    }
    return requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest(wait["liff"], xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    #data = line.server.liff(data)
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTextTemplateB(to, text):
    data = {
            "type": "flex",
            "altText": "TEAM TERMUX",
            "contents": {
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "url": "https://i.ibb.co.com/PrqwbmV/20241013-222804.jpg",
    "size": "full",
    "aspectRatio": "70:1",
    "aspectMode": "cover",
    "animated": True
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": text,
        "color": "#ffff00",
        "wrap": True,
        "align": "start",
        "size": "sm"
      }
    ],
    "backgroundColor": "#000000",
    "paddingAll": "0px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "https://wa.me/message/ANCIF474MS6OL1"
    }
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co.com/PrqwbmV/20241013-222804.jpg",
        "size": "full",
        "aspectRatio": "70:1",
        "aspectMode": "cover",
        "animated": True
      }
    ],
    "paddingAll": "0px"
  }
}
}
    sendTemplate(to, data)  


    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def pretyPrintJson(djson):
        print(json.dumps(djson, indent=4, sort_keys=True))   
    
def runtime2(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Menit %02d Detik' % (mins, secs)

def flex3(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    #scover = cl.getProfileCoverURL(mid)
    time.sleep(1)
    data = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "139.5px", "height": "17.5px", "cornerRadius": "2px", "offsetTop": "9px", "offsetStart": "10.5px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
    sendTemplate(to, data)
#ganti fidio qr
def flexvian(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    #scover = cl.getProfileCoverURL(mid)
    time.sleep(1)
    data = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "139.5px", "height": "17.5px", "cornerRadius": "2px", "offsetTop": "9px", "offsetStart": "10.5px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
    sendTemplate(to, data)

def flex2(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    #scover = cl.getProfileCoverURL(mid)
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    time.sleep(1)
    data = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "139.5px", "height": "17.5px", "cornerRadius": "2px", "offsetTop": "9px", "offsetStart": "10.5px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
    sendTemplate(to, data)         

def flextext(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    #scover = cl.getProfileCoverURL(mid)
    time.sleep(1)
    data = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "carousel", "contents": [ { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "backgroundColor": "#000000" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "SELFBOT LINE", "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "115px", "height": "10px", "offsetTop": "21.5px", "offsetStart": "22px" }, { "type": "text", "text": text, "size": "8px", "color": "#00ff00", "wrap": True, "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "backgroundColor": "#000000" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "LINE CORPOROTATION", "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "115px", "height": "10px", "offsetStart": "22px", "offsetBottom": "21.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } ] } }
    sendTemplate(to, data)                  
#help
def modflex(to, text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    contact = cl.getContact(mid)
    time.sleep(1)
    data = {"type": "flex","altText": "TEAM TERMUX","contents": {"type": "carousel","contents": [{"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectMode": "cover","aspectRatio": "2:3","backgroundColor": "#000000"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "30px","height": "30px","backgroundColor": "#000000","cornerRadius": "50px","offsetTop": "3px","offsetStart": "8px","borderWidth": "0.1px","borderColor": "#00ffff"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "13px","height": "13px","backgroundColor": "#000000","cornerRadius": "50px","offsetTop": "17px","offsetStart": "47px","borderWidth": "0.1px","borderColor": "#00ffff"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "2:3","aspectMode": "cover","animated": True}],"position": "absolute","width": "130px","height": "170px","offsetTop": "50px","offsetStart": "13px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "🄼🄰🄸🄽 🄼🄴🄽🅄","size": "8px","color": "#00ffff","align": "center","offsetTop": "3px"}],"position": "absolute","width": "77px","height": "14px","borderWidth": "0.1px","borderColor": "#00ffff","cornerRadius": "3px","offsetTop": "17px","offsetEnd": "14px"},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐀𝐃𝐌𝐈𝐍","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "50px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Admin"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "🆀🆄🅸🆂 🅾🅽","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "80px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Translate"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "SPONSOR","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "110px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Banned"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐒𝐄𝐓𝐓𝐈𝐍𝐆","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "140px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Setting"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐆𝐑𝐎𝐔𝐏","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "170px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Group"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐌𝐄𝐃𝐈𝐀","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "200px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Media"}},{"type": "text","text": "TEAM TERMUX","size": "6px","color": "#ffffff","offsetTop": "1px","offsetEnd": "27px","position": "absolute"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "𝔖𝔢𝔩𝔣𝔟𝔬𝔱","size": "6px","color": "#00ffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "46px","height": "8px","borderWidth": "0.1px","borderColor": "#00ffff","cornerRadius": "2px","offsetBottom": "1.5px","offsetStart": "12px","backgroundColor": "#000000"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "𝔗𝔢𝔪𝔭𝔩𝔞𝔱𝔢","size": "6px","color": "#00ffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "46px","height": "8px","borderWidth": "0.1px","borderColor": "#00ffff","cornerRadius": "2px","offsetBottom": "1.5px","backgroundColor": "#000000","offsetEnd": "10.5px"}],"paddingAll": "0px"},"action": {"type": "uri","label": "action","uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"}},{"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/h8bC8T2/1639913956273.png","size": "full","aspectMode": "cover","aspectRatio": "2:3","backgroundColor": "#000000"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "30px","height": "30px","backgroundColor": "#000000","cornerRadius": "50px","offsetTop": "3px","offsetStart": "8px","borderWidth": "0.1px","borderColor": "#00ffff"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "13px","height": "13px","backgroundColor": "#000000","cornerRadius": "50px","offsetTop": "17px","offsetStart": "47px","borderWidth": "0.1px","borderColor": "#00ffff"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "2:3","aspectMode": "cover","animated": True}],"position": "absolute","width": "130px","height": "170px","offsetTop": "50px","offsetStart": "13px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "🄼🄰🄸🄽 🄼🄴🄽🅄","size": "8px","color": "#00ffff","align": "center","offsetTop": "3px"}],"position": "absolute","width": "77px","height": "14px","borderWidth": "0.1px","borderColor": "#00ffff","cornerRadius": "3px","offsetTop": "17px","offsetEnd": "14px"},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "LAPORKAN","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "50px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Protect"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐏𝐑𝐎𝐅𝐈𝐋𝐄","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "80px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Profile"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "DANA","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "110px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Remote"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐇𝐄𝐋𝐏 𝐉𝐒","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "140px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Help%20js"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐒𝐓𝐀𝐓𝐔𝐒","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "170px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Status"}},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "𝐂𝐑𝐄𝐀𝐓𝐎","size": "10px","color": "#00ffff","align": "center","offsetTop": "4px"}],"position": "absolute","width": "80px","height": "20px","backgroundColor": "#000000","borderWidth": "0.5px","borderColor": "#00ffff","cornerRadius": "5px","offsetTop": "200px","offsetStart": "43px","action": {"type": "uri","label": "action","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Creator"}},{"type": "text","text": "TEAM TERMUX","size": "6px","color": "#ffffff","offsetTop": "1px","offsetEnd": "27px","position": "absolute"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "𝔖𝔢𝔩𝔣𝔟𝔬𝔱","size": "6px","color": "#00ffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "46px","height": "8px","borderWidth": "0.1px","borderColor": "#00ffff","cornerRadius": "2px","offsetBottom": "1.5px","offsetStart": "12px","backgroundColor": "#000000"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "𝔗𝔢𝔪𝔭𝔩𝔞??𝔢","size": "6px","color": "#00ffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "46px","height": "8px","borderWidth": "0.1px","borderColor": "#00ffff","cornerRadius": "2px","offsetBottom": "1.5px","backgroundColor": "#000000","offsetEnd": "10.5px"}],"paddingAll": "0px"}}]}}
    sendTemplate(to, data)
#atolike
def sendAhmad(to, text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    contact = cl.getContact(mid)
    time.sleep(1)
    data = {"type": "flex","altText": "TEAM TERMUX ","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image","url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),"size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
    sendTemplate(to, data)

def sendFoter(to, text):
    time.sleep(1)
    data = {
        "type": "text",
        "text": text,
        "sentBy": {
             "label": "• TEAM TERMUX •",
             "iconUrl": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg",
             "linkUrl": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"
         }
     }
    sendTemplate(to, data)

def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"

def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+cl.google_url_shorten(links)
    
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "update profile failed"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("vp.mp4")

def changeProfileVideo(to):
    if settings['changevp']['picture'] == None:
        return cl.sendReplyMessage(msg_id, to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == None:
        return cl.sendReplyMessage(msg_id, to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendReplyMessage(msg_id, to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')
def siderMembers4(to, mid):
    try:
        arrData = ""
        textx = ""
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getChats(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["siderMsg"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getChats(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getChats(to)
        textx = "╭─「 Daftar anggota 」\n├↘\n├↘1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n├↘\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├↘ {}. ".format(str(no))
            else:
                textx += "╰─「 Mentions {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def FakeStickerV2(to, spkg,sid, mids=[]): #DONE
    if clMID in mids: mids.remove(clMID)
    parsed_len = len(mids)//140+1
    result = '「 Mention Members 」\n'
    mention = '@Zul..\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*140:(point+1)*140]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees}),'STKPKGID':spkg,'STKID':sid}, 7)
        result = ''

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Zulkifli "
    if mids == []:
       raise Exception("Invalid mids")
    if "@!" in text:
       if text.count("@!") != len(mids):
          raise Exception("Invalid mids")
       texts = text.split("@!")
       textx = ""
       for mid in mids:
          textx += str(texts[mids.index(mid)])
          slen = len(textx)
          elen = len(textx) + 15
          arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
          arr.append(arrData)
          textx += mention
       textx += str(texts[len(mids)])
    else:
       textx = ""
       slen = len(textx)
       elen = len(textx) + 15
       arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
       arr.append(arrData)
       textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)


def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Result {} Sider 」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getChats(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ʜᴀʏ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getChats([to],True,True).chats[0]
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".cl.getChats([to],True,True).chats[0]
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        #cl.sendMessage(msg.to, None, contentMetadata={"STKID":"2713783","STKPKGID":"3524","STKVER":"1"}, contentType=7)             
    except Exception as error:
        cl.sendMessage(msg.to, "[ INFO ] Error :\n" + str(error))


#def welcomeMembers(to, mid):
#    try:
#        arrData = ""
#        textx = "Welcome:  ".format(str(len(mid)))
#        arr = []
#        no = 1
#        num = 2
#        for i in mid:
#            ginfo = cl.getChats(to)
#            mention = "@x\n"
#            slen = str(len(textx))
#            elen = str(len(textx) + len(mention) - 1)
#            arrData = {'S':slen, 'E':elen, 'M':i}
#            arr.append(arrData)
#            textx += mention+wait["welcome"]+"\n"+str(ginfo.name)
#            if no < len(mid):
#                no += 1
#                textx += "%i " % (num)
#                num=(num+1)
#            else:
#                try:
#                    no = "\n╚══[ {} ]".format(str(cl.getChats(to).name))
 #               except:
 #                   no = "\n╚══[ Success ]"
#        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
 #   except Exception as error:
#        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Bye :".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getChats(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getChats(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@ZulBots  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getContact("u176ef6889643e290ba5801bffc83457b").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def ZulBots(to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Zulkifli "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 5
                else:slen = len(textx);elen = len(textx) + 5
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def ZulKiller(to, mid):
    try:
        aa = '{"S":"0","E":"5","M":'+json.dumps(mid)+'}'
        text_ = '@Zul'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def getUserActivity(user, to_biasa=""):
    jam = pytz.timezone("Asia/Jakarta")
    jamSek = datetime.now(tz=jam)
    jamm = datetime.strftime(jamSek, "%d-%m-%Y")
    jam_time = datetime.strftime(jamSek, "%H:%M:%S")
    msgs = " 𝙉𝙊𝙏𝙞𝙁 𝘿𝙀𝙇𝙀𝙏𝙀 𝘼𝘾𝘾𝙊𝙐𝙉𝙏"
    msgs += f"\n• {jamm} {jam_time}"
    resId = False
    try:
        cl.getContact(user)
        resId = True
    except:
        resId = False
    try:
        if user not in thedata["history_upname"]:
            thedata["history_upname"][user] = [getname(user)]
        indexName = len(thedata["history_upname"][user])
        msgs += f"\n• Display Name: {thedata['history_upname'][user][0]}\n"
        if indexName > 1:
            msgs += "• Previous:\n"
            for no, logName in enumerate(thedata["history_upname"][user][1:indexName], 1):
                msgs += f"{no}. {logName}\n"
    except:
        pass
    if user in thedata["useract"]:
        if thedata["useract"][user]["type"] is not None and thedata["useract"][user]["data"] != {}:
            actType = thedata["useract"][user]["type"]
            actData = thedata["useract"][user]["data"]
            times = humanize.naturaltime(datetime.fromtimestamp(actData["time"]/1000))
            type_mapping = {
                "add": "Add Contact",
                "announce": "Announce",
                "message": "Send Message",
                "read": "Read Message",
                "unsend": "Unsend Message",
                "reaction": "Reaction Message",
                "join": "Join Group",
                "leave": "Leave Group",
                "invite": "Invite User",
                "kick": "Kick User",
                "cancel": "Cancel User",
                "album": "Album Group",
                "call invitation": "Call Invitation",
                "call group": "Call Group",
                "update group": "Update Group",
                "update profile": "Update Profile"
            }
            if actType in type_mapping:
                msgs += "\n𝙉𝙤𝙩𝙞𝙛 𝗔𝗰𝘁𝗶𝘃𝗶𝘁𝙖𝙨\n"
                msgs += f"• Type: {type_mapping[actType]}\n"
                msgs += f"• Time: {times}\n"
                msgs += f"• Group: {actData.get('group', 'N/A')}\n"
                msgs += f"• Detail: {actData.get('msg', 'N/A')}\n"
                if actType == "invite" and len(actData["invited"]) != 0:
                    msgs += f"• Invited: {len(actData['invited'])}\n"
                    try:contacts = [c.displayName for c in cl.getContacts(actData["invited"])]
                    except:contacts = []
                    for no, i in enumerate(contacts, 1):
                        msgs += f"{no}. {i}\n"
                elif actType in ["kick", "cancel"]:
                    msgs += f"• {actType.capitalize()}: {cl.getContact(actData.get('kicked' if actType == 'kick' else 'canceled')).displayName}\n"

    if to_biasa != "":
        return cl.sendMessage(to_biasa, msgs)
    for to in thedata["user_gid"][user]:
        try:cl.sendMessage(to, msgs)
        except:pass
        time.sleep(0.1)


def unregister_User(op):
    group = cl.getChats([op.param1],True,True).chats[0]
    adv = cl.getContact(op.param2)
    jam = pytz.timezone("Asia/Jakarta")
    jamSek = datetime.now(tz=jam)
    tgl = datetime.strftime(jamSek, '%d-%m-%Y')
    jamnya = datetime.strftime(jamSek,'%H:%M:%S')
    adv = cl.getContact(op.param2)
    res = "╭─「 𝗡𝗼𝘁𝗶𝗳 𝗣𝘂𝘀𝗞𝘂𝗻 」"
    res += "\n├• ᴛᴀɴɢɢᴀʟ : " + tgl
    res += "\n├• ᴀᴍ : " + jamnya
    res += "\n├• ɴᴀᴍᴀ : {}".format(adv.displayName)
    res += "\n╰─「 𝐀𝐃𝐕𝐄𝐍𝐓𝐔𝐑𝐄™ 」"
    try:
        if len(wait["puskun"]) > 0:
            for x in wait["puskun"]:
                cl.sendMessage(x, res)
        else:
            cl.sendMessage(x, res)
    except:
        cl.sendMessage(x, res)


def mentionMembers2(to, mids=[]):
    if clMID in mids: mids.remove(clMID)
    parsed_len = len(mids)//20+1
    result = '╭───「 Mention 」\n'
    mention = '@ZulKiller1\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 TEAM TERMUX 」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def removeCmd(cmd, text):
	key = Setmain["keyCommand"]
	#if Setmain["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
def helpjs():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭─╼Help Js \n"+\
                  "├⌬ " + key + "nukeall\n" + \
                  "├⌬ " + key + "bantai: no\n" + \
                  "├⌬ " + key + "sapu: no\n" + \
                  "├⌬ " + key + "#bypass\n" + \
                  "├⌬ " + key + "#cancel\n" + \
                  "├⌬ " + key + "Set js\n" + \
                  "├⌬ " + key + "Set bypass\n" + \
                  "╰╼─┅TEAM TERMUX"
    return helpMessage1
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 13 or op.type == 124:
            if clMID in op.param3:
                group = cl.getChats(op.param1)
                contact = cl.getContact(op.param2)
                if wait["autoJoinquis"] and clMID in op.param3:
                	cl.acceptChatInvitation(op.param1)
                	quisdata[op.param1] = {
                            "point": {},
                            "saklar": False,
                            "quest": "",
                            "tmp": [],
                            "asw": []
                    }
        if op.type in [13,124]:
            if clMID in op.param3:
                G = cl.getChats(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            time.sleep(5)
                        else:
                            cl.acceptChatInvitation(op.param1)
                            contact = cl.getContact(op.param2)
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            time.sleep(1)
                            data = {"type": "flex","altText": "TEAM TERMUX","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "13px", "offsetEnd": "13.5px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "87px", "height": "10px", "offsetBottom": "12px", "offsetEnd": "10px", "cornerRadius": "2px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1.5px" } ], "position": "absolute", "width": "44px", "height": "12px", "offsetBottom": "11px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "Thanks for invite me dan salam kenal semuanya", "size": "7px", "color": "#00ffff", "wrap": True, "align": "center" } ], "position": "absolute", "width": "90px", "height": "24.5px", "offsetTop": "13px", "offsetStart": "12.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                            sendTemplate(op.param1, data)           
                    else:
                        cl.acceptChatInvitation(op.param1)
                        data = {"type": "flex","altText": "TEAM TERMUX","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "13px", "offsetEnd": "13.5px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "87px", "height": "10px", "offsetBottom": "12px", "offsetEnd": "10px", "cornerRadius": "2px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1.5px" } ], "position": "absolute", "width": "44px", "height": "12px", "offsetBottom": "11px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "Thanks for invite me dan salam kenal semuanya", "size": "7px", "color": "#00ffff", "wrap": True, "align": "center" } ], "position": "absolute", "width": "90px", "height": "24.5px", "offsetTop": "13px", "offsetStart": "12.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                        sendTemplate(op.param1, data)           
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            
            if clMID in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptChatInvitation(op.param1)
                        cl.deleteSelfFromChat(op.param1)
                    else:
                        cl.acceptChatInvitation(op.param1)                              

        if op.type in [15,128]:
           #if op.param1 in welcome:
             if wait["welcomeOn"] == True:
                ginfo = cl.getChats([op.param1],True,True).chats[0]
             #   cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                #cover = cl.getProfileCoverURL(op.param2)
                leaveMembers(op.param1, [op.param2])
                
        if op.type in [17,130]:
           #if op.param1 in welcome:
             if wait["welcomeOn"] == True:
                ginfo = cl.getChats([op.param1],True,True).chats[0]
             #   cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                #cover = cl.getProfileCoverURL(op.param2)
                welcomeMembers(op.param1, [op.param2])


        if op.type in [17,130]:
            if op.param1 in welcome:
                ginfo = cl.getChats(op.param1)
                contact = cl.getContact(op.param2)
                #cover = cl.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                time.sleep(1)
                data = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "34px", "height": "34px", "offsetTop": "10px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co.com/PzBdQ6W/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "22px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "35px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": wait["welcome"], "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "142px", "height": "20px", "offsetBottom": "9.5px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                sendTemplate(op.param1, data)                                                
                sid = str(wait["AddstickerWelcome"]["sid"])
                spkg = str(wait["AddstickerWelcome"]["spkg"])
                cl.sendSticker(op.param1, spkg, sid)

        if op.type in [15,128]:
            if op.param1 in leave:
                ginfo = cl.getChats(op.param1)
                contact = cl.getContact(op.param2)
                #cover = cl.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                time.sleep(1)
                data = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "34px", "height": "34px", "offsetTop": "10px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co.com/PzBdQ6W/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "22px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "35px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": wait["leave"], "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "142px", "height": "20px", "offsetBottom": "9.5px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                sendTemplate(op.param1, data)                                                
                sid = str(wait["AddstickerLeave"]["sid"])
                spkg = str(wait["AddstickerLeave"]["spkg"])
                cl.sendSticker(op.param1, spkg, sid)

        if op.type == 2:
            if wait["detectvp"] == True:
                a = op.param1
                G = cl.getAllChatMids().memberChatMids
                contact = cl.getContact(op.param1)
                cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                a = cl.getAllContactIds()
                Bio = "Bio : {}".format(contact.statusMessage)
                cl.sendText(op.param1, str(Bio))




        if op.type == 33:           
            if wait["puskun"] == True:                
               groups = cl.getChats([op.param1]).chats[0].chatName
               ginfo = cl.getChats([op.param1],True,True).chats[0]
#               cover = cl.getProfileCoverURL(op.param2)
               jam = pytz.timezone("Asia/Jakarta")
               jamSek = datetime.now(tz=jam)
               jamnya = datetime.strftime(timeNow,'%d-%m-%Y')                     
               tgl = datetime.strftime(timeNow,'%H:%M:%S')
#               text = "ʙᴀᴘᴇʀᴀɴ"                      
               res = "╭─「❑ ᴍᴇᴍʙᴇʀ ᴘᴜsᴋᴜɴ ❑  」"
               res += "\n├• ɴᴀᴍᴀ : {}".format(adv.displayName)
               res += "\n├• ᴍɪᴅ : {}".format(contact.mid)
               res += "\n├• ʙɪᴏ : {}".format(cl.getProfile)
               res += "\n├• ᴛᴀɴɢɢᴀʟ : " + timeDate
               res += "\n├• ᴊᴀᴍ : " + timeHours
               res += "\n├• sᴇʙᴀʙ : " + random.choice(text)             
               res += "\n╰─「❑ TERMUX_ᴋɪʟʟᴇʀ ❑」"
               cl.sendMessage(op.param1,(res))                      
               cl.sendMessage(x, res)
               cl.backupData()              
           #except Exception as error:           
               #cl.sendMessage(msg.to, str(error))


        if op.type in [65]:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getChats(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─「 Gambar Dihapus 」\n│ Pengirim : "
                                ret_ = "│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getChats(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭─「 Pesan Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n│ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
        if op.type in [65]:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getChats(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭─「 Sticker Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        
        if op.type in [55]:
            if op.param2 in wait["blacklist"]:
                cl.deleteOtherFromChat(op.param1,[op.param2]);cl.sendMessage(op.param1,"contact ini ʙʟᴀᴄᴋʟɪsᴛ")
            else:pass
            if op.param1 in read["readPoint"]:
                if op.param2 in read["readMember"][op.param1]:
                    pass
                else:
                    read["readMember"][op.param1][op.param2] = True
            else:pass
        if op.type in [55]:
            if op.param1 in cctv4['cyduk']:
                if op.param1 in cctv4['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv4['sidermem'][op.param1]:
                        pass
                    else:
                        cctv4['sidermem'][op.param1] += "\n~ " + Name
                        try:
                            user = ["Halloo kak... Nanti malam di mohon hadir ya,.. ada accara YASIN RUTIN jam 8 wib 🙏🙏"]
                            mentiones = '{"S":"0","E":"3","M":'+json.dumps(op.param2)+'}'
                            text_ = '@x  {}'.format(str(random.choice(user)))
                            A = contentMetadata={'MENTION':'{"MENTIONEES":['+mentiones+']}'}
                            cl.sendMessage(op.param1, text_, A)
                        except:pass
        if op.type in [55]:
            if cctv1['cyduk1'][op.param1]==True:
                if op.param1 in cctv1['point1']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv1['sidermem1'][op.param1]:
                        pass
                    else:
                        cctv1['sidermem1'][op.param1] += "\n~ " + Name
                        contact = cl.getContact(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        #cover = cl.getProfileCoverURL(op.param2)
                        timeNow = datetime.now(tz=tz)
                        time.sleep(1)
                        data = {
                            "type": "flex",
                            "altText": "TEAM TERMUX V 1",
                            "contents": {
                            
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co.com/3kTMsnR/ezgif-com-gif-maker.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:2",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "size": "full",
                "aspectMode": "cover",
                "url": "https://www.kibrispdr.org/data/wallpaper-melengkung-1.jpg"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "148px",
            "height": "147px",
            "position": "absolute",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "SIDER MEMBER",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px",
                "offsetStart": "30px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "148px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "5px",
            "offsetStart": "5px",
            "backgroundColor": "#000080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TEAM TERMUX V 2",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "17px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "148px",
            "height": "20px",
            "position": "absolute",
            "offsetStart": "5px",
            "offsetTop": "132px",
            "backgroundColor": "#8B0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "SELFBOT",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px",
                "offsetStart": "15px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "80px",
            "height": "20px",
            "position": "absolute",
            "offsetStart": "5px",
            "offsetTop": "24px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px",
                "offsetStart": "10px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "69px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "24px",
            "offsetStart": "84px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "borderColor": "#F0F8FF",
            "cornerRadius": "1px",
            "borderWidth": "1px",
            "width": "70px",
            "height": "70px",
            "position": "absolute",
            "offsetTop": "43px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": wait["mention"],
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px",
                "offsetStart": "1px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "position": "absolute",
            "width": "148px",
            "height": "21px",
            "offsetTop": "112px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/TMj9gJD/ezgif-com-gif-maker.png",
                "size": "full",
                "aspectMode": "cover",
                "animated": True
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "68px",
            "height": "66px",
            "position": "absolute",
            "offsetTop": "43px",
            "offsetStart": "80px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "⌚ "+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px",
                "offsetStart": "1px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "70px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "47px",
            "offsetStart": "5px",
            "backgroundColor": "#800080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🗓️ "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "70px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "70px",
            "offsetStart": "5px",
            "backgroundColor": "#008080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderWidth": "1px",
            "cornerRadius": "100px",
            "width": "50px",
            "height": "50px",
            "position": "absolute",
            "offsetTop": "52px",
            "offsetStart": "88px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " {} ".format(cl.getContact(op.param2).displayName),
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "1px",
                "offsetStart": "1px"
              }
            ],
            "borderColor": "#F0F8FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "position": "absolute",
            "width": "70px",
            "height": "21px",
            "offsetTop": "92px",
            "offsetStart": "5px",
            "backgroundColor": "#8B0000"
          }
        ],
        "paddingAll": "0px",
#        "borderColor": warnanya1,
        "borderWidth": "1px",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://wa.me/message/ANCIF474MS6OL1"
        }
      }
    }
  ]
}
}
                        sendTemplate(op.param1, data)
        if op.type in [55]:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        contact = cl.getContact(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        #cover = cl.getProfileCoverURL(op.param2)
                        timeNow = datetime.now(tz=tz)
                        time.sleep(1)
                        data = {
                                "type": "flex",
                                "altText": "TEAM TERMUX 01",
                                "contents": {
                                
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4EHbxAIv86EkedPB45QJaXIirvByt5RTZcg&usqp=CAU",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "SIDER MEMBER",
                "color": "#FFFFFF",
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "35px"
              }
            ],
            "position": "absolute",
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "152px",
            "height": "20px",
            "offsetTop": "2px",
            "offsetStart": "2px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "borderColor": "#7CFC00",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "152px",
            "height": "88px",
            "position": "absolute",
            "offsetTop": "23px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "borderColor": "#FF00FF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "position": "absolute",
            "height": "85px",
            "width": "150px",
            "offsetTop": "25px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "2:2"
              }
            ],
            "position": "absolute",
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "height": "83px",
            "width": "148px",
            "offsetTop": "26px",
            "offsetStart": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "  "+ datetime.strftime(timeNow,'%H:%M:%S'),
                "color": "#FFFFFF",
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "10px"
              }
            ],
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "cornerRadius": "2px",
            "width": "70px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "112px",
            "offsetStart": "2px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "  "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "2px"
              }
            ],
            "borderColor": "#00FFFF",
            "cornerRadius": "2px",
            "borderWidth": "1px",
            "width": "80px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "112px",
            "offsetStart": "74px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "❒    {} ".format(cl.getContact(op.param2).displayName),
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "3px",
                "offsetStart": "2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "width": "152px",
            "height": "22px",
            "offsetTop": "133px",
            "offsetStart": "2px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CREATOR",
                "color": "#FFFFFF",
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "5px"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "absolute",
            "width": "70px",
            "height": "20px",
            "offsetTop": "212px",
            "offsetStart": "2px",
            "backgroundColor": "#800080",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ORDER",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "17px"
              }
            ],
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "width": "80px",
            "height": "20px",
            "position": "absolute",
            "backgroundColor": "#4B0082",
            "offsetTop": "212px",
            "offsetStart": "73px",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "width": "152px",
            "height": "33px",
            "position": "absolute",
            "offsetTop": "155px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqaS60Dv8DBRF7xpsODJT-7UPdt5PdWCtOiBV9xDfvvndPARGBZQf6cpQqJ_k1QajGmmChLjO_MELOmiml7YyYpfzK5_6z5AE&usqp=CAU&ec=45725302",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "height": "20px",
            "width": "20px",
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "offsetTop": "190px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": wait["mention"],
                "size": "xxs",
                "color": "#FFFFFF",
                "wrap": True,
                "offsetTop": "1px",
                "offsetStart": "3px"
              }
            ],
            "position": "absolute",
            "borderColor": "#FF0000",
            "borderWidth": "1px",
            "width": "150px",
            "height": "32px",
            "offsetTop": "156px",
            "offsetStart": "3px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrL6_OWpBPDFXt37Mu-tf-yN53HCcQwpmPHA&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "borderColor": "#00FFFF",
            "offsetTop": "190px",
            "borderWidth": "1px",
            "offsetStart": "25px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "size": "full",
                "aspectMode": "cover",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRzUbZPwMHcKGnRudeq6VCtiW3Mla0MQ5eBOPZEeGNIXd8ypsdhTVU-PAfAumHIcPerNSew8p53aKX1qZaOBBSnA3zRezSrwQ&usqp=CAU&ec=45725302"
              }
            ],
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "height": "20px",
            "width": "20px",
            "position": "absolute",
            "offsetTop": "190px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "aspectMode": "cover",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWwPoxnFCmfGNNu8bckmjLVlO2OKIebl8v47Xj4vExmDMt42Wz8C6vePLb9ruVsq1UKAtsBwJbmTgyEuD1QuhmniHO99j3JwM&usqp=CAU&ec=45725302"
              }
            ],
            "height": "20px",
            "width": "20px",
            "borderColor": "#00FFFF",
            "borderWidth": "1px",
            "position": "absolute",
            "offsetTop": "190px",
            "offsetStart": "77px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "aspectMode": "cover",
                "url": "https://pbs.twimg.com/profile_images/1308010958862905345/-SGZioPb.jpg"
              }
            ],
            "offsetTop": "190px",
            "offsetStart": "106px",
            "width": "20px",
            "height": "20px",
            "position": "absolute",
            "borderColor": "#00FFFF",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://assets.stickpng.com/images/580b57fcd9996e24bc43c545.png",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#00FFFF",
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "borderWidth": "1px",
            "offsetTop": "190px",
            "offsetStart": "133px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#00FFFF",
        "cornerRadius": "10px",
        "borderWidth": "2px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://wa.me/message/ANCIF474MS6OL1"
        }
      }
    }
  ]
}
}
                        sendTemplate(op.param1, data)
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).deleteOtherFromChat(msg.to, [msg._from])
                      except:
                          try:
                              cl.deleteOtherFromChat(msg.to, [msg._from])
                          except:
                              cl.deleteOtherFromChat(msg.to, [msg._from])
   
        if op.type == 25 or op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                to = msg.to
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != cl.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                    elif msg.contentType == 16:
                        if wait["likeOn"] == True:
                            try:
                                contact = cl.getContact(sender);tz = pytz.timezone("Asia/Jakarta");timeNow = datetime.now(tz=tz)
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂🇮🇩➢ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂??🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂🇮🇩➢ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂🇮??➢ Tulisan :\n╠❂🇮🇩➢ {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                sendpostTemplate(to, data)
                            except:
                                data = {"type": "flex","altText": "TEAM TERMUX V 5","contents": {"type": "bubble","size": "micro","header": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/KbfDFN1/1657636839741.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "17px","height": "17px","backgroundColor": "#000000","offsetEnd": "5px","cornerRadius": "50px","offsetTop": "2px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "TEAM TERMUX V 6","size": "10px","color": "#ffffff","align": "center"}],"position": "absolute","width": "130px","height": "15px","borderWidth": "0.5px","borderColor": "#ffffff","cornerRadius": "3px","offsetTop": "3px","offsetStart": "5px"}],"backgroundColor": "#000000"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": text,"size": "10px","color": "#000000","wrap": True}]},"action": {"type": "uri","label": "action","uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"}}}
                                sendTemplate(to, data)
            except:pass
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
              if wait["respontag"] == True:
                contact = cl.getContact(msg._from)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                #cover = cl.getProfileCoverURL(sender)
                name = re.findall(r'@(\w+)', msg.text)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                for mention in mentionees:
                     if mention ['M'] in clMID:
                        XFUCK = {"type": "flex","altText": "TEAM TERMUX V 6","contents": {"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/d0xpypN/20211220-072435.png","size": "full","aspectMode": "cover","aspectRatio": "5:8","gravity": "center"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "{}".format(wait["Tag"]),"size": "10px","color": "#ffffff","wrap": True,"align": "center"}],"position": "absolute","width": "143px","height": "50px","backgroundColor": "#ff000050","borderWidth": "1px","borderColor": "#ff0000","cornerRadius": "3px","offsetBottom": "31px","offsetStart": "5px"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),"size": "full","aspectRatio": "1:1","aspectMode": "cover"}],"position": "absolute","width": "140px","height": "140px","borderWidth": "0.5px","borderColor": "#ff0000","cornerRadius": "5px","offsetTop": "31px","offsetStart": "10px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": " "+ datetime.strftime(timeNow,'%H:%M:%S'),"size": "7px","color": "#ffffff","align": "center"}],"position": "absolute","width": "60px","height": "10px","backgroundColor": "#ff000050","borderWidth": "0.5px","borderColor": "#ff0000","cornerRadius": "2px","offsetTop": "2px","offsetStart": "10px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Name : {}".format(cl.getContact(sender).displayName),"size": "7px","color": "#ffffff","align": "center"}],"position": "absolute","width": "113px","height": "10px","backgroundColor": "#ff000050","borderWidth": "0.5px","cornerRadius": "3px","offsetTop": "19px","offsetStart": "10px","borderColor": "#ff0000"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": " " + datetime.strftime(timeNow,'%d-%m-%Y'),"size": "7px","color": "#ffffff","align": "center"}],"position": "absolute","width": "60px","height": "10px","backgroundColor": "#ff000050","borderWidth": "0.5px","borderColor": "#ff0000","cornerRadius": "2px","offsetBottom": "3px","offsetEnd": "10px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "AUTO RESPON MENTION","size": "7px","color": "#ffffff","align": "center"}],"position": "absolute","width": "113px","height": "10px","backgroundColor": "#ff000050","borderWidth": "0.5px","cornerRadius": "3px","borderColor": "#ff0000","offsetBottom": "19px","offsetEnd": "10px"}],"paddingAll": "0px","borderWidth": "1px","borderColor": "#ff0000","cornerRadius": "10px"},"action": {"type": "uri","label": "action","uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"}}}                            
                        sendTemplate(to, XFUCK)
                        sid = str(wait["AddstickerTag"]["sid"])
                        spkg = str(wait["AddstickerTag"]["spkg"])
                        cl.sendSticker(msg.to, spkg, sid)
            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
              if wait["detectMention1"] == True:
                contact = cl.getContact(msg._from)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                #cover = cl.getProfileCoverURL(sender)
                name = re.findall(r'@(\w+)', msg.text)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                for mention in mentionees:
                     if mention ['M'] in clMID:
                        XFUCK = wait["balasan"]
                        cl.sendMessage(to, XFUCK)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
                     
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if temptag["stealtag"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention["M"] in clMID:
                           contact = cl.getContact(msg._from)
                           anu = contact.displayName
                           cl.sendReplyMessage(msg.id,to, " " +anu+ " {}".format(wait["Tag"]))
                           sid = str(wait["AddstickerTag"]["sid"])
                           spkg = str(wait["AddstickerTag"]["spkg"])
                           cl.sendSticker(msg.to, spkg, sid)
                           break
                                                                                                    
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in clMID:
                           cl.sendMessage(msg.to, "Don't Tag Me !!")
                           cl.deleteOtherFromChat(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["stickerOn"] == True:
                    msg.contentType = 0
                    sendFoter(msg.to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n├↘ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                #if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getChats([msg.to],True,False).chats[0]
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "ʟɪsᴛ ʙʟ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  #cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoChat(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 sᴜᴋsᴇs ɪɴᴠɪᴛᴇ 」\nɴᴀᴍᴀ"
                                  ret_ = "ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ᴏғғ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendMessage(msg.to,"ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ sᴛʀᴜᴋ")
                                  wait["invite"] = False
                                  break       



               if msg.contentType == 13:
                 if wait["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getChats([msg.to],True,False).chats[0]
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invi"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                #cl.findAndAddContactsByMid(target)
                                cl.inviteIntoChat(msg.to,[target])
                                cl.sendReplyMessage(msg.id, to, "ᴅᴏɴᴇ ᴊᴇᴘɪᴛ \n➡" + _name)
                                wait["Invi"] = False
                                break

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))

               if msg.contentType == 7:
                 #
                    if wait["AddstickerTag"]["status"] == True:
                        wait["AddstickerTag"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerTag"]["spkg"] = msg.contentMetadata['STKPKGID']
                        sendFoter(msg.to, "Add Stickers Tag Succes ♪")
                        wait["AddstickerTag"]["status"] = False     
               if msg.contentType == 7:
                 #
                    if wait["AddstickerSider"]["status"] == True:
                        wait["AddstickerSider"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerSider"]["spkg"] = msg.contentMetadata['STKPKGID']
                        sendFoter(msg.to, "Add stickers sider ♪")
                        wait["AddstickerSider"]["status"] = False                   
               if msg.contentType == 7:
                 #
                    if wait["AddstickerPesan"]["status"] == True:
                        wait["AddstickerPesan"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerPesan"]["spkg"] = msg.contentMetadata['STKPKGID']
                        sendFoter(msg.to, "Succes add Stickers ♪")
                        wait["AddstickerPesan"]["status"] = False                   
               if msg.contentType == 7:
                 #
                    if wait["AddstickerWelcome"]["status"] == True:
                        wait["AddstickerWelcome"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerWelcome"]["spkg"] = msg.contentMetadata['STKPKGID']
                        sendFoter(msg.to, "Succes add Stickers ♪")
                        wait["AddstickerWelcome"]["status"] = False                   
               if msg.contentType == 7:
                 #
                    if wait["AddstickerLeave"]["status"] == True:
                        wait["AddstickerLeave"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerLeave"]["spkg"] = msg.contentMetadata['STKPKGID']
                        sendFoter(msg.to, "Succes add Stickers Leave ♪")
                        wait["AddstickerLeave"]["status"] = False                   
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
               if msg.contentType == 7:
                   #
                       try:
                           if wait["sticker"] == True:
                               wait["stickers"][wait["stk"]] = msg.contentMetadata
                               wait["stk"] = {}
                               wait["sticker"] = False
                               f=codecs.open("wait.json","w","utf-8")
                               json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                               sendFoter(msg.to,"Tersimpan")
                       except Exception as e:
                           sendFoter(msg.to,"{}".format(str(e)))
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = cl.getProfile()
               		path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = cl.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		sendFoter(to, "succes")
                       
               if msg.contentType == 7:
                 if wait["stickerOn"] == True:
                    msg.contentType = 0
                    sendFoter(msg.to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," ╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n╰─ 「Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#UPDATE FOTO
               if msg.contentType == 1:
                #
                  if wait["Addimage"] == True:
                    try:
                        cl.downloadObjectMsg(msg.id,'path','dataFoto/'+wait["Img"]+'.jpg')
                        sendFoter(msg.to, "Berhasil menambahkan gambar")
                        wait["Img"] = {}                
                        wait["Addimage"] = False
                    except Exception as e:
                        cl.downloadObjectMsg(msg.id,'path','dataFoto/'+wait["Img"]+'.jpg')
                        sendFoter(msg.to, "Berhasil menambahkan gambar")
                        wait["Img"] = {}
                        wait["Addimage"] = False
               if msg.contentType == 2:
                #
                  if wait["Addvideo"] == True:
                    try:
                        cl.downloadObjectMsg(msg.id,'path','dataVideo/'+wait["Video"]+'.mp4')
                        sendFoter(msg.to, "Berhasil menambahkan video")
                        wait["Video"] = {}                
                        wait["Addvideo"] = False
                    except Exception as e:
                        cl.downloadObjectMsg(msg.id,'path','dataVideo/'+wait["Video"]+'.mp4')
                        sendFoter(msg.to, "Berhasil menambahkan video")
                        wait["Video"] = {}
                        wait["Addvideo"] = False
               if msg.toType == 2:
                 #
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendFoter(msg.to, "Success")
               if msg.contentType == 1:
                   #
                       if clMID in wait["changeFoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del wait["changeFoto"][clMID]
                            cl.updateProfilePicture(path)
                            sendFoter(msg.to,"Foto berhasil dirubah")
                   #
                       if clMID in settings["changeCover"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del settings["changeCover"][clMID]
                            cl.updateProfileCover(path)
                            sendFoter(to, "Updated")                                                            

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "chatbot on":
                            #
                                wait["selfbot"] = True
                                ret = "Chatbot Enable."
                                sendFoter(msg.to, str(ret))

                        elif cmd == comd["help"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd[",help"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd[".help"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd["/help"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd["help "]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd["zhelp"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd["1help"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd["ช่วย"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")

                        elif cmd == comd["يساعد"]:
                          ##
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")
                                
                        elif cmd == "chatbot off":
                            #
                                wait["selfbot"] = False
                                ret = "Chatbot Disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["invite"] = True
                                sendTextTemplateB(msg.to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ'ɴʏᴀ")
                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                wait["invite"] = False
                                sendTextTemplateB(msg.to,"ɪɴᴠɪᴛᴇ ᴠɪᴀ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")


                        elif cmd == "clear":
                            #
                                process = os.popen('cd /tmp/ && rm -r *')
                                a = process.read()
                                ret = "Cleared Temp File"
                                sendFoter(msg.to, str(ret))
    
                        elif cmd == "remote":
                          if wait["selfbot"] == True:
                            #
                                ret = "• Tag: (numb)\n"
                                ret += "• Gurl (numb)\n"
                                ret += "• Bye: (numb)\n"
                                ret += "• Close(numb)\n"
                                ret += "• Infogrup (numb)\n"
                                ret += "• Infomem (numb)\n"
                                ret += "• Bantai: (numb)"
                                sendFoter(msg.to, str(ret))    
    
                        elif cmd == "group":
                          if wait["selfbot"] == True:
                            #
                                ret = "• Me\n"
                                ret += "• Mid\n"
                                ret += "• Block @\n"
                                ret += "• Cek @\n"
                                ret += "• Find @\n"
                                ret += "• Rename @\n"
                                ret += "• Mid @\n"
                                ret += "• Speed|Sp\n"
                                ret += "• Stag\n"
                                ret += "• Tag\n"
                                ret += "• Tagall sticker\n"
                                ret += "• Ginfo\n"
                                ret += "• Buka qr\n"
                                ret += "• Tutup qr\n"
                                ret += "• @bye\n"
                                ret += "• Url\n"
                                ret += "• Idline (idline)\n"
                                ret += "• Gruplist\n"
                                ret += "• Gnamegrup (text)\n"
                                ret += "• Call @\n"
                                ret += "• Fotgbc (Text)\n"
                                ret += "• Fotfbc (Text)\n"
                                ret += "• Flexgbc (Text)\n"
                                ret += "• Flexfbc (Text)\n"
                                ret += "• Clearallfriend\n"
                                ret += "• Clearchat\n"
                                ret += "• Refresh\n"
                                ret += "• Sider (on|off)\n"
                                ret += "• Broadcast: (Text)\n"
                                ret += "• Setkey (key)\n"
                                ret += "• Mykey\n"
                                ret += "• Resetkey\n"
                                ret += "• Unsend (numb)\n"
                                ret += "• Jumlah: (jumlh)\n"
                                ret += "• Spamtag (jumlh)\n"
                                ret += "• Spamtag @ (jumlh)\n"
                                ret += "• Spamcall (numb)\n"
                                ret += "• Spamcall: (jumlh)\n"
                                ret += "• Spamcall\n"
                                ret += "• Gift: (mid)(jumlh)\n"
                                ret += "• Spam: (mid)(jumlh)\n"
                                ret += "• Spam on|jumlah|text\n"
                                ret += "• Tag (jumlah di pm)"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "profile":
                          if wait["selfbot"] == True:
                            #
                                ret = "• Myname\n"
                                ret += "• Mybio\n"
                                ret += "• Mypict\n"
                                ret += "• Myvideo\n"
                                ret += "• Steal @\n"
                                ret += "• Video @\n"
                                ret += "• Pict @\n"
                                ret += "• Cover\n"
                                ret += "• Bio\n"
                                ret += "• Name:\n"
                                ret += "• Cvp: (link yt)"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "admin":
                          if wait["selfbot"] == True:
                            #
                                ret = "• Blc\n"
                                ret += "• Bot:on\n"
                                ret += "• Bot:repeat\n"
                                ret += "• Staff:on\n"
                                ret += "• Staff:repeat\n"
                                ret += "• Admin:on\n"
                                ret += "• Admin:repeat\n"
                                ret += "• Staffadd @\n"
                                ret += "• Staffdell @\n"
                                ret += "• Adminadd @\n"
                                ret += "• Admindell @\n"
                                ret += "• Ulti @"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "banned":
                          if wait["selfbot"] == True:
                            #
                                ret = "• Blc\n"
                                ret += "• Banlist\n"
                                ret += "• Clearban\n"
                                ret += "• Ban:on\n"
                                ret += "• Unban:on\n"
                                ret += "• Ban @\n"
                                ret += "• Unban @\n"
                                ret += "• Talkban @\n"
                                ret += "• Untalkban @\n"
                                ret += "• Talkbanlist @"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "setting":
                          if wait["selfbot"] == True:
                            #
                                ret = "• protect on\n"
                                ret = "• protect:on/off (no gc)\n"
                                ret = "• CekSider\n"
                                ret += "• CekSpam\n"
                                ret += "• CekPesan\n"
                                ret += "• CekRespon\n"
                                ret += "• Cekwelcome\n"
                                ret += "• CekLeave\n"
                                ret += "• Cekcomment\n"
                                ret += "• Sticker tag\n"
                                ret += "• Sticker sider\n"
                                ret += "• Sticker pesan\n"
                                ret += "• Sticker Welcome\n"
                                ret += "• Sticker Leave\n"
                                ret += "• Setreject: (jumlah)\n"
                                ret += "• Setliff: (liff ny)\n"
                                ret += "• Setsider: (Text)\n"
                                ret += "• Setcomment: (Text)\n"
                                ret += "• Setwelcome: (Text)\n"
                                ret += "• Setleave: (Text)\n"
                                ret += "• respon1 on/off\n"
                                ret += "• Setrespon1: (Text)\n"
                                ret += "• Setcall: (Text)\n"
                                ret += "• Setcall1: (Text)\n"
                                ret += "• Setrespon: (Text)\n"
                                ret += "• Setpesan: (Text)\n"
                                ret += "• Setcban: (Text)\n"
                                ret += "• Setbye: (Text)\n"
                                ret += "• Sethelp: (Text)\n"
                                ret += "• Setspeed: (Text)\n"
                                ret += "• sider2 on/off\n"
                                ret += "• Setsider2:(Text)\n"
                                ret += "• Setsider on: (Text)\n"
                                ret += "• Setsider off: (Text)\n"
                                ret += "• Setkick: (Text)\n"
                                ret += "• Settagall: (Text)\n"
                                ret += "• Setunsend: (Text)\n"
                                ret += "• Myname: (Text)\n"
                                ret += "• Udatefoto\n"
                                ret += "• Updategrup\n"
                                ret += "• Autojoin (On|Off)\n"
                                ret += "• Autochat (On|Off)\n"
                                ret += "• Autoleave (On|Off)\n"
                                ret += "• Autoread (On|Off)\n"
                                ret += "• Autoblock (On|Off)\n"
                                ret += "• Autolike (On|Off)\n"
                                ret += "• Respon (On|Off)\n"
                                ret += "• Respon2 (On|Offa)\n"
                                ret += "• Responcall (On|Off)\n"
                                ret += "• Sticker (On|Off)\n"
                                ret += "• Unsend (On|Off)\n"
                                ret += "• Timeline (On|Off)\n"
                                ret += "• Contact: (On|Off)\n"
                                ret += "• Jointicket (On|Off\n"
                                ret += "• Welcomemsg (On|Off)\n"
                                ret += "• Leavemsg (On|Off)"
                                ret += "• Snule (On|Off)"
                                ret += "• Tiktok url (On|Off)"
                                ret += "• Yt url (On|Off)"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "media":
                          if wait["selfbot"] == True:
                            #
                                ret = "• Addsticker: (Text)\n"
                                ret += "• Dellsticker: (Text)\n"
                                ret += "• Stickerlist\n"
                                ret += "• Addtext: (Text)\n"
                                ret += "• Deltext: (Text)\n"
                                ret += "• List text\n"
                                ret += "• Corona\n"
                                ret += "• Info bmkg\n"
                                ret += "• Acara tv\n"
                                ret += "• Info loker\n"
                                ret += "• Ciname xx1\n"
                                ret += "• Fs (text)\n"
                                ret += "• Cctv code\n"
                                ret += "• Cctv (number)\n"
                                ret += "• Github (search)\n"
                                ret += "• Ytmp3 (query)\n"
                                ret += "• Ytmp4 (query )\n"
                                ret += "• Porn (search)\n"
                                ret += "• Randomname\n"
                                ret += "• Lyrik (search)\n"
                                ret += "• Joox: (search)\n"
                                ret += "• Cuaca (wilayah)\n"
                                ret += "• Sholat (wilayah)\n"
                                ret += "• Surahlist\n"
                                ret += "• Surah (ayat)\n"
                                ret += "• Fancytext (text)\n"
                                ret += "• Acaratv (search)\n"
                                ret += "• Zodiak (bintang)\n"
                                ret += "• Instagram (search)\n"
                                ret += "• Ponsel (type)\n"
                                ret += "• Google (search)\n"
                                ret += "• Resi-jnt: (resi)\n"
                                ret += "• Resi-pos: (resi)\n"
                                ret += "• Resi-rex: (resi)\n"
                                ret += "• Resi-ninja: (resi)\n"
                                ret += "• Resi-sicepat: (resi)\n"
                                ret += "• Anime: (search)\n"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "protect":
                          if wait["selfbot"] == True:
                            #
                                ret += "• Notag On|Off\n"
                                ret += "• Pinvite On|Off\n"
                                ret += "• Pqr On|Off\n"
                                ret += "• Pjoin On|Off \n"
                                ret += "• Pkick On|Off\n"
                                ret += "• Pcancell On|Off"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            #
                                ret = "❑ Indo: Text\n"
                                ret += "❑ Jawa: Text\n"
                                ret += "❑ Jp: Text\n"
                                ret += "❑ Thai: Text\n"
                                ret += "❑ Eng: Text\n"
                                ret += "❑ Arab: Text\n"
                                ret += "❑ Korea: Text\n"
                                ret += "❑ India: Text\n"
                                ret += "❑ China: Text\n"
                                ret += "❑ Rusia: Text\n"
                                ret += "❑ Spanyol: Text\n"
                                ret += "❑ Franchis: Text\n"
                                ret += "❑ Malay: Text\n"
                                ret += "❑ Itali: Text\n"
                                ret += "❑ Filipin: Text\n"
                                ret += "❑ Turki: Text\n"
                                ret += "❑ Vietnam: Text\n"
                                ret += "❑ Belanda: Text\n"
                                ret += "❑ German: Text"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "cmd list":
                          if wait["selfbot"] == True:
                            #
                                vian = "╭─「👥 Cmd List 👥」\n"
                                for u in comd:
                                    vian += "├❑ {} : {}\n".format(u,comd[u])
                                vian += '╰────────'
                                sendFoter(msg.to, str(vian))
                            
                        elif cmd.startswith("footgbc"):
                          if wait["selfbot"] == True:
                            #
                                khie = text.split(" ")
                                hey = text.replace(khie[0] + " ", "")
                                text = "{}".format(hey)
                                groups = cl.getAllChatIds()
                                for gr in groups:
                                    flextezt(gr, text)
 
                        elif cmd.startswith("textgbc "):
                            #
                                sep = text.split(" ")
                                bc = text.replace(sep[0] + " ","")
                                saya = cl.getAllChatIds()
                                for rom in saya:
                                    cl.sendMessage(rom," BROADCAST \n\n"+bc)
                                sendFoter(to, "Berhasil broadcast ke {} group".format(str(len(saya))))
 
                        elif cmd.startswith("flexgbc "):
                          if wait["selfbot"] == True:
                            #
                                rah = text.split(" ")
                                matt = text.replace(rah[0] + " ","")
                                chat = "{}".format(matt)
                                groups = cl.getAllChatIds()
                                for gr in groups:
                                    cl.sendMessage(gr, chat)
                        elif text.lower() == "mid" or text.lower() == "mid":
                            data = {"type": "text","text": "{}".format(msg._from),"sentBy":{"label": " • TEAM TERMUX•","iconUrl": "https://i.ibb.co.com/DkxfZFn/de9b402e111bc99dc7c5d2609cea06db.gif","linkUrl": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"}}
                            sendTemplate(to, data)
                                
                        elif cmd.startswith("flexfbc "):
                          if wait["selfbot"] == True:
                            #
                                rah = text.split(" ")
                                matt = text.replace(rah[0] + " ","")
                                chat = "{}".format(matt)
                                friends = cl.getAllContactIds()
                                for friend in friends:
                                    cl.sendMessage(friend, chat)
                                    time.sleep(1)
                                sendFoter(to, "Succes friend cast to {} friend ".format(str(len(friends))))
                            
                        elif cmd.startswith("fotfbc"):
                          if wait["selfbot"] == True:
                            #
                                khie = text.split(" ")
                                hey = text.replace(khie[0] + " ", "")
                                text = "{}".format(hey)
                                groups = cl.getAllChatIds()
                                for friend in friends:
                                    cl.sendMessage(friend, text)
                              
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            #
                                #tz = pytz.timezone("Asia/Jakarta")
                                #timeNow = datetime.now(tz=tz)
                                md = "╭─「 STATUS BOTS 」\n"
                                if wait["ytube"] == True: md+="├ ✓  ❑ Youtube Url\n"
                                else: md+="├ ✗  ❑ Youtube Url\n"
                                if wait["tiktok"] == True: md+="├ ✓  ❑ Tiktok Url\n"
                                else: md+="├ ✗  ❑ Tiktok Url\n"
                                if wait["rsmule"] == True: md+="├ ✓  ❑ Smule\n"
                                else: md+="├ ✗  ❑ Smule\n"
                                if wait["sticker"] == True: md+="├ ✓  ❑ Sticker\n"
                                else: md+="├ ✗  ❑ Sticker\n"
                                if wait["contact"] == True: md+="├ ✓  ❑ Contact\n"
                                else: md+="├ ✗  ❑ Contact\n"
                                if wait["unsend"] == True: md+="├ ✓  ❑ Unsend\n"
                                else: md+="├ ✗  ❑ Unsend\n"
                                if wait["Timeline"] == True: md+="├ ✓  ❑ Timeline\n"
                                else: md+="├ ✗  ❑ Timeline\n"
                                if wait["respontag"] == True: md+="├ ✓  ❑ Respon\n"
                                else: md+="├ ✗  ❑ Respon\n"
                                if temptag["stealtag"] == True: md+="├ ✓  ❑ Respon2\n"
                                else: md+="├ ✗  ❑ Respon2\n"
                                if wait["autoBlock"] == True: md+="├ ✓  ❑ Auto Block\n"
                                else: md+="├ ✗  ❑ Auto Block\n"
                                if wait["talkban"] == True: md+="├ ✓  ❑ Talkban\n"
                                else: md+="├ ✗  ❑ Talkban\n"
                                if wait["Mentionkick"] == True: md+="├ ✓  ❑ Notag\n"
                                else: md+="├ ✗  ❑ Notag\n"
                                if wait["detectMention"] == True: md+="├ ✓  ❑ Respon2\n"
                                else: md+="├ ✗  ❑ Respon2\n"
                                if wait["autoJoin"] == True: md+="├ ✓  ❑ Autojoin\n"
                                else: md+="├ ✗  ❑ Autojoin\n"
                                if wait["autoCancel"]["on"] == True: md+="├ ✓  ❑ AutoReject : " + str(wait["autoCancel"]["members"]) + "\n"
                                else: md+="├ ✗  ❑ AutoReject\n"
                                if wait["likeOn"] == True: md+="├ ✓  ❑ Autolike\n"
                                else: md+="├ ✗  ❑ Autolike\n"
                                if wait["responGc"] == True: md+="├ ✓  ❑ Respon Gc\n"
                                else: md+="├ ✗  ❑ Respon Gc\n"
                                if msg.to in welcome: md+="├ ✓  ❑ Welcome\n"
                                else: md+="├ ✗  ❑ Welcome\n"
                                if wait["autoLeave"] == True: md+="├ ✓  ❑ Autoleave\n"
                                else: md+="├ ✗  ❑ Autoleave\n"
                                if msg.to in protectqr: md+="├ ✓  ❑ Protectqr\n"
                                else: md+="├ ✗  ❑ Protectqr\n"
                                if msg.to in protectjoin: md+="├ ✓  ❑ ProtectJoin\n"
                                else: md+="├ ✗  ❑ ProtectJoin\n"
                                if msg.to in protectkick: md+="├ ✓  ❑ ProtectKick\n"
                                else: md+="├ ✗  ❑ ProtectKick\n"
                                if msg.to in protectcancel: md+="├ ✓  ❑ ProtectCancell\n"
                                else: md+="├ ✗  ❑ ProtectCancell\n"
                                if msg.to in protectinvite: md+="├ ✓  ❑ ProtectInvite\n╰─❑ Zul-Bots ❑"
                                else: md+="├ ✗  ❑ ProtectInvite\n╰───────────────"
                                sendFoter(msg.to, str(md))

                                                                
                        elif cmd == "rejectall":
                          if wait["selfbot"] == True:
                            #
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    sendFoter(to, "Rejected {} Group Invite".format(str(len(ginvited))))
                                else:
                                    sendFoter(to, "Nothing")
                                
                        elif cmd == "cancelall":
                          if wait["selfbot"] == True:
                            #
                                if msg.toType == 2:
                                    group = cl.getChats(to)
                                    if group.invitee is None or group.invitee == []:
                                        sendFoter(to, "Nothing")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for inv in invitee:
                                            cl.cancelChatInvitation(to, [inv])
                                        cl.sendReplyMessage(to, "Cancelled {} Group Pending".format(str(len(invitee))))


                        elif cmd == "cc1":
                            if msg._from in owner:
                                mid  = list(cl.getChats([to]).chats[0].extra.groupExtra.inviteeMids)
                                if len(mid) >= 1:
                                    mid = mid[0:1]
                                cms = 'kickall.js gid={} token={} app=desktopwin'.format(to, cl.authToken)
                                for target in mid:
                                    if target not in admin and target not in Bots:
                                        cms += ' uid={}'.format(target)
                                success = execute_js(cms)
                                if success:pass

                                
                        elif cmd == "accept:all":
                          if wait["selfbot"] == True:
                            #
                                if msg.toType == 2:
                                    group = cl.getChats(to)
                                    if group.invitee is None or group.invitee == []:
                                        sendFoter(to, "No Have Groups Invitation.")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for acc in invitee:
                                            cl.acceptChatInvitation(to, [acc])
                                        sendFoter(to, "Join {} Groups".format(str(len(invitee))))
                              
                        elif cmd == "#?@logoutZul":
                          if wait["selfbot"] == True:
                            #
                                sendFoter(msg.to, "Logout Success ♪")
                                sys.exit("Logout")
                               
                        elif cmd == "help js":
                          if wait["selfbot"] == True:
                            #
                               helpMessage1 = helpjs()
                               sendFoter(msg.to, str(helpMessage1))
                              
                        elif cmd == "about":
                            if wait["selfbot"] == True:
                                #
                                    try:
                                        arr = []
                                        today = datetime.today()
                                        thn = 2025 
                                        bln = 3    #isi bulannya yg sewa
                                        hr = 2   #isi tanggalnya yg sewa
                                        future = datetime(thn, bln, hr)
                                        days = (str(future - today))
                                        comma = days.find(",")
                                        days = days[:comma]
                                        h = cl.getContact(clMID)
                                        groups = cl.getAllChatIds()
                                        contactlist = cl.getAllContactIds()
                                        kontak = cl.getContacts(contactlist)
                                        favorite = cl.getFavoriteMids()
                                        fil = cl.getSettings().privacyReceiveMessagesFromNotFriend
                                        seal = cl.getSettings().e2eeEnable
                                        blockedlist = cl.getBlockedContactIds()
                                        src = cl.getSettings().privacySearchByUserid
                                        kontak2 = cl.getContacts(blockedlist)
                                        status = {"kick": "", "invite": ""}
                                        peler = {"receivercount": 0, "sendcount": 0}
                                        try:cl.deleteOtherFromChat(to, [clMID]);status["kick"] = "Normal"
                                        except:status["kick"] = "Limit"
                                        try:cl.inviteIntoChat(to, [clMID]);status["invite"] = "Normal"
                                        except:status["invite"] = "Limit"
                                        if src == True:alid = "Add From LineID : True"
                                        else:alid = "Add From LineID : False"                            
                                        if seal == True:letsel = "Letter Sealing : True"
                                        if seal == False:letsel = "Letter Sealing : False"
                                        if fil == True:fpes = "Filter Message : False"
                                        if fil == False:fpes = "Filter Message : True"
                                        kontol = "╭── • ABOUT SELFBOT • ──"
                                        kontol += "\n├ ◌ User : {}".format(h.displayName)
                                        kontol += "\n├ ◌ Group : {}".format(str(len(groups)))
                                        kontol += "\n├ ◌ Friend : {}".format(str(len(kontak)))
                                        kontol += "\n├ ◌ Favorite: {}".format(str(len(favorite)))
                                        kontol += "\n├ ◌ Blocked : {}".format(str(len(kontak2)))
                                        kontol += "\n├ ◌ Chat send : {}".format(str(peler["sendcount"]))
                                        kontol += "\n├ ◌ Chat received : {}".format(str(peler["receivercount"]))
                                        kontol += "\n├ ◌ {}".format(alid)
                                        kontol += "\n├ ◌ {}".format(letsel)
                                        kontol += "\n├ ◌ {}".format(fpes)
                                        kontol += "\n├ ◌ Kick : %s" % status["kick"]
                                        kontol += "\n├ ◌ Invite : %s" % status["invite"]
                                        kontol += "\n├ ◌ Type : Public Bots"
                                        kontol += "\n├ ◌ Update : 02-03-2025"
                                        kontol += "\n├ ◌AppName : ANDROID	14.21.1	Android OS	13.0.9279"
                                        kontol += "\n├ ◌UserAgent : Line/14.21.1 Android OS 13.0.9279"
                                        kontol += "\n├ ◌ Version : TM ZULKIFLI\n╰────────────────"
                                        sendFoter(to, str(kontol))
                                    except Exception as e:
                                        cl.sendReplyMessage(msg.id,to, str(e))
                               
                        elif cmd.startswith("mid "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendReplyMessage(msg.id,to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Steal " in msg.text):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendReplyMessage(msg.id,to, "╭─「 Contact Info 」\n│ Nama : "+str(mi.displayName)+"\n│ Mid : " +key1+"\n│ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))



                        elif text.lower() == "clearchat":
                          if wait["selfbot"] == True:
                            #
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendFoter(msg.to, "Cleared messages")
                               except:
                                   pass

                        elif ("/ti/g/" in msg.text):
                           if msg._from in admin or msg._from in staff:
                              if settings["autoJoinTicket"] == True:
                                 #link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))


                        elif text.lower() == "c":
                          if wait["selfbot"] == True:
                            #
                               try:
                                   cl.removeAllMessages(to)
                                   cl.removeAllMessages(op.param2)
                                   sendFoter(msg.to, "Cleared messages")
                               except:
                                   pass

                        elif text.lower() == "rchat":
                          if wait["selfbot"] == True:
                            ##if msg._from in admin or msg._from in clmid:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"◕ ᴄʜᴀᴛ ʙᴇʀsɪʜ...√")
                               except:
                                   pass


                        elif text.lower() == "rc":
                          if wait["selfbot"] == True:
                            ##if msg._from in admin:
                               cl.sendReplyMessage(msg.id, to, "☛ ᴄʜᴀᴛ ʙᴇʀsɪʜ...♪");cl.removeAllMessages(msg.to)

                                
                        elif cmd.startswith("bc: "):
                          if wait["selfbot"] == True:
                            #  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getAllChatIds()
                                for group in groups:
                                    sendFoter(group, "{}".format(str(txt)))
                                cl.sendMessage(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif cmd.startswith("broadcast "):
                          if wait["selfbot"] == True:
                            #if msg._from in admin or msg._from in clmid:
                               sep = text.split(" ")
                               txt = text.replace(sep[0] + " ","")
                               groups = cl.getAllChatMids().memberChatMids
                               for group in groups:
                                   try:
                                       time.sleep(2)
                                       cl.sendMessage(group, "{}".format(str(txt)))
                                   except:pass
                        elif cmd.startswith("bcvoice "):
                            #if msg._from in admin or msg._from in clmid:
                                bctxt = removeCmd("bcvoice", text)
                                bc = ("broadcast dari adventure team")
                                cb = (bctxt + bc)
                                tts = gTTS(cb, lang='id', slow=False)
                                tts.save('tts.mp3')
                                wowo = cl.getAllChatMids().memberChatMids
                                for group in wowo:
                                    time.sleep(2);cl.sendAudio(group, 'tts.mp3')
                        elif cmd.startswith("fbc "):
                          if wait["selfbot"] == True:
                            #if msg._from in admin or msg._from in clmid:
                               txt = removeCmd("fbc", text)
                               friends = cl.getAllContactIds()
                               for friend in friends:
                                   cl.sendText(friend, "{}".format(str(txt)))
                                   time.sleep(2)
                               cl.sendMessage(to, "Succes broadcast ke {} Friend ".format(str(len(friends))))

                        elif cmd.startswith("bcteman "):
                          if wait["selfbot"] == True:
                            #if msg._from in admin or msg._from in clmid:
                               txt = removeCmd("bcteman", text)
                               friends = cl.getAllContactIds()
                               for friend in friends:
                                   cl.sendText(friend, "{}".format(str(txt)))
                                   time.sleep(2)
                               cl.sendMessage(to, "Succes broadcast ke {} Friend ".format(str(len(friends))))

                        elif cmd.startswith("keteman "):
                          if wait["selfbot"] == True:
                            #if msg._from in admin or msg._from in clmid:
                               txt = removeCmd("fbc", text)
                               friends = cl.getAllContactIds()
                               for friend in friends:
                                   cl.sendText(friend, "{}".format(str(txt)))
                                   time.sleep(2)
                               cl.sendMessage(to, "Succes broadcast ke {} Friend ".format(str(len(friends))))

                        elif text.lower() == 'kalender':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'saur sauuurr':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'sahur':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'sahur ':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'Imsyak':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'Imsyak ':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'subuuh':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'subuuh ':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'Solat ':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)

                        elif text.lower() == 'Solat':
                          ###if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendFoter(msg.to, readTime)


                        elif cmd.startswith("sabarin: "):
                          if wait["selfbot"] == True:
                            #  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getAllChatIds()
                                for group in groups:
                                    sendFoter(group, "{}".format(str(txt)))
                                cl.sendMessage(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif cmd.startswith("status: "):
                          if wait["selfbot"] == True:
                            #  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getAllChatIds()
                                for group in groups:
                                    sendFoter(group, "{}".format(str(txt)))
                                cl.sendMessage(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif cmd.startswith("status1: "):
                          #if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                pname = cl.getContact(sender).statusMessage
                                profile = cl.getProfile()
                                profile.statusMessage = string
                                cl.updateProfile(profile)
                                cl.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+ pname +"\nTo :"+ string)

                        elif cmd.startswith("kontak"):
                          #if msg._from in admin:
                            if msg.contentMetadata != None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.sendContact(to,str(ls))


                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            #  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getAllChatIds()
                                for group in groups:
                                    sendFoter(group, "{}".format(str(txt)))
                                cl.sendMessage(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif cmd.startswith("kamu: "):
                          if wait["selfbot"] == True:
                            #  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getAllChatIds()
                                for group in groups:
                                    sendFoter(group, "{}".format(str(txt)))
                                cl.sendMessage(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif cmd.startswith("ling: "):
                          if wait["selfbot"] == True:
                            #  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getAllChatIds()
                                for group in groups:
                                    sendFoter(group, "{}".format(str(txt)))
                                cl.sendMessage(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            #
                               sendFoter(msg.to, "Setkey Anda: " + str(Setmain["keyCommand"]))
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendFoter(msg.to, "Update to {}".format(str(key).lower()))

                        elif cmd.startswith("setsider: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Gagal mengganti key")
                               else:
                                   wait["mention"] = str(key).lower()
                                   sendFoter(msg.to, "Update to {}".format(str(key).lower()))
                        elif cmd.startswith("setsider1: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Gagal mengganti key")
                               else:
                                   wait["mention1"] = str(key).lower()
                                   sendFoter(msg.to, "Update to {}".format(str(key).lower()))
                        elif cmd.startswith("setreject: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["autoCancel"]["members"] = str(key).lower()
                                   sendFoter(msg.to, "Auto reject set to {}".format(str(key).lower()))

                        elif cmd.startswith("setapikey: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Gagal mengganti key")
                               else:
                                   wait["apikey"] = str(key).lower()
                                   sendFoter(msg.to, "Success update apikey")

                        elif cmd.startswith("setwelcome: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["welcome"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd == "cekliff":
                            #
                               sendFoter(msg.to, "line://app/"+ str(wait["liff"]))
                        elif cmd.startswith("setliff: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["liff"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif cmd.startswith("setleave: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["leave"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            #
                               Setmain["keyCommand"] = ""
                               sendFoter(msg.to, "Succes")

                        elif cmd == "1reboot":
                          if wait["selfbot"] == True:
                            #
                               sendFoter(msg.to, "waitting 1 second")
                               time.sleep(5)
                               Setmain["restartPoint"] = msg.to
                               sendFoter(msg.to, "Be reboot to pee.")
                               restartBot()

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            ##if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "myname":
                          ##if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id, to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))

                        elif cmd == "mybio":
                          ##if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id, to, "[ sᴛᴀᴛᴜs ʟɪɴᴇ ]\n{}".format(contact.statusMessage))

                        elif cmd == "Profile1":
                          if wait["selfbot"] == True:
                            text = "~ Profile ~"
                            contact = cl.getContact(sender)
                            #cover = cl.getProfileCoverURL(sender)
                            result = "╔══[ Details Profile ]"
                            result += "\n├≽ Display Name : @!"
                            result += "\n├≽ Mid : {}".format(contact.mid)
                            result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                            result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n├≽ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            sendFoter(msg.to, text, result, [sender])

                        elif cmd == "byeme":
                              ##if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                G = cl.getChats([to]).chats[0]
                                time.sleep(1);cl.sendMessage(to, "Invite uLang Ya Akun Loadchat 🤭")
                                cl.deleteSelfFromChat(to)

                        elif text.lower() == "zleaveall":
                            ##if msg._from in admin:
                                gid = cl.getChats([to]).chats[0].chatName               	
                                for i in gid:
                                    cl.deleteSelfFromChat(i)
                                    print ("Pamit semua group")


                                                          
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            #
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                sendFoter(msg.to, bot)
                               
                        elif cmd == "blocklist":
                          if wait["selfbot"] == True:
                            #
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="「 Blocked List 」\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                sendFoter(msg.to, msgs)
                                
                        elif cmd.startswith("delfriend "):
                          #
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.deleteContact(ls)
                                sendFoter(to, "Success Remove " + str(contact.displayName) + " to Friendlist")

                        elif cmd == "invite on":
                            #if msg._from in admin:
                                wait["Invi"] = True
                                cl.sendMessage(msg.to,"❑ sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")

                        elif cmd == "invite off":
                            #if msg._from in admin:
                                wait["Invi"] = False
                                cl.sendMessage(msg.to,"❑ sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ off")

                                
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            #
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               sendFoter(msg.id,to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")
                               
                        elif cmd.startswith("bye: "):
                            if wait["selfbot"] == True:
                              #
                                  separate = cmd.split(":")
                                  number = cmd.replace(separate[0] + ":","")
                                  groups = cl.getAllChatIds()
                                  try:
                                      group = groups[int(number)-1]
                                      G = cl.getChats(group)
                                      try:
                                          cl.deleteSelfFromChat(G.id)
                                      except:
                                          cl.deleteSelfFromChat(G.id)
                                      sendFoter(msg.to, "Leave Group : " + G.name)
                                  except Exception as error:
                                      sendFoter(msg.to, str(error))

                        elif cmd == 'ginfo':
#                          ##if msg._from in admin or msg._from in clmid:
                            group = cl.getChats([to]).chats[0]
                            try:ccreator = group.extra.groupExtra.creator;gcreator = cl.getContact(ccreator).displayName
                            except:ccreator = None;gcreator = 'Not found'
                            if not group.extra.groupExtra.inviteeMids:pendings = 0
                            else:pendings = len(group.extra.groupExtra.inviteeMids)
                            qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
                            if group.extra.groupExtra.preventedJoinByTicket:ticket = 'Not found'
                            else:ticket = 'https://line.me/R/ti/g/' + str(cl.reissueChatTicket(group.chatMid).ticketId)
                            created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
                            img ="https://obs.line-scdn.net/{}".format(cl.getChats([to]).chats[0].picturePath)
                            cl.sendImageWithURL(msg.to, str(img))
                            if ccreator:cl.sendMessage(to, None, contentMetadata={'mid': ccreator}, contentType=13)
                            cl.sendReplyMessage(msg.id, to,'「 Group Info 」\n\n    • Group ID : ' + group.chatMid + '\n    • Group Name : ' + group.chatName + '\n    • Pembuat : ' + gcreator + '\n    • Created Time : ' + created + '\n    • Sisa Member : ' + str(len(group.extra.groupExtra.memberMids)) + '\n    • Member Pending : ' + str(pendings) + '\n    • Link QR : ' + qr)

                        elif cmd == "#ginfo":
                          #
                            try:
                                G = cl.getChats(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "╭─「 Group Info 」\n├↘ Nama Group : {}".format(G.name)+ "\n├↘ ID Group : {}".format(G.id)+ "\n├↘ Pembuat : {}".format(G.creator.displayName)+ "\n├↘ Waktu Dibuat : {}".format(str(timeCreated))+ "\n├↘ Jumlah Member : {}".format(str(len(G.members)))+ "\n├↘ Jumlah Pending : {}".format(gPending)+ "\n├↘ Group Qr : {}".format(gQr)+ "\n├↘ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendFoter(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          #
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getAllChatIds()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getChats(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╭───「 Group Info 」───"
                                ret_ += "\n├↘ Nama Group : {}".format(G.name)
                                ret_ += "\n├↘ ID Group : {}".format(G.id)
                                ret_ += "\n├↘ Pembuat : {}".format(gCreator)
                                ret_ += "\n├↘ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n├↘ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n├↘ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n├↘ Group Qr : {}".format(gQr)
                                ret_ += "\n├↘ Group Ticket : {}".format(gTicket)
                                ret_ += "\n├↘ Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                ret_ += "\n╰──────────────"
                                sendFoter(msg.to, str(ret_))
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass

                        elif cmd.startswith("curiqr "):
                          ##if msg._from in admin or msg._from in clmid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getAllChatMids().memberChatMids
                            _gd = list(groups)
                            wowo = _gd[int(number)-1]
                            if msg.toType == 2:
                                   X = cl.getChats([wowo],True,False).chats[0]
                                   X.extra.groupExtra.preventedJoinByTicket = False
                                   cl.updateChat(X , 4)
                            gurl = cl.reissueChatTicket(wowo).ticketId
                            cl.sendReplyMessage(msg.id, to,"line://ti/g/{}".format(gurl))

                        elif cmd.startswith("openqr "):
                          ##if msg._from in admin or msg._from in clmid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getAllChatMids().memberChatMids
                            _gd = list(groups)
                            wowo = _gd[int(number)-1]
                            if msg.toType == 2:
                                   X = cl.getChats([wowo],True,False).chats[0]
                                   X.extra.groupExtra.preventedJoinByTicket = False
                                   cl.updateChat(X , 4)
                            gurl = cl.reissueChatTicket(wowo).ticketId
                            cl.sendReplyMessage(msg.id, to,"line://ti/g/{}".format(gurl))

                        elif cmd.startswith("curi "):
                          ##if msg._from in admin or msg._from in clmid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getAllChatMids().memberChatMids
                            _gd = list(groups)
                            wowo = _gd[int(number)-1]
                            if msg.toType == 2:
                                   X = cl.getChats([wowo],True,False).chats[0]
                                   X.extra.groupExtra.preventedJoinByTicket = False
                                   cl.updateChat(X , 4)
                            gurl = cl.reissueChatTicket(wowo).ticketId
                            cl.sendReplyMessage(msg.id, to,"line://ti/g/{}".format(gurl))


                        elif cmd.startswith("gurl "):
                          #
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getAllChatIds()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getChats(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                sendFoter(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("close "):
                          #
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getAllChatIds()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getChats(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                sendFoter(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          #
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getAllChatIds()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getChats(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "├↘ "+ str(no) + ". " + mem.displayName
                                sendFoter(msg.to,"├↘ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            #
                              CM = cl.getAllChatMids()
                              r = "• Group List :"
                              r += f"\n⌖ Groups:"
                              if len(list(CM.memberChatMids)) != 0:
                                  for i, x in enumerate(list(CM.memberChatMids)):
                                      r += (
                                          f"\n\t\t[{i+1}] "
                                          + str(cl.getChats([x]).chats[0].chatName)[0:15]
                                          + "... ("
                                          + str(
                                              len(
                                                  list(
                                                      cl.getChats([x])
                                                      .chats[0]
                                                      .extra.groupExtra.memberMids
                                                  )
                                              )
                                          )
                                          + ")"
                                      )
                              else:
                                  r += f"\n\t\t[x] No Group Joined"
                              r += f"\n⌖ PENDINGAN :"
                              if len(list(CM.invitedChatMids)) != 0:
                                  for i, x in enumerate(list(CM.invitedChatMids)):
                                      r += (
                                          f"\n\t\t[{i+1}] "
                                          + str(cl.getChats([x]).chats[0].chatName)[0:15]
                                          + "... ("
                                          + str(
                                              len(
                                                  list(
                                                      cl.getChats([x])
                                                      .chats[0]
                                                      .extra.groupExtra.inviteeMids
                                                  )
                                              )
                                          )
                                          + ")"
                                      )
                              else:
                                  r += f"\n\t\t[x] No Pending Group"
                              sendFoter(to, str(r))

                        elif cmd == "buka qr":
                          if wait["selfbot"] == True:
                            #
                                if msg.toType == 2:
                                   X = cl.getChats(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   sendFoter(msg.to, "Open Link Groups")

                        elif cmd == "tutup qr":
                          if wait["selfbot"] == True:
                            #
                                if msg.toType == 2:
                                   X = cl.getChats(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendFoter(msg.to, "Blocked Url Groups")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            #
                                if msg.toType == 2:
                                   x = cl.getChats(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   sendFoter(msg.to, "Nama : "+str(x.name)+ "\nUrl : http://line.me/R/ti/g/"+gurl)
                                                        
                        elif cmd.startswith("food "):
                          #
                              query = text.replace("food ","")
                              cond = query.split("|")
                              search = str(cond[0])
                              r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                              data=r.text
                              data=json.loads(r.text)
                              if data != []:
                                  ret_ = []                                	
                                  for food in data:
                                      if 'http://' in food["url"]:
                                          pass
                                      else:
                                          if len(ret_) >= 10:
                                              pass
                                          else:
                                              ret_.append({
                                                  "imageUrl": "{}".format(str(food["url"])),
                                                  "action": {
                                                      "type": "uri",
                                                      "label": "Send Image",
                                                      "uri": "line://app/1655623470-81eDd9kM?type=image&img={}".format(str(food["url"]))
                                                      }
                                                  }
                                              )
                                  k = len(ret_)//10
                                  for aa in range(k+1):
                                      data = {
                                          "type": "template",
                                          "altText": "I'm hungry",
                                          "template": {
                                              "type": "image_carousel",
                                              "columns": ret_[aa*10 : (aa+1)*10]
                                          }
                                      }
                                      sendTemplate(to, data)                                                                        
  
                        elif cmd == "order" or cmd == "promo":
                          if wait["selfbot"] == True:
                                kontol = wait["order"]
                                sendFoter(to, str(kontol))
#batas
                        elif cmd == "liff" or cmd == "liffs":
                            #
                                sendFoter(to, "Berikut Data Liff nya\nLiff [ 01 ] https://liff.line.me/2000602682-YP5KArqL\nLiff [ 02 ]https://liff.line.me/2000602728-ZB8DrLMB\nLiff [ 03 ] https://liff.line.me/2000602744-qe53a4vv")
                             

                        elif cmd == "bot" or text.lower() == 'bot' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ɢᴜᴇ ʙᴜᴋᴀɴ ʙᴏᴛ ᴋᴜʏᴀ ʟᴏᴇ ʏᴀɴɢ ʙᴏᴛ")

                        elif cmd == "asalamualaikum wr wb" or text.lower() == 'asalamualaikum' or text.lower() == 'asalamualaikum ' or text.lower() == 'asalamualaikum wr wb ':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "Waalaikum salam wr wb")

                        elif cmd == "assalamu'alaikum" or text.lower() == ' assalamualaikum ' or text.lower() == 'asalamualaikum ' or text.lower() == 'asalamualaikum wr wb ':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "Waalaikum salam wr wb")
                               
                        elif cmd == "pm" or text.lower() == 'pm' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴍᴀᴀꜰ ᴛɪᴅᴀᴋ ᴍᴇɴᴇʀɪᴍᴀ ᴘᴍ")
                               
                        elif cmd == "bang" or text.lower() == 'bang' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴀᴅᴀ ᴀᴘᴀ ꜱᴀʏᴀɴɢ ᴍᴀᴜ ᴍɪɴᴛᴀ ᴊᴀᴛᴀʜ ʏᴀʜ")
                               
                        elif cmd == "sepi" or text.lower() == 'sepi' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇᴘɪ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏʀᴀɴɢ ʟᴀɢɪ ᴘᴀᴅᴀ ᴋᴇʟᴏɴ ᴍᴜɴɢᴋɪɴ")

                        elif cmd == "pagi" or text.lower() == 'sepi' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "pagi juga ꜱᴇᴘɪ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏʀᴀɴɢ ʟᴀɢɪ ᴘᴀᴅᴀ KERJA ᴍᴜɴɢᴋɪɴ")

                        elif cmd == "up" or text.lower() == 'ayo naik' or text.lower() == '@All' or text.lower() == '@All ' or text.lower() == 'kang bot' or text.lower() == 'hai kang bot ' or text.lower() == 'hai kang bot' or text.lower() == 'kang bot ' or text.lower() == 'bentar' or text.lower() == 'js on' or text.lower() == '@moko ' or text.lower() == '@zul ' or text.lower() == '@all' or text.lower() == '@all ' or text.lower() == 'bypas on' or text.lower() == 'login js' or text.lower() == 'menu js' or text.lower() == 'kojom on' or text.lower() == 'mojok on' or text.lower() == 'sayang' or text.lower() == '@zul' or text.lower() == '@moko' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "Fitur ini tidak didukung di versi LINE yang digunakan. Silakan update ke versi terbaru LINE dan coba lagi.")
                               
                        elif cmd == "kangen" or text.lower() == 'kangen' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴀᴍᴀ ꜱᴀʏᴀɴɢ ᴀᴋᴜ ᴊᴜɢᴀ ᴋᴀɴɢᴇɴ ᴋᴀᴍᴜ ᴄɪᴜᴍ ᴅᴜʟᴜ ᴅᴏɴɢ")
                               
                        elif cmd == "selamat malam" or text.lower() == 'selamat malam' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴍᴀʟᴀᴍ ᴊᴜɢᴀ ꜱᴀʏᴀɴɢ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴛɪᴅᴜʀ ʏᴀʜ")
                               
                        elif cmd == "selamat pagi" or text.lower() == 'selamat pagi' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇʟᴀᴍᴀᴛ ᴘᴀɢɪ ᴊᴜɢᴀ ꜱᴀʏᴀɴɢᴋᴜ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ʙᴀʜᴀɢɪᴀ")
                               
                        elif cmd == "assalamualaikum" or text.lower() == 'as' or text.lower() == 'Assallamuallaikum' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                               
                        elif cmd == "selamat siang" or text.lower() == 'selamat siang' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇʟᴀᴍᴀᴛ ꜱɪᴀɴɢ ꜱᴀʏᴀɴɢ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ɴɢᴏᴘɪ ʙɪᴀʀ ʙᴀʜᴀɢɪᴀ")
                               
                        elif cmd == "selamat sore" or text.lower() == 'selamat sore' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇʟᴀᴍᴀᴛ ꜱᴏʀᴇ ᴊᴜɢᴀ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴍᴀɴᴅɪ ʏᴀɴɢ ʙᴇʀꜱɪʜ")
                               
                        elif cmd == "pm mesla" or text.lower() == 'pm mesla' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴘᴍ ᴍᴇꜱʀᴀ ᴍᴀᴜ ᴘɪɴᴊᴇᴍ ᴅᴜɪᴛ ɴɪʜ ᴏʀᴀɴɢ")

                        elif cmd == "mari menyanyikan " or text.lower() == 'mari menyanyikan' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "KETIK bc: ling smule, tiktok, yutup DLL BUAT BROKES ATW SEBARIN KATA-KATA 😇😇")
                             
                        elif cmd == "kojom" or text.lower() == 'kojom' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴋᴏᴊᴏᴍ ᴍᴜʟᴜ ᴀᴡᴀꜱ ʜᴘ ɴʏᴀʜ ʙᴜɴᴛɪɴɢ")
                               
                        elif cmd == "bentar" or text.lower() == 'bentar' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ʙᴇɴᴛᴀʀ ᴀᴋᴜ ᴀᴅᴀ ᴛᴀᴍᴜ ᴘᴀᴋ ʀᴛ ꜱᴜʀᴜʜ ʙɪᴋɪɴᴋᴀɴ ᴋᴏᴘɪ")
                               
                        elif cmd == "salken semua" or text.lower() == 'salken semua' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇᴍᴜᴀ ɪᴛᴜ ꜱɪᴀᴘᴀ ᴀᴊᴀʜ ᴀᴋᴜ ᴛᴇʀᴍᴀꜱᴜᴋ ɢᴀ ɴɪʜ")
                               
                        elif cmd == "wc" or text.lower() == 'wc' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ ʀᴏᴏᴍ ᴋᴀᴍɪ ꜱᴀʟᴀᴍ ᴋᴇɴᴀʟ ʏᴀʜ ᴅᴀʀɪ ᴀᴋᴜ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴘᴍ ᴍᴇꜱʀᴀ")

                        elif cmd == "wc1" or text.lower() == 'wc1 ' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ยินดีต้อนรับสู่ห้องของเรา คำทักทายจากฉัน อย่าลืมแชทส่วนตัวที่เป็นมิตร")
                               
                        elif cmd == "sibuk" or text.lower() == 'sibuk' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱɪʙᴜᴋ ᴍᴀᴜ ᴋᴇᴍᴀɴᴀ ᴘᴀʟɪɴɢ ᴋᴇʟᴏɴ ꜱᴀᴍᴀ ʙᴏᴊᴏɴʏᴀʜ")

                        elif cmd == "sari" or text.lower() == 'zul' or text.lower() == 'liya' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "Berikut Data Liffmu Majikanku\n\nLiff [ 01 ] https://liff.line.me/2000602682-YP5KArqL\n\n\n\nLiff [ 02 ] https://liff.line.me/2000602728-ZB8DrLMB\n\nLiff [ 03 ] https://liff.line.me/2000602744-qe53a4vv")

                               
                        elif cmd == "wa" or text.lower() == 'wa' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                               
#                        elif cmd == "puskun" or text.lower() == 'puskun' or text.lower() == '1368o' or text.lower() == 'bot':
#                          if wait["selfbot"] == True:                            
#                               sendFoter(to, "ᴀᴡᴀꜱ ᴛᴜʜ ᴀɴᴀᴋ ᴏʀᴀɴɢ ᴅɪ ʙᴀᴘᴇʀɪɴ ᴋᴀꜱɪᴀɴ ʟᴏʜ")
                               
                        elif cmd == "tunggu bentar" or text.lower() == 'tunggu bentar' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ʙᴇɴᴛᴀʀ ᴀᴅᴀ ᴘᴀᴋ ʀᴛ")
                               
                        elif cmd == "war" or text.lower() == 'war' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴄᴏʙᴀ ʀᴇꜱᴘᴏɴɪɴ ʙᴏᴛɴʏᴀ")
                               
                        elif cmd == "naik" or text.lower() == 'naik' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ɴᴀɪᴋ ᴋᴇᴍᴀɴᴀ ꜱᴀʏᴀʜ ʙᴇʟᴜᴍ ᴘɪɴᴊᴀᴍ ᴛᴀɴɢɢᴀ")
                               
                        elif cmd == "banyak cctv" or text.lower() == 'banyak cctv' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ɪʏᴀʜ ᴘᴀᴅᴀ ɴʏɪᴍᴀᴋ ɪᴛᴜ ᴊᴏɴᴇꜱ ꜱᴇᴍᴜᴀ")
                               
                        elif cmd == "done" or text.lower() == 'sukses' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:         
                            if msg._from in owner or msg._from in admin:
                               sendFoter(to, "ʙɪʟᴀɴɢ ᴛᴇʀɪᴍᴀᴋᴀꜱɪʜ ᴋᴇ ʙᴀɴɢ ʀᴀᴋᴀ ꜱʙ ɴʏᴀʜ ꜱᴜᴅᴀʜ ʙᴇʀʜᴀꜱɪʟ ʟᴏɢɪɴ ᴅᴀɴ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ɴᴀɴᴛɪ ᴍᴀʟᴀᴍ ᴋᴏᴊᴏᴍ ʏᴀʜ")
                               
                        elif cmd == "good night" or text.lower() == 'good night' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇʟᴀᴍᴀᴛ ᴍᴀʟᴀᴍ ᴊᴜɢᴀ ꜱᴇʟᴀᴍᴀᴛ ʙᴏʙᴏ ᴍɪᴍᴘɪ ɪɴᴅᴀʜ ʏᴀʜ ꜱᴀʏᴀɴɢᴋᴜ")
                               
                        elif cmd == "bang pm" or text.lower() == 'bang pm' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴘᴍ ᴍᴀᴜ ᴍᴏᴅᴜꜱ ɴɪʜ ᴏʀᴀɴɢ ᴘᴀʟɪɴɢ ɴɢᴀᴊᴀᴋɪɴ ᴋᴏᴊᴏᴍ")
                             
                        elif cmd == "d" or text.lower() == 'd' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "Dengan Adanyah Kamu Aku Merasa Bahagia")                              
                             
                        elif cmd == "sinyal" or text.lower() == 'sinyal' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴄᴏʙᴀ ɴᴀɪᴋ ᴛɪʜᴀɴɢ ʙᴇɴᴅᴇʀᴀ ʙɪᴀʀ ʙᴀɴʏᴀᴋ ꜱɪɴʏᴀʟ")
                                                  
                        elif cmd == "wait" or text.lower() == 'wait' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴡᴀɪᴛ ɪᴛᴜ ᴀᴘᴀᴀɴ ꜱᴀʏᴀʜ ᴛɪᴅᴀᴋ ᴘᴀʜᴀᴍ ʙᴀʜᴀꜱᴀɴʏᴀ")
                               
                        elif cmd == "dudul" or text.lower() == 'dudul' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴋᴀᴍᴜ ᴛᴜʜ ʏᴀɴɢ ᴅᴜᴅᴜʟ ᴋᴜʏᴀ ᴅᴀꜱᴀʀ")
                               
                        elif cmd == "bomat" or text.lower() == 'bomat' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ʙᴏᴍᴀᴛ ɪᴛᴜ ᴀᴘᴀᴀɴ ꜱᴀʏᴀʜ ɢᴀ ᴘᴀʜᴀᴍ ᴋᴋ")
                               
                        elif cmd == "awas" or text.lower() == 'awas' or text.lower() == '1368o' or text.lower() == 'bot':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴀᴡᴀꜱ ᴅɪᴀ ᴘᴇʟᴀᴋᴏʀ ᴊᴀɴɢᴀɴ ᴍᴇɴᴅᴇᴋᴀᴛ")
                               
                        elif cmd == "salken" or text.lower() == 'salken':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴀʟᴋᴇɴ ᴍᴜʟᴜ ᴊᴀᴅɪᴀɴ ᴋᴀɢᴀᴋ ᴋᴀɴ ꜱᴜᴇ ")
                               
                        elif cmd == "as" or text.lower() == 'as':
                          if wait["selfbot"] == True:         
                           if msg._from in owner or msg._from in admin:                    
                               sendFoter(to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ ")

                        elif cmd == "assallamuallaikum" or text.lower() == 'ass':
                          if wait["selfbot"] == True:         
                           if msg._from in owner or msg._from in admin:                    
                               sendFoter(to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ ")

                        elif cmd == "salken smuah" or text.lower() == 'salken':
                          if wait["selfbot"] == True:         
                           if msg._from in owner or msg._from in admin:                    
                               sendFoter(to, "Salken Juga kk")
                               
                          elif cmd == "sue" or text.lower() == 'sue':
                           if wait["selfbot"] == True:                            
                               sendFoter(to, "ᴀᴘᴀɴ ꜱɪʜ ᴘᴇᴀ ᴋᴍᴜ")
                               
                          elif cmd == "asem" or text.lower() == 'asem':
                           if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴜᴇ ʏᴀʜ ᴅɪ ᴊᴀʜɪᴛ ʟᴀʜ ʙɪᴀʀ ᴘᴇʀᴀᴡᴀɴ ʟᴀɢɪ")
                               
                          elif cmd == "walaikumsalam" or text.lower() == 'walaikumsalam':
                           if wait["selfbot"] == True:                            
                               sendFoter(to, "ꜱᴇꜱᴀᴍᴀ ᴏʀᴀɴɢ ᴍᴜꜱʟɪᴍ ᴡᴀᴊɪʙ ᴛᴜʜ ᴊᴀᴡᴀʙ ꜱᴀʟᴀᴍ")
                                                 
                        elif cmd == "kikil" or text.lower() == 'kikil':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ʟᴏᴇ ᴛᴜʜ ʏᴀɴɢ ᴋɪᴋɪʟ ᴛᴜᴋᴀɴɢ ᴊꜱ ʀᴏᴏᴍ ᴏʀᴀɴɢ")
                               
                        elif cmd == "nah" or text.lower() == 'nahhh':
                          if wait["selfbot"] == True:                            
                               sendFoter(to, "ɴᴀʜ ᴋᴇɴᴀᴘᴀ ꜱᴜᴅᴀʜ ᴄᴀᴘᴇ ʏᴀʜ ᴍᴏᴅᴜꜱɪɴ ᴏʀᴀɴɢ")

#a sampe z
                        elif text.lower() == "midd":
                          if wait["selfbot"] == True:
                               middd = "ɴᴀᴍᴀ : " +cl.getContact(msg._from).displayName + "\nᴍɪᴅ : " +msg._from                              
                               cl.sendReplyMessage(msg.id, to,middd)
                        elif text.lower() == "rc":
                          if wait["selfbot"] == True:
                             
                               sendFoter(to, "☛ ᴄʜᴀᴛ ʙᴇʀsɪʜ...♪");cl.removeAllMessages(msg.to)
                        elif text.lower() == "assalamualaikum":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                               
                        elif text.lower() == "waalaikumsalam":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Nah Gitu Dong Di Jawab kalo ada salam")      
 
                        elif text.lower() == "malam":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, " Malam Juga Kawan")      
                               
                        elif text.lower() == "sue":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Apanya Yang Sue kk")      
                               
                        elif text.lower() == "pagi":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Pagi Juga Kawan")      
                               
                        elif text.lower() == "siang":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Siang Juga Kawan") 
       
                        elif text.lower() == "sore":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Sore juga kawan") 
                         
                        elif text.lower() == "sepi":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "mau yg Rame kepasar Bro..😆") 
                               
                        elif text.lower() == "dudul":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Persamaan dari OoN 😂") 
      
                        elif text.lower() == "salam":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                         
                        elif text.lower() == "jawab":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Nah Gitu Dong Di Jawab ") 

                        elif text.lower() == "wc":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Selamat Datang BoLoo Moga Betah ")                                                       

                        elif text.lower() == "desah":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Desah Sama Kamu aja yukkkk ") 

                        elif text.lower() == "naik":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Naik Duluan aja Ntar ku Susul ") 

                        elif text.lower() == "welcome":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Selamat Datang kawan Moga Betah ")                                                       

                        elif text.lower() == "salken":
                          if wait["selfbot"] == True:                              
                               sendFoter(to, "Salam Kenal Balik bolo ")        
                                   
                        elif text.lower() == "d":
                          if wait["selfbot"] == True:                              
                               a = ['Dalamnya lautan tak sedalam hatiku','Dimana dirimu sayang 🤭🤭','Duniya ini hanya milik kita berdua🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b) 
          
                        elif text.lower() == "e":
                          if wait["selfbot"] == True:                              
                               a = ['Emangnya Otong mu gede🤣🤣🤣','Eh ada sayang ada🤭🤭']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b) 
                               
                        elif text.lower() == "f":
                          if wait["selfbot"] == True:                              
                               a = ['Fikiranku selalu mikirin kamu','Faham bebz.. saya di sini..mau ngasih duit ye🤣🤣??']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b) 
                               
                        elif text.lower() == "g":
                          if wait["selfbot"] == True:                              
                               a = ['Gak semudah itu untuk menjadi orang yg sabar..','Gk pake tapi tapian,,,,awaas kl boong kao,,,']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)         
       
                        elif text.lower() == "h":
                          if wait["selfbot"] == True:                              
                               a = ['Hatiku hanya untukmu 🤣🤣🤣','Hari ini semoga Berkah 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)         
                               
                        elif text.lower() == "i":
                          if wait["selfbot"] == True:                              
                               a = ['Indah nya Hari ini Bersamamu 🤣🤣🤣','Ini untukmu tapi Bohong 🤣??🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)

                        elif text.lower() == "ip":
                          if wait["selfbot"] == True:                              
                               a = ['Berikut Data Liffmu Majikanku\n\nLiff [ 01 ] https://liff.line.me/2000602682-YP5KArqL\n\n\n\nLiff [ 02 ] https://liff.line.me/2000602728-ZB8DrLMB\n\nLiff [ 03 ] https://liff.line.me/2000602744-qe53a4vv']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)

                        elif text.lower() == "j":
                          if wait["selfbot"] == True:                              
                               a = ['Janda selalu di depan om 🤣🤣🤣','Jangan kau curi hatiku 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)
                               
                        elif text.lower() == "k":
                          if wait["selfbot"] == True:                              
                               a = ['Kolor mu masih menempel di hatiku 🤣🤣🤣','Kepadamu aku bisa Berbagi 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)

                        elif text.lower() == "l":
                          if wait["selfbot"] == True:                              
                               a = ['Los doll ngadepin kamu 🤣🤣🤣','Lika-liku hidup emang susah brow jngan aborsi🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)
                               
                        elif text.lower() == "m":
                          if wait["selfbot"] == True:                              
                               a = ['Mau Ajak Desah Ya Kak Paling 🤣🤣🤣','Memang aku tidak bisa melupakan mu🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)        
                               
                        elif text.lower() == "n":
                          if wait["selfbot"] == True:                              
                               a = ['Nah pm aim ketahuan nich🤣🤣🤣','Ning kene aku ngenteni koe🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)    

                        elif text.lower() == "o":
                          if wait["selfbot"] == True:                              
                               a = ['Oh my good gede banget🤣🤣🤣','Oh yes lah klo gtu 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)

                        elif text.lower() == "p":
                          if wait["selfbot"] == True:                              
                               a = ['Pulang sono klo baperan 🤣🤣🤣','Pean kok ngilangan siee?? 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)
                               
                        elif text.lower() == "r":
                          if wait["selfbot"] == True:                              
                               a = ['Rasa ini semakin membuatku melayang2.. 🤣🤣🤣','Rapopo aku kamu cuekin 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)        
                               
                        elif text.lower() == "s":
                          if wait["selfbot"] == True:                              
                               a = ['Selalu ada Bersamamu 🤣🤣🤣','Salahku apa padamu beb 🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)

                        elif text.lower() == "t":
                          if wait["selfbot"] == True:                              
                               a = ['Tapi Boong aku lope kamu 🤣🤣🤣','tak kan terbagi sayangku untukmu...🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)                
                               
                        elif text.lower() == "u":
                          if wait["selfbot"] == True:                              
                               a = ['Untuk apa hidup kalo tanpa ada kamu🤣','untuk apa kau bersumpah bila mengotori bibir mu🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)                
                               
                        elif text.lower() == "w":
                          if wait["selfbot"] == True:                              
                               a = ['Walau menengis hati ini....sayangku tak kan terbagi... 🤣🤣🤣','Wow Gede Banget nich. .🤣🤣🤣']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)                        

                        elif text.lower() == "z":
                          if wait["selfbot"] == True:                              
                               a = ['ZULKIFLI MOKOAGOW']
                               b = random.choice(a)
                               cl.sendReplyMessage(msg.id, to, b)                        


                        elif cmd == "me" or cmd == "aim":
                          if wait["selfbot"] == True:
                            #
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                #cover = cl.getProfileCoverURL(sender)
                                time.sleep(1)
                                data = {"type": "flex","altText": "TEAM TERMUX V 5","contents":{"type": "carousel","contents": [{"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectMode": "cover","aspectRatio": "1:1"}],"paddingAll": "0px"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "18px","height": "18px","cornerRadius": "50px","offsetTop": "1px","offsetStart": "5px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "TEAM TERMUX V 5","size": "9px","color": "#ffffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "130px","height": "15px","borderWidth": "1px","borderColor": "#ffffff","offsetTop": "2px","offsetStart": "25px","cornerRadius": "3px"}],"backgroundColor": "#000000"},"action": {"type": "uri","label": "action","uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"}},{"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectMode": "cover","aspectRatio": "1:1","gravity": "top"}],"paddingAll": "0px"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "18px","height": "18px","cornerRadius": "50px","offsetTop": "1px","offsetStart": "5px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "PROTECTION YOUR GROUPS","size": "9px","color": "#ffffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "130px","height": "15px","borderWidth": "1px","borderColor": "#ffffff","offsetTop": "2px","offsetStart": "25px","cornerRadius": "3px"}],"backgroundColor": "#000000"},"action": {"type": "uri","label": "action","uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1"}},{"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "text","text": "TEAM TERMUX V 5","size": "10px","color": "#00ff00","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "20px","offsetTop": "2px","offsetStart": "3px"},{"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "text","text": "TEAM : Zulkifli","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "MAKER : Zulkifli","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "15px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "RILISE : 2016","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "30px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "VERSION : SELFBOT V17","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "45px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "OPEN RENTAL BOT","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "60px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "SELFBOT","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "75px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "PROTECT ROOM","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "90px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "GOLANG","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "105px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "BOT WAR","size": "10px","color": "#ffffff","align": "center"},{"type": "separator","color": "#ffffff"}],"position": "absolute","width": "150px","height": "15px","offsetTop": "120px"}],"position": "absolute","width": "150px","height": "140px","offsetTop": "15px","offsetStart": "3px"}],"paddingAll": "0px","backgroundColor": "#000000"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg","size": "full","aspectRatio": "1:1","aspectMode": "cover","animated": True}],"position": "absolute","width": "18px","height": "18px","cornerRadius": "50px","offsetTop": "1px","offsetStart": "5px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "TAP HERE FOR ORDER","size": "9px","color": "#ffffff","align": "center","offsetTop": "1px"}],"position": "absolute","width": "130px","height": "15px","borderWidth": "1px","borderColor": "#ffffff","offsetTop": "2px","offsetStart": "25px","cornerRadius": "3px"}],"backgroundColor": "#000000"}}]}}
                                sendTemplate(to, data)

#
                        elif cmd == "helpjs":
                          if wait["selfbot"] == True:
                            #
                               contact = cl.getProfile()
                               mids = [contact.mid]
#                               #cover = cl.getProfileCoverURL(sender)
#                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
#                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "〔 TEAM_TERMUX 〕 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 TEAM_TERMUX 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n\n◯help js\n◯nukeall\n◯bantai: no\n◯sapu: no\n◯#bypass\n◯#cancel\n◯Set js\n◯Set bypass\nTEAM TERMUX\n\n◯TEAM TERMUX", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               sendTemplate(to, data)


                        elif cmd == "ช่วยด้วย":
                          if wait["selfbot"] == True:
                            #
                               contact = cl.getProfile()
                               mids = [contact.mid]
#                               #cover = cl.getProfileCoverURL(sender)
#                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
#                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "〔 TEAM_TERMUX 〕 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 TEAM_TERMUX 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n\n◯help js\n◯nukeall\n◯bantai: no\n◯sapu: no\n◯#bypass\n◯#cancel\n◯Set js\n◯Set bypass\nTEAM TERMUX\n\n◯TEAM TERMUX", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               sendTemplate(to, data)

                                                        
                        elif cmd == "aku" or cmd == "gue":
                          if wait["selfbot"] == True:
                            ##
                                sendMention(msg.to, sender, " User Selfbot \n", "")
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': mid}
                                sendFoter1(msg)
                        elif cmd == "creator" or cmd == "developer":
                          if wait["selfbot"] == True:
                            ##
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                #cover = cl.getProfileCoverURL(sender)
                                time.sleep(1)
                                data = { "type": "flex", "altText": "TEAM TERMUX", "contents":{ "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                                sendTemplate(to, data)
                                                        
                        elif cmd == "randomtiktok":
                          #
                            contact = cl.getContact(sender)
                            time.sleep(1)
                            data = {
                                "type": "video",
                                "originalContentUrl": "https://rest.farzain.com/api/tiktok.php?apikey=fn",
                                "previewImageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                }
                            sendTemplate(to, data)
                            

                        elif cmd.startswith(comd["unsend"]):
                            #
                                sep = text.split(" ")
                                args = text.replace(sep[0] + " ", "")
                                mes = 0
                                try:
                                    mes = int(args[1])
                                except:
                                    mes = 1
                                M = cl.getRecentMessagesV2(to, 101)
                                MId = []
                                for ind, i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == cl.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                                break

                                def unsMes(id):
                                    cl.unsendMessage(id)

                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.start()
                                    thread1.join()
                                sendFoter(to, "pesan di urungkan")       
                                                                                                                                    
                        elif cmd == "tag":
                          ##
                            group = cl.getChats(to)
                            nama = cl.getChatMemberMids(to)
                            nama.remove(cl.getProfile().mid)
                            cl.datamention(to,'Mention',nama)
                                                                                                                                    
                        elif cmd == "mention":
                          #
                            group = cl.getChats(to)
                            midMembers = [contact.mid for contact in group.members]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "「 Mention member 」\n"
                                dataMid = []
                                for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention.mid)
                                    no += 1
                                    ret_ += "\n{}. @!".format(str(no))
                                ret_ += "\n\n「 Jumlah {} member 」".format(str(len(dataMid)))
                                ZulBots(to, ret_, dataMid)    
   
                        elif cmd == comd["tagall"]:
                          #
                            members = []
                            if msg.toType == 1:
                                room = cl.getCompactRoom(to)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = cl.getChats([to], True, False)
                                members = [mem for mem in group.chats[0].extra.groupExtra.memberMids]
                            else:
                                return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                mentionMembers2(to, members)
        
                        elif cmd.startswith("tag: "):
                          #
                            separate = msg.text.split(":")
                            number = msg.text.replace(separate[0] + ":"," ")
                            groups = cl.getAllChatIds()
                            gid = groups[int(number)-1]                                                                                                      
                            members = []
                            if msg.toType == 1:
                                room = cl.getCompactRoom(gid)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = cl.getChats([gid], True, False)
                                members = [mem for mem in group.chats[0].extra.groupExtra.memberMids]
                            else:
                                return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                mentionMembers2(gid, members)
                                cl.sendMessage(msg.to, "Remote Mentions Group: " + str(group.name))      
 
                        elif cmd == "tagall sticker":
                          #
                            members = []
                            if msg.toType == 1:
                                room = cl.getCompactRoom(to)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = cl.getChats(to)
                                members = [mem.mid for mem in group.members]
                            else:
                                return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                FakeStickerV2(to,"11537" ,"52002736", members)
                        elif "https://www.smule.com/p/" in msg.text.lower() or "https://link.smule.com/" in msg.text.lower() or "https://www.smule.com/c/" in msg.text.lower() or "https://www.smule.com/" in msg.text.lower():
                            if wait["rsmule"] == True:
                                time.sleep(0.5)
                                rr1 = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                rr2 = re.findall(rr1, text)
                                roy = []
                                for skbot in rr2:
                                    if skbot not in roy:
                                        roy.append(skbot)
                                        headers = {
                                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/51.0.2704.106",
                                            "Apikey": "Bstm0109"
                                        }
                                for teamsk in roy:
                                    rr3 = teamsk
                                    data = json.loads(requests.get("https://jvrestapi.site/smuledl="+rr3,headers=headers).text)
                                    sk1=data["result"]
                                    skbot = "{}".format(data["result"]["thumbnail"])
                                    skbot2 = "{}".format(data["result"]["mp4Url"])
                                    skbot1 = "{}".format(data["result"]["mp3Url"])
                                    pp = "{}".format(data["result"]["thumbnail"])
                                    roysoak = "╭──[  𝙎𝙢𝙪𝙡𝙚 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙..♪♪"
                                    roysoak += "\n├• S𝙢𝙪𝙡𝙚-𝙞𝙙 : "+str(sk1["username"])
                                    roysoak += "\n├• J𝙪𝙙𝙪𝙇 : "+str(sk1["title"])
                                    roysoak += "\n├• T𝘆𝗽𝗘 : "+str(sk1["type"])
                                    roysoak += "\n├• 𝘿𝙞𝙗𝙪𝙖𝙩 : "+str(sk1["created"])
                                    roysoak += "\n├• 𝘿𝙞𝙥𝙪𝙩𝙖𝙧 : "+str(sk1["listens"])
                                    roysoak += "\n├• 𝘿𝙚𝙨𝙠𝙧𝙞𝙥𝙨𝙞 : "+str(sk1["caption"])                                                                   
                                    roysoak += "\n╰──[ ˚TEAM TERMUX♪]"                                    
                                    soak = {     
                                        "type": "flex",
                                        "altText": "TEAM TERMUX",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "animated": True,
            "url": "https://i.ibb.co.com/kcxnLKc/ezgif-com-gif-maker.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:2",
            "gravity": "top",
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/8nYJYLXR/1746508782571.jpg",
                "size": "full",
                "aspectRatio": "4:2",
                "aspectMode": "cover"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "animated": True,
                        "url": "https://i.ibb.co.com/JBGDynS/ezgif-com-gif-maker-3.png",
                        "size": "xs",
                        "aspectRatio": "8:2",
                        "aspectMode": "cover",
                        "offsetStart": "-44px"
                      }
                    ],
                    "position": "absolute",
                    "width": "158px",
                    "height": "20px",
                    "offsetTop": "64px",
                    "offsetStart": "0px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "animated": True,
                        "url": "https://i.ibb.co.com/JBGDynS/ezgif-com-gif-maker-3.png",
                        "size": "xs",
                        "aspectRatio": "8:2",
                        "aspectMode": "cover",
                        "offsetStart": "25px"
                      }
                    ],
                    "position": "absolute",
                    "width": "158px",
                    "height": "20px",
                    "offsetTop": "64px",
                    "offsetStart": "20px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "position": "absolute",
                    "width": "158px",
                    "height": "90px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "𝙎𝙢𝙪𝙡𝙚-𝙞𝙙 : "+str(sk1["username"]),
                        "size": "xxs",
                        "color": "#ffffff",
                        "weight": "bold",
                        "offsetStart": "2px"
                      },
                      {
                        "type": "text",
                        "text": "𝙅𝙪𝙙𝙪𝙇 : "+str(sk1["title"]),
                        "size": "xxs",
                        "color": "#ffffff",
                        "weight": "bold",
                        "offsetStart": "2px"
                      },
                      {
                        "type": "text",
                        "text": "𝗧𝘆𝗽e : "+str(sk1["type"]),
                        "size": "xxs",
                        "weight": "bold",
                        "offsetStart": "2px",
                        "color": "#ffffff", 
                        "color": "#ffffff"
                      },
                      {
                        "type": "text",
                        "text": "creativ desaint zul ",
                        "size": "xxs",
                        "weight": "bold",
                        "style": "italic",
                        "offsetTop": "24px",
                        "offsetStart": "20px"
                      }
                    ],
                    "position": "absolute",
                    "width": "158px",
                    "height": "80px",
                    "offsetTop": "0px",
                    "offsetStart": "0px"
                  }
                ],
                "position": "absolute",
                "width": "158px",
                "height": "85px",
                "backgroundColor": "#000000",
                "offsetTop": "75px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": pp,
                    "size": "full",
                    "aspectRatio": "2:2",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "30px",
                "height": "30px",
                "borderWidth": "1px",
                "borderColor": "#00ff00",
                "offsetTop": "1px",
                "offsetStart": "2px",
                "cornerRadius": "5px"
              }
            ],
            "position": "absolute",
            "width": "158px",
            "height": "158px",
            "borderWidth": "1px",
            "borderColor": "#00ff00",
            "cornerRadius": "10px",
            "offsetTop": "1px",
            "offsetStart": "1px"
          }
        ],
        "paddingAll": "0px"
      },
      "action": {
        "type": "uri",
        "label": "action",
        "uri": "http://line.me/ti/p/~zul.1.02",
      }
    }
  ]
}
}
                                    sendTemplate(msg.to,soak)                                                                   
                                    time.sleep(0.5)
                                    if "video" in data["result"]["type"]:
                                        sendFlexVid2025(to, skbot2, pp)
                                        sendFlexAudio(to,data["result"]["mp3Url"])
                                    else:
                                        sendFlexAudio(to,data["result"]["mp3Url"])
                        
                        elif "https://www.tiktok.com/" in msg.text.lower() or 'https://vt.tiktok.com/' in msg.text.lower():
                            if wait["tiktok"] == True:
                                regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                links = re.findall(regex, text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for Ticket_id in n_links:
                                    link = Ticket_id
                                    url = f"https://jvrestapi.site/tiktokdl={link}"
                                    apikey = {
                                        "Apikey": "Bstm0109",
                                        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/51.0.2704.106"
                                    }
                                    response = requests.get(url, headers=apikey)
                                    data = response.json()
                                    pp = "{}".format(data["result"]["thumbnail"])
                                    video = "{}".format(data["result"]["vid_nowatermark"])                                    
                                    result = "╭──[  𝗥𝗲𝘀𝗽𝗼𝗻 𝗟𝗶𝗻𝗸 𝗧𝗶𝗸𝘁𝗼𝗸 ♪"
                                    result += "\n├• User-ID  : {}".format(data["result"]["username"])
                                    result += "\n├• Music  : {}".format(data["result"]["music"])
                                    result += "\n├• Play : {}".format(data["result"]["play_count"])
                                    result += "\n├• Share : {}".format(data["result"]["share_count"])
                                    result += "\n├• Comment : {}".format(data["result"]["comment_count"])                                   
                                    result += "\n╰──[ TEAM TERMUX ]"
                                    soak = {                                                                        
                                       "type": "flex",
                                       "altText": "TEAM TERMUX", 
                                       "contents":
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co.com/HBRGznW/ezgif-com-gif-to-apng.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "animated": True,
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "TIK TOK ",
                    "size": "xxs",
                    "color": "#ff0000",
                    "weight": "bold",
                    "style": "italic",
                    "offsetTop": "2px",
                    "offsetStart": "35px"
                  }
                ],
                "position": "absolute",
                "width": "116px",
                "height": "20px",
                "borderWidth": "1px",
                "borderColor": "#ffff00"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg",
                    "size": "full",
                    "aspectRatio": "2:2",
                    "aspectMode": "cover",
                    "animated": True,
                  }
                ],
                "position": "absolute",
                "width": "5px",
                "height": "5px",
                "cornerRadius": "100px",
                "offsetTop": "4px",
                "offsetEnd": "4px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": pp,
                    "size": "full",
                    "aspectRatio": "2:2",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "116px",
                "height": "116px",
                "offsetTop": "20px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "♻️User-ID : {}".format(data["result"]["username"]),
                    "size": "5px",
                    "color": "#ffffff",
                    "weight": "bold",
                    "style": "italic",
                    "offsetTop": "2px",
                    "offsetStart": "2px"
                  },
                  {
                    "type": "text",
                    "text": "♻️Play : {}".format(data["result"]["play_count"]),
                    "size": "5px",
                    "color": "#ffffff",
                    "weight": "bold",
                    "style": "italic",
                    "offsetTop": "2px",
                    "offsetStart": "2px"
                  },
                  {
                    "type": "text",
                    "text": "♻️Share : {}".format(data["result"]["share_count"]), 
                    "size": "5px",
                    "color": "#ffffff",
                    "weight": "bold",
                    "style": "italic",
                    "offsetTop": "2px",
                    "offsetStart": "2px"
                  },
                  {
                    "type": "text",
                    "text": "♻️Music : {}".format(data["result"]["music"]),
                    "size": "5px",
                    "color": "#ffffff",
                    "weight": "bold",
                    "style": "italic",
                    "offsetTop": "2px",
                    "offsetStart": "2px"
                  }
                ],
                "position": "absolute",
                "width": "116px",
                "height": "60px",
                "backgroundColor": "#000000",
                "borderWidth": "1px",
                "borderColor": "#ffff00",
                "offsetTop": "134px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co.com/0th6341/ezgif-com-gif-to-apng-3.png",
                    "size": "full",
                    "aspectRatio": "2:2",
                    "aspectMode": "cover",
                    "animated": True,
                  }
                ],
                "position": "absolute",
                "width": "10px",
                "height": "10px",
                "borderWidth": "1px",
                "borderColor": "#ffff00",
                "offsetTop": "5px",
                "offsetStart": "20px"
              }
            ],
            "position": "absolute",
            "width": "116px",
            "height": "176px",
            "backgroundColor": "#ffffff",
            "borderWidth": "1px",
            "borderColor": "#ffff00",
            "cornerRadius": "10px",
            "offsetTop": "2px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px"
      },
      "action": {
        "type": "uri",
        "label": "action",
        "uri": "http://line.me/ti/p/~zul.1.02",
      }
    }
  ]
}
}
                                    time.sleep(0.5)
                                    sendTemplate(to, soak)
                                    #cl.sendReplyMessage(msg.id, to,(result))
                                    sendFlexVid2024(to, video, pp)
                                    time.sleep(0.5)                
                        elif "youtu.be" in text.lower() or "https://youtube.com/shorts" in text.lower() or "https://youtu.be" in msg.text.lower():
                            if wait["ytube"] == True:
                                try:
#                                    url = re.search("(?P<url>https?://[^\s]+)", text).group("url")
                                    host = "https://jvrestapi.site/youtubedl=" + url
                                    headers  =  {
                                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/51.0.2704.106",
                                        "Apikey": "Bstm0109"
                                    }
                                    data   =  requests.get(host, headers=headers).json()                          
                                    pict = "https://i.ibb.co.com/cbH5wDy/pngwing-com-2.png"     
                                    page = str(data["result"]["pageUrl"])
                                    thumb = "https://i.ytimg.com/vi/{}/hq720.jpg".format(page.split("/youtu.be/")[1])
                                    desk = str(data["result"]["title"])
                                    type = str(data["result"]["duration"])
                                    ids = str(data["result"]["author"])
                                    video = data["result"]["videoUrl"]  
                                    audio = data["result"]["audioUrl"]                
                                    soak =  {                                                                                                               
                                      "type": "flex",
                                       "altText": "TEAM TERMUX",
                                       "contents":
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip1.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg",
                "size": "full",
                "aspectMode": "cover",
                "animated": True,
                "aspectRatio": "6:1",
                "offsetBottom": "2px"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "backgroundColor": "#ffffff",
            "borderWidth": "1px",
            "borderColor": "#000000",
            "width": "120px",
            "offsetTop": "14px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/4W6bPg9/ezgif-com-gif-to-apng.png",
                "size": "full",
                "aspectRatio": "6:1",
                "aspectMode": "cover",
                "animated": True,
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "120px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/HPjSHBf/ezgif-com-gif-to-apng-1.png",
                "size": "full",
                "aspectRatio": "2:2",
                "aspectMode": "cover",
                "animated": True,
              }
            ],
            "position": "absolute",
            "width": "3px",
            "height": "3px",
            "cornerRadius": "100px",
            "offsetStart": "4px",
            "offsetTop": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ ᴠɪᴅᴇᴏ ʏᴛᴜʙᴇ",
                "size": "6px",
                "color": "#ffffff",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "120px",
            "height": "10px",
            "offsetTop": "5px",
            "offsetStart": "18px"
          }
        ],
        "paddingAll": "0px",
        "height": "30px",
        "cornerRadius": "10px",
        "borderWidth": "1px",
        "borderColor": "#000000"
      },
      "action": {
        "type": "uri",
        "label": "action",
        "uri": "http://line.me/ti/p/~zul.1.02",
      }
    }
  ]
}
}
                                    time.sleep(0.5)
                                    sendTemplate(to, soak)
                                    #cl.sendReplyMessage(msg.id, to,(wowo))
                                    sendFlexVid2026(to, video, thumb)
                                    sendFlexAudio(to, audio) 
                                    time.sleep(0.5)
                                except Exception as error:
                                    cl.sendMessage(msg.to, str(error))
                        

                        elif cmd.startswith("joox"):
                            try:
                                x = text.split(" ")
                                y = text.replace(x[0] + " ","")
                                r=requests.get("https://api.chstore.me/joox?search=joox_query={}".format(str(y)))
                                data=r.text
                                data=json.loads(data)
                                ret_ = " Joox music \n"
                                ret_ += "\nArtis : {}".format(str(data["result"][0]["artist"]))
                                ret_ += "\nJudul: {}".format(str(data["result"][0]["title"]))
                                modflex(to, str(ret_))
                                cl.farelsendAudio(to, str(data["result"][0]["mp3Url"]))
                            except Exception as e:
                                print (error)
#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            #
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendFoter (msg.to,"Send a Picture ♪")
                                
                        elif cmd == "updatecover":
                          if wait["selfbot"] == True:
                            #
                                settings["changeCover"][clMID] = True
                                sendFoter(msg.to,"Send a Picture ♪")

                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            #
                                wait["changeFoto"][clMID] = True
                                sendFoter(msg.to,"Send a Picture ♪")
                                                             
                        elif cmd.startswith(".myname: "):
                          #
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendFoter(msg.id,to,"Update to " + string + "")

                        elif text.startswith("myname: "):
                            #
                              separate = msg.text.split(" ")
                              string = msg.text.replace(separate[0] + " ","")
                              if len(string) <= 10000000000:
                                  profile = cl.getProfile()
                                  profile.displayName = string
                                  cl.updateProfile(profile)
                                  sendFoter(msg.to,"Nama diganti jadi " + string + "")


                        elif cmd.startswith("cek "):
                          #
                            separate = msg.text.split(" ")
                            mid = msg.text.replace(separate[0] + " ","")
                            if mid is not None:
                                listMid = mid.split("*")
                                if len(listMid) > 1:
                                    for a in listMid:
                                        cl.sendContact(to,a)
                                else:
                                    cl.sendContact(to,mid)

                        elif cmd.startswith("stag"):
                            #
                                gname = cl.getChats(msg.to)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n╭───────────────\n│Mention {} '.format(str(gname.name))
                                            atas += '\n│Total {} Members\n╰───────────────'.format(str(len(local)))
                                        sendFoter(to, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    sendFoter(to, str(error)) 

                        elif cmd.startswith("addtext "):
                            #
                                sep = text.split(" ")
                                apl = text.replace(sep[0] + " ","")
                                sam = apl.split("/")
                                chat1 = sam[0]
                                chat2 = sam[1]
                                apk = ""+chat1
                                tes["Message"][apk] = chat2
                                tes["msg"] = chat1
                                anu = tes["msg"]+'.'
                                cl.sendReplyMessage(msg.id,to,"Command %s created."%chat1)
                                tes["msg"] = {}

                        elif cmd == "list text":
                            #
                                if tes["Message"] == {}:
                                    sendFoter(to,"empty text")
                                else:
                                    mc = ""
                                    jml = 1
                                    for listword in tes["Message"]:
                                        mc += "\n"+str(jml)+". "+listword+""
                                        jml += 1
                                    cl.sendResplyMessage(msg.id,to, "List text :\n"+str(mc))

                        elif cmd.startswith("deltext "):
                            	#
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in tes["Message"]:
                                        del tes["Message"][xres]                                        
                                        cl.sendReplyMessage(msg.id,to,"Command %s has been removed."%tetx)
                                    else:
                                        cl.sendReplyMessage(msg.id,to,"Command %s does not exist."%tetx)
                            
                        elif cmd == "screen -ls":
                          #
                              process = os.popen('screen -list')
                              a = process.read()
                              sendFoter(to, "{}".format(a))
                              process.close()

                        elif cmd == "myname":
                          #
                            h = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id,to,"「 Name 」\n"+str(h.displayName))


                        elif cmd == "kibar":
                          if wait["selfbot"] == True:
                            ###if msg._from in admin:
                               #cl.sendContact(to, mid)
                               cl.sendMessage(msg.to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ᴀꜱꜱᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ\n"
"  ╭━T✒E✒A✒M✒Z✒U✒L\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HLO▪┃KMI DTANG LGI┃\n"
"  ┗Ⓑ┻┻ⓞ━━Ⓣ┻┻Ⓢ━╯\n"
"ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜꜱᴜʀ\nʀᴏᴏᴍ ᴋᴀʟɪᴀɴ\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"🖕━━━━━━━━━━━━━🖕\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"🖕━━━━━━━━━━━━━🖕\n"        
"TEAM TERMUX\n ⓢⓟⓔⓔⓓ ⓑⓞⓣⓢ\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
"><Ⓕⓤⓒⓚ ⓐⓝⓙⓘⓝⓖ ><\n><Ⓜⓨ ⓒⓡⓔⓐⓣⓞⓡ><\n")
                               cl.sendMessage(to, "OWNER TEAM TERMUX FAMILIY")
                               cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")
                               cl.sendContact(to, "ub3a4144fd62686316824b3e1c39a5f04")
                               cl.sendContact(to, "u9aa1500e7383f6c22fa9220cfe9784ce")
                               #cl.sendContact(to, "u4bf02fa0f10b66844ce3daf390e984d2")
                               #cl.sendContact(to, "ud97cb23f659bc57bdc14b090569c7904")
                               #cl.sendContact(to, "u862ad072aceb7ce6009fb175e386a566")
                               #cl.sendContact(to, "u01b2583b98a923a9e91dffd86877842f")
                               #cl.sendContact(to, "u02913d0c3f45eb23aa4f586fd6f6c62b")
                               #cl.sendContact(to, "u3068a0b6958068c9c3002ae5d9cc9a33")
                               #cl.sendContact(to, "uef44eba9bf0ba2cdfdd64135241a59a9")
                               #cl.sendContact(to, "u63576cdc20dbb3c978b41d3a593ca70b")
                               #cl.sendContact(to, "u9bef22a6f6ee633bdf4dddd6572dcd3f")
                            
                        elif cmd == "mybio":
                          #
                            h = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id,to,"「 Status 」\n"+str(h.statusMessage))
                            
                        elif cmd == "mypict":
                          #
                            h = cl.getContact(sender)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            cl.sendReplyMessage(msg.id,to, image)     

                        elif cmd == "myvideo":
                          #
                            h = cl.getContact(sender)
                            if h.videoProfile == None:
                            	return sendFoter(to, "「 Video 」\nNone")
                            cl.sendVideo(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")       
#===========BOT UPDATE============#                                                     
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            #
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n│"
                                sendFoter(msg.to,"╭─「 User botlist」\n│\n│"+ma+"\n╰──「 Total「%s」User Botlist 」" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            #
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n│"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n│'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n│"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n│'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n│"
                                sendFoter(msg.to,"╭─「 List Admin Selfbot 」\n│\n│Owner:\n│"+ma+"\n│Admin:\n│"+mb+"\n│Staff:\n│"+mc+"\n╰──「Total「%s」Team 」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            #
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getChats(group).name + "\n│"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n│'
                                    mb += str(b) + ". " +cl.getChats(group).name + "\n│"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n│'
                                    md += str(d) + ". " +cl.getChats(group).name + "\n│"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n│'
                                    mc += str(c) + ". " +cl.getChats(group).name + "\n│"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n│'
                                    me += str(e) + ". " +cl.getChats(group).name + "\n"
                                sendFoter(msg.to,"╭─「 Setting Protection List 」\n│\n│ PROTECT URL :\n│"+ma+"\n│ PROTECT KICK :\n│"+mb+"\n│ PROTECT JOIN :\n│"+md+"\n│ PROTECT CANCEL:\n│"+mc+"\n│ PROTECT INVITE:\n│"+me+"\n╰──「 Total「%s」Protect 」" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))


                        elif cmd == comd["bye"]:
                          if wait["selfbot"] == True:
                            #
                                G = cl.getChats(msg.to)
                                sendFoter(msg.to, "Selamat Tinggall..")
                                cl.deleteSelfFromChat(msg.to)

                        elif cmd == "respontime":
                          if wait["selfbot"] == True:
                            #
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getAllChatIds()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendFoter(msg.to, "「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == comd["speed"]:
                          if wait["selfbot"] == True:
                            #
                                start = time.time()
                                elapsed_time = time.time() - start
                                sendFoter(msg.to,"...{}detik".format(str(elapsed_time)))
                                  
                             
                        elif cmd == comd["yasinon"]:
                          if wait["selfbot"] == True:
                           #
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendFoter(msg.to, "Sider yasin Enable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv4['point'][msg.to]
                                  del cctv4['sidermem'][msg.to]
                                  del cctv4['cyduk'][msg.to]
                              except:
                                  pass
                              cctv4['point'][msg.to] = msg.id
                              cctv4['sidermem'][msg.to] = ""
                              cctv4['cyduk'][msg.to]=True
                              cctv['cyduk'][msg.to]=False
                              cctv1['cyduk1'][msg.to]=False

                        elif cmd == comd["yasinoff"]:
                          if wait["selfbot"] == True:
                           #
                              if msg.to in cctv4['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv4['cyduk'][msg.to]=False
                                  sendFoter(msg.to, "Sider yasin Disable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendFoter(msg.to, "None Active..!!")                             
                                                               
                        elif cmd == comd["sider1On"]:
                          if wait["selfbot"] == True:
                           #
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendFoter(msg.to, "Sider1 Enable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv1['point1'][msg.to]
                                  del cctv1['sidermem1'][msg.to]
                                  del cctv1['cyduk1'][msg.to]
                              except:
                                  pass
                              cctv1['point1'][msg.to] = msg.id
                              cctv1['sidermem1'][msg.to] = ""
                              cctv1['cyduk1'][msg.to]=True
                              cctv['cyduk'][msg.to]=False
                              cctv4['cyduk'][msg.to]=False

                        elif cmd == comd["sider1Off"]:
                          if wait["selfbot"] == True:
                           #
                              if msg.to in cctv1['point1']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv1['cyduk1'][msg.to]=False
                                  sendFoter(msg.to, "Sider1 Disable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendFoter(msg.to, "None Active..!!")
 
#sider 1 dan 2                                                              
                        elif cmd == comd["siderOn"]:
                          if wait["selfbot"] == True:
                           ##
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendFoter(msg.to, "Sider Enable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
                              cctv4['cyduk'][msg.to]=False
                              cctv1['cyduk1'][msg.to]=False

                        elif cmd == comd["siderOff"]:
                          if wait["selfbot"] == True:
                           ##
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendFoter(msg.to, "Sider Disable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendFoter(msg.to, "None Active..!!")
                             
#sider tai
                        elif cmd == comd["ซีรอน"]:
                          if wait["selfbot"] == True:
                           ##
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendFoter(msg.to, "Sider Enable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
                              cctv4['cyduk'][msg.to]=False
                              cctv1['cyduk1'][msg.to]=False

                        elif cmd == comd["ไซด์โรฟ"]:
                          if wait["selfbot"] == True:
                           ##
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendFoter(msg.to, "Sider Disable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendFoter(msg.to, "None Active..!!")

                                                              
                        elif cmd.startswith("tag "):
                          #
                            text = removeCmd("tag", text)
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ", text)
                            cond = text.split(" ")
                            jml = int(cond[0])
                            for x in range(jml):
                                name = cl.getContact(to)
                                ZulKiller(to, name.mid)
                                
                        elif cmd.startswith("spam "):
                          #
                            dzin = removeCmd("spam", text)
                            line = dzin.split("|")
                            count = int(line[1])
                            text1 = removeCmd("spam"+str(line[0])+"|"+str(count)+"|", text)
                            text2 = count * (text1+"\n")
                            if line[0] == "on":
                                if count <= 1000:
                                    for a in range(count):
                                        sendFoter(msg.to, str(text1))
                                else:
                                    sendFoter(msg.to, "Max 1000.")
                            if line[0] == "off":
                                if count <= 1000:
                                    sendFoter(msg.to, str(text2))
                                else:
                                    sendFoter(msg.to, "Max 1000.")
                            
                        elif cmd.startswith('github '):
                          #
                           args = text.split(" ")
                           search = text.replace(args[0] + " ","")
                           kontol = requests.get("http://dolphinapi.herokuapp.com/api/github?name={}".format(search))
                           data = kontol.text
                           data = json.loads(data)
                           kontol = "GITHUB SEARCH"
                           for b in data["result"]["repository"]:
                               kontol += "\n•{} \n{}".format(str(b["title"]), str(b["url"]))
                           kontol += "GITHUB SEARCH"
                           cl.sendReplyMessage(msg.id,to, str(kontol))

                        elif cmd == "cctv code":
                          #
                           api = imjustgood(wait["apikey"])
                           data = api.cctv_code()
                           kontol = "RESULT CCTV"
                           for b in data["result"]["active"]:
                               kontol += "\n• {} {}".format(b,data["result"]["active"][b])
                           kontol += "{}\nExample : Cctv (number)"
                           sendFoter(msg.to, str(kontol))
                        elif cmd.startswith('cctv '):
                          #
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.cctvSearch(userId)
                                  kontol = "DETAIL CCTV INFO"
                                  kontol += "\nArea : {}".format(data["result"]["area"])
                                  kontol += "\nWilayah : {}".format(data["result"]["wilayah"])
                                  sendFoter(msg.to, str(kontol))
                                  time.sleep(1)
                                  sendFlexVideo(to, "{}".format(data["result"]["video"]))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith('lyrik '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.lyric(userId)
                           vian = "Title : {}".format(data["result"]["title"])
                           vian += "\nArtist : {}".format(data["result"]["artist"])
                           vian += "\n{}".format(data["result"]["lyric"])
                           cl.sendReplyMessage(msg.id,to, str(vian))         

                        elif cmd == "clearallfriend":
                          #
                            n = len(cl.getAllContactIds())
                            try:
                                cl.clearContacts()
                            except: 
                                pass
                            t = len(cl.getAllContactIds())
                            sendFoter(msg.to,"Type: Friendlist\n • Detail: Clear Contact\n • Before: %s Friendlist\n • After: %s Friendlist\n • Total removed: %s Friendlist\n • Status: Succes.."%(n,t,(n-t)))
#===========Hiburan============#
                        elif cmd.startswith("eng:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('en', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("indo:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('id', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jp:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ja', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("india:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('hi', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("sunda:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('su', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("china:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('zh-cn', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("arab:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ar', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("rusia:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ru', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("thai:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('th', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("spanyol:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('es', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("franchis:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('fr', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("korea:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ko', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("malay:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ms', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("turki:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('tr', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jawa:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('jw', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("itali:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('it', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("belanda:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('nl', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("filipin:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('tl', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("german:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('de', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("vietnam:"):
                          #
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('vi', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("joox:"):
                           #
                                set = text.split(" ")
                                userId = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.joox(userId)
                                title = "{}".format(data["result"]["title"])
                                durasi = "{}".format(data["result"]["duration"])
                                artis = "{}".format(data["result"]["singer"])
                                size = "{}".format(data["result"]["size"])
                                img = "{}".format(data["result"]["thumbnail"])
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                time.sleep(1)
                                KONTOL = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(artis), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                                sendTemplate(to, KONTOL)  
                                sendFlexAudio(to, "{}".format(data["result"]["mp3Url"]))

                        elif cmd.startswith('ytmp3 '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api  = imjustgood(wait["apikey"])
                           data = api.youtube(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           autor = "{}".format(data["result"]["author"])
                           audio = "{}".format(data["result"]["audioUrl"])
                           durasi = "Durasi : {}".format(data["result"]["duration"])
                           img = "{}".format(data["result"]["thumbnail"])
                           title = "{}".format(data["result"]["title"])
                           wath = "{}".format(data["result"]["watched"])
                           time.sleep(1)
                           KONTOL = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(autor), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                           sendTemplate(to, KONTOL)         
                           sendFlexAudio(to, "{}".format(data["result"]["audioUrl"]))

                        elif cmd.startswith('porn '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api  = imjustgood(wait["apikey"])
                           data = api.porn(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           durasi = "Durasi : {}".format(data["result"]["duration"])
                           quality = "Quality : {}".format(data["result"]["quality"])
                           img = "{}".format(data["result"]["thumbnail"])
                           title = "{}".format(data["result"]["title"])
                           wath = "{}".format(data["result"]["watched"])
                           time.sleep(1)
                           KONTOL = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(quality), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                           sendTemplate(to, KONTOL)         
                           sendFlexVideo(to, "{}".format(data["result"]["videoUrl"]))

                        elif cmd.startswith('ytmp4 '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api  = imjustgood(wait["apikey"])
                           data = api.youtube(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           autor = "{}".format(data["result"]["author"])
                           audio = "{}".format(data["result"]["audioUrl"])
                           durasi = "Durasi : {}".format(data["result"]["duration"])
                           img = "{}".format(data["result"]["thumbnail"])
                           title = "{}".format(data["result"]["title"])
                           wath = "{}".format(data["result"]["watched"])
                           time.sleep(1)
                           KONTOL = { "type": "flex", "altText": "TEAM TERMUX", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(autor), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u9b0ae88d7cf669da9a8416bd4c765cd1" } } }
                           sendTemplate(to, KONTOL)         
                           sendFlexVideo(to, "{}".format(data["result"]["videoUrl"]))

                        elif cmd.startswith('cuaca '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.cuaca(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           kontol = "╭───「 INFO CUACA 」───"
                           kontol += "\n├⌬ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')
                           kontol += "\n├⌬ Tanggal : "+datetime.strftime(timeNow,'%d-%m-%Y')
                           kontol += "\n├⌬ Lokasi : {}".format(data["result"]["location"])
                           kontol += "\n├⌬ Cuaca : {}".format(data["result"]["description"])
                           kontol += "\n├⌬ Suhu : {}".format(data["result"]["humidity"])
                           kontol += "\n├⌬ Tempratur : {}".format(data["result"]["temperature"])
                           kontol += "\n├⌬ Angin : {}".format(data["result"]["wind"])
                           kontol += "\n╰───────────────"         
                           sendFoter(msg.to, str(kontol))

                        elif cmd.startswith('sholat '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.adzan(userId)
                           kontol = "╭───「 INFO SHOLAT 」───"
                           kontol += "\n├⌬ Date : {}".format(data["result"]["tanggal"])
                           kontol += "\n├⌬ Wilayah : {}".format(data["result"]["wilayah"])
                           kontol += "\n├⌬ Ashar : {}".format(data["result"]["adzan"]["ashar"])
                           kontol += "\n├⌬ Duha : {}".format(data["result"]["adzan"]["dhuha"])
                           kontol += "\n├⌬ Dzuhur : {}".format(data["result"]["adzan"]["dzuhur"])
                           kontol += "\n├⌬ Imsyak : {}".format(data["result"]["adzan"]["imsyak"])
                           kontol += "\n├⌬ Isya : {}".format(data["result"]["adzan"]["isya"])
                           kontol += "\n├⌬ Mag'rib : {}".format(data["result"]["adzan"]["maghrib"])
                           kontol += "\n├⌬ Subuh : {}".format(data["result"]["adzan"]["subuh"])
                           kontol += "\n├⌬ Fajar : {}".format(data["result"]["adzan"]["terbit"])
                           kontol += "\n╰────────────────"         
                           sendFoter(msg.to, str(kontol))       

                        elif cmd == "corona":
                          #
                           api = imjustgood(wait["apikey"])
                           data = api.corona()
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           kontol = "╭──「 CORONA VIRUS 」──"
                           kontol += "\n├⌬ TIME : "+datetime.strftime(timeNow,'%H:%M:%S')
                           kontol += "\n├⌬ DATE : {}".format(data["result"]["date"])
                           kontol += "\n├⌬─────────────⌬"
                           kontol += "\n├⌬ INDONESIA"
                           kontol += "\n├⌬ TERJANGKIT : {}".format(data["result"]["indonesia"]["case"])
                           kontol += "\n├⌬ SEMBUH : {}".format(data["result"]["indonesia"]["fit"])
                           kontol += "\n├⌬ MENINGGAL : {}".format(data["result"]["indonesia"]["rip"])
                           kontol += "\n├⌬─────────────⌬"
                           kontol += "\n├⌬ SELURUH DUNIA"
                           kontol += "\n├⌬ TERJANGKIT : {}".format(data["result"]["world"]["case"])
                           kontol += "\n├⌬ SEMBUH : {}".format(data["result"]["world"]["fit"])
                           kontol += "\n├⌬ MENINGGAL : {}".format(data["result"]["world"]["rip"])
                           kontol += "\n╰────────────────"         
                           sendFoter(msg.to, str(kontol))        

                        elif cmd == "surahlist":
                          #
                           api = imjustgood(wait["apikey"])
                           data = api.alquran()
                           vian  = "LIST SURAH AL-QUR'AN"
                           for qs in data:
                               vian += "\n{}".format(qs)
                           sendFoter(to, str(vian))

                        elif cmd.startswith('surah '):
                          #
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.alquranQS(userId) 
                                  audioUrl = data["result"]["audio"]
                                  vian = "Di Turunkan Di :{}\n".format(data["result"]["place"])
                                  vian += "{}".format(data["result"]["desc"])
                                  cl.sendReplyMessage(msg.id,to, (vian))
                                  sendFoterAudio(to, str(audioUrl))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, "ERROR!\nText Terlalu Panjang!!")         

                        elif cmd == "info bmkg":
                          #
                           api = imjustgood(wait["apikey"])
                           data = api.bmkg()
                           kontol = "╭──「 INFO BMKG 」──"
                           kontol += "\n├⌬ Time : {}".format(data["result"]["pukul"])
                           kontol += "\n├⌬ Date : {}".format(data["result"]["tanggal"])
                           kontol += "\n├⌬ Wilayah : {}".format(data["result"]["wilayah"])
                           kontol += "\n├⌬ Kekuatan : {}".format(data["result"]["kekuatan"])
                           kontol += "\n├⌬ Kedalaman : {}".format(data["result"]["kedalaman"])
                           kontol += "\n├⌬ Kordinat : {}".format(data["result"]["kordinat"])
                           kontol += "\n├⌬ Lokasi : {}".format(data["result"]["lokasi"])
                           kontol += "\n├⌬ Arhan : {}".format(data["result"]["arahan"])
                           kontol += "\n├⌬ Saran : {}".format(data["result"]["saran"])
                           kontol += "\n╰─────────────"         
                           sendFoter(msg.to, str(kontol))        

                        elif cmd.startswith('fancytext '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.fancy(userId) 
                           vian = "FANCY RESULT :\n"
                           for s in data["result"]:
                               vian += "\n{}\n".format(s)
                           cl.sendReplyMessage(msg.id,to, str(vian))         

                        elif cmd.startswith('acaratv '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.acaratv_channel(userId) 
                           vian = "Jadwal Acara TV"
                           for a in data["result"]:
                               vian += "\n{}".format(a)
                           sendFoter(msg.to, str(vian))    

                        elif cmd == "acara tv":
                          #
                           api = imjustgood(wait["apikey"])
                           data   = api.acaratv()
                           result = "ACARA TV"
                           for a in data["result"]:
                               for b in a:
                                   result += "\n\nChannel : {}".format(b)
                                   for c in a[b]:
                                       result += "\n{}".format(c)
                           sendFoter(msg.to, str(result))      

                        elif cmd == "info loker":
                          #
                           api = imjustgood(wait["apikey"])
                           data   = api.karir()
                           number = 0
                           apkbot = "INFO LOWONGAN KERJA"
                           for a in data["result"]:
                               number += 1
                               apkbot += "\n\n{}. {}".format(number,a["perusahaan"])
                               apkbot += "\nLokasi : {}".format(a["lokasi"])
                               apkbot += "\nProfesi : {}".format(a["profesi"])
                               apkbot += "\nBagian : {}".format(a["bagian"])
                               apkbot += "\nJabatan : {}".format(a["jabatan"])
                               apkbot += "\nGaji : {}".format(a["gaji"])
                               apkbot += "\nPendidikan : {}".format(a["pendidikan"])
                               apkbot += "\nPengalaman : {}".format(a["pengalaman"])
                               apkbot += "\nSyarat : {}".format(a["syarat"])
                               apkbot += "\nDeskirpsi : {}".format(a["deskripsi"])
                               apkbot += "\nSumber : {}".format(a["sumber"])
                           cl.sendReplyMessage(msg.id,to, str(apkbot))     

                        elif cmd.startswith("zodiak"):
                            #
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.zodiac(search)
                                vian = "╭─── • ZODIAK • ──"
                                vian += "\n├≽ Sign : {}".format(data["result"]["zodiac"])
                                vian += "\n├≽ Couple : {}".format(data["result"]["couple"])
                                vian += "\n├≽ Date Range : {}".format(data["result"]["date"])
                                vian += "\n├≽ Lucky Color : {}".format(data["result"]["color"])
                                vian += "\n├≽ Lucky Time : {}".format(data["result"]["time"])
                                vian += "\n├≽ Lucky Number : {}".format(data["result"]["number"])
                                vian += "\n├≽ Public : {}".format(data["result"]["public"])
                                vian += "\n├≽ Money : {}".format(data["result"]["money"])
                                vian += "\n├≽ Love Couple : {}".format(data["result"]["love"]["couple"])
                                vian += "\n├≽ Love Single : {}".format(data["result"]["love"]["single"])
                                vian += "\n╰── • TM_BOTS • ──"
                                cl.sendReplyMessage(msg.id,to, str(vian)) 

                        elif cmd.startswith('instagram '):
                          #
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.instagram(userId) 
                                  user = "{}".format(data["result"]["username"])
                                  folwer = "{}".format(data["result"]["follower"])
                                  folwing = "{}".format(data["result"]["following"])
                                  post = "{}".format(data["result"]["post"])
                                  bio = "{}".format(data["result"]["biography"])
                                  pict = "{}".format(data["result"]["picture"])
                                  INSTA = {"type": "flex","altText": "TEAM_TERMUX","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co.com/vz3vV2G/ezgif-com-gif-maker-16.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(pict), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "102px", "height": "102px", "offsetTop": "20px", "offsetStart": "29px" }, { "type": "image", "url": "https://i.ibb.co.com/rfj2q51/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(user), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "113px", "height": "10px", "offsetTop": "7px", "offsetStart": "24px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(folwer), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "90px", "height": "10px", "offsetTop": "127px", "offsetStart": "35px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(folwing), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "90px", "height": "10px", "offsetTop": "142px", "offsetStart": "35px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(post), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "90px", "height": "10px", "offsetTop": "156px", "offsetStart": "35px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(bio), "size": "7px", "color": "#00ff00", "wrap": True, "align": "center" } ], "position": "absolute", "width": "130px", "height": "30px", "offsetBottom": "16px", "offsetStart": "15px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u1c5233bdc0da4800d07131656e106068" } } }
                                  sendTemplate(to, INSTA)           
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to,str(error))

                        elif cmd.startswith('google '):
                          #
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.search(userId) 
                           pretyPrintJson(data)
                           number = 0
                           result = "GOOGLE SEARCH RESULT :"
                           for s in data["result"]:
                               number += 1
                               result += "\n{}. {}".format(number,s["title"])
                               result += "\n{}".format(s["snippet"])
                               result += "\n{}".format(s["url"])
                           cl.sendReplyMessage(msg.id,to, str(result))                  

                        elif cmd.startswith("ponsel"):
                            #
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.cellular(search)
                                pretyPrintJson(data)
                                number = 0
                                vian = "SPESIFIKASI PONSEL\n"
                                for a in data["result"]:
                                    number += 1
                                    vian += "\n• {}. {}\n".format(number,a["brands"])
                                    vian += "\n• Release : {}".format(a["release"])
                                    vian += "\n• Chipset : {}".format(a["chipset"])
                                    vian += "\n• Screen : {}".format(a["screen"])
                                    vian += "\n• Battery : {}".format(a["battery"])
                                    vian += "\n• Display : {}".format(a["display"])
                                    vian += "\n• Ram : {}".format(a["ram"])
                                    vian += "\n• Storage : {}\n".format(a["storage"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
 
                        elif cmd.startswith("resi-sicepat:"):
                          #
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"sicepat")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))
 
                        elif cmd.startswith("resi-pos:"):
                          #
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"pos")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-rex:"):
                          #
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"rex")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-jnt:"):
                          #
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"jnt")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-ninja:"):
                          #
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"ninja")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))
                                                                                  
                        elif cmd.startswith("gnamegrup"):
                          #
                            if msg.toType == 2:
                                X = cl.getChats(to)
                                X.name = text.split(" ")
                                cl.updateGroup(X)
                                                               
                        elif cmd.startswith("spamtag "):
                          #
                            text_ = cmd.replace("spamtag ", "")
                            cond = text_.split(" ")
                            text = text_.replace(cond[0] + " ", "")
                            jml = int(cond[0])
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    text = text.replace("@{}".format(str(contact.displayName)),"")
                                if "|" in text:
                                    cond = text.split("|")
                                    fm = cond[0]
                                    lm = cond[1]
                                else:
                                    fm = ""
                                    lm = text
                                for ls in lists:
                                    for x in range(jml):
                                        sendMention(to, ls, str(fm), str(lm))
                                sendFoter(msg.to, "「 Succes tag {} user , with amount {} tags 」".format(str(len(lists)), str(jml)))
                                return
                            else:
                                sendFoter(msg.to, "Nothing user :v")
                                return


                        elif cmd == "gcall":
                          if wait["selfbot"] == True:
                          #if 'MENTION' in msg.contentMetadata.keys()!= None:
                            #if msg._from in admin:
                                a = cl.getGroupCall(to);print(a);k = len(a.memberMids)//20                        
                                if a.memberMids is not None:
                                  #k = len(a.memberMids)//20
                                  for i in range(k+1):
                                     try:
                                         if i == 0:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if a.mediaType == 1:typenya = 'Voice Call Group'
                                             if a.mediaType == 2:typenya = 'Video Call Group'
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
                                     except:
                                         if a.mediaType == 3:typenya = 'Group Live'
                                         if i == 0:aa = 'INFO LIVE\nName Grup: {}\nDurasi Live : {}\n• Talent:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO LIVE GROUP \nName Group: {}\nDurasi Live: {}\n• Talent:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])                                         
                                else:sendReplyMessage(msg.id,to,'🛑Tidak Ada Aktifitas Group')                     

                        elif cmd == "gcall1":
                          #if wait["selfbot"] == True:
                            #if msg._from in admin:
                                a = cl.getGroupCall(to);print(a);k = len(a.memberMids)//20                        
                                if a.memberMids is not None:
                                  #k = len(a.memberMids)//20
                                  for i in range(k+1):
                                     try:
                                         if i == 0:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if a.mediaType == 1:typenya = 'Voice Call Group'
                                             if a.mediaType == 2:typenya = 'Video Call Group'
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
                                     except:
                                         pass

                        elif cmd == "gcall2":
                          #if wait["selfbot"] == True:
                            #if msg._from in admin:
                                a = cl.getGroupCall(to);print(a);k = len(a.memberMids)//20                        
                                if a.memberMids is not None:
                                  #k = len(a.memberMids)//20
                                  for i in range(k+1):
                                     try:
                                         if i == 0:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if a.mediaType == 1:typenya = 'Voice Call Group'
                                             if a.mediaType == 2:typenya = 'Video Call Group'
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
                                     except:
                                         if a.mediaType == 3:typenya = 'Group Live'
                                         if i == 0:aa = 'INFO LIVE\nName Grup: {}\nDurasi Live : {}\n• Talent:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO LIVE GROUP \nName Group: {}\nDurasi Live: {}\n• Talent:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])                                         
                                else:cl.sendReplyMessage(msg.id,to,'Tidak Ada Aktifitas Group')                     


                        elif cmd == "gcall3":
                          #if wait["selfbot"] == True:
                            #if msg._from in admin:
                                a = cl.getGroupCall(to);print(a);k = len(a.memberMids)//20                        
                                if a.memberMids is not None:
                                  #k = len(a.memberMids)//20
                                  for i in range(k+1):
                                     try:
                                         if i == 0:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO CALL GROUP\nName Group: {}\nDurasi Panggilan: {}:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if a.mediaType == 1:typenya = 'Voice Call Group'
                                             if a.mediaType == 2:typenya = 'Video Call Group'
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
                                     except:
                                         if a.mediaType == 3:typenya = 'Group Live'
                                         if i == 0:aa = 'INFO LIVE\nName Grup: {}\nDurasi Live : {}\n• Talent:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                         else:aa = 'INFO LIVE GROUP \nName Group: {}\nDurasi Live: {}\n• Talent:'.format(cl.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                         ret = aa
                                         for b in a.memberMids[i*20 : (i+1)*20]:
                                             no += 1;c = a.hostMids                        
                                             if no == len(a.memberMids):ret+='\n• {}. @!\n › Type: {}\n• Host: @!'.format(no,typenya)
                                             else:ret+='\n• {}. @!'.format(no)
                                         cl.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])                                         
                                else:cl.sendReplyMessage(msg.id,to,'Tidak Ada Aktifitas Group')                     

                                    
                        elif cmd.startswith("call "):
                          #
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                group = cl.getChats(to)
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0,500):                                        	
                                        cl.acquireGroupCallRoute(to)                                            
                                        members = [ls for ls in lists]
                                        cl.inviteIntoChatCall(to, contactIds=members)
                                    try:
                                        sendFoter(msg.to,"Success 500 invite call group")
                                        break
                                    except Exception as error:
                                        logError(error)                     
                                                                               
                        elif cmd.startswith("block "):
                          #
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                sendFoter(msg.to, "Success add " + str(contact.displayName) + " to Blocklist")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            #
                                settings["changevp"] = True
                                sendFoter(msg.to, "Kirim Video ny")

                        elif cmd.startswith("cvp: "):
                          if wait["selfbot"] == True:
                            #
                                sep = text.split(" ")
                                FckVeza = text.replace(sep[0] + " ","")
                                FckVezaGans = cl.getContact(sender)
                                flexvian(msg.to, "Loading...")
                                pic = "http://dl.profile.line-cdn.net/{}".format(FckVezaGans.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output vp.mp4 {}'.format(FckVeza))
                                pict = cl.downloadFileURL(pic)
                                vids = "vp.mp4"
                                changeVideoAndPictureProfile(pict, vids)
                                flexvian(msg.to, "Dual Profile Video ♪")
                                os.remove("vp.mp4")
                                
                        elif cmd.startswith("scall "):
                          #
                            sep = text.split(" ")
                            num = int(sep[1])
                            try:                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            group = cl.getChats(to)
                                            members = [ls]
                                            kunkun = cl.getContact("u176ef6889643e290ba5801bffc83457b").displayName
                                            cl.acquireGroupCallRoute(to)
                                            cl.inviteIntoGroupCall(to, contactIds=members)
                                        sendFoter(msg.to, "Success Invite Groups Call")
                            except Exception as error:
                                sendFoter(to, str(error))
                                      
                        elif cmd == "cinema xx1":
                          #
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "[ Cinema XX1 ]\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            cl.sendReplyMessage(msg.id,to, str(hasil))
                                        
                        elif cmd.startswith("fs "):
                          #
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=nda12345&text={}".format(txt)
                            sendFoterImage(to, url)

                        elif cmd.startswith("anime: "):
                          #
                            sep = msg.text.split(" ")
                            judul = msg.text.replace(sep[0] + " ","")
                            tahun = msg.text.replace(sep[1] + " ","")
                            r=requests.get('https://www.omdbapi.com/?t='+judul+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                            data=r.text
                            data=json.loads(data)
                            ret_ = "「 Anime Search 」"
                            ret_ += "\nTitle : " +str(data["Title"])  + " ("+str(data["Year"])+ ")"
                            ret_ += "\n\n " + str(data["Plot"])
                            ret_ += "\n\nSumber Info: https://myanimelist.net/anime"                       
                            img = data["Poster"]
                            sendFoterImage(msg.to,str(img))
                            cl.sendReplyMessage(msg.id,to, str(ret_))
                                                                                                                               
                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           #
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                sendFoter(msg.to,"Changed to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           #
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendFoter(msg.to,"Changed to " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           #
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                sendFoter1(msg)
                                            except Exception as e:
                                                sendFoter(msg.to,str(e))
                                    else:
                                        sendFoter(msg.to,"Jumlah melebihi 1000")
        
                        elif cmd.startswith('pict '):
                          if wait["selfbot"] == True:
                           #
                               res = '╭───「 Picture Status 」'
                               no = 0
                               if 'MENTION' in msg.contentMetadata.keys():
                                   mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   if len(mentions['MENTIONEES']) == 1:
                                       profile = cl.getContact(mentions['MENTIONEES'][0]['M'])
                                       if profile.pictureStatus:
                                           path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                                           cl.sendImageWithURL(to, path)
                                       else:
                                           cl.sendReplyMessage(msg.id,to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                                
                        elif cmd.startswith('cover '):
                          if wait["selfbot"] == True:
                           #
                               res = '╭───「 Picture Cover 」'
                               no = 0
                               if 'MENTION' in msg.contentMetadata.keys():
                                   mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   if len(mentions['MENTIONEES']) == 1:
                                       mid = mentions['MENTIONEES'][0]['M']
                                       cover = cl.getProfileCoverURL(mid)
                                       cl.sendImageWithURL(to, cover)
                                   else:
                                       sendFoter(to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                                    
                        elif cmd.startswith("video "):
                          #  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    if contact.videoProfile == None:
                                    	continue
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "/vp"
                                    cl.sendVideoWithURL(to, str(path))
                                                                            
                        elif cmd.startswith("name "):
                          #  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendReplyMessage(msg.id,to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                                    
                        elif cmd.startswith("bio "):
                          #  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendReplyMessage(msg.id,to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                                
                        elif cmd.startswith("ulti "):
                          #  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        cl.deleteOtherFromChat(to, [ls])
                                        cl.inviteIntoChat(to, [ls])
                                        cl.cancelChatInvitation(to, [ls])
                                    except:
                                       sendFoter(msg.to, "Limited !")
      
                        elif cmd.startswith("invite "):
                                if msg._from in creator or msg._from in owner or msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:                                                                            
                                        try:      
                                            #cl.findAndAddContactsByMid(target)
                                            cl.inviteIntoChat(to,[target])                                             
                                            cl.sendMentionV2(mag.to, "User @!\nTarget sudah di invite..", [target])
                                        except:
                                            pass

                        elif cmd == "/////spamcall":
                          if wait["selfbot"] == True:
                           #
                             if msg.toType == 2:
                                group = cl.getChats([to], True, False)
                                members = [mem for mem in group.chats[0].extra.groupExtra.memberMids]
                                jmlh = int(wait["limit"])
                                sendFoter(msg.to, "Success {} Call Groups".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        sendFoter(msg.to,str(e))
                                else:
                                    sendFoter(msg.to,"Jumlah melebihi batas")
                        elif cmd.startswith('spamcall '):
                          if wait["selfbot"] == True:
                           #
                               if msg.toType != 2: return sendFoter(to, 'command ini hanya dapat digunakan di dalam group!!')
                               sep = msg.text.split(" ")
                               strnum = msg.text.replace(sep[0] + " ","")
                               if strnum.isdigit():
                                   num = int(strnum)
                                   for var in range(0, num):
                                       group = cl.getChats([to], True, False).chats[0]
                                       cl.acquireGroupCallRoute(to)
                                       cl.inviteIntoGroupCall(to, contactIds=[a for a in group.extra.groupExtra.memberMids])
                                   sendFoter(msg.to, 'Success {} Call Groups: '.format(int(num)))

                        elif cmd.startswith('naik '):
                          if wait["selfbot"] == True:
                           #
                               if msg.toType != 2: return sendFoter(to, 'command ini hanya dapat digunakan di dalam group!!')
                               sep = msg.text.split(" ")
                               strnum = msg.text.replace(sep[0] + " ","")
                               if strnum.isdigit():
                                   num = int(strnum)
                                   for var in range(0, num):
                                       group = cl.getChats([to], True, False).chats[0]
                                       cl.acquireGroupCallRoute(to)
                                       cl.inviteIntoGroupCall(to, contactIds=[a for a in group.extra.groupExtra.memberMids])
                                   sendFoter(msg.to, 'Success {} Call Groups: '.format(int(num)))

                        elif cmd.startswith('panggilan '):
                          if wait["selfbot"] == True:
                           #
                               if msg.toType != 2: return sendFoter(to, 'command ini hanya dapat digunakan di dalam group!!')
                               sep = msg.text.split(" ")
                               strnum = msg.text.replace(sep[0] + " ","")
                               if strnum.isdigit():
                                   num = int(strnum)
                                   for var in range(0, num):
                                       group = cl.getChats([to], True, False).chats[0]
                                       cl.acquireGroupCallRoute(to)
                                       cl.inviteIntoGroupCall(to, contactIds=[a for a in group.extra.groupExtra.memberMids])
                                   sendFoter(msg.to, 'Success {} Call Groups: '.format(int(num)))

                        elif cmd.startswith('s '):
                          if wait["selfbot"] == True:
                           #
                               if msg.toType != 2: return sendFoter(to, 'command ini hanya dapat digunakan di dalam group!!')
                               sep = msg.text.split(" ")
                               strnum = msg.text.replace(sep[0] + " ","")
                               if strnum.isdigit():
                                   num = int(strnum)
                                   for var in range(0, num):
                                       group = cl.getChats([to], True, False).chats[0]
                                       cl.acquireGroupCallRoute(to)
                                       cl.inviteIntoGroupCall(to, contactIds=[a for a in group.extra.groupExtra.memberMids])
                                   sendFoter(msg.to, 'Success {} Call Groups: '.format(int(num)))

                        elif cmd.startswith('kojom '):
                          if wait["selfbot"] == True:
                           #
                               if msg.toType != 2: return sendFoter(to, 'command ini hanya dapat digunakan di dalam group!!')
                               sep = msg.text.split(" ")
                               strnum = msg.text.replace(sep[0] + " ","")
                               if strnum.isdigit():
                                   num = int(strnum)
                                   for var in range(0, num):
                                       group = cl.getChats([to], True, False).chats[0]
                                       cl.acquireGroupCallRoute(to)
                                       cl.inviteIntoGroupCall(to, contactIds=[a for a in group.extra.groupExtra.memberMids])
                                   sendFoter(msg.to, 'Success {} Call Groups: '.format(int(num)))

                        elif cmd.startswith("///spamcall "):
                          if wait["selfbot"] == True:
                            #
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getChats(to)
                                members = [mem.mid for mem in group.members]
                                sendFoter(msg.to,"Success {} Call Groups".format(str(strnum)))
                                jumlah = int(strnum)
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           cl.acquireGroupCallRoute(to)
                                           cl.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           #
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           #
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sendFoter(midd, str(Setmain["RAmessage1"]))

                        elif 'idline: ' in msg.text:
                          if wait["selfbot"] == True:
                           #
                              msgs = msg.text.replace('idline: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendReplyMessage(msg.id,to, "http://line.me/ti/p/~" + msgs)
                                  sendFoter(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif msg.text.lower() in tes["Message"]:
                            if wait["autotext"] == True:
                                sid = tes["Message"][msg.text.lower()]
                                cl.sendReplyMessage(msg.id, to, sid)     
                                    
                        elif msg.text.lower() in wait["stickers"]:
                           if wait["apkTikel"] == True:
                             if msg.text.lower() in wait["stickers"]:
                                 sid = wait["stickers"][msg.text.lower()]["STKID"]
                                 time.sleep(1)
                                 data = {
                                     "type": "template",
                                     "altText": "Sticker",
                                     "baseSize": { #
                                         "height": 1040, #
                                         "width": 1040 #
                                     }, #
                                     "template": {
                                         "type": "image_carousel",
                                         "columns": [{
                                             "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid), 
                                             "action": {
                                                 "type": "uri",
                                                 "uri": "line://ti/p/~zul.1.02",
                                                 "area": {
                                                     "x": 520,
                                                     "y": 0,
                                                     "width": 520,
                                                     "height": 1040
                                                 }
                                             }
                                         }]
                                     }
                                 }
                                 sendTemplate(to, data)      
                                    
                        elif cmd.startswith("dellsticker: "):
                          #
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama not in wait["stickers"]:
                                        sendFoter(msg.to,"List Sticker Kosong.")
                                    else:
                                        del wait["stickers"][nama]
                                        f=codecs.open("sticker.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        sendFoter(msg.to,"Hapus Sticker ✓")
                                except Exception as e:
                                    sendFoter(msg.to,"{}".format(str(e)))
                                    
                        elif cmd.startswith("stickerlist"):
                          #
                                if wait["stickers"] == {}:
                                    sendFoter(msg.to,"Nothing sticker")
                                else:
                                    no = 0
                                    ret_ = "List\n"
                                    for a in wait["stickers"]:
                                        no += 1
                                        ret_ += "\n" +str(no)+". " +str(a)
                                    ret_ += "\n\nList %i Sticker" % len(wait["stickers"])
                                    sendFoter(to, ret_)  
  
                        elif cmd.startswith("addsticker: "):
                          #
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama in wait["stickers"]:
                                        sendFoter(msg.to,"Sudah ada dalam list")
                                    else:
                                        wait["stk"] = nama
                                        wait["sticker"] = True
                                        f=codecs.open("sticker.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        sendFoter(msg.to,"Send a stickers ✓")
                                except Exception as e:
                                    sendFoter(msg.to,"{}".format(str(e)))
                   
#===========Protection============#
                        elif cmd.startswith("welcomemsg "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Sudah Aktif ♪"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Leave Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendFoter(msg.to, "Welcome Enable ✓")
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Leave Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Leave Msg sudah tidak aktif"
                                    sendFoter(msg.to, "Welcome Disable ✓")

                                
                        elif cmd.startswith("leavemsg "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in leave:
                                       msgs = "Leave Msg sudah aktif"
                                  else:
                                       leave.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Leave Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendFoter(msg.to, "Leave Msg Enable ✓")
                              elif spl == 'off':
                                    if msg.to in leave:
                                         leave.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Leave Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Leave Msg sudah tidak aktif"
                                    sendFoter(msg.to, "Leave Msg Disable ✓")

                        elif cmd.startswith("pqr "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendFoter(msg.to, "Protect qr enable")
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    sendFoter(msg.to, "Protect qr disable")

                        elif cmd.startswith("pkick "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendFoter(msg.to, "Protect kick enable")
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    sendFoter(msg.to, "Protect kick disable")

                        elif cmd.startswith("pjoin "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendFoter(msg.to, "Protect join enable")
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    sendFoter(msg.to, "Protect join disble")

                        elif cmd.startswith("pcancell "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendFoter(msg.to, "Protect cancel enable")
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    sendFoter(msg.to, "Protect cancel disable")
                        elif cmd == "quis on" or text.lower() == 'quis on':
                            ##
                                wait["quis"] = True                          
                                sendFoter(msg.to, "QUIST AKTIF")
                        elif cmd == "quis off" or text.lower() == 'quis off':
                            ##
                                wait["quis"] = False                        
                                sendFoter(msg.to, "QUIST MATI BOS")

                        elif cmd == "cekbot":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == "!cek":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == ".cek":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == "/cek":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == "#cek":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == "?cek":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == "😁cek":
#                            ##if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u9b0ae88d7cf669da9a8416bd4c765cd1"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰ZULKIFLI ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰ZULKIFLI ❎"
                               cl.sendReplyMessage(msg.id,to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))

                        elif cmd == "cek":
                            #
                               try:cl.deleteOtherFromChat(to, [""]);has1 = "OK"
                               except:has1 = "NOT"
                               try:cl.inviteIntoChat(to, [""]);has = "OK"
                               except:has = "NOT"
                               if has == "OK":sil = "Normal"
                               else:sil = "limit"
                               if has1 == "OK":sil1 = "Normal"
                               else:sil1 = "limit"
                               cl.sendReplyMessage(msg.id,to, "Kick: {} \nInvite: {}".format(sil1,has))   


                                                                            
                        elif cmd == "joinquis on":
                            #
                                if wait["autoJoinquis"] == True:
                                    foro2(to, "join aktif")
                                else:
                                    wait["autoJoinquis"] = True
                                    sendFoter(msg.to, "join Diaktifkan")

                        elif cmd == "joinquis off":
                            #
                                if wait["autoJoinquis"] == False:
                                    foro(to, "Auto Tewas")
                                else:
                                    wait["autoJoin"] = False
                                    sendFoter(msg.to, "Auto Tewas")

                        elif cmd.startswith("pinvite "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getChats(msg.to)
                                       msgs = "Protect in : " +str(ginfo.name)
                                  sendFoter(msg.to, "Protect invite enable")
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    sendFoter(msg.to, "Protect invite disable")
                        elif cmd.startswith('protect:off '):
                            #
                               sep = text.split(" ")
                               num = text.replace(sep[0] + " ","")
                               groups = cl.getAllChatIds()
                               target = groups[int(num)-1]
                               try:
                                   protectqr.remove(target)
                                   protectkick.remove(target)
                                   protectjoin.remove(target)
                                   protectinvite.remove(target)
                                   protectcancel.remove(target)
                                   sendFoter(to, "Succes off Pro Group  {} ".format(cl.getChats(target).name))
                               except:pass
                        elif cmd.startswith('protect:on '):
                            #
                               sep = text.split(" ")
                               num = text.replace(sep[0] + " ","")
                               groups = cl.getAllChatIds()
                               target = groups[int(num)-1]
                               try:
                                   protectqr.append(target)
                                   protectkick.append(target)
                                   protectjoin.append(target)
                                   protectinvite.append(target)
                                   protectcancel.append(target)
                                   sendFoter(to, "Succes on pro di Group  {} ".format(cl.getChats(target).name))
                               except:pass
                        elif cmd.startswith("protect "):
                           #
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getChats(msg.to)
                                      msgs = "Max protection enable "
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getChats(msg.to)
                                      msgs = "Max protection allready On"
                                  sendFoter(msg.to, "All protection enable")
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Max protection Disable"
                                    else:
                                         ginfo = cl.getChats(msg.to)
                                         msgs = "Max protection allready disble"
                                    sendFoter(msg.to, "All protection disable")

#===========KICKOUT============#
#===========ADMIN ADD============#
                        elif cmd.startswith("adminadd "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendFoter(msg.to,"Add To Adminlist ✓")
                                       except:
                                           pass

                        elif cmd.startswith("staffadd "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendFoter(msg.to,"Add To Stafflist ✓")
                                       except:
                                           pass


                        elif cmd.startswith("admindell "):
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in ZulBots:
                                       try:
                                           admin.remove(target)
                                           sendFoter(msg.to,"Delete Admin ✓")
                                       except:
                                           pass

                        elif cmd.startswith("staffdell "):
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in ZulBots:
                                       try:
                                           staff.remove(target)
                                           sendFoter(msg.to,"Delete Staff ✓")
                                       except:
                                           pass

                        elif cmd.startswith("botdell "):
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in ZulBots:
                                       try:
                                           Bots.remove(target)
                                           sendFoter(msg.to,"delete Botlist ✓")
                                       except:
                                           pass
                                           
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            #
                                wait["addadmin"] = True
                                sendFoter(msg.to,"Send Contact ✓")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            #
                                wait["delladmin"] = True
                                sendFoter(msg.to,"Send Contact ✓")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            #
                                wait["addstaff"] = True
                                sendFoter(msg.to,"Send Contact ✓")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            #
                                wait["dellstaff"] = True
                                sendFoter(msg.to,"Send Contact ✓")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            #
                                wait["addbots"] = True
                                sendFoter(msg.to,"Send Contact ✓")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            #
                                wait["dellbots"] = True
                                sendFoter(msg.to,"Send Contact ✓")

#                        elif cmd == "refresh" or text.lower() == 'abort':
                            #
#                                wait["addadmin"] = False
#                                wait["Talkdblacklist"] = False
#                                sendFoter(msg.to,"Command abort to abort")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            #
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    sendFoter(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            #
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    sendFoter(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            #
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    sendFoter(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#

                        elif "assalamualaikum" in msg.text.lower():
                             if wait["responsalam"] == True:  
                                cl.sendReplyMessage(msg.id,to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")

                        elif cmd == "notag off":
                            #
                                wait["Mentionkick"] = False
                                ret = "Notag Disable ✓"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "respon1 on":
                            #
                                wait["detectMention1"] = True
                                ret = "Auto Respon1 Enable ✓"
                                sendFoter(msg.to, str(ret))
                           
                        elif cmd == "respon1 off":
                            #
                                wait["detectMention1"] = False
                                ret = "Auto Respon1 Disable ✓"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "respon on":
                            #
                                wait["respontag"] = True
                                ret = "Auto Respon Enable ✓"
                                sendFoter(msg.to, str(ret))
                           
                        elif cmd == "respon off":
                            #
                                wait["respontag"] = False
                                ret = "Auto Respon Disable ✓"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "detectvp on":
                            #
                                wait["detectvp"] = True
                                ret = "Auto Respon Enable ✓"
                                sendFoter(msg.to, str(ret))
                           
                        elif cmd == "detectvp off":
                            #
                                wait["detectvp"] = False
                                ret = "Auto Respon detectvp Disable ✓"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "dvp on":
                            #
                                wait["detectvp"] = True
                                ret = "Auto Respon Enable ✓"
                                sendFoter(msg.to, str(ret))
                           
                        elif cmd == "dvp off":
                            #
                                wait["detectvp"] = False
                                ret = "Auto Respon detectvp Disable ✓"
                                sendFoter(msg.to, str(ret))

                           
                        elif cmd == "autoread on":
                            #
                                Setmain["autoRead"] = True
                                ret = "Auto Read Enable ✓"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "autoread off":
                            #
                                Setmain["autoRead"] = False
                                ret = "Auto Read Disable ✓"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "contact on":
                            #
                                wait["contact"] = True
                                ret = "Detail contact Enable ✓"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "contact off":
                            #
                                wait["contact"] = False
                                ret = "Detail Contact Disable ✓"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "autotext on":
                            #
                                wait["autotext"] = True
                                ret = "Autotext Enable ✓"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "autotext off":
                            #
                                wait["autotext"] = False
                                ret = "Autotext Disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "autoblock on":
                            #
                                wait["autoBlock"] = True
                                ret = "Auto Block Enable"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "autoblock off":
                            #
                                wait["autoBlock"] = False
                                ret = "Auto Block Disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "unsend on":
                            #
                                wait["unsend"] = True
                                ret = "Unsend Chat Enable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "unsend off":
                            #
                                wait["unsend"] = False
                                ret = "Unsend Chat Disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "timeline on":
                            #
                                wait["Timeline"] = True
                                ret = "Detail Post Enable"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "timeline off":
                            #
                                wait["Timeline"] = False
                                ret = "Detail Post Disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "autojoin on":
                            #
                                wait["autoJoin"] = True
                                ret = "Auto Join Enable."
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "autojoin off":
                            #
                                wait["autoJoin"] = False
                                ret = "Auto Join Disable"
                                sendFoter(msg.to, str(ret))

                                
                        elif cmd == "tikelgede on":
                            #
                                wait["apkTikel"] = True
                                ret = "Sticker Temp On."
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "tikelgede off":
                            #
                                wait["apkTikel"] = False
                                ret = "Sticker Temp Off"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "sticker on":
                            #
                                wait["sticker"] = True
                                ret = "Detail Sticker On"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "sticker off":
                            #
                                wait["sticker"] = False
                                ret = "Detail sticker Off"
                                sendFoter(msg.to, str(ret))
                                
                        elif cmd == "smule on":
                            #
                                wait["rsmule"] = True
                                ret = "Detect smule On"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "smule off":
                            #
                                wait["rsmule"] = False
                                ret = "Detect smule Off"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "tiktok on":
                            #
                                wait["tiktok"] = True
                                ret = "Tiktok url enable"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "tiktok off":
                            #
                                wait["tiktok"] = False
                                ret = "Tiktok url disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "youtube on":
                            #
                                wait["ytube"] = True
                                ret = "youtube url enable"
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "youtube off":
                            #
                                wait["ytube"] = False
                                ret = "youtube url disable"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "jointicket on":
                            #
                                wait["autoJoinTicket"] = True
                                ret = "Join Ticket On."
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "jointicket off":
                            #
                                wait["autoJoinTicket"] = False
                                ret = "Join Ticket Off."
                                sendFoter(msg.to, str(ret))
                                
                        elif cmd == "autolike on":
                            #
                                wait["likeOn"] = True
                                ret = "Auto Like Enable."
                                sendFoter(msg.to, str(ret))
                            
                        elif cmd == "autolike off":
                            #
                                wait["likeOn"] = False
                                ret = "Auto like Disable."
                                sendFoter(msg.to, str(ret))                                
        
                        elif cmd == "responsalam on":
                            #
                                wait["responsalam"] = True
                                ret = "Auto salam On."
                                sendFoter(msg.to, str(ret))
                                
                        elif cmd == "responsalam off":
                            #
                                wait["responsalam"] = False
                                ret = "Auto salam Off."
                                sendFoter(msg.to, str(ret))
  
                        elif cmd == "token on":
                            #
                                wait["token"] = True
                                ret = "Cek Token On."
                                sendFoter(msg.to, str(ret))
                                
                        elif cmd == "token off":
                            #
                                wait["token"] = False
                                ret = "Cek Token Off."
                                sendFoter(msg.to, str(ret))
                          
                        elif cmd == "autolike off":
                            #
                                wait["likeOn"] = False
                                ret = "Auto like Disable."
                                sendFoter(msg.to, str(ret))                                

                        elif cmd == "c on":
                            wait["nganu"] = True
                            ret = "Cek Mid Kontact Token On"
                            sendFoter(msg.to, str(ret))

                        elif cmd == "c off":
                            wait["nganu"] = False
                            ret = "Cek Mid Kontact Token Off"
                            sendFoter(msg.to, str(ret))

                        elif cmd == "respon2 on":
                            #
                                temptag["stealtag"] = True
                                ret = "Respon 2 Enable !"
                                sendFoter(msg.to, str(ret))
                                                        
                        elif cmd == "respon2 off":
                            #
                                temptag["stealtag"] = False
                                ret = "Respon 2 Disable !"
                                sendFoter(msg.to, str(ret))
                                
                        elif cmd == "responcall on":
                            #
                                wait["responGc"] = True
                                ret = "Detect call enable"
                                sendFoter(msg.to, str(ret))
                                                        
                        elif cmd == "responcall off":
                            #
                                wait["responGc"] = False
                                ret = "Detect call disable"
                                sendFoter(msg.to, str(ret))
                                                                                      
                        elif cmd == "sticker sider":
                            #
                                wait["AddstickerSider"]["status"] = True
                                ret = "Send a stickers ♪"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                           ##if msg._from in admin or msg._from in clmid:
                               get_profile_time_start = time.time()
                               get_profile = cl.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               time.sleep(1);cl.sendMessage(msg.to, "𝚂𝚙𝚎𝚎𝚍 : %.4f ♪" % (get_profile_time/3))

                            
                        elif cmd == "sticker tag":
                            #
                                wait["AddstickerTag"]["status"] = True
                                ret = "Send a stickers ♪"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "vps":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               am = subprocess.getoutput('cat /proc/meminfo')
                               core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
                               for anu in am.splitlines():
                                   if 'MemTotal:' in anu:
                                       mem = anu.split('MemTotal:')[1].replace(' ','')
                                   if 'MemFree:' in anu:
                                       fr = anu.split('MemFree:')[1].replace(' ','')
                               res = '╭───[ Memory ]'
                               res += "\n├➢ Cpu Core : {}".format(core)
                               res += "\n├➢ Total Memory: {}".format(mem)
                               res += "\n├➢ Free Memory: {}".format(fr)
                               res += '\n╰───[ Memory_vps ]'
                               cl.sendReplyMessage(msg.id, to, format(str(res)))


                        elif cmd == "sticker pesan":
                            #
                                wait["AddstickerPesan"]["status"] = True
                                ret = "Send a stickers ♪"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "sticker welcome":
                            #
                                wait["AddstickerWelcome"]["status"] = True
                                ret = "Send a stickers ♪"
                                sendFoter(msg.to, str(ret))

                        elif cmd == "payment":
                          if wait["selfbot"] == True:
                            ##if msg._from in admin or msg._from in clmid:
                               cl.sendReplyMessage(msg.id, to, " ━━━┅┅━━\n"
"      REKENING & DANA\n"
"╭━━━━━━━━━━━━━━\n"
"║╭❉ 🔷TOP UP via\n"
"║│            🔻🔻\n"
"║│🔷BANK BRI \n"
"║│🔷734301002990505\n"
"║│🔷AN :  ZULKIFLI BALANSUBU \n"
"║│🔷DANA TOP UP \n"
"║│🔷0857-5707-6639 \n"
"║┝─────────────\n"
"║╰❉ 🔷 Terimakasih\n"
"╰━━━━━━━━━━━━━━")




                        elif cmd == "sticker leave":
                            #
                                wait["AddstickerLeave"]["status"] = True
                                ret = "Send a stickers ♪"
                                sendFoter(msg.to, str(ret))
       
                        elif cmd == comd["cban"]:
                          if wait["selfbot"] == True:  
                            #
                              if wait["blacklist"] == {}:
                                   ret = "Blacklist Empty"
                                   sendFoter(msg.to, str(ret))
                              else:
                                   ret = "Cleared {} Blacklist".format(str(len(wait["blacklist"])))
                                   sendFoter(msg.to, str(ret))
                                   wait["blacklist"] = {}
                    

#===========COMEN PANGGILAN======
                        elif cmd.startswith("tag: "):
                          if wait["selfbot"] == True:
                           #if msg._from in admin or msg._from in clmid:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendReplyMessage(msg.id, to,"Spamtag Menjadi " +strnum)

                        elif cmd.startswith("setcall: "):
                          if wait["selfbot"] == True:
                           #if msg._from in admin or msg._from in clmid:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendReplyMessage(msg.id, to,"Setting Spamcall Menjadi : " +strnum)

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getChats([to]).chats[0](chatName)                   	        
                            try:
                                group = groups[int(number)-1]
                                G = cl.getChats([group]).chats[0]
                                try:
                                    cl.deleteSelfFromChat(G.id)
                                except:
                                    cl.deleteSelfFromChat(G.id)
                                cl.sendMessage(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                cl.sendMessage(to, str(error))
                                                                                                 
#===========COMMAND BLACKLIST============#

                        elif cmd.startswith("talkban "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendFoter(msg.to,"Added Blacklist")
                                       except:
                                           pass

                        elif cmd.startswith("untalkban "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendFoter(msg.to,"Clear Blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            #
                                wait["Talkwblacklist"] = True
                                sendFoter(msg.to,"Send Contact")

                        elif cmd == "res" or cmd == "ping":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                                cl.sendMessage(msg.to, "»➪ Dalemb sayank....")

                        elif cmd == '*ginfo':
                          #if msg._from in admin or msg._from in clmid:
                            group = cl.getChats([to]).chats[0]
                            try:ccreator = group.extra.groupExtra.creator;gcreator = cl.getContact(ccreator).displayName
                            except:ccreator = None;gcreator = 'Not found'
                            if not group.extra.groupExtra.inviteeMids:pendings = 0
                            else:pendings = len(group.extra.groupExtra.inviteeMids)
                            qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
                            if group.extra.groupExtra.preventedJoinByTicket:ticket = 'Not found'
                            else:ticket = 'https://line.me/R/ti/g/' + str(cl.reissueChatTicket(group.chatMid).ticketId)
                            created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
                            img ="https://obs.line-scdn.net/{}".format(cl.getChats([to]).chats[0].picturePath)
                            cl.sendImageWithURL(msg.to, str(img))
                            if ccreator:cl.sendMessage(to, None, contentMetadata={'mid': ccreator}, contentType=13)
                            cl.sendReplyMessage(msg.id, to,'「 Group Info 」\n\n    • Group ID : ' + group.chatMid + '\n    • Group Name : ' + group.chatName + '\n    • Pembuat : ' + gcreator + '\n    • Created Time : ' + created + '\n    • Sisa Member : ' + str(len(group.extra.groupExtra.memberMids)) + '\n    • Member Pending : ' + str(pendings) + '\n    • Link QR : ' + qr)
                        elif cmd.startswith("ginfo "):
                          #if msg._from in admin or msg._from in clmid:
                            sep = msg.text.split(" ");num = msg.text.replace(sep[0] + " ","");gids = [a for a in cl.getAllChatMids(True, True).memberChatMids];gid = gids[int(num) - 1];group = cl.getChats([gid], True , False).chats[0]
                            try:ccreator = group.extra.groupExtra.creator;gcreator = cl.getContact(ccreator).displayName
                            except:ccreator = None;gcreator = 'Not found'
                            if not group.extra.groupExtra.inviteeMids:pendings = 0
                            else:pendings = len(group.extra.groupExtra.inviteeMids)
                            qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
                            if group.extra.groupExtra.preventedJoinByTicket:ticket = 'Not found'
                            else:ticket = 'https://line.me/R/ti/g/' + str(cl.reissueChatTicket(group.chatMid).ticketId)
                            created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
                            img ="https://obs.line-scdn.net/{}".format(cl.getChats([gid]).chats[0].picturePath)
                            cl.sendImageWithURL(msg.to, str(img))
                            if ccreator:cl.sendMessage(to, None, contentMetadata={'mid': ccreator}, contentType=13)
                            cl.sendReplyMessage(msg.id, to,'「 Informasi Group 」\n\n•   ID : ' + group.chatMid + '\n•   Group Name : ' + group.chatName + '\n•   Creator : ' + gcreator + '\n•   Created Time : ' + created + '\n•   Group Member : ' + str(len(group.extra.groupExtra.memberMids)) + '\n•   Group Pending : ' + str(pendings) + '\n•   QR Status : ' + qr)
                        elif cmd == '*gid':
                          #if msg._from in admin or msg._from in clmid:
                            cl.sendMessage(msg.to, "Group Id : {}".format(cl.getChats([to]).chats[0].chatMid))                        

                        elif cmd.startswith('rcall '):
                          #if msg._from in admin or msg._from in clmid: 
                            sep = text.split(" ");num = int(sep[1]);numb = int(sep[2]);sep2 = text.replace(sep[0] + ' ','');text = sep2.replace(sep[1] + ' ','');groups = [a for a in cl.getAllChatMids(True, True).memberChatMids];group = groups[int(num) - 1];G = cl.getChats([group], True , False).chats[0]                                             
                            for var in range(0,numb):G = cl.getChats([group]).chats[0];members = G.extra.groupExtra.memberMids;cl.acquireGroupCallRoute(group);time.sleep(0.4);cl.inviteIntoGroupCall(group, contactIds=members)      
                            cl.sendReplyMessage(msg.id, to, '• RemoteCall diGroup: {} \n• Sebanyak : {} x Done ♪'.format(G.chatName, numb))
                        elif cmd == 'gid':
                          #if msg._from in admin or msg._from in clmid:
                            cl.sendMessage(msg.to, "Group Id : {}".format(cl.getChats([to]).chats[0].chatMid))
                        elif cmd == 'idline':
                          #if msg._from in admin or msg._from in clmid:
                            time.sleep(1);cl.sendReplyMessage(msg.id, to, "Add my idline : \nhttps://line.me/ti/p/~" + cl.profile.userid)

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = denal.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n┣[]► "+ str(no) + ". " + mem.displayName
                                sendTextTemplateB(to,"╔══「 Group Info 」\n┣[]► Group Name : " + str(G.name) + "\n┣══「Member List」" + ret_ + "\n╚══「Total %i Members」" % len(G.members))
                            except:
                                pass
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠[]► " + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplateB(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
#invite for mention



                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            #
                                wait["Talkdblacklist"] = True
                                sendFoter(msg.to,"Send Contact")

                        elif cmd.startswith("ban "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendFoter(msg.to,"Added To Blacklist")
                                       except:
                                           pass

                        elif cmd.startswith("unban "):
                          if wait["selfbot"] == True:
                            #
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendFoter(msg.to,"Unbaned Blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            #
                                wait["wblacklist"] = True
                                sendFoter(msg.to,"Send Contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            #
                                wait["dblacklist"] = True
                                sendFoter(msg.to,"Send Contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            #
                              if wait["blacklist"] == {}:
                                sendFoter(msg.to,"No Body Is Banned")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendFoter(msg.to,"↘Blacklist User↘\n\n"+ma+"\n↘Total「%s」Blacklist User↘" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            #
                              if wait["Talkblacklist"] == {}:
                                sendFoter(msg.to,"No Body Is Banned")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendFoter(msg.to,"↘Talkban User↘\n\n"+ma+"\n↘Total「%s」Talkban User↘" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            #
                              if wait["blacklist"] == {}:
                                    sendFoter(to,"No body is baned")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        sendFoter(msg.to, None, contentMetadata={'mid': i}, contentType=13)
#===========COMMAND SET============#wait["noTiFcall"],
                        elif cmd.startswith("setrespon1: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["balasan"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif cmd.startswith("setcall: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["noTiFcall"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif cmd.startswith("setcall1: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["noTiFcall1"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif cmd.startswith("setsider2: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["siderMsg"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif cmd.startswith("setpesan: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["pesan"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setcomment: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["comment"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                                  
                        elif cmd.startswith("setspeed: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["speed"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                                  
                        elif cmd.startswith("setbye: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["bye"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setsider1on: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["sider1On"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setsider1off: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["sider1Off"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif cmd.startswith("setsideron: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["siderOn"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setsideroff: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["siderOff"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("settagall: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["tagall"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))
                        elif 'Set js ' in msg.text:
                           #
                              spl = msg.text.replace('Set js ','')
                              if spl in [""," ","\n",None]:
                                  sendFoter(msg.to, "Gagal mengganti Pesan amda")
                              else:
                                  wait["amda"] = spl
                                  sendFoter(msg.to, "「amda」\namda diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set bypass ' in msg.text:
                           #
                              spl = msg.text.replace('Set bypass ','')
                              if spl in [""," ","\n",None]:
                                  sendFoter(msg.to, "Gagal mengganti Pesan amdb")
                              else:
                                  wait["amdb"] = spl
                                  sendFoter(msg.to, "「amdb」\namdb diganti jadi :\n\n「{}」".format(str(spl)))
                        elif cmd.startswith("sethelp: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["help"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd == "pirus":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                               helpKvirus2 = helpvirus()
                               cl.sendMessage(msg.to, str(helpKvirus2))

                        elif cmd == "help protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               sendFoter(msg.to, str(helpMessage1))

                        elif cmd.startswith("setcban: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["cban"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setrespon: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   wait["Tag"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setspam: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   Setmain["RAmessage1"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setunsend: "):
                          if wait["selfbot"] == True:
                            #
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFoter(msg.to, "Failed..!!")
                               else:
                                   comd["unsend"] = str(key).lower()
                                   sendFoter(msg.to, "{}".format(str(key).lower()))

                        elif cmd == "cekpesan":
                            #
                               sendFoter(msg.to, "Pesan anda\n"+ str(wait["pesan"]))
                               
                        elif cmd == "cekwelcome":
                            #
                               sendFoter(msg.to, "Msg Welcome\n" + str(wait["welcome"]))
                               
                        elif cmd == "cekcomment":
                            #
                               sendFoter(msg.to, "Msg Comment\n" + str(wait["comment"]))                               

                        elif cmd == "cekrespon":
                            #
                               sendFoter(msg.to, "Msg Respon\n" + str(wait["Tag"]))

                        elif cmd == "cekspam":
                            #
                               sendFoter(msg.to, "Msg Spam\n" + str(Setmain["RAmessage1"]))

                        elif cmd == "ceksider":
                            #
                               sendFoter(msg.to, "Msg Sider\n" + str(wait["mention"]))

                        elif cmd == "ceksider1":
                            #
                               sendFoter(msg.to, "Msg Sider\n" + str(wait["mention1"]))
                               
                        elif cmd == "cekcomment":
                            #
                               sendFoter(msg.to, "Msg Comment\n" + str(wait["comment"]))

                        elif cmd == "cekleave":
                            #
                               sendFoter(msg.to, "Msg Leave\n" + str(wait["leave"]))

                        elif cmd.startswith("lefft: "):
                            #
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getAllChatIds()
                                for i in gid:
                                    h = cl.getChats(i).name
                                    if h == ng:
                                        sendFoter(i, "waitting for notifed success")
                                        cl.deleteSelfFromChat(i)
                                        sendFoter(to,"Leave all group " +h)

                        elif cmd.startswith("sapu: "):
                          if wait["selfbot"] == True:
                            #
                                separate = msg.text.split(":")
                                number = msg.text.replace(separate[0] + ":"," ")
                                groups = cl.getAllChatIds()
                                gid = groups[int(number)-1]                             
                                xyz = cl.getChats(gid)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(gid, cl.authToken, win)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif text.lower() == wait["amda"]:
                          if wait["selfbot"] == True:
                            #
                                xyz = cl.getChats(to)
                                #if xyz.invitee == None:pends = []
                                #else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(to, cl.authToken, win)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif cmd.startswith("bantai: "):
                          if wait["selfbot"] == True:
                            #
                                separate = msg.text.split(":")
                                number = msg.text.replace(separate[0] + ":"," ")
                                groups = cl.getAllChatIds()
                                gid = groups[int(number)-1]                             
                                xyz = cl.getChats(gid)
                                #if xyz.invitee == None:pends = []
                                #else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(gid, cl.authToken, win)
                                for x in targp:lolz += ' uid={}'.format(x)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif text.lower() == wait["amdb"]:
                          if wait["selfbot"] == True:
                            #
                                bypassJS(to)
                                
                        elif cmd == "#cl" or text.lower() == "#cencel":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                ZulBots = cl.getChats(to)
                                if ZulBots.invitee == None:pends = []
                                else:pends = [c.mid for c in ZulBots.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                pokeh = 'cancel.js gid={} token={}'.format(to, cl.authToken, win)
                                for x in targp:pokeh += ' uid={}'.format(x)
                                execute_js(pokeh)



               if msg.contentType == 6:
                 if wait["responGc"] == True:
                     a = cl.getContact(sender)
                     if msg.toType == 2:
                         b = msg.contentMetadata['GC_EVT_TYPE']
                         c = msg.contentMetadata["GC_MEDIA_TYPE"]
                         if c == "VIDEO" and b == "S":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             ##cover = cl.getProfileCoverURL(sender)
                             time.sleep(1)
                             data = {
                                        "type": "flex",
                                        "altText": "TEAM TERMUX",
                                        "contents": {

  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://media.suara.com/pictures/653x366/2015/04/17/o_19j3m1hgthf63ni1h951v366r6a.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NOTIFCALL GRUP",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "25px"
              }
            ],
            "width": "149px",
            "height": "20px",
            "borderColor": "#FF0000",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "position": "absolute",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#000080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "width": "150px",
            "height": "90px",
            "position": "absolute",
            "offsetTop": "30px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "borderColor": "#FF0000",
            "cornerRadius": "5px",
            "borderWidth": "1px",
            "width": "150px",
            "height": "40px",
            "position": "absolute",
            "offsetTop": "147px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "nah kan ngajakin oncam aim belunah kan ngajakinm mandi tau masih jelek",
                "size": "xxs",
                "color": "#FFFFFF",
                "wrap": True,
                "offsetStart": "2px",
                "offsetTop": "2px"
              }
            ],
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "width": "148px",
            "height": "38px",
            "position": "absolute",
            "offsetTop": "148px",
            "offsetStart": "3px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "SUPPORT  BYE: TEAM TERMUX",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "7px"
              }
            ],
            "borderColor": "#FF00FF",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "width": "150px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "210px",
            "offsetStart": "2px",
            "backgroundColor": "#2E8B57"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CREATOR",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "6px"
              }
            ],
            "borderColor": "#FF00FF",
            "cornerRadius": "5px",
            "borderWidth": "1px",
            "width": "70px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "188px",
            "offsetStart": "2px",
            "backgroundColor": "#800080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ORDER",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "15px"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "cornerRadius": "5px",
            "width": "76px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "188px",
            "offsetStart": "75px",
            "backgroundColor": "#0000FF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": []
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://www.blackxperience.com/assets/blackattitude/blacktips//cover-wa-300x300.jpg",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "20px",
            "width": "20px",
            "cornerRadius": "100px",
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQBeiKDJTqSrl0DE7K8pIaNYe1uUsXNVqz9dg&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "20px",
            "width": "20px",
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "100px",
            "borderColor": "#FFFF00",
            "offsetTop": "124px",
            "offsetStart": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://play-lh.googleusercontent.com/74iMObG1vsR3Kfm82RjERFhf99QFMNIY211oMvN636_gULghbRBMjpVFTjOK36oxCbs",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "cornerRadius": "100px",
            "borderWidth": "1px",
            "width": "20px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "70px",
            "height": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRK_yDc42L7ssYuvce24MqTgvesOvYZgQIi8Q&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "100px",
            "width": "20px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTBtVrDomP1KCahV0TSV9hITha-PhnvetHd0g&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "cornerRadius": "100px",
            "borderWidth": "1px",
            "width": "20px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "130px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#FFFF00",
        "cornerRadius": "10px",
        "borderWidth": "2px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://wa.me/message/ANCIF474MS6OL1"
        }
      }
    }
  ]
}
}
                             sendTemplate(to, data)
                         if c == "VIDEO" and b == "E":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             ##cover = cl.getProfileCoverURL(sender)
                             time.sleep(1)
                             data = {
                                        "type": "flex",
                                        "altText": "TEAM TERMUX",
                                        "contents": {

   "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://media.suara.com/pictures/653x366/2015/04/17/o_19j3m1hgthf63ni1h951v366r6a.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NOTIFCALL GRUP",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "25px"
              }
            ],
            "width": "149px",
            "height": "20px",
            "borderColor": "#FF0000",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "position": "absolute",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#000080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co.com/9tdnpsd/1652980705963.jpg",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "width": "150px",
            "height": "90px",
            "position": "absolute",
            "offsetTop": "30px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "borderColor": "#FF0000",
            "cornerRadius": "5px",
            "borderWidth": "1px",
            "width": "150px",
            "height": "40px",
            "position": "absolute",
            "offsetTop": "147px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ah tidak asik oncam bentar engga basah aku diatas wkwkwk",
                "size": "xxs",
                "color": "#FFFFFF",
                "wrap": True,
                "offsetStart": "2px",
                "offsetTop": "2px"
              }
            ],
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "width": "148px",
            "height": "38px",
            "position": "absolute",
            "offsetTop": "148px",
            "offsetStart": "3px",
            "backgroundColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "SUPPORT  BYE: TEAM TERMUX",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "7px"
              }
            ],
            "borderColor": "#FF00FF",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "width": "150px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "210px",
            "offsetStart": "2px",
            "backgroundColor": "#2E8B57"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CREATOR",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "6px"
              }
            ],
            "borderColor": "#FF00FF",
            "cornerRadius": "5px",
            "borderWidth": "1px",
            "width": "70px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "188px",
            "offsetStart": "2px",
            "backgroundColor": "#800080"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ORDER",
                "size": "xxs",
                "color": "#FFFFFF",
                "offsetTop": "2px",
                "offsetStart": "15px"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "cornerRadius": "5px",
            "width": "76px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "188px",
            "offsetStart": "75px",
            "backgroundColor": "#0000FF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": []
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://www.blackxperience.com/assets/blackattitude/blacktips//cover-wa-300x300.jpg",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "20px",
            "width": "20px",
            "cornerRadius": "100px",
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQBeiKDJTqSrl0DE7K8pIaNYe1uUsXNVqz9dg&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "20px",
            "width": "20px",
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "100px",
            "borderColor": "#FFFF00",
            "offsetTop": "124px",
            "offsetStart": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://play-lh.googleusercontent.com/74iMObG1vsR3Kfm82RjERFhf99QFMNIY211oMvN636_gULghbRBMjpVFTjOK36oxCbs",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "cornerRadius": "100px",
            "borderWidth": "1px",
            "width": "20px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "70px",
            "height": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRK_yDc42L7ssYuvce24MqTgvesOvYZgQIi8Q&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "borderWidth": "1px",
            "cornerRadius": "100px",
            "width": "20px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTBtVrDomP1KCahV0TSV9hITha-PhnvetHd0g&usqp=CAU",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "borderColor": "#FFFF00",
            "cornerRadius": "100px",
            "borderWidth": "1px",
            "width": "20px",
            "height": "20px",
            "position": "absolute",
            "offsetTop": "124px",
            "offsetStart": "130px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#FFFF00",
        "cornerRadius": "10px",
        "borderWidth": "2px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://wa.me/message/ANCIF474MS6OL1"
        }
      }
    }
  ]
}
}
                             sendTemplate(to, data)
                         if c == "AUDIO" and b == "S":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                           #  #cover = cl.getProfileCoverURL(sender)
                             time.sleep(1)
                             data = {
                                        "type": "flex",
                                        "altText": "〔 TEAM TERMUX V 3 〕",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "4:3",
            "gravity": "top",
            "url": "https://i.ibb.co.com/QNFxN8N/1652366614290.jpg",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Detect call"
              },
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "size": "full",
                "aspectMode": "cover",
                "offsetBottom": "22px"
              }
            ],
            "position": "absolute",
            "width": "66px",
            "height": "66px",
            "borderWidth": "1px",
            "borderColor": "#FF8C00",
            "cornerRadius": "5px",
            "offsetTop": "120px",
            "offsetStart": "153px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Detect call"
              },
              {
                "type": "image",
                "animated": True,
                "url": "https://i.ibb.co.com/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectMode": "cover",
                "offsetBottom": "22px"
              }
            ],
            "position": "absolute",
            "width": "41px",
            "height": "41px",
            "borderWidth": "1px",
            "borderColor": "#FF8C00",
            "cornerRadius": "100px",
            "offsetBottom": "140.5px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxs",
                "color": "#ffffff",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "offsetEnd": "150px",
            "offsetTop": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(msg._from).displayName),
                "color": "#ffffff",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "offsetTop": "63px",
            "offsetStart": "47px",
            "width": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "color": "#ffffff",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "cornerRadius": "5px",
            "borderWidth": "1px",
            "offsetTop": "116px",
            "offsetStart": "60px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Cari tikungan",
                "size": "xxs",
                "color": "#ffffff"
              }
            ],
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "offsetTop": "142px",
            "offsetStart": "62px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Dimulai",
                "color": "#ffffff",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "1px",
            "offsetTop": "166px",
            "offsetEnd": "148px"
          }
        ],
        "paddingAll": "0px",
        "height": "195px",
        "borderWidth": "1px",
        "borderColor": "#FF8C00",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://wa.me/message/ANCIF474MS6OL1"
        }
      }
    }
  ]
}
}
                             sendTemplate(to, data)
                         if c == "AUDIO" and b == "E":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             ##cover = cl.getProfileCoverURL(sender)
                             time.sleep(1)
                             data = {
                                        "type": "flex",
                                        "altText": "〔 TEAM TERMUX V 3 〕",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "4:3",
            "gravity": "top",
            "url": "https://i.ibb.co.com/QNFxN8N/1652366614290.jpg",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Detect call"
              },
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                "size": "full",
                "aspectMode": "cover",
                "offsetBottom": "22px"
              }
            ],
            "position": "absolute",
            "width": "66px",
            "height": "66px",
            "borderWidth": "1px",
            "borderColor": "#FF8C00",
            "cornerRadius": "5px",
            "offsetTop": "120px",
            "offsetStart": "153px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Detect call"
              },
              {
                "type": "image",
                "animated": True,
                "url": "https://i.ibb.co.com/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectMode": "cover",
                "offsetBottom": "22px"
              }
            ],
            "position": "absolute",
            "width": "41px",
            "height": "41px",
            "borderWidth": "1px",
            "borderColor": "#FF8C00",
            "cornerRadius": "100px",
            "offsetBottom": "140.5px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxs",
                "color": "#ffffff",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "offsetEnd": "150px",
            "offsetTop": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(msg._from).displayName),
                "color": "#ffffff",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "offsetTop": "63px",
            "offsetStart": "47px",
            "width": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ""+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "color": "#ffffff",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "cornerRadius": "5px",
            "borderWidth": "1px",
            "offsetTop": "116px",
            "offsetStart": "60px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "UDAH DAPA Kojoman",
                "size": "xxs",
                "color": "#ffffff"
              }
            ],
            "borderWidth": "1px",
            "cornerRadius": "5px",
            "offsetTop": "142px",
            "offsetStart": "62px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Dimulai",
                "color": "#ffffff",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "cornerRadius": "1px",
            "offsetTop": "166px",
            "offsetEnd": "148px"
          }
        ],
        "paddingAll": "0px",
        "height": "195px",
        "borderWidth": "1px",
        "borderColor": "#FF8C00",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://wa.me/message/ANCIF474MS6OL1"
        }
      }
    }
  ]
}
}


                             sendTemplate(to, data)
        if op.type in [26, 25]:
            if op.type == 26: print ("[26] RECEIVE MESSAGE")
            else: print ("[25] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = receiver
            try:
                if msg.contentType == 0:
                    if msg.toType == 2:
                        if wait["quis"] == True:
                            contactlist = cl.getAllContactIds()
                            kontak = [cont.mid for cont in cl.getContacts(contactlist)]
                            for i in range(len(quisdata[to]['asw'])):
                                if text.lower() == quisdata[to]['asw'][i].lower() and sender and clMID and quisdata[to]['saklar'] == True:
                                    if sender:
                                        wnr = cl.getContact(sender).displayName
                                        wna = cl.getContact(sender)
                                        if wnr in quisdata[to]['point']:
                                            quisdata[to]['point'][wnr] += 1
                                        else:
                                            quisdata[to]['point'][wnr] = 1
                                        if i != len(quisdata[to]['asw']):
                                            quisdata[to]['tmp'][i] = str(i+1)+'. '+quisdata[to]['asw'][i]+' (1)'+' ['+wnr+']'
                                            quisdata[to]['asw'][i] = quisdata[to]['asw'][i]+' (*)'
                                        else:
                                            quisdata[to]['tmp'].remove(str(quisdata[to]['tmp'][i]))
                                            quisdata[to]['tmp'].append(str(i+1)+'. '+quisdata[to]['asw'][i]+' (1)'+' ['+wnr+']')
                                            quisdata[to]['asw'].remove(str(quisdata[to]['asw'][i]))
                                            quisdata[to]['tmp'].append(quisdata[to]['asw'][i]+' (*)')
                                        rsl,rnk = '',''
                                        for j in quisdata[to]['tmp']:
                                            rsl += j+'\n'
                                        for k in quisdata[to]['point']:
                                            rnk += 'zulkifli QUIS '+k+' : '+str(quisdata[to]['point'][k])+'\n'
                                        if '_________' in str(quisdata[to]['tmp']):
                                            isi = str(quisdata[to]['quest'])+'\n'+rsl
                                            sendTextTemplateB(to, isi)
                                        else:
                                            quisdata[to]['saklar'] = False
                                            isi = str(quisdata[to]['quest'])+'\n'+rsl
                                            sendTextTemplateB(to, isi)
                                            sendTextTemplateB(to, 'Papan Poin :\n'+rnk)
                                            sendTextTemplateB(to, 'Ketik /mulai untuk Pertanyaan Lainnya.')
                                    else:
                                        sendMention(to, sender, '', 'Anda belum menambahkan TEAM TERMUX Kuis sebagai teman, Untuk ikut bermain silahkan tambahkan TEAM TERMUX Kuis sebagai teman.')
            except Exception as e:
                cl.log("[RECEIVE_MESSAGE] ERROR : " + str(e))
                traceback.print_tb(e.__traceback__)
            if msg.toType == 0 and sender:
                to = sender
            else:
            	to = receiver
            if receiver in temp_flood:
                if temp_flood[receiver]["expire"] == True:
                    if temp_flood[receiver]["expire"] >= 20:
                        temp_flood[receiver]["expire"] = False
                        temp_flood[receiver]["time"] = time.time()
                        #sendTextTemplateB(to, "TEAM TERMUX kembali aktif.")
                    return
                elif time.time() - temp_flood[receiver]["time"] <= 5:
                    temp_flood[receiver]["flood"] += 1
                    if temp_flood[receiver]["flood"] >= 20:
                        temp_flood[receiver]["flood"] = 0
                        temp_flood[receiver]["expire"] = True
                        #ret_ = "Spam terdeteksi, TEAM TERMUX akan silent selama 30 detik pada ruangan ini atau ketik Open untuk mengaktifkan kembali."
                        sendTextTemplateB(to, str(ret_))
                else:
                     temp_flood[receiver]["flood"] = 0
                     temp_flood[receiver]["time"] = time.time()
            else:
                temp_flood[receiver] = {
    	            "time": time.time(),
    	            "flood": 0,
    	            "expire": False
                }
            if text is None: return
            if text.lower() == "/mulai" or text.lower() == '/mulai ' or text.lower() == 'mulai' or text.lower() == 'gas ' or text.lower() == 'gas' or text.lower() == 'go ' or text.lower() == 'go' or text.lower() == 'mulai ' and sender:
                if wait["quis"] == True:
                    if quisdata[to]['saklar'] == False:
                        quisdata[to]['saklar'] = True
                        getQuest(to)
                        aa = ''
                        for aswr in quisdata[to]['tmp']:
                            aa += aswr+'\n'
                            q = quisdata[to]['quest']+'\n'+aa
                        sendTextTemplateB(to, q)
                    else:
                        aa = '' 
                        for aswr in quisdata[to]['tmp']:
                            aa += aswr+'\n'
                        q = quisdata[to]['quest']+'\n'+aa
                        sendTextTemplateB(to, q)
                        sendTextTemplateB(to, 'Ketik /nyerah untuk mengakhiri pertanyaan ini.')
            elif text.lower() == '/nyerah' or text.lower() == '/nyrah' or text.lower() == '/nyerah ' and sender:
                if wait["quis"] == True:
                    if quisdata[to]['saklar'] == True:
                        rnk,asd = '',''
                        quisdata[to]['saklar'] = False
                        for j in range(len(quisdata[to]['tmp'])):
                            if '_________' in quisdata[to]['tmp'][j]:
                                if j != len(quisdata[to]['tmp']):
                                    quisdata[to]['tmp'][j] = str(j+1)+'. '+quisdata[to]['asw'][j]+' (*system)'
                                else:
                                    quisdata[to]['tmp'][j].remove(str(quisdata[to]['tmp'][j]))
                                    quisdata[to]['tmp'][j].append(str(j+1)+'. '+quisdata[to]['asw'][j]+' (*system)')
                        for m in quisdata[to]['tmp']:
                            asd += m+'\n'
                        for k in quisdata[to]['point']:
                            rnk += 'zulkifli QUIS '+k+' : '+str(quisdata[to]['point'][k])+'\n'
                        sendTextTemplateB(to, str(quisdata[to]['quest'])+'\n'+asd)
                        sendTextTemplateB(to, 'Papan Poin :\n'+rnk)
                        sendTextTemplateB(to, 'Ketik /mulai untuk Pertanyaan Lainnya')
                    else:
                        sendTextTemplateB(to, 'Game belum di mulai.')
                        sendTextTemplateB(to, 'Ketik /mulai untuk memulai permainan.')
            elif text.lower() == "/next" or text.lower() == '/next' or text.lower() == 'next' or text.lower() == 'lanjut' and sender:
                if wait["quis"] == True:
                    if quisdata[to]['saklar'] == True:
                        getQuest(to)
                        aa = ''
                        for aswr in quisdata[to]['tmp']:
                            aa += aswr+'\n'
                            q = quisdata[to]['quest']+'\n'+aa
                        sendTextTemplateB(to, q)
                    else:
                        sendTextTemplateB(to, 'game belom mulai bro.')
            elif text.lower() == '/reset' and sender:
                if wait["quis"] == True:
                    quisdata[to]['point'] = {}
                    quisdata[to]['saklar'] = False
                    sendTextTemplateB(to, 'Permainan telah di reset.')
                    sendTextTemplateB(to, 'Ketik /mulai untuk memulai permainan.')


            elif text.lower() == 'helpquis' and sender:
              if wait["quis"] == True:
                    sendTextTemplateB(to, 'Ketik /mulai untuk memulai permainan.')
                    sendTextTemplateB(to, '/mulai ')
                    sendTextTemplateB(to, '/nyerah ')
                    sendTextTemplateB(to, '/next ')
                    sendTextTemplateB(to, 'laporkan ')
                    sendTextTemplateB(to, 'rek ')


            elif "u" in msg.text.lower():
              if wait["nganu"] == True:
                if msg._from in sender:
                    mid = re.compile(r'u\w{32}')
                    mymid = mid.findall(text)
                    n_links = []
                    for l in mymid:
                        if l not in n_links:
                            n_links.append(l)
                    if n_links == []:
                        pass
                    else:
                        for midd in n_links:
                            time.sleep(0.2)
                            cl.sendContact(to, midd)
                        #cl.removeAllMessages(to)

            elif text.lower() == 'laporkan' and sender not in clMID:
                cl.sendMessage(to, "Untuk melaporkan masalah yang di alami atau ingin memberikan saran, kalian bisa langsung menghubungi admin melalui kontak dibawah ini :")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == '/laporkan' and sender not in clMID:
                cl.sendMessage(to, "Untuk melaporkan masalah yang di alami atau ingin memberikan saran, kalian bisa langsung menghubungi admin melalui kontak dibawah ini :")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == 'rek' and sender not in clMID:
                cl.sendMessage(to, "DANA :  0857-5707-6639 \nNama  : ZULKIFLI MOKOAGOW\nWa. : +62 857-5707-6639 ")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == 'dana' and sender not in clMID:
                cl.sendMessage(to, "DANA :  0857-5707-6639 \nNama  : ZULKIFLI MOKOAGOW\nWa. : +62 857-5707-6639 ")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == 'sponsor cowo' and sender not in clMID:
                cl.sendMessage(to, "TEAM TERMUX")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")
                cl.sendContact(to, "u7f7a535b2fc2b738585dababcecd8439")
                cl.sendContact(to, "u9bef22a6f6ee633bdf4dddd6572dcd3f")

            elif text.lower() == 'sponsor cewe' and sender not in clMID:
                cl.sendMessage(to, "TEAM TERMUX")
                cl.sendContact(to, "ub3a4144fd62686316824b3e1c39a5f04")
                cl.sendContact(to, "u9aa1500e7383f6c22fa9220cfe9784ce")
                cl.sendContact(to, "u4bf02fa0f10b66844ce3daf390e984d2")
                cl.sendContact(to, "ud97cb23f659bc57bdc14b090569c7904")
                cl.sendContact(to, "u862ad072aceb7ce6009fb175e386a566")
                cl.sendContact(to, "u01b2583b98a923a9e91dffd86877842f")
                cl.sendContact(to, "u02913d0c3f45eb23aa4f586fd6f6c62b")
                cl.sendContact(to, "u3068a0b6958068c9c3002ae5d9cc9a33")
                cl.sendContact(to, "uef44eba9bf0ba2cdfdd64135241a59a9")
                cl.sendContact(to, "u63576cdc20dbb3c978b41d3a593ca70b")

            elif text.lower() == 'jawaban' and sender not in clMID:
                cl.sendMessage(to, "apa yang dilakukan ketika ketahuan pacar sedang berjalan dengan mantan?*salah tingkah*kabur*menghindar*bohong*diam*pasrah *menjelaskan*minta maaf")
                cl.sendMessage(to, "selain tidur apa yang bisa orang lakukan di atas tempat tidur?*membaca*nonton tv*ngobrol*melamun*bermesraan*telepon")
                cl.sendMessage(to, "sebutkan tempat-tempat kencan?*bioskop*pantai*warnet*restorant*rumah *toilet")
                cl.sendMessage(to, "sebutkan sesuatu yang sekali pakai langsung buang?*pembalut*tisu*popok*korek*teh celup*kondom")
                cl.sendMessage(to, "bagaimana cara mendekati orang yang ditaksir?*chatt*ngobrol*beri perhatian*rayu*menyapa*minta kenalan*antar pulang")
                cl.sendMessage(to, "perasaan apa yang ada bila mau kencan pertama?*grogi*malu*takut*senang")
                cl.sendMessage(to, "apa yg di lakukan saat pertama kali pacaran?*gandengan tangan*makan*duduk*ciuman")
                cl.sendMessage(to, "selain ibu kandung, siapa yang dipanggil ibu?*guru*mertua*atasan*tiri")
                cl.sendMessage(to, "selain cinta apa yang dibutuhkan agar pernikahan bahagia?*Kejujuran*Materi*Anak*Kepercayaan")
                cl.sendMessage(to, "tempat untuk pacaran?*Rumah*Kuburan*Sawah*Rumah sakit")
                cl.sendMessage(to, "dimana orang biasa mendengarkan musik?*kamar*pub*diskotik*cafe*mobil")
                cl.sendMessage(to, "acara tv disalurkan indosiar?*patroli*sinetron*sinetron*ftv unggulan*power ranger*ultraman")
                cl.sendMessage(to, "batas kecepatan mobil di jalan tol?*60 km/jam*80km/jam*100 km/jam*120 km/jam*70 km/jam")
                cl.sendMessage(to, "berhubungan dengan sumatra barat?*jam gadang*tugu bonjol*benteng fort de kock*danau maninjau*ngarai sianok*rendang")
                cl.sendMessage(to, "tempat apa yg dipilih orang untuk berpetualang?*hutan*gunung*sungai*laut*padang pasir")
                cl.sendMessage(to, "dimana tempat nonton film?*bioskop*kamar*komputer*lapangan*dimana-mana*rumah teman*kost teman")
                cl.sendMessage(to, "penyanyi luar cewek?*madona*mariah carey*britney spears*christina aguilera*shania twain*celine dion")
                cl.sendMessage(to, "organ tubuh manusia yg berpasangan?*tangan*kaki*mata*telinga*paru-paru*ginjal*buah zakar")
                cl.sendMessage(to, "bagian dari harimau?*belang*bulu*ekor*cakar*taring")
                cl.sendMessage(to, "apa yang berhubungan dengan sangkuriang?*gunung*perahu*legenda*anjing*dayang sumbi*durhaka*tangkuban")
                cl.sendMessage(to, "transportasi di darat?*bus*becak*bus*kereta api*mobil*motor*bemo*ojek*bajaj*sepeda motor*dokar*taksi*kapal*angkutan umum")
                cl.sendMessage(to, "nama operator hp?*indosat*mentari*telkomsel*mobile 8")
                cl.sendMessage(to, "bahan bakar yang berasal dari alam?*bensin*solar*batu bara*minyak tanah*lpg")
                cl.sendMessage(to, "penduduk negara mana yang biasanya memakai pakaian negaranya?*india*indonesia*jepang*arab*vietnam")
                cl.sendMessage(to, "berapa juta sel dalam otak manusia?*1000 juta")
                cl.sendMessage(to, "merk gel rambut?*gatsby*brisk*johny andrean*rudy hadisuwarno*clear")
                cl.sendMessage(to, "software chatting?*mirc*yahoo messenger*msn*google talk*skype*camfrog*live connector*icq*windows live")
                cl.sendMessage(to, "seorang sahabat?*dapat diajak curhat*saling berbagi*bukan pasangan")
                cl.sendMessage(to, "personil ngelaba?*eko*parto*akri")
                cl.sendMessage(to, "yang biasa mengambang di sungai?*bangkai*pakaian*mayat*sampah*kayu*tokai")
                cl.sendMessage(to, "aduh aku digigit....*nyamuk*anjing*ular*tikus*pacarku")
                cl.sendMessage(to, "apa saja kelemahan polisi lalu lintas?*kena rasia satgas*polisi provos lewat*liat pelat nomor terbalik")
                cl.sendMessage(to, "nama kapal berdasarkan pelayarannya?*Kapal permukaan*kapal selam*Kapal mengambang*Kapal bantalan udara")
                cl.sendMessage(to, "berhubungan dengan musim kemarau?*kering*panas*kebakaran")
                cl.sendMessage(to, "julukan club real madrid C.F?*The real samba*Los Galacticos*Los blancos*Los merengueZ*The white*El real")
                cl.sendMessage(to, "nama danau?*toba*gajah mungkur*jatiluhur*towuti")
                cl.sendMessage(to, "tempat yang dijadikan ajang maksiat?*hotel*tempat judi*diskotik*pub*bar*lokasi pelacuran")
                cl.sendMessage(to, "tempat wisata di belanda?*madame tussaud*keunkenhoff*madurondam utrecht*vlieland")
                cl.sendMessage(to, "situs berita?*bolanews*kompas*detik")
                cl.sendMessage(to, "jenis sampah?*organik*unorganik*b3")
                cl.sendMessage(to, "apa saja yang dibeli ketika ingin menonton bioskop?*snack*minuman*popcorn*tissu*permen*roti")
                cl.sendMessage(to, "sebutkan lagu linkin park?*numb*faint*breaking the habbit*somewhere i belong*paper cut")
                cl.sendMessage(to, "Istilah Samurai?*buke*kabukimono*musha*si*mononofu*tsuwamono")
                cl.sendMessage(to, "universitas Palembang?*iba*mdp*igm*musi*unsri")
                cl.sendMessage(to, "mall di surabaya/ semarang?*java mall*ciputra*sri ratu*matahari*ramayana")
                cl.sendMessage(to, "mobil keluaran honda?*stream*civic*cr-v*jazz*city")
                cl.sendMessage(to, "rokok di indonesia?*djarum*marlboro*a mild*lucky strike*dji sam soe*sampoerna")
                cl.sendMessage(to, "sebutkan alat penunjuk arah?*bayangan*bulan*matahari*kompas")
                cl.sendMessage(to, "penyanyi seksi keluaran hollywood?*britney spears*shakira*jennifer lopez*christina aguilera*madonna")
                cl.sendMessage(to, "berhubungan dgn kombinasi*warna*pakaian*pukulan*tendangan")
                cl.sendMessage(to, "tokoh dlm Pilm peterpan?*Peterpan*Wendy*Kapten hook*Tinkerbell")
                cl.sendMessage(to, "kepanjangan pasutri?*pasangan suami istri*pasangan suami takut istri")
                cl.sendMessage(to, "mainan apa saja yang ada di dunia fantasi?*halilintar*niagara*arung jeram*kora-kora*pontang-panting")
                cl.sendMessage(to, "berapa lama orang menjemur kasur?*satu jam*empat jam*sehari")
                cl.sendMessage(to, "nama lain alat kelamin?*burung*rudal*tempek*apem")
                cl.sendMessage(to, "disaat apa orang mematikan ponsel?*ujian*kuliah*pacaran*ibadah*tidur*rapat")
                cl.sendMessage(to, "batuan mineral yg berharga tinggi*berlian*intan*mutiara*jamrud*permata*delima")
                cl.sendMessage(to, "nama pasukan yang di pimpin oleh letnan jendral soeharto pada waktu pemberihan ormas pki?*trisula")
                cl.sendMessage(to, "nama bulan dalam bahasa jepang?|Ichigatsu*Nigatsu*Sangatsu*Shigatsu*Gogatsu*Rokugatsu*Nanagatsu*Hachigatsu*Kugatsu*Jugatsu*Juuichigatsu*Juunigatsu")
                cl.sendMessage(to, "tanda kendaraan?*dk*cd*b*aa*d*dd*bh*bg*h*s*t*k*f*ab*ad*kt*r*L*dh*g*be")
                cl.sendMessage(to, "yang mengaku sebagai jendral nasution?*pierre tendean")
                cl.sendMessage(to, "negara afrika utara?*mesir*aljazair*libya*maroko*tunisia*mauritania")
                cl.sendMessage(to, "penerbit buku di INDONESIA?*erlangga*gramedia*penerbit andi*intan pariwara*grafindo")
                cl.sendMessage(to, "tempat wisata di indonesia?*bali*danau toba*malioboro*puncak*borobudur*ancol*saritem*cibubur*dolly*dunia fantasy")
                cl.sendMessage(to, "cara efektif membunuh nyamuk*semprot*lempar*cablek*injek*tabok*pites*gigit")
                cl.sendMessage(to, "mall/pusat perbelanjaan yang ada di Surabaya?*Tunjungan plasa*Delta plasa*Galaxy mall*Jembatan Merah plasa*PTC*Giant*Carefour")
                cl.sendMessage(to, "mata uang yg berawalan R*rupiah*riyal*riel*rupee*ringgit")
                cl.sendMessage(to, "senjata tradisional indonesia (2)?*kujang*mandau*keris*badik*rudus*parang*pehduk payan*golok*terapang*kelewang*kuduk")
                cl.sendMessage(to, "personil laruku?*yuki*teru*hyde*ken")
                cl.sendMessage(to, "tingkatan kelas dalam tinju?*berat*welter*bantam*berat ringan*penjelajah")
                cl.sendMessage(to, "nama burung?*kutilang*beo*cendrawasih*elang*pipit*gagak*kakatua")
                cl.sendMessage(to, "macam tense inggris?*perfect tense*past tense*present tense*future tense")
                cl.sendMessage(to, "nama pelawak indonesia yang sudah alm?*benyamin*dono*kasino*ishak")
                cl.sendMessage(to, "profesi yg memerlukan orang dengan tubuh tinggi*tentara*peragawati*model*pramugari*pilot*pramugara*polisi")
                cl.sendMessage(to, "personil UNGU?*pasha*enda*onci*makki*rowman")
                cl.sendMessage(to, "yang dapat dimakan campuran dengan roti*Selada*Mentega*telor*Coklat*Selai*Keju*Sosis*daging ham*susu")
                cl.sendMessage(to, "service dalnet?*memoserv*chanserv*nickserv*operserv")
                cl.sendMessage(to, "teman donald bebek?*lang ling lung*agus angsa*untung*desi")
                cl.sendMessage(to, "nama negara eropa?*inggris*italia*belanda")
                cl.sendMessage(to, "merk baterai di Indonesia*National*ABC*Energizer*Eveready*Panasonic*Hitachi")
                cl.sendMessage(to, "negara bagian australia?*sydney*hobart*adelaide*melbourne*perth*brisbane")
                cl.sendMessage(to, "tokoh kartun jepang?*doraemon*sinchan*kenji*sailormoon*candy-candy")
                cl.sendMessage(to, "mata air?*sungai*laut *danau*air tanah*samudera")
                cl.sendMessage(to, "ukuran kertas?*a4*legal*a5*letter*executive")
                cl.sendMessage(to, "susu sekarang ada berbagai rasa, apa saja itu?*manis*coklat*kopi*strawberry*mocca*grape*nanas*pisang")
                cl.sendMessage(to, "raja kerajaan singasari?*tunggul ametung")
                cl.sendMessage(to, "kenapa orang makan?*lapar*stress*gengsi*waktunya makan*kerja sales*ikut sayembara*pengen gemuk")
                cl.sendMessage(to, "apa yg biasanya sering lupa dibawa*uang*dompet*handphone*kunci*kacamata*rokok*stnk")
                cl.sendMessage(to, "macam - macam pisang?*raja*ambon*sepatu*tanduk*mas *molen")
                cl.sendMessage(to, "jenis makanan atau minuman yang disukai untuk berbuka puasa?*air putih*teh hangat*es kelapa muda*gorengan*kolak")
                cl.sendMessage(to, "nama mobil terkenal?*honda*mercy*ferarri*bmw*jaguar")
                cl.sendMessage(to, "tempat Kencan Paling Enak?*bioskop*pantai*warnet*restorant*rumah*toilet")
                cl.sendMessage(to, "presiden congo?*laurent kabila")
                cl.sendMessage(to, "ilmu yang digunakan dukun?*jagaraga*lembu sakilan*jaran goyang*semar mesem*raga sukma")
                cl.sendMessage(to, "jenis minuman alkohol tinggi?*whiski*martell*arak*martini*sake*jack daniel*soju*long island")
                cl.sendMessage(to, "dunia lain?*fatamorgana*mimpi*dimensi lain")
                cl.sendMessage(to, "struktur sel?*membran sel*sitoplasma*nukleus*organel")
                cl.sendMessage(to, "nama pemain bulutangkis indonesia?*susi susanti*alan budikusuma*djoko suprianto*ricky subagja")
                cl.sendMessage(to, "makanan khas sulawesi?*buras*kapurung*barongkong*coto makassar*pisang ijo")
                cl.sendMessage(to, "hewan mamalia?*anjing*kucing*singa*kelinci*beruang")
                cl.sendMessage(to, "sesuatu yang diangkut dengan truk?*perabotan*kayu*beras*besi*baja")
                cl.sendMessage(to, "apa reaksi suami waktu malam pertama anda membuka pakaian?*marah*tertawa*bingung*pergi*cuek*nangis*menampar")
                cl.sendMessage(to, "kalo di rumah sendirian kamu bakal*Tidur*Belajar*Baca buku*Telpon*Dengerin musik*Seks")
                cl.sendMessage(to, "merek hardisk*quantum*seagate*maxtor*wdc*mdt")
                cl.sendMessage(to, "ciri gajah?*belalai*gading*telinga lebar*besar*kulit tebal")
                cl.sendMessage(to, "sarjana jurusan non tehnik?*ekonomi*psikolog*hukum*kesenian*designer*sastra")
                cl.sendMessage(to, "makanan ringan yang biasa dimakan anak2?*es*makroni*agar-agar*coklat*permen*chiki")
                cl.sendMessage(to, "makanan - makanan pokok di dunia*nasi*kentang*jagung*sagu*mie*sayur*roti*gandum")
                cl.sendMessage(to, "anggota keluarga the osbornes*kelly*ozzy*jack*sharon*aimee")
                cl.sendMessage(to, "hiburan apa yang ada di pesta ulang tahun?*band*badut*sulap*kuis*game")
                cl.sendMessage(to, "siklus windu?*dal*alip*be*ehe*wawu*jimawal*jimakir*je")
                cl.sendMessage(to, "fasilitas beternak ikan?*jala*tambak*saringan")
                cl.sendMessage(to, "apa yg biasa dilakukan orang bila ngantuk*tidur*menguap*minum kopi*cuci muka*ke tempat tidur*minum susu*denger musik")
                cl.sendMessage(to, "majalah komputer di indonesia?*linux*info komputer*chip*pc media*file magazine")
                cl.sendMessage(to, "jenis penyakit kulit?*panu*kurap*gatal gatal*koreng*kadas*kutu air")
                cl.sendMessage(to, "ciri orang emosi?*main pukul*pergi lokalisasi*bunuh orang")
                cl.sendMessage(to, "suara yang ditakuti anak2?*anjing*hantu*petir*harimau")
                cl.sendMessage(to, "corak rasa ice cream?*susu*strawberry*moka*lemon*nanas*jeruk*vanila")
                cl.sendMessage(to, "sebutkan acara tv favorit?*kartun*kuis*telenovela*sinetron*olahraga*film seri")
                cl.sendMessage(to, "mall di orchad road di singapore?*i-setan*takhasimaya*lucky plaza*tang plaza")
                cl.sendMessage(to, "warnet di yogyakarta?*hijaunet*hasilnet*nasanet*neptune*planet*ahanetwiskanet*thunder*ANGELnet")
                cl.sendMessage(to, "nama pengarang novel terkenal di dunia?*jhon grisham*alfred hitchok*barbara cartland*sidney sheldon")
                cl.sendMessage(to, "ciri-ciri negara mesir?*piramida*sungai nil*firaun*mumi*sphinx")
                cl.sendMessage(to, "komentar kamu setelah liat pilm Independence Day*Bagus*Keren*Tegang*Seru*Biasa aja*jelek")
                cl.sendMessage(to, "animals on the sea?*crab*fish*shark*sealion*dolphin*turtle")
                cl.sendMessage(to, "olahraga yang berbahaya?*arung jerang*tinju*balap mobil*balap motor*ski salju*panjat tebing")
                cl.sendMessage(to, "kalo cewe liat tikus*lari*teriak*pingsan*loncat*kaget")
                cl.sendMessage(to, "apa saja keuntungan menjadi orang gila?*terkenal*masuk surga*santai membunuh*makan gratis*selalu riang*ditakuti preman*pusat perhatian")
                cl.sendMessage(to, "yang biasa ada di diskotik?*psk*dj*minuman*lampu disko*gigolo*orang mabuk")
                cl.sendMessage(to, "makanan dengan kandungan karbohidrat*nasi*roti*kentang*sagu*jagung")
                cl.sendMessage(to, "makanan yang termasuk gorengan?*ubi*tahu*tempe*pisang*cireng*bakwan")
                cl.sendMessage(to, "siapakah tokoh terkenal nyata/fiksi yang berhubungan dengan cinta?*romeo dan juliet*rama sinta*arjuna")
                cl.sendMessage(to, "jenis lagu yang disukai anak muda?*rnb*pop*rock*house music*hiphop")
                cl.sendMessage(to, "nama negara yang punya hak VETO PBB dalam bahasa inggris*China*France*USA*RUSSIA*England")
                cl.sendMessage(to, "Artis terseksi di Indonesia*ayu ashari*sarah azhari*sophia latjuba*paramitha rusadi*ratna listi")
                cl.sendMessage(to, "yang berhubungan dgn club malam / diskotik?*rasia*narkoba*minuman keras*orang mabuk*dj*dugem*jablai")
                cl.sendMessage(to, "kebiasaan waktu tidur?*mendengkur*menguap*ngiler")
                cl.sendMessage(to, "jenis tv televisi?*politron*sony*panasonic*toshiba*samsung*sanken*akira")
                cl.sendMessage(to, "Jenis-jenis energi*listrik*panas bumi*gas alam*tenaga air*batu bara")
                cl.sendMessage(to, "apa yang dilakukan orang di stadion sambil menunggu pertandingan dimulai*ngobrol*makan*minum*pemanasan*tidur*ngemil*baca koran")
                cl.sendMessage(to, "yang dilakukan orang pada saat sedang menunggu*merokok*membaca*melamun*cemas")
                cl.sendMessage(to, "macam pajak*barang mewah*bumi dan bangunan*undian*penghasilan*barang mewah")
                cl.sendMessage(to, "cara2 bunuh diri*gantung diri*minum baygon*potong nadi*lompat*belajar matematika*tembak kepala sendiri")
                cl.sendMessage(to, "apa yang dikatakan cowo utk melamar kekasih?*saya hanya bawa cinta*bolehkan saya mempersunting putri anda")
                cl.sendMessage(to, "jenis hewan vertebrata?*reptilia*aves*amphibia*mamalia*pisces")
                cl.sendMessage(to, "barang bekas apa yg biasanya dijual oleh tukang loak di pinggir jalan*Sepatu*Sandal*Kardus*Jaket*Tape*Onderdil")
                cl.sendMessage(to, "jenis anjing terkenal?*dalmation*buldog*pom")
                cl.sendMessage(to, "fungsi fungsional handphone?*sms*telepon*foto*mms*internet*denger musik*main game*bergaya*chatting*modem")
                cl.sendMessage(to, "apa yang terjadi jika sakit hati?*nangis*bunuh diri*mabuk*curhat*stress*jadi gila*sedih")
                cl.sendMessage(to, "macam-macam tepung?*kanji*beras*terigu")
                cl.sendMessage(to, "tempat wisata di surabaya?*njarak*kenjeran*kebun binatang surabaya*taman remaja*dolly")
                cl.sendMessage(to, "alat musik sederhana?*gitar*drum*seruling*terompet*harmonika*pianika*angklung")
                cl.sendMessage(to, "pemeran si midun?*sandi nayoan")
                cl.sendMessage(to, "jenis ilmu hitan?*pelet*santet*guna guna*pesugihan")
                cl.sendMessage(to, "universitas di surabaya?*unair*unesa*upn*ubaya*stiesia*petra*itats*its")
                cl.sendMessage(to, "makanan yang ada di warteg*Rawon*Soto*Krengsengan*Pecel*Kari ayam*Sayur lodeh")
                cl.sendMessage(to, "1 + 1 ?*2*dua")
                cl.sendMessage(to, "2 + 2 = 4 BERAPA?*24")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == 'jawaban kuis' and sender not in clMID:
                cl.sendMessage(to, "apa yang dilakukan ketika ketahuan pacar sedang berjalan dengan mantan?*salah tingkah*kabur*menghindar*bohong*diam*pasrah *menjelaskan*minta maaf")
                cl.sendMessage(to, "selain tidur apa yang bisa orang lakukan di atas tempat tidur?*membaca*nonton tv*ngobrol*melamun*bermesraan*telepon")
                cl.sendMessage(to, "sebutkan tempat-tempat kencan?*bioskop*pantai*warnet*restorant*rumah *toilet")
                cl.sendMessage(to, "sebutkan sesuatu yang sekali pakai langsung buang?*pembalut*tisu*popok*korek*teh celup*kondom")
                cl.sendMessage(to, "bagaimana cara mendekati orang yang ditaksir?*chatt*ngobrol*beri perhatian*rayu*menyapa*minta kenalan*antar pulang")
                cl.sendMessage(to, "perasaan apa yang ada bila mau kencan pertama?*grogi*malu*takut*senang")
                cl.sendMessage(to, "apa yg di lakukan saat pertama kali pacaran?*gandengan tangan*makan*duduk*ciuman")
                cl.sendMessage(to, "selain ibu kandung, siapa yang dipanggil ibu?*guru*mertua*atasan*tiri")
                cl.sendMessage(to, "selain cinta apa yang dibutuhkan agar pernikahan bahagia?*Kejujuran*Materi*Anak*Kepercayaan")
                cl.sendMessage(to, "tempat untuk pacaran?*Rumah*Kuburan*Sawah*Rumah sakit")
                cl.sendMessage(to, "dimana orang biasa mendengarkan musik?*kamar*pub*diskotik*cafe*mobil")
                cl.sendMessage(to, "acara tv disalurkan indosiar?*patroli*sinetron*sinetron*ftv unggulan*power ranger*ultraman")
                cl.sendMessage(to, "batas kecepatan mobil di jalan tol?*60 km/jam*80km/jam*100 km/jam*120 km/jam*70 km/jam")
                cl.sendMessage(to, "berhubungan dengan sumatra barat?*jam gadang*tugu bonjol*benteng fort de kock*danau maninjau*ngarai sianok*rendang")
                cl.sendMessage(to, "tempat apa yg dipilih orang untuk berpetualang?*hutan*gunung*sungai*laut*padang pasir")
                cl.sendMessage(to, "dimana tempat nonton film?*bioskop*kamar*komputer*lapangan*dimana-mana*rumah teman*kost teman")
                cl.sendMessage(to, "penyanyi luar cewek?*madona*mariah carey*britney spears*christina aguilera*shania twain*celine dion")
                cl.sendMessage(to, "organ tubuh manusia yg berpasangan?*tangan*kaki*mata*telinga*paru-paru*ginjal*buah zakar")
                cl.sendMessage(to, "bagian dari harimau?*belang*bulu*ekor*cakar*taring")
                cl.sendMessage(to, "apa yang berhubungan dengan sangkuriang?*gunung*perahu*legenda*anjing*dayang sumbi*durhaka*tangkuban")
                cl.sendMessage(to, "transportasi di darat?*bus*becak*bus*kereta api*mobil*motor*bemo*ojek*bajaj*sepeda motor*dokar*taksi*kapal*angkutan umum")
                cl.sendMessage(to, "nama operator hp?*indosat*mentari*telkomsel*mobile 8")
                cl.sendMessage(to, "bahan bakar yang berasal dari alam?*bensin*solar*batu bara*minyak tanah*lpg")
                cl.sendMessage(to, "penduduk negara mana yang biasanya memakai pakaian negaranya?*india*indonesia*jepang*arab*vietnam")
                cl.sendMessage(to, "berapa juta sel dalam otak manusia?*1000 juta")
                cl.sendMessage(to, "merk gel rambut?*gatsby*brisk*johny andrean*rudy hadisuwarno*clear")
                cl.sendMessage(to, "software chatting?*mirc*yahoo messenger*msn*google talk*skype*camfrog*live connector*icq*windows live")
                cl.sendMessage(to, "seorang sahabat?*dapat diajak curhat*saling berbagi*bukan pasangan")
                cl.sendMessage(to, "personil ngelaba?*eko*parto*akri")
                cl.sendMessage(to, "yang biasa mengambang di sungai?*bangkai*pakaian*mayat*sampah*kayu*tokai")
                cl.sendMessage(to, "aduh aku digigit....*nyamuk*anjing*ular*tikus*pacarku")
                cl.sendMessage(to, "apa saja kelemahan polisi lalu lintas?*kena rasia satgas*polisi provos lewat*liat pelat nomor terbalik")
                cl.sendMessage(to, "nama kapal berdasarkan pelayarannya?*Kapal permukaan*kapal selam*Kapal mengambang*Kapal bantalan udara")
                cl.sendMessage(to, "berhubungan dengan musim kemarau?*kering*panas*kebakaran")
                cl.sendMessage(to, "julukan club real madrid C.F?*The real samba*Los Galacticos*Los blancos*Los merengueZ*The white*El real")
                cl.sendMessage(to, "nama danau?*toba*gajah mungkur*jatiluhur*towuti")
                cl.sendMessage(to, "tempat yang dijadikan ajang maksiat?*hotel*tempat judi*diskotik*pub*bar*lokasi pelacuran")
                cl.sendMessage(to, "tempat wisata di belanda?*madame tussaud*keunkenhoff*madurondam utrecht*vlieland")
                cl.sendMessage(to, "situs berita?*bolanews*kompas*detik")
                cl.sendMessage(to, "jenis sampah?*organik*unorganik*b3")
                cl.sendMessage(to, "apa saja yang dibeli ketika ingin menonton bioskop?*snack*minuman*popcorn*tissu*permen*roti")
                cl.sendMessage(to, "sebutkan lagu linkin park?*numb*faint*breaking the habbit*somewhere i belong*paper cut")
                cl.sendMessage(to, "Istilah Samurai?*buke*kabukimono*musha*si*mononofu*tsuwamono")
                cl.sendMessage(to, "universitas Palembang?*iba*mdp*igm*musi*unsri")
                cl.sendMessage(to, "mall di surabaya/ semarang?*java mall*ciputra*sri ratu*matahari*ramayana")
                cl.sendMessage(to, "mobil keluaran honda?*stream*civic*cr-v*jazz*city")
                cl.sendMessage(to, "rokok di indonesia?*djarum*marlboro*a mild*lucky strike*dji sam soe*sampoerna")
                cl.sendMessage(to, "sebutkan alat penunjuk arah?*bayangan*bulan*matahari*kompas")
                cl.sendMessage(to, "penyanyi seksi keluaran hollywood?*britney spears*shakira*jennifer lopez*christina aguilera*madonna")
                cl.sendMessage(to, "berhubungan dgn kombinasi*warna*pakaian*pukulan*tendangan")
                cl.sendMessage(to, "tokoh dlm Pilm peterpan?*Peterpan*Wendy*Kapten hook*Tinkerbell")
                cl.sendMessage(to, "kepanjangan pasutri?*pasangan suami istri*pasangan suami takut istri")
                cl.sendMessage(to, "mainan apa saja yang ada di dunia fantasi?*halilintar*niagara*arung jeram*kora-kora*pontang-panting")
                cl.sendMessage(to, "berapa lama orang menjemur kasur?*satu jam*empat jam*sehari")
                cl.sendMessage(to, "nama lain alat kelamin?*burung*rudal*tempek*apem")
                cl.sendMessage(to, "disaat apa orang mematikan ponsel?*ujian*kuliah*pacaran*ibadah*tidur*rapat")
                cl.sendMessage(to, "batuan mineral yg berharga tinggi*berlian*intan*mutiara*jamrud*permata*delima")
                cl.sendMessage(to, "nama pasukan yang di pimpin oleh letnan jendral soeharto pada waktu pemberihan ormas pki?*trisula")
                cl.sendMessage(to, "nama bulan dalam bahasa jepang?|Ichigatsu*Nigatsu*Sangatsu*Shigatsu*Gogatsu*Rokugatsu*Nanagatsu*Hachigatsu*Kugatsu*Jugatsu*Juuichigatsu*Juunigatsu")
                cl.sendMessage(to, "tanda kendaraan?*dk*cd*b*aa*d*dd*bh*bg*h*s*t*k*f*ab*ad*kt*r*L*dh*g*be")
                cl.sendMessage(to, "yang mengaku sebagai jendral nasution?*pierre tendean")
                cl.sendMessage(to, "negara afrika utara?*mesir*aljazair*libya*maroko*tunisia*mauritania")
                cl.sendMessage(to, "penerbit buku di INDONESIA?*erlangga*gramedia*penerbit andi*intan pariwara*grafindo")
                cl.sendMessage(to, "tempat wisata di indonesia?*bali*danau toba*malioboro*puncak*borobudur*ancol*saritem*cibubur*dolly*dunia fantasy")
                cl.sendMessage(to, "cara efektif membunuh nyamuk*semprot*lempar*cablek*injek*tabok*pites*gigit")
                cl.sendMessage(to, "mall/pusat perbelanjaan yang ada di Surabaya?*Tunjungan plasa*Delta plasa*Galaxy mall*Jembatan Merah plasa*PTC*Giant*Carefour")
                cl.sendMessage(to, "mata uang yg berawalan R*rupiah*riyal*riel*rupee*ringgit")
                cl.sendMessage(to, "senjata tradisional indonesia (2)?*kujang*mandau*keris*badik*rudus*parang*pehduk payan*golok*terapang*kelewang*kuduk")
                cl.sendMessage(to, "personil laruku?*yuki*teru*hyde*ken")
                cl.sendMessage(to, "tingkatan kelas dalam tinju?*berat*welter*bantam*berat ringan*penjelajah")
                cl.sendMessage(to, "nama burung?*kutilang*beo*cendrawasih*elang*pipit*gagak*kakatua")
                cl.sendMessage(to, "macam tense inggris?*perfect tense*past tense*present tense*future tense")
                cl.sendMessage(to, "nama pelawak indonesia yang sudah alm?*benyamin*dono*kasino*ishak")
                cl.sendMessage(to, "profesi yg memerlukan orang dengan tubuh tinggi*tentara*peragawati*model*pramugari*pilot*pramugara*polisi")
                cl.sendMessage(to, "personil UNGU?*pasha*enda*onci*makki*rowman")
                cl.sendMessage(to, "yang dapat dimakan campuran dengan roti*Selada*Mentega*telor*Coklat*Selai*Keju*Sosis*daging ham*susu")
                cl.sendMessage(to, "service dalnet?*memoserv*chanserv*nickserv*operserv")
                cl.sendMessage(to, "teman donald bebek?*lang ling lung*agus angsa*untung*desi")
                cl.sendMessage(to, "nama negara eropa?*inggris*italia*belanda")
                cl.sendMessage(to, "merk baterai di Indonesia*National*ABC*Energizer*Eveready*Panasonic*Hitachi")
                cl.sendMessage(to, "negara bagian australia?*sydney*hobart*adelaide*melbourne*perth*brisbane")
                cl.sendMessage(to, "tokoh kartun jepang?*doraemon*sinchan*kenji*sailormoon*candy-candy")
                cl.sendMessage(to, "mata air?*sungai*laut *danau*air tanah*samudera")
                cl.sendMessage(to, "ukuran kertas?*a4*legal*a5*letter*executive")
                cl.sendMessage(to, "susu sekarang ada berbagai rasa, apa saja itu?*manis*coklat*kopi*strawberry*mocca*grape*nanas*pisang")
                cl.sendMessage(to, "raja kerajaan singasari?*tunggul ametung")
                cl.sendMessage(to, "kenapa orang makan?*lapar*stress*gengsi*waktunya makan*kerja sales*ikut sayembara*pengen gemuk")
                cl.sendMessage(to, "apa yg biasanya sering lupa dibawa*uang*dompet*handphone*kunci*kacamata*rokok*stnk")
                cl.sendMessage(to, "macam - macam pisang?*raja*ambon*sepatu*tanduk*mas *molen")
                cl.sendMessage(to, "jenis makanan atau minuman yang disukai untuk berbuka puasa?*air putih*teh hangat*es kelapa muda*gorengan*kolak")
                cl.sendMessage(to, "nama mobil terkenal?*honda*mercy*ferarri*bmw*jaguar")
                cl.sendMessage(to, "tempat Kencan Paling Enak?*bioskop*pantai*warnet*restorant*rumah*toilet")
                cl.sendMessage(to, "presiden congo?*laurent kabila")
                cl.sendMessage(to, "ilmu yang digunakan dukun?*jagaraga*lembu sakilan*jaran goyang*semar mesem*raga sukma")
                cl.sendMessage(to, "jenis minuman alkohol tinggi?*whiski*martell*arak*martini*sake*jack daniel*soju*long island")
                cl.sendMessage(to, "dunia lain?*fatamorgana*mimpi*dimensi lain")
                cl.sendMessage(to, "struktur sel?*membran sel*sitoplasma*nukleus*organel")
                cl.sendMessage(to, "nama pemain bulutangkis indonesia?*susi susanti*alan budikusuma*djoko suprianto*ricky subagja")
                cl.sendMessage(to, "makanan khas sulawesi?*buras*kapurung*barongkong*coto makassar*pisang ijo")
                cl.sendMessage(to, "hewan mamalia?*anjing*kucing*singa*kelinci*beruang")
                cl.sendMessage(to, "sesuatu yang diangkut dengan truk?*perabotan*kayu*beras*besi*baja")
                cl.sendMessage(to, "apa reaksi suami waktu malam pertama anda membuka pakaian?*marah*tertawa*bingung*pergi*cuek*nangis*menampar")
                cl.sendMessage(to, "kalo di rumah sendirian kamu bakal*Tidur*Belajar*Baca buku*Telpon*Dengerin musik*Seks")
                cl.sendMessage(to, "merek hardisk*quantum*seagate*maxtor*wdc*mdt")
                cl.sendMessage(to, "ciri gajah?*belalai*gading*telinga lebar*besar*kulit tebal")
                cl.sendMessage(to, "sarjana jurusan non tehnik?*ekonomi*psikolog*hukum*kesenian*designer*sastra")
                cl.sendMessage(to, "makanan ringan yang biasa dimakan anak2?*es*makroni*agar-agar*coklat*permen*chiki")
                cl.sendMessage(to, "makanan - makanan pokok di dunia*nasi*kentang*jagung*sagu*mie*sayur*roti*gandum")
                cl.sendMessage(to, "anggota keluarga the osbornes*kelly*ozzy*jack*sharon*aimee")
                cl.sendMessage(to, "hiburan apa yang ada di pesta ulang tahun?*band*badut*sulap*kuis*game")
                cl.sendMessage(to, "siklus windu?*dal*alip*be*ehe*wawu*jimawal*jimakir*je")
                cl.sendMessage(to, "fasilitas beternak ikan?*jala*tambak*saringan")
                cl.sendMessage(to, "apa yg biasa dilakukan orang bila ngantuk*tidur*menguap*minum kopi*cuci muka*ke tempat tidur*minum susu*denger musik")
                cl.sendMessage(to, "majalah komputer di indonesia?*linux*info komputer*chip*pc media*file magazine")
                cl.sendMessage(to, "jenis penyakit kulit?*panu*kurap*gatal gatal*koreng*kadas*kutu air")
                cl.sendMessage(to, "ciri orang emosi?*main pukul*pergi lokalisasi*bunuh orang")
                cl.sendMessage(to, "suara yang ditakuti anak2?*anjing*hantu*petir*harimau")
                cl.sendMessage(to, "corak rasa ice cream?*susu*strawberry*moka*lemon*nanas*jeruk*vanila")
                cl.sendMessage(to, "sebutkan acara tv favorit?*kartun*kuis*telenovela*sinetron*olahraga*film seri")
                cl.sendMessage(to, "mall di orchad road di singapore?*i-setan*takhasimaya*lucky plaza*tang plaza")
                cl.sendMessage(to, "warnet di yogyakarta?*hijaunet*hasilnet*nasanet*neptune*planet*ahanetwiskanet*thunder*ANGELnet")
                cl.sendMessage(to, "nama pengarang novel terkenal di dunia?*jhon grisham*alfred hitchok*barbara cartland*sidney sheldon")
                cl.sendMessage(to, "ciri-ciri negara mesir?*piramida*sungai nil*firaun*mumi*sphinx")
                cl.sendMessage(to, "komentar kamu setelah liat pilm Independence Day*Bagus*Keren*Tegang*Seru*Biasa aja*jelek")
                cl.sendMessage(to, "animals on the sea?*crab*fish*shark*sealion*dolphin*turtle")
                cl.sendMessage(to, "olahraga yang berbahaya?*arung jerang*tinju*balap mobil*balap motor*ski salju*panjat tebing")
                cl.sendMessage(to, "kalo cewe liat tikus*lari*teriak*pingsan*loncat*kaget")
                cl.sendMessage(to, "apa saja keuntungan menjadi orang gila?*terkenal*masuk surga*santai membunuh*makan gratis*selalu riang*ditakuti preman*pusat perhatian")
                cl.sendMessage(to, "yang biasa ada di diskotik?*psk*dj*minuman*lampu disko*gigolo*orang mabuk")
                cl.sendMessage(to, "makanan dengan kandungan karbohidrat*nasi*roti*kentang*sagu*jagung")
                cl.sendMessage(to, "makanan yang termasuk gorengan?*ubi*tahu*tempe*pisang*cireng*bakwan")
                cl.sendMessage(to, "siapakah tokoh terkenal nyata/fiksi yang berhubungan dengan cinta?*romeo dan juliet*rama sinta*arjuna")
                cl.sendMessage(to, "jenis lagu yang disukai anak muda?*rnb*pop*rock*house music*hiphop")
                cl.sendMessage(to, "nama negara yang punya hak VETO PBB dalam bahasa inggris*China*France*USA*RUSSIA*England")
                cl.sendMessage(to, "Artis terseksi di Indonesia*ayu ashari*sarah azhari*sophia latjuba*paramitha rusadi*ratna listi")
                cl.sendMessage(to, "yang berhubungan dgn club malam / diskotik?*rasia*narkoba*minuman keras*orang mabuk*dj*dugem*jablai")
                cl.sendMessage(to, "kebiasaan waktu tidur?*mendengkur*menguap*ngiler")
                cl.sendMessage(to, "jenis tv televisi?*politron*sony*panasonic*toshiba*samsung*sanken*akira")
                cl.sendMessage(to, "Jenis-jenis energi*listrik*panas bumi*gas alam*tenaga air*batu bara")
                cl.sendMessage(to, "apa yang dilakukan orang di stadion sambil menunggu pertandingan dimulai*ngobrol*makan*minum*pemanasan*tidur*ngemil*baca koran")
                cl.sendMessage(to, "yang dilakukan orang pada saat sedang menunggu*merokok*membaca*melamun*cemas")
                cl.sendMessage(to, "macam pajak*barang mewah*bumi dan bangunan*undian*penghasilan*barang mewah")
                cl.sendMessage(to, "cara2 bunuh diri*gantung diri*minum baygon*potong nadi*lompat*belajar matematika*tembak kepala sendiri")
                cl.sendMessage(to, "apa yang dikatakan cowo utk melamar kekasih?*saya hanya bawa cinta*bolehkan saya mempersunting putri anda")
                cl.sendMessage(to, "jenis hewan vertebrata?*reptilia*aves*amphibia*mamalia*pisces")
                cl.sendMessage(to, "barang bekas apa yg biasanya dijual oleh tukang loak di pinggir jalan*Sepatu*Sandal*Kardus*Jaket*Tape*Onderdil")
                cl.sendMessage(to, "jenis anjing terkenal?*dalmation*buldog*pom")
                cl.sendMessage(to, "fungsi fungsional handphone?*sms*telepon*foto*mms*internet*denger musik*main game*bergaya*chatting*modem")
                cl.sendMessage(to, "apa yang terjadi jika sakit hati?*nangis*bunuh diri*mabuk*curhat*stress*jadi gila*sedih")
                cl.sendMessage(to, "macam-macam tepung?*kanji*beras*terigu")
                cl.sendMessage(to, "tempat wisata di surabaya?*njarak*kenjeran*kebun binatang surabaya*taman remaja*dolly")
                cl.sendMessage(to, "alat musik sederhana?*gitar*drum*seruling*terompet*harmonika*pianika*angklung")
                cl.sendMessage(to, "pemeran si midun?*sandi nayoan")
                cl.sendMessage(to, "jenis ilmu hitan?*pelet*santet*guna guna*pesugihan")
                cl.sendMessage(to, "universitas di surabaya?*unair*unesa*upn*ubaya*stiesia*petra*itats*its")
                cl.sendMessage(to, "makanan yang ada di warteg*Rawon*Soto*Krengsengan*Pecel*Kari ayam*Sayur lodeh")
                cl.sendMessage(to, "1 + 1 ?*2*dua")
                cl.sendMessage(to, "2 + 2 = 4 BERAPA?*24")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == 'jawab' and sender not in clMID:
                cl.sendMessage(to, "apa yang dilakukan ketika ketahuan pacar sedang berjalan dengan mantan?*salah tingkah*kabur*menghindar*bohong*diam*pasrah *menjelaskan*minta maaf")
                cl.sendMessage(to, "selain tidur apa yang bisa orang lakukan di atas tempat tidur?*membaca*nonton tv*ngobrol*melamun*bermesraan*telepon")
                cl.sendMessage(to, "sebutkan tempat-tempat kencan?*bioskop*pantai*warnet*restorant*rumah *toilet")
                cl.sendMessage(to, "sebutkan sesuatu yang sekali pakai langsung buang?*pembalut*tisu*popok*korek*teh celup*kondom")
                cl.sendMessage(to, "bagaimana cara mendekati orang yang ditaksir?*chatt*ngobrol*beri perhatian*rayu*menyapa*minta kenalan*antar pulang")
                cl.sendMessage(to, "perasaan apa yang ada bila mau kencan pertama?*grogi*malu*takut*senang")
                cl.sendMessage(to, "apa yg di lakukan saat pertama kali pacaran?*gandengan tangan*makan*duduk*ciuman")
                cl.sendMessage(to, "selain ibu kandung, siapa yang dipanggil ibu?*guru*mertua*atasan*tiri")
                cl.sendMessage(to, "selain cinta apa yang dibutuhkan agar pernikahan bahagia?*Kejujuran*Materi*Anak*Kepercayaan")
                cl.sendMessage(to, "tempat untuk pacaran?*Rumah*Kuburan*Sawah*Rumah sakit")
                cl.sendMessage(to, "dimana orang biasa mendengarkan musik?*kamar*pub*diskotik*cafe*mobil")
                cl.sendMessage(to, "acara tv disalurkan indosiar?*patroli*sinetron*sinetron*ftv unggulan*power ranger*ultraman")
                cl.sendMessage(to, "batas kecepatan mobil di jalan tol?*60 km/jam*80km/jam*100 km/jam*120 km/jam*70 km/jam")
                cl.sendMessage(to, "berhubungan dengan sumatra barat?*jam gadang*tugu bonjol*benteng fort de kock*danau maninjau*ngarai sianok*rendang")
                cl.sendMessage(to, "tempat apa yg dipilih orang untuk berpetualang?*hutan*gunung*sungai*laut*padang pasir")
                cl.sendMessage(to, "dimana tempat nonton film?*bioskop*kamar*komputer*lapangan*dimana-mana*rumah teman*kost teman")
                cl.sendMessage(to, "penyanyi luar cewek?*madona*mariah carey*britney spears*christina aguilera*shania twain*celine dion")
                cl.sendMessage(to, "organ tubuh manusia yg berpasangan?*tangan*kaki*mata*telinga*paru-paru*ginjal*buah zakar")
                cl.sendMessage(to, "bagian dari harimau?*belang*bulu*ekor*cakar*taring")
                cl.sendMessage(to, "apa yang berhubungan dengan sangkuriang?*gunung*perahu*legenda*anjing*dayang sumbi*durhaka*tangkuban")
                cl.sendMessage(to, "transportasi di darat?*bus*becak*bus*kereta api*mobil*motor*bemo*ojek*bajaj*sepeda motor*dokar*taksi*kapal*angkutan umum")
                cl.sendMessage(to, "nama operator hp?*indosat*mentari*telkomsel*mobile 8")
                cl.sendMessage(to, "bahan bakar yang berasal dari alam?*bensin*solar*batu bara*minyak tanah*lpg")
                cl.sendMessage(to, "penduduk negara mana yang biasanya memakai pakaian negaranya?*india*indonesia*jepang*arab*vietnam")
                cl.sendMessage(to, "berapa juta sel dalam otak manusia?*1000 juta")
                cl.sendMessage(to, "merk gel rambut?*gatsby*brisk*johny andrean*rudy hadisuwarno*clear")
                cl.sendMessage(to, "software chatting?*mirc*yahoo messenger*msn*google talk*skype*camfrog*live connector*icq*windows live")
                cl.sendMessage(to, "seorang sahabat?*dapat diajak curhat*saling berbagi*bukan pasangan")
                cl.sendMessage(to, "personil ngelaba?*eko*parto*akri")
                cl.sendMessage(to, "yang biasa mengambang di sungai?*bangkai*pakaian*mayat*sampah*kayu*tokai")
                cl.sendMessage(to, "aduh aku digigit....*nyamuk*anjing*ular*tikus*pacarku")
                cl.sendMessage(to, "apa saja kelemahan polisi lalu lintas?*kena rasia satgas*polisi provos lewat*liat pelat nomor terbalik")
                cl.sendMessage(to, "nama kapal berdasarkan pelayarannya?*Kapal permukaan*kapal selam*Kapal mengambang*Kapal bantalan udara")
                cl.sendMessage(to, "berhubungan dengan musim kemarau?*kering*panas*kebakaran")
                cl.sendMessage(to, "julukan club real madrid C.F?*The real samba*Los Galacticos*Los blancos*Los merengueZ*The white*El real")
                cl.sendMessage(to, "nama danau?*toba*gajah mungkur*jatiluhur*towuti")
                cl.sendMessage(to, "tempat yang dijadikan ajang maksiat?*hotel*tempat judi*diskotik*pub*bar*lokasi pelacuran")
                cl.sendMessage(to, "tempat wisata di belanda?*madame tussaud*keunkenhoff*madurondam utrecht*vlieland")
                cl.sendMessage(to, "situs berita?*bolanews*kompas*detik")
                cl.sendMessage(to, "jenis sampah?*organik*unorganik*b3")
                cl.sendMessage(to, "apa saja yang dibeli ketika ingin menonton bioskop?*snack*minuman*popcorn*tissu*permen*roti")
                cl.sendMessage(to, "sebutkan lagu linkin park?*numb*faint*breaking the habbit*somewhere i belong*paper cut")
                cl.sendMessage(to, "Istilah Samurai?*buke*kabukimono*musha*si*mononofu*tsuwamono")
                cl.sendMessage(to, "universitas Palembang?*iba*mdp*igm*musi*unsri")
                cl.sendMessage(to, "mall di surabaya/ semarang?*java mall*ciputra*sri ratu*matahari*ramayana")
                cl.sendMessage(to, "mobil keluaran honda?*stream*civic*cr-v*jazz*city")
                cl.sendMessage(to, "rokok di indonesia?*djarum*marlboro*a mild*lucky strike*dji sam soe*sampoerna")
                cl.sendMessage(to, "sebutkan alat penunjuk arah?*bayangan*bulan*matahari*kompas")
                cl.sendMessage(to, "penyanyi seksi keluaran hollywood?*britney spears*shakira*jennifer lopez*christina aguilera*madonna")
                cl.sendMessage(to, "berhubungan dgn kombinasi*warna*pakaian*pukulan*tendangan")
                cl.sendMessage(to, "tokoh dlm Pilm peterpan?*Peterpan*Wendy*Kapten hook*Tinkerbell")
                cl.sendMessage(to, "kepanjangan pasutri?*pasangan suami istri*pasangan suami takut istri")
                cl.sendMessage(to, "mainan apa saja yang ada di dunia fantasi?*halilintar*niagara*arung jeram*kora-kora*pontang-panting")
                cl.sendMessage(to, "berapa lama orang menjemur kasur?*satu jam*empat jam*sehari")
                cl.sendMessage(to, "nama lain alat kelamin?*burung*rudal*tempek*apem")
                cl.sendMessage(to, "disaat apa orang mematikan ponsel?*ujian*kuliah*pacaran*ibadah*tidur*rapat")
                cl.sendMessage(to, "batuan mineral yg berharga tinggi*berlian*intan*mutiara*jamrud*permata*delima")
                cl.sendMessage(to, "nama pasukan yang di pimpin oleh letnan jendral soeharto pada waktu pemberihan ormas pki?*trisula")
                cl.sendMessage(to, "nama bulan dalam bahasa jepang?|Ichigatsu*Nigatsu*Sangatsu*Shigatsu*Gogatsu*Rokugatsu*Nanagatsu*Hachigatsu*Kugatsu*Jugatsu*Juuichigatsu*Juunigatsu")
                cl.sendMessage(to, "tanda kendaraan?*dk*cd*b*aa*d*dd*bh*bg*h*s*t*k*f*ab*ad*kt*r*L*dh*g*be")
                cl.sendMessage(to, "yang mengaku sebagai jendral nasution?*pierre tendean")
                cl.sendMessage(to, "negara afrika utara?*mesir*aljazair*libya*maroko*tunisia*mauritania")
                cl.sendMessage(to, "penerbit buku di INDONESIA?*erlangga*gramedia*penerbit andi*intan pariwara*grafindo")
                cl.sendMessage(to, "tempat wisata di indonesia?*bali*danau toba*malioboro*puncak*borobudur*ancol*saritem*cibubur*dolly*dunia fantasy")
                cl.sendMessage(to, "cara efektif membunuh nyamuk*semprot*lempar*cablek*injek*tabok*pites*gigit")
                cl.sendMessage(to, "mall/pusat perbelanjaan yang ada di Surabaya?*Tunjungan plasa*Delta plasa*Galaxy mall*Jembatan Merah plasa*PTC*Giant*Carefour")
                cl.sendMessage(to, "mata uang yg berawalan R*rupiah*riyal*riel*rupee*ringgit")
                cl.sendMessage(to, "senjata tradisional indonesia (2)?*kujang*mandau*keris*badik*rudus*parang*pehduk payan*golok*terapang*kelewang*kuduk")
                cl.sendMessage(to, "personil laruku?*yuki*teru*hyde*ken")
                cl.sendMessage(to, "tingkatan kelas dalam tinju?*berat*welter*bantam*berat ringan*penjelajah")
                cl.sendMessage(to, "nama burung?*kutilang*beo*cendrawasih*elang*pipit*gagak*kakatua")
                cl.sendMessage(to, "macam tense inggris?*perfect tense*past tense*present tense*future tense")
                cl.sendMessage(to, "nama pelawak indonesia yang sudah alm?*benyamin*dono*kasino*ishak")
                cl.sendMessage(to, "profesi yg memerlukan orang dengan tubuh tinggi*tentara*peragawati*model*pramugari*pilot*pramugara*polisi")
                cl.sendMessage(to, "personil UNGU?*pasha*enda*onci*makki*rowman")
                cl.sendMessage(to, "yang dapat dimakan campuran dengan roti*Selada*Mentega*telor*Coklat*Selai*Keju*Sosis*daging ham*susu")
                cl.sendMessage(to, "service dalnet?*memoserv*chanserv*nickserv*operserv")
                cl.sendMessage(to, "teman donald bebek?*lang ling lung*agus angsa*untung*desi")
                cl.sendMessage(to, "nama negara eropa?*inggris*italia*belanda")
                cl.sendMessage(to, "merk baterai di Indonesia*National*ABC*Energizer*Eveready*Panasonic*Hitachi")
                cl.sendMessage(to, "negara bagian australia?*sydney*hobart*adelaide*melbourne*perth*brisbane")
                cl.sendMessage(to, "tokoh kartun jepang?*doraemon*sinchan*kenji*sailormoon*candy-candy")
                cl.sendMessage(to, "mata air?*sungai*laut *danau*air tanah*samudera")
                cl.sendMessage(to, "ukuran kertas?*a4*legal*a5*letter*executive")
                cl.sendMessage(to, "susu sekarang ada berbagai rasa, apa saja itu?*manis*coklat*kopi*strawberry*mocca*grape*nanas*pisang")
                cl.sendMessage(to, "raja kerajaan singasari?*tunggul ametung")
                cl.sendMessage(to, "kenapa orang makan?*lapar*stress*gengsi*waktunya makan*kerja sales*ikut sayembara*pengen gemuk")
                cl.sendMessage(to, "apa yg biasanya sering lupa dibawa*uang*dompet*handphone*kunci*kacamata*rokok*stnk")
                cl.sendMessage(to, "macam - macam pisang?*raja*ambon*sepatu*tanduk*mas *molen")
                cl.sendMessage(to, "jenis makanan atau minuman yang disukai untuk berbuka puasa?*air putih*teh hangat*es kelapa muda*gorengan*kolak")
                cl.sendMessage(to, "nama mobil terkenal?*honda*mercy*ferarri*bmw*jaguar")
                cl.sendMessage(to, "tempat Kencan Paling Enak?*bioskop*pantai*warnet*restorant*rumah*toilet")
                cl.sendMessage(to, "presiden congo?*laurent kabila")
                cl.sendMessage(to, "ilmu yang digunakan dukun?*jagaraga*lembu sakilan*jaran goyang*semar mesem*raga sukma")
                cl.sendMessage(to, "jenis minuman alkohol tinggi?*whiski*martell*arak*martini*sake*jack daniel*soju*long island")
                cl.sendMessage(to, "dunia lain?*fatamorgana*mimpi*dimensi lain")
                cl.sendMessage(to, "struktur sel?*membran sel*sitoplasma*nukleus*organel")
                cl.sendMessage(to, "nama pemain bulutangkis indonesia?*susi susanti*alan budikusuma*djoko suprianto*ricky subagja")
                cl.sendMessage(to, "makanan khas sulawesi?*buras*kapurung*barongkong*coto makassar*pisang ijo")
                cl.sendMessage(to, "hewan mamalia?*anjing*kucing*singa*kelinci*beruang")
                cl.sendMessage(to, "sesuatu yang diangkut dengan truk?*perabotan*kayu*beras*besi*baja")
                cl.sendMessage(to, "apa reaksi suami waktu malam pertama anda membuka pakaian?*marah*tertawa*bingung*pergi*cuek*nangis*menampar")
                cl.sendMessage(to, "kalo di rumah sendirian kamu bakal*Tidur*Belajar*Baca buku*Telpon*Dengerin musik*Seks")
                cl.sendMessage(to, "merek hardisk*quantum*seagate*maxtor*wdc*mdt")
                cl.sendMessage(to, "ciri gajah?*belalai*gading*telinga lebar*besar*kulit tebal")
                cl.sendMessage(to, "sarjana jurusan non tehnik?*ekonomi*psikolog*hukum*kesenian*designer*sastra")
                cl.sendMessage(to, "makanan ringan yang biasa dimakan anak2?*es*makroni*agar-agar*coklat*permen*chiki")
                cl.sendMessage(to, "makanan - makanan pokok di dunia*nasi*kentang*jagung*sagu*mie*sayur*roti*gandum")
                cl.sendMessage(to, "anggota keluarga the osbornes*kelly*ozzy*jack*sharon*aimee")
                cl.sendMessage(to, "hiburan apa yang ada di pesta ulang tahun?*band*badut*sulap*kuis*game")
                cl.sendMessage(to, "siklus windu?*dal*alip*be*ehe*wawu*jimawal*jimakir*je")
                cl.sendMessage(to, "fasilitas beternak ikan?*jala*tambak*saringan")
                cl.sendMessage(to, "apa yg biasa dilakukan orang bila ngantuk*tidur*menguap*minum kopi*cuci muka*ke tempat tidur*minum susu*denger musik")
                cl.sendMessage(to, "majalah komputer di indonesia?*linux*info komputer*chip*pc media*file magazine")
                cl.sendMessage(to, "jenis penyakit kulit?*panu*kurap*gatal gatal*koreng*kadas*kutu air")
                cl.sendMessage(to, "ciri orang emosi?*main pukul*pergi lokalisasi*bunuh orang")
                cl.sendMessage(to, "suara yang ditakuti anak2?*anjing*hantu*petir*harimau")
                cl.sendMessage(to, "corak rasa ice cream?*susu*strawberry*moka*lemon*nanas*jeruk*vanila")
                cl.sendMessage(to, "sebutkan acara tv favorit?*kartun*kuis*telenovela*sinetron*olahraga*film seri")
                cl.sendMessage(to, "mall di orchad road di singapore?*i-setan*takhasimaya*lucky plaza*tang plaza")
                cl.sendMessage(to, "warnet di yogyakarta?*hijaunet*hasilnet*nasanet*neptune*planet*ahanetwiskanet*thunder*ANGELnet")
                cl.sendMessage(to, "nama pengarang novel terkenal di dunia?*jhon grisham*alfred hitchok*barbara cartland*sidney sheldon")
                cl.sendMessage(to, "ciri-ciri negara mesir?*piramida*sungai nil*firaun*mumi*sphinx")
                cl.sendMessage(to, "komentar kamu setelah liat pilm Independence Day*Bagus*Keren*Tegang*Seru*Biasa aja*jelek")
                cl.sendMessage(to, "animals on the sea?*crab*fish*shark*sealion*dolphin*turtle")
                cl.sendMessage(to, "olahraga yang berbahaya?*arung jerang*tinju*balap mobil*balap motor*ski salju*panjat tebing")
                cl.sendMessage(to, "kalo cewe liat tikus*lari*teriak*pingsan*loncat*kaget")
                cl.sendMessage(to, "apa saja keuntungan menjadi orang gila?*terkenal*masuk surga*santai membunuh*makan gratis*selalu riang*ditakuti preman*pusat perhatian")
                cl.sendMessage(to, "yang biasa ada di diskotik?*psk*dj*minuman*lampu disko*gigolo*orang mabuk")
                cl.sendMessage(to, "makanan dengan kandungan karbohidrat*nasi*roti*kentang*sagu*jagung")
                cl.sendMessage(to, "makanan yang termasuk gorengan?*ubi*tahu*tempe*pisang*cireng*bakwan")
                cl.sendMessage(to, "siapakah tokoh terkenal nyata/fiksi yang berhubungan dengan cinta?*romeo dan juliet*rama sinta*arjuna")
                cl.sendMessage(to, "jenis lagu yang disukai anak muda?*rnb*pop*rock*house music*hiphop")
                cl.sendMessage(to, "nama negara yang punya hak VETO PBB dalam bahasa inggris*China*France*USA*RUSSIA*England")
                cl.sendMessage(to, "Artis terseksi di Indonesia*ayu ashari*sarah azhari*sophia latjuba*paramitha rusadi*ratna listi")
                cl.sendMessage(to, "yang berhubungan dgn club malam / diskotik?*rasia*narkoba*minuman keras*orang mabuk*dj*dugem*jablai")
                cl.sendMessage(to, "kebiasaan waktu tidur?*mendengkur*menguap*ngiler")
                cl.sendMessage(to, "jenis tv televisi?*politron*sony*panasonic*toshiba*samsung*sanken*akira")
                cl.sendMessage(to, "Jenis-jenis energi*listrik*panas bumi*gas alam*tenaga air*batu bara")
                cl.sendMessage(to, "apa yang dilakukan orang di stadion sambil menunggu pertandingan dimulai*ngobrol*makan*minum*pemanasan*tidur*ngemil*baca koran")
                cl.sendMessage(to, "yang dilakukan orang pada saat sedang menunggu*merokok*membaca*melamun*cemas")
                cl.sendMessage(to, "macam pajak*barang mewah*bumi dan bangunan*undian*penghasilan*barang mewah")
                cl.sendMessage(to, "cara2 bunuh diri*gantung diri*minum baygon*potong nadi*lompat*belajar matematika*tembak kepala sendiri")
                cl.sendMessage(to, "apa yang dikatakan cowo utk melamar kekasih?*saya hanya bawa cinta*bolehkan saya mempersunting putri anda")
                cl.sendMessage(to, "jenis hewan vertebrata?*reptilia*aves*amphibia*mamalia*pisces")
                cl.sendMessage(to, "barang bekas apa yg biasanya dijual oleh tukang loak di pinggir jalan*Sepatu*Sandal*Kardus*Jaket*Tape*Onderdil")
                cl.sendMessage(to, "jenis anjing terkenal?*dalmation*buldog*pom")
                cl.sendMessage(to, "fungsi fungsional handphone?*sms*telepon*foto*mms*internet*denger musik*main game*bergaya*chatting*modem")
                cl.sendMessage(to, "apa yang terjadi jika sakit hati?*nangis*bunuh diri*mabuk*curhat*stress*jadi gila*sedih")
                cl.sendMessage(to, "macam-macam tepung?*kanji*beras*terigu")
                cl.sendMessage(to, "tempat wisata di surabaya?*njarak*kenjeran*kebun binatang surabaya*taman remaja*dolly")
                cl.sendMessage(to, "alat musik sederhana?*gitar*drum*seruling*terompet*harmonika*pianika*angklung")
                cl.sendMessage(to, "pemeran si midun?*sandi nayoan")
                cl.sendMessage(to, "jenis ilmu hitan?*pelet*santet*guna guna*pesugihan")
                cl.sendMessage(to, "universitas di surabaya?*unair*unesa*upn*ubaya*stiesia*petra*itats*its")
                cl.sendMessage(to, "makanan yang ada di warteg*Rawon*Soto*Krengsengan*Pecel*Kari ayam*Sayur lodeh")
                cl.sendMessage(to, "1 + 1 ?*2*dua")
                cl.sendMessage(to, "2 + 2 = 4 BERAPA?*24")
                cl.sendContact(to, "u9b0ae88d7cf669da9a8416bd4c765cd1")

            elif text.lower() == 'mia' and sender not in clMID:
                cl.sendMessage(to, "KENALIN INI SETANYA ZUL  SI MIA PEKO")
                cl.sendContact(to, "ua0850ec995284ecee169d9b683cfe71b")

            elif text.lower() == 'nella' and sender not in clMID:
                cl.sendMessage(to, "OWNER 🆂🅽🅹 Sᴬᴴᴬᴮᴬᵀ Nᴱᴸᴸᴬ Jᴼᴹᴮᴸᴼ")
                cl.sendContact(to, "u02e28e71b5f0799460f0cad4708d0fbb")

            elif text.lower() == 'tes' and sender not in clMID:
                cl.sendMessage(to, "tes 1")


    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        pass