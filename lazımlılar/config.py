from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 28348304
API_HASH = "99275a99d9d593fd50ecf6127f0ac312" 
bot_token = "6079678077:AAGKQjLzvE5a5NiHs8wnA8OvXZ65Bz8FVnE"
string_session = "1ApWapzMBu1g-oDeolumFkvMqFEh_0GZ7TdxgU1k-491a0itPC4Arw3CWdO-vs8hX2SXE3SoHEn6pxm4KG0fVl7p6vNRtQ0nVBvUlO1G-fMuzqDncIrFwVCWHgCReRwKEmbJHdiOxrXALlXQSGU2vbVfBxVJbz__fmyZu5LWB_hbSQah9FlFoZ88TwwXBOTzHfdxTHiImcoIO4HH-6FlNzHQwZaufYaML_By58e1KUdH1td1YJJFTv8-GOUpvwDf-Sx7vOtlBK5g3fihM0JJCoHBSI0etWNPcdKjsFXJzVeF7hddbcxRxD63SaQzlZcLIIxUzs46ma1s632l2xUEv6fRpV6Usckg="
admin_qrup = int(os.environ.get(""))
etiraf_qrup = int(os.environ.get(""))
kanal = os.environ.get("")
log_group = int(os.environ.get(""))
botad = os.environ.get("")
etirafmsg = os.environ.get("")
startmsg = os.environ.get("")
etirafyaz = os.environ.get("")
qrupstart = os.environ.get("")
gonderildi = os.environ.get(""))
support = os.environ.get("")
sahib = os.environ.get("")
Luna = TelegramClient(StringSession(string_session), API_ID, API_HASH).start(bot_token=bot_token)

print("Modul Yüklendi5")
