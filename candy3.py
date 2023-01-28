import os
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet")
	print("نصب شد!")
	print("_"*40)
	os.system("clear")
try:
	from re import findall
except:
	os.system("pip install re")
	print("نصب شد!")
	print("_"*40)
	os.system("clear")
try:
	from random import choice
except:
	os.system("pip install random")
	print("نصب شد!")
	print("_"*40)
	os.system("clear")
try:
	import time
except:
	os.system("pip install time")
	print("نصب شد!")
	print("_"*40)
	os.system("clear")
try:
	from libraryArsein.Arsein import Robot_Rubika
except:
	os.system("pip install libraryArsein")
	print("نصب شد!")
	print("_"*40)
	os.system("clear")
	os.system("pip install pycryptodome")
	print("نصب شد!")
	print("_"*40)
	os.system("clear")


import os
import time
import pyfiglet
import datetime
from re import findall
from random import choice
from libraryArsein.Arsein import Robot_Rubika
os.system("clear")

red = '\033[31m' 
green = '\033[32m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'
print('\033[31m'+pyfiglet.figlet_format("  CANDY BOT",font='slant')+ "\n "+'\033[34m'+"_"*67+white)

#لینک_گپ
your_Group_Link="https://rubika.ir/joing/DGDFGICJ0ZKJPKAWTPBNFYOPUDUKGFXL"
#شناسه
bot = Robot_Rubika("chynvchlngaeadnwsaefxfzdfcypkdih")
#لینک_دونی
Linkdooni_Guid = ["c0BTXy05d5dbf4aa17e8c92e7e260973","c0Btyq095a83abe72ecf41080c6f1c35","c0Ee8O06d4d835c994ab8a51ea0e4880","c0Ee9X09008b057804dadf8f941e305a","c0HGkO0951a2f9159b86470742c0b5d0","c0MTeU0f77bd1c780b8b7509797bfd68","c0HGkO0951a2f9159b86470742c0b5d0","c0RSKL05e95414cec64d48b54f2e943e"]

Group_Guid=bot.joinGroup(your_Group_Link)["data"]["group"]["group_guid"]

alarm=10
TImeeSleep=0
errFor=0
forMsg=0
answered=[]
stop_finish=[]


bot.sendMessage(Group_Guid,"""فعال شد برای راهنمایی دستور help را ارسال کنید 🤖""")
while 1:
	try:
		min_id = bot.getGroupInfo(Group_Guid)["data"]["chat"]["last_message_id"]
		
		
		while 1:
			try:
				messages = bot.getMessages(Group_Guid,min_id)
				break
			except:
				continue

		for msg in messages:
			if msg['type'] == 'Text' :
					if msg.get('message_id') not in answered:
						answered.append(msg.get("message_id"))
						if msg.get("text").startswith("seen") :
								teedad_seen=msg.get("text").replace("seen ","")
								try:
									for i in bot.getMessagesInfo(Group_Guid, [msg.get("reply_to_message_id")]):
										if i.get("message_id")==msg.get("reply_to_message_id"):
											Bener__id=i['forwarded_from']['message_id']
											Baner_Guid=i['forwarded_from']['object_guid']
											for banner in bot.getMessagesInfo(Baner_Guid, [Bener__id]):
												if banner['message_id']==Bener__id:
													if int(teedad_seen) > int(banner['count_seen']) :
														teedad_seen1=teedad_seen
														azab=int(teedad_seen) - int(banner['count_seen'])
														bot.sendMessage(Group_Guid,f"درخواست شما تایید شد!\n تغداد سین باقی مانده = {azab}",message_id=msg.get("message_id"))
														start_time = datetime.datetime.now()
														bot.sendMessage(Group_Guid,f"درحال دریافت لینک گروه!",message_id=msg.get("message_id"))
														if int(teedad_seen) > int(banner['count_seen']):
															open("Group_Link.txt","w").write("Yasin_Bot")
															tedad_link=0
															for Linkdooni___Guid in Linkdooni_Guid:
																try:
																	File=open("Group_Link.txt","a")
																	bot.joinChannel(Linkdooni___Guid)
																	Channel_Message_Id = bot.getChannelInfo(Linkdooni___Guid)["data"]["chat"]["last_message_id"]
																	for Channel_Message in bot.getMessages(Linkdooni___Guid,Channel_Message_Id) :
																		for Group_Link in findall(r"https://rubika.ir/joing/\w{32}", Channel_Message.get("text")):
																			tedad_link+=1
																			File.write("\n"+Group_Link)
																except:pass
																		
														bot.sendMessage(Group_Guid,f"تعداد لینک های دریافت شده={tedad_link}",message_id=msg.get("message_id"))
													bot.sendMessage(Group_Guid,f"سین زدن شروع شد 🕊️!!!")
													ajibe=0
													while True:
														
														if int(teedad_seen) < int(banner['count_seen']):
															bot.sendMessage(Group_Guid,f"""‼️تمام شد!!!
❕ 🤖 تعداد فوروارد : {forMsg}
❕تعداد گروه های بسته 🕊️ {errFor}""",message_id=msg.get("message_id"))
															break
														try:
															for banner in bot.getMessagesInfo(Baner_Guid, [Bener__id]):
																if banner['message_id']==Bener__id:
																	if int(teedad_seen) > int(banner['count_seen']):
																			try:
																			
																				link=choice(open("Group_Link.txt","r").read().split("\n"))
																				Namad=bot.joinGroup(link)["data"]['chat_update']
																				if "SendMessages" in Namad["chat"]['access']:
																					ajibe+=1
																					if int(ajibe)==int(alarm):
																						ajibe=0
																						aaal=int(teedad_seen1) - int(banner['count_seen'])
																						bot.sendMessage(Group_Guid,f"""کاربر گرامی
پست شما به {alarm}گروه ارسال شد🕊️
تعداد سین فعلی بنر شما:{banner['count_seen']}
تعداد سین باقی مانده: {aaal}""",message_id=msg.get("message_id"))
																					Join_Guid=Namad['object_guid']
																					bot.forwardMessages(Baner_Guid,[Bener__id],Join_Guid)
																					bot.leaveGroup(Join_Guid)
																					forMsg+=1
																					time.sleep(int(TImeeSleep))
																				else:
																					bot.leaveGroup(Join_Guid)
																					errFor+=1
																			except:pass
														except:pass

								except:pass
						elif msg.get("text").startswith("اعلان") :
							try:
								adite_eelane=msg.get("text").replace("اعلان ","")
								if int(adite_eelane) != int(alarm) and int(adite_eelane) > 0:
									bot.sendMessage(Group_Guid,f"""ok
اعلان از {alarm} به {adite_eelane} تغییر کرد""",message_id=msg.get("message_id"))
									alarm=int(adite_eelane)
								else:
									if int(adite_eelane) > 0:
										bot.sendMessage(Group_Guid,f"""کاربر گرامی
سقف اعلان از قبل {alarm} بود candy bot 🤖""",message_id=msg.get("message_id"))
									else:
										bot.sendMessage(Group_Guid,f"""اعلان نمیتواند 0 باشد""",message_id=msg.get("message_id"))
							except:
								bot.sendMessage(Group_Guid,f"خطا 🕊️",message_id=msg.get("message_id"))
						elif msg.get("text").startswith("help") :
							try:
								bot.sendMessage(Group_Guid,f"""⛓️ راهنما  | دستورات 🔥

ممنونیم که از این ربات 🤖 استفاده میکنید !

دستور اول 🥶 
برای سین زدن کافیه بگید seen 200 
بعد ربات ۲۰۰ سین میزند 🌿

دستور دوم 🍉

اعلان هست که توی پیش فرض روی ۱۰ هست برای مثال اگه ربات ۱۰ فوروارد کنه به شما اطلاع میده 🥞

دستور آخر 🕊️

 تایم هست که میتونید تایم فوروارد را عوض کنید برای مثال تایم 2 الان ربات هر ۲ ثانیه فوروارد می‌کنه 

Candy bot 🤖""",message_id=msg.get("message_id"))
							except:pass
						elif msg.get("text").startswith("تایم") :
							try:
								adite_TImeeSleep=msg.get("text").replace("تایم","")
								TImeeSleep=int(adite_TImeeSleep)
								bot.sendMessage(Group_Guid,f"تایم با موفقیت به {adite_TImeeSleep} تغییر یافت \n از این به بعد هر {adite_TImeeSleep} ثانیه یک فوروارد انجام میشود",message_id=msg.get("message_id"))
							except:
								bot.sendMessage(Group_Guid,f"خطا در تغییر تایم📍",message_id=msg.get("message_id"))
	except:pass
