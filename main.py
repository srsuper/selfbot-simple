#Thanks To : Uwewwwxyz, Dyu, Dolphin, Yehezkiel Bagas, RendyTR
#Supported By : My Lovely, ExcellentTeamBots, Om Squad, MPCORPS, NoelV2, LsC, MI BOTS, BoneToReborn, P.K BOTS, SPENAH, HBT
#Error? Please Contact Me
#Id Line : ibalv3

from linepy import *
from liff.ttypes import *
from linepy import*
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from tmp.MySplit import *
from datetime import datetime
from datetime import timedelta
from gtts import gTTS
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from io import StringIO
import subprocess
import youtube_dl, math
import humanize
import traceback
import time
import random
import sys
import pafy
import os
import json
import null
import codecs
import html5lib
import shutil
import glob
import re
import base64
import string
import requests
import ast
import pytz
import platform
import wikipedia
import importlib
import atexit
import asyncio
import livejson
loop = asyncio.get_event_loop()
devi = LINE("Gmail","Password")
print("Login Success,Type Help On Your Group")
print("Selfbot Edition\nBy NoiBots")
deviMID = devi.profile.mid
deviProfile = devi.profile
devi_poll = OEPoll(devi)
waitOpen = codecs.open("wait.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
#==================
cctv = {
	"cyduk":{},
	"point":{},
	"MENTION":{},
	"sidermem":{}
}

read = {
	"readPoint": {},
	"readMember": {},
	"readTime": {},
	"ROM": {}
}
#==========
with open("temp.json", "r", encoding="utf_8_sig") as f:
	set = json.loads(f.read())
	set.update(settings)
	settings = set
with open("wait.json", "r", encoding="utf_8_sig") as f:
	waits = json.loads(f.read())
	waits.update(wait)
	wait = waits
def backupData():
	try:
		backup = settings
		f = codecs.open('temp.json','w','utf-8')
		json.dump(backup,f,sort_keys=True,indent=4,ensure_ascii=False)
		backup = wait
		f = codecs.open('wait.json','w','utf-8')
		json.dump(backup,f,sort_keys=True,indent=4,ensure_ascii=False)
		return True
	except Exception as error:
		logError(error)
		return False
def speed_fetch():
	start = time.time()
	get = devi.getProfile()
	taken = time.time() - start
	took = time.time() - start
	return "Speed Fetch ♪\n- Took : %.3fms♪\n- Taken : %.6fms♪" % (took,taken)
def auto_liff():
	url = 'https://access.line.me/dialog/api/permissions'
	data = {
	    'on': [
	        'P',
	        'CM'
	    ],
	    'off': []
	}
	headers = {
	    'X-Line-Access': devi.authToken,
	    'X-Line-Application': devi.server.APP_NAME,
	    'X-Line-ChannelId': '1653391722',
	    'Content-Type': 'application/json'
	}
	requests.post(url, json=data, headers=headers)
def sendTemplate(group, data):
	auto_liff()
	xyz = LiffChatContext(group)
	xyzz = LiffContext(chat=xyz)
	view = LiffViewRequest('1653391722-QN5aXrrz', xyzz)
	token = devi.liff.issueLiffView(view)
	url = 'https://api.line.me/message/v3/share'
	headers = {
	    'Content-Type': 'application/json',
	    'Authorization': 'Bearer %s' % token.accessToken
	}
	data = {"messages":[data]}
	requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(to, data):
	auto_liff
	xyz = LiffChatContext(to)
	xyzz = LiffContext(chat=xyz)
	view = LiffViewRequest('1653391722-QN5aXrrz', xyzz)
	token = devi.liff.issueLiffView(view)
	url = 'https://api.line.me/message/v3/share'
	headers = {
	    'Content-Type': 'application/json',
	    'Authorization': 'Bearer %s' % token.accessToken
	}
	data = {"messages":[data]}
	requests.post(url, headers=headers, data=json.dumps(data))
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
		devi.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		logError(error)
		devi.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMessageCustom(to, text, icon , name):
	annda = {'MSG_SENDER_ICON': icon,
		'MSG_SENDER_NAME':  name,
	}
	devi.sendMessage(to, text, contentMetadata=annda)
def mentions(to, text="", mids=[]):
	arrData = ""
	arr = []
	mention = "@IbalxDevi  "
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
	devi.sendMessage(to, textx, {'AGENT_NAME':'devi OFFICIAL', 'AGENT_LINK': 'devi://ti/p/~{}'.format(devi.getProfile().userid), 'AGENT_ICON': "http://dl.profile.devi-cdn.net/" + devi.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def siderMembers(to, mid):
	try:
		arrData = ""
		textx = "Sider Terus,Sini Gabung Chat".format(str(mid))
		arr = []
		no = 1
		num = 2
		for i in mid:
			mention = "@IbalxDevi\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention
			if no < len(mid):
				no += 1
				textx += "%i. " % (num)
				num=(num+1)
			else:
				try:
					no = "\n {} ".format(str(devi.getGroup(to).name))
				except:
					no = "\n Success "
		devi.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		devi.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
	noi = text.lower()
	if settings["setKey"] == True:
		if noi.startswith(settings["keyCommand"]):
			cmd = noi.replace(settings["keyCommand"],"")
		else:
			cmd = "Undefined Command"
	else:
		cmd = text.lower()
	return cmd
def restartBot():
	python = sys.executable
	os.execl(python,python,*sys.argv)
def changeVideoAndPictureProfile(pict, vids):
	try:
		files = {'file': open(vids, 'rb')}
		obs_params = devi.genOBSParams({'oid': deviMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
		data = {'params': obs_params}
		r_vp = devi.server.postContent('{}/talk/vp/upload.nhn'.format(str(devi.server.devi_OBS_DOMAIN)), data=data, files=files)
		if r_vp.status_code != 201:
			return "Failed..."
		devi.updateProfilePicture(pict, 'vp')
		return "Success..."
	except Exception as e:
		raise Exception("Error change video and picture profile {}".format(str(e)))
		os.remove("ExcellentTeamBots.mp4")
medias = """Hello @!
Selfbot Edition!
By : NoiBots
      
 Media Commands :
     Music [ Query ]
     KBBI [ Query ]
      Cuaca [ City ]
     Corona
     Hentai
     Gempa
      Tribun news
Note : Without Brackets!
"""
profiles = """Hello @!
Selfbot Edition!
By : NoiBots
      
 Profile Commands :
     MyName
     MyBio
     MyPicture
     MyCover
     ChangeVideo [ Url YouTube ]
Note : Without Brackets!
"""
steals = """Hello @!
Selfbot Edition!
By : NoiBots
      
 Steal Commands :
     GetName @Tag
     GetBio @Tag
     GetPicture @Tag
     GetCover @Tag
     GetContact @Tag
     Chat @Tag [ Text ]
Note : Without Brackets!
"""
#==================
async def ibal_devi(op):
	try:
		if op.type == 0:
			return
		if op.type == 5:
			pesan = ["Haii","Thanks For Add Me"] #You Can Custome It
			rndm = random.choice(pesan)
			devi.sendMessage(op.param1, rndm)
		if op.type == 25:
			msg = op.message
			text = str(msg.text)
			msg_id = msg.id
			reply = msg.id
			receiver = msg.to
			sender = msg._from
			ibal = command(text)
			if msg.toType == 0 and sender != devi.profile.mid:
				to = sender
			else:
				to = receiver
			if msg.contentType == 0:
				for ibal in ibal.split(" & "):
					if ibal == "hi":
						devi.sendMention(to, "@! Hi Too","",[sender])
					elif ibal == "speed":
						devi.sendReplyMessage(msg.id, to, speed_fetch())
					elif ibal == "help":
						dataa = {"type": "bubble","size": "kilo","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/5jCXDdd/a354e7ed2dba2cfe122e8e7af06d75a5.png","size": "full","aspectMode": "cover","aspectRatio": "1:1","gravity": "center"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Help-Menu","weight": "bold","align": "center","wrap": True,"adjustMode": "shrink-to-fit","color": "#ffffff"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Media","color": "#ffffff"}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "50px","offsetStart": "20px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Profile","color": "#ffffff","wrap": True}],"offsetTop": "90px","position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "90px","offsetStart": "20px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Steal","size": "md","wrap": True,"color": "#ffffff"}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "50px","offsetStart": "80px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Sider","size": "md","color": "#ffffff","wrap": True}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "90px","offsetStart": "80px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Tagall","size": "md","color": "#ffffff","wrap": True}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "50px","offsetStart": "130px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Group","size": "md","color": "#ffffff","wrap": True}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "90px","offsetStart": "130px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Logout","size": "md","color": "#ffffff","wrap": True}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "50px","offsetStart": "190px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Restart","size": "md","color": "#ffffff","wrap": True}],"position": "absolute","borderWidth": "light","borderColor": "#ffffff","cornerRadius": "sm","offsetTop": "90px","offsetStart": "190px"}],"position": "absolute","offsetBottom": "0px","offsetStart": "0px","offsetEnd": "0px","paddingAll": "20px","offsetTop": "130px"}],"paddingAll": "0px"}}
						data = {"type": "flex","altText": "Ibal Was Here~","contents": {"type": "carousel","contents": [dataa]}}
						sendTemplate(to,data)
					elif ibal == "media":
						devi.sendMention(to, medias,"",[sender])
					elif ibal == "profile":
						devi.sendMention(to, profiles,"",[sender])
					elif ibal == "steal":
						devi.sendMention(to, steals,"",[sender])
					elif ibal == "about":
						h = devi.getContact("ucf9bf411b5ee4c9e6a1faa0be27d94e9")
						groups = devi.getGroupIdsJoined()
						contactlist = devi.getAllContactIds()
						kontak = devi.getContacts(contactlist)
						ac = subprocess.getoutput('lsb_release -a')
						am = subprocess.getoutput('cat /proc/meminfo')
						ax = subprocess.getoutput('lscpu')
						core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
						python_imp = platform.python_implementation()
						python_ver = platform.python_version()
						for noi in ac.splitnois():
							if 'Description:' in noi:
								osi = noi.split('Description:')[1].replace('  ','')
						for noi in ax.splitnois():
							if 'Architecture:' in noi:
								architecture =  noi.split('Architecture:')[1].replace(' ','')
						for noi in am.splitnois():
							if 'MemTotal:' in noi:
								mem = noi.split('MemTotal:')[1].replace(' ','')
							if 'MemFree:' in noi:
								fr = noi.split('MemFree:')[1].replace(' ','')
						ret_ = "About System :\n\n"
						ret_ +="OS System : {}\n".format(osi)
						ret_ +="Language : {}\n".format(python_imp)
						ret_ +="Version : {}\n".format(python_ver)
						ret_ +="Architecture : {}\n".format(architecture)
						ret_ +="CPU Core : {}\n".format(core)
						ret_ +="Memory : {}\n".format(mem)
						ret_ +="Free Memory : {}".format(fr)
						ret_ += "About Bots :\n\n"
						ret_ += "\nCreator : {}".format(h.displayName)
						ret_ += "\nGroup : {}".format(str(len(groups)))
						ret_ += "\nFriend : {}".format(str(len(kontak)))
						ret_ += "\nType : SelfbotBot"
						devi.sendReplyMessage(msg.id, to, str(ret_))
					elif ibal == 'logout':
						devi.sendMention(to,"User @! Has Been Logout","",[sender])
						time.sleep(3)
						sys.exit('Logout')
					elif ibal == "restart":
						devi.sendReplyMessage(msg.id,to,"Please Wait")
						restartBot()
					elif ibal == "sider":
						devi.sendReplyMessage(msg.id,to,"If You Want To Activated Check Sider, Type\nSider On\nIf You Want To Deactivated Check Sider, Type\nSider Off")
					elif ibal == 'sider on':
						try:
							devi.sendReplyMessage(msg.id,to, "Check Sider Set To Enable")
							del cctv['point'][to]
							del cctv['sidermem'][to]
							del cctv['cyduk'][to]
						except:
							pass
						cctv['point'][to] = msg.id
						cctv['sidermem'][to] = ""
						cctv['cyduk'][to]=True
					elif ibal == 'sider off':
						if to in cctv['point']:
							cctv['cyduk'][to]=False
							devi.sendReplyMessage(msg.id,to, "Check Sider Set To Disable")
						else:
							devi.sendReplyMessage(msg.id,to, "Check Sider Has Been Disable")
#=====================================================
#Profile
					elif ibal.startswith('chat '):
						try:
							if 'MENTION' in msg.contentMetadata.keys()!=None:
								key = eval(msg.contentMetadata["MENTION"])
								key1 = key["MENTIONEES"][0]["M"]
								nama = devi.getContact(key1).displayName
								anu = devi.getContact(key1)
								if len(ibal.split(" ")) >= 2:
									mid  = "{}".format(key1)
									text = "{}".format(str(ibal.replace(ibal.split(" ")[0]+" ","")))
									icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
									name = "{}".format(anu.displayName)
									b = [sendMessageCustom(key1, text, icon, name)];devi.sendMention(to, '「 Personal Chat 」\n@! Please Cek My Pc','',[key1])
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, f" Notification Error \n {e}")
					elif ibal.startswith("changevideo "):
						try:
							sep = text.split(" ")
							link = text.replace(sep[0] + " ","")
							devi.sendReplyMessage(msg.id, to, "Starting Download....")
							pic = "https://obs.line-scdn.net/{}".format(devi.getProfile().pictureStatus)
							subprocess.getoutput(f'youtube-dl --format mp4 --output NoiBots.mp4 {link}')
							pict = devi.downloadFileURL(pic)
							vids = "NoiBots.mp4"
							time.sleep(2)
							changeVideoAndPictureProfile(pict, vids)
							devi.sendReplyMessage(msg.id, to, "Success....")
							os.remove("NoiBots.mp4")
						except Exception as e:
							devi.sendReplyMessage(msg.id,to,str(e))
					elif ibal == "mypicture":
						path = devi.getContact(sender).pictureStatus
						devi.sendReplyMessage(msg.id,to,"https://obs.line-scdn.net/{}".format(str(path)))
					elif ibal == "mycover":
						image = devi.getProfileCoverURL(sender)
						path = str(image)
						devi.sendReplyMessage(msg.id,to,path)
					elif ibal == "myname":
						devi.sendReplyMessage(msg.id,to,"Name :\n"+str(devi.getContact(sender).displayName))
					elif ibal == "mybio":
						devi.sendReplyMessage(msg.id,to,"Bio :\n"+str(devi.getContact(sender).statusMessage))
#=================================================
#Media
					elif ibal == "corona":
						try:
							r = requests.get("https://ibalapi.herokuapp.com/api/kawalcorona")
							data = json.loads(r.text)
							ret = "Info Corona Indonesia\n"
							ret += "\n• City : "+str(data["result"]["city"])
							ret += "\n• Death : "+str(data["result"]["death"])
							ret += "\n• Healed : "+str(data["result"]["heal"])
							ret += "\n• Case : "+str(data["result"]["opname"])
							ret += "\n• Positive : "+str(data["result"]["positive"])
							devi.sendReplyMessage(msg.id, to, str(ret))
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, str(e))
					elif ibal == "hentai":
						try:
							r = json.loads(requests.get("https://mnazria.herokuapp.com/api/picanime?list=lewd").text)
							devi.sendReplyImageWithURL(msg.id, to, r["gambar"])
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, str(e))
					elif ibal == "gempa":
						try:
							r = json.loads(requests.get("https://mnazria.herokuapp.com/api/bmkg-gempa").text)
							devi.sendReplyImageWithURL(msg.id, to, r["result"])
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, str(e))
					elif ibal.startswith("music "):
						try:
							sep = ibal.split(" ")
							queryy = ibal.replace(sep[0] + " ","")
							r = json.loads(requests.get(f"https://mnazria.herokuapp.com/api/jooxnich?search={queryy}").text)
							#devi.sendReplyImageWithURL(msg.id, to, r["result"]["album_url"])
							devi.sendReplyMessage(msg.id, to, r["lirik"])
							devi.sendAudioWithURL(to, r["result"]["mp3Url"])
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, str(e))
					elif ibal.startswith("kbbi "):
						try:
							sep = ibal.split(" ")
							hehe = ibal.replace(sep[0] + " ","")
							r = requests.get(f"https://mnazria.herokuapp.com/api/kbbi?search={hehe}")
							data = json.loads(r.text)
							ret = f"KBBI From : {hehe}\n"
							ret += "\n• "+str(data["result"][0])
							devi.sendReplyMessage(msg.id, to, str(ret))
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, str(e))
					elif ibal.startswith("cuaca "):
						try:
							sep = ibal.split(" ")
							daerah = ibal.replace(sep[0] + " ","")
							r = requests.get(f"http://dolphinapi.herokuapp.com/api/weather?city={daerah}")
							d = json.loads(r.text)
							ret = f"Prakiraan Cuaca Kota : {daerah}\n"
							ret += "\n Desc : "+str(d["result"]["desc"])
							ret += "\n Humidity : "+str(d["result"]["humidity"])
							ret += "\n Temprature : "+str(d["result"]["temprature"])
							ret += "\n Weather : "+str(d["result"]["weather"])
							devi.sendReplyMessage(msg.id, to, str(ret))
						except Exception as e:
							devi.sendReplyMessage(msg.id, to, str(e))
					elif ibal == "tribun news":
						r = requests.get("https://ibalapi.herokuapp.com/api/tribunnews")
						data = json.loads(r.text)
						ret = "TribunNews\n"
						ret += "\n• Title : "+str(data["result"][0]["title"])
						ret += "\n• Url : "+str(data["result"][0]["url"])
						ret += "\n• Title : "+str(data["result"][1]["title"])
						ret += "\n• Url : "+str(data["result"][1]["url"])
						ret += "\n• Title : "+str(data["result"][2]["title"])
						ret += "\n• Url : "+str(data["result"][2]["url"])
						devi.sendReplyMessage(msg.id, to, str(ret))
#=================================================
#Steal
					elif ibal.startswith("getpicture "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								devi.sendReplyMessage(msg.id,to,f"https://obs.line-scdn.net/{devi.getContact(ls).pictureStatus}")
					elif ibal.startswith("getcover "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								image = devi.getProfileCoverURL(ls)
								path = str(image)
								devi.sendReplyMessage(msg.id,to,path)
					elif ibal.startswith("getbio "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								devi.sendReplyMessage(msg.id,to,"Status Message\n" + str(devi.getContact(ls).statusMessage))
					elif ibal.startswith("getname "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								devi.sendReplyMessage(msg.id,to," Name \n" + str(devi.getContact(ls).displayName))
					elif ibal.startswith("getcontact "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								contact = devi.getContact(ls)
								mi_d = contact.mid
								devi.sendContact(to, mi_d)
					elif ibal == "group":
						groups = devi.groups
						ret_ = "Group List"
						no = 0 + 1
						for gid in groups:
							group = devi.getGroup(gid)
							ret_ += "\n {}. {} | {} ".format(str(no), str(group.name), str(len(group.members)))
							no += 1
						ret_ += "\n Total {} Groups ".format(str(len(groups)))
						devi.sendReplyMessage(msg.id,to, str(ret_))
					elif ibal == "tagall" or ibal == "mentionall" or ibal == "dor":
						group = devi.getGroup(to)
						member = [a.mid for a in group.members]
						member.remove(devi.profile.mid)
						devi.datamention(to,"Mention Members",member)
#============================================
#End
		if op.type == 55:
			try:
				if op.param1 in read['readPoint']:
					if op.param2 in read['readMember'][op.param1]:
						pass
					else:
						read['readMember'][op.param1] += op.param2
					read['ROM'][op.param1][op.param2] = op.param2
				if cctv['cyduk'][op.param1]==True:
					if op.param1 in cctv['point']:
						Name = devi.getContact(op.param2).displayName
						if Name in cctv['sidermem'][op.param1]:
							pass
						else:
							cctv['sidermem'][op.param1] += "~ " + Name
							siderMembers(op.param1, [op.param2])
							contact = devi.getContact(op.param2)
					backupData()
				else:
					pass
			except:
				pass
	except Exception as error:
		error = traceback.format_exc()
def run_bot():
	while True:
		try:
			ops = devi_poll.singleTrace(count=50)
			if ops != None:
				for op in ops:
					loop.run_until_complete(ibal_devi(op))
					devi_poll.setRevision(op.revision)
		except TalkException as error:
			traceback.print_tb(error.__traceback__)
if __name__ == "__main__":
	run_bot()