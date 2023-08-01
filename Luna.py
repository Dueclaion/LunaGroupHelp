from telethon import *
from lazımlılar.config import Luna
from telethon.sessions import StringSession
import asyncio
import random
import os
import youtube_dl
from youtube_search import YoutubeSearch
import yt_dlp
import requests
from telethon.errors import MessageNotModifiedError
from telethon.sync import TelegramClient, events
from telethon import events
from Temalar.tema import temalar
import time
from  Toollar.sozler import salam, necesen, geldim, ayrılan_user, yeni_user, ban, Ruslan

SAHIB = [5823466637]


@Luna.on(events.NewMessage(pattern="/start"))
async def start(event):
		if event.is_private:
		  		async for usr in Luna.iter_participants(event.chat_id):
		  			ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
		  			await Luna.send_message(-1001906435140, f"Start Verən İstifadəçi - {ad}")
		  			await event.reply(f"🤩Salam, Mən Ruslan Tərəfindən Hazırlanmış Bir Sadə Botam😋\nƏraflı Məlumat Üçün 👨‍💻@Dueclaion Hesabına Yazın\n\nÇox Yaxında Yeni Funksiyalar Olacaq🤗", buttons=(
		  			[Button.url('👨‍💻Kodlayan', 'https://t.me/Dueclaion')],
		  	 	[Button.url('👨🏼‍💻Credits', 'https://t.me/edalet_22')],
		  	 	[Button.url('🎮Oyun Qurubumuz', 'https://t.me/TheBorzMaf')],
		  	 	[Button.inline(f"📕Əmrlər", data="help")]
		  			),
		  			link_preview=False)
		  			
@Luna.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
		if event.is_private:
			await event.reply(f"🤩Salam, Mən Ruslan Tərəfindən Hazırlanmış Bir Sadə Botam😋\nƏraflı Məlumat Üçün 👨‍💻@Dueclaion Hesabına Yazın\n\nÇox Yaxında Yeni Funksiyalar Olacaq🤗", buttons=(
		  			[Button.url('👨‍💻Kodlayan', 'https://t.me/Dueclaion')],
		  	 	[Button.url('👨🏼‍💻Credits', 'https://t.me/edalet_22')],
		  	 	[Button.url('🎮Oyun Qurubumuz', 'https://t.me/TheBorzMaf')],
		  	 	[Button.inline(f"🔙Geri", data="geri")],
		  	 	[Button.inline(f"📕Əmrlər", data="help")]
		  			),
		  			link_preview=False)
		  			
@Luna.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
			await event.edit("🙋‍♂️Salam Əmrlər Bölmesinə Xoş Gəlmisiz, 📕Əmrlərimi Görmek Üçün Aşağı Baxınn👇", buttons=(
			[Button.inline('📩Etiraf Et', data="etiraf"),
			 Button.inline('💾Temalar', data="Tema")],
			[Button.inline('🎧Musiqi', data="music"),
			Button.inline('🖊Matematik', data="math")],
			[Button.inline('🔢Sayı Tahmin', data="sayi")],
			
			[Button.inline('🚹Tağ', data="tag"),
			Button.inline('🔙Geri', data="start")],
			),
			link_preview=False)
			
@Luna.on(events.callbackquery.CallbackQuery(data="tag"))
async def tag(event):
  await event.edit("🤗Salam Mənim Tağ Bölməmə Xoş Gəlmisiz🤩.Mən Qurubdakı İnsanları Tağ Etmek Xususiyətinə Malikəm🚹.Tək Eləmən Gərək Aşagıdakı Əmrlərə Baxman👇\n\n\nİnsanları Daha Tez Çagırmak Üçün🚀 - /hizlitag\n\nİnsanlari Yavaş Çagırman Üçün⏳ - /yavastag\nT\nTag prosini Dayanmırmaq Üçün Ise🛑 - /stop Əmrini Yerinə Yetir.\nƏminəmki Məni Bəyəndin🥰", buttons=(
    [Button.inline('🔙Geri', data="help")],
    ),
    link_preview = False)
    
    
@Luna.on(events.callbackquery.CallbackQuery(data="sayi"))
async def handler(event):
  await event.edit("🤗Salam Sən Mənimlə Sayı Tahmin Edə Bilərsən🤩.Bot 1 dən 500 ə Qədər Bir Sayı Seçir🔢 Ve İstifadəçiler O Sayıyı Tapmağa Çalışır.🎮Oynamaq Üçün /oyun Komandasını Yerinə Yetirin." , buttons=(
    [Button.inline('🔙Geri', data="help")]
    ),
    link_preview = False)
    
    
@Luna.on(events.callbackquery.CallbackQuery(data="music"))
async def handler(event):
  
  await event.edit("🤗Salam, Musiqi Bölməmə Xoş Gəlmisiz.Siz Mənə Istediyin 🎧Musiqinin Sadəcə Adını Desen Mən Sizin Üçün O Musiqiyi Yükleyib Ata Bilerem\n\nTək Elemen Gərək, ✅/song Əmrini Yazıb Musiqinin Adını Yazmaq\n\n🔁Nümune : /song Altüst Olmuşum", buttons=(
    [Button.inline('🔙Geri', data="help")],
    ),
    link_preview = False)
#Temalarr						
last_message_time = time.time()
@Luna.on(events.NewMessage(pattern="^/Tema ?(.*)"))
async def yeni_mesaj(event):
    global last_message_time
    current_time = time.time()
    
    if current_time - last_message_time >= 3:  # 3 saniyeden daha uzun süre geçtiyse
        await event.reply(f"{random.choice(temalar)}", buttons=[
            Button.inline("🔄Dəyiş", data="Tema"),
            Button.inline("🔙Geri", data="help")
        ])
        last_message_time = current_time
    else:
        # Daha hızlı basıldığında bildirim gönder
        await event.respond("Daha yavaş basın!")
		
			
@Luna.on(events.callbackquery.CallbackQuery(data="Tema"))
async def handler(event):
	await event.edit(f"{random.choice(temalar)}", buttons=[
	Button.inline("🔄Dəyiş", data="Tema"),
	Button.inline("🔙Geri", data="help")
	])
		
#Tema

# Telethon oturumu oluşturma veya kayıtlı oturumu yükleme
# Eğer daha önce bir oturum oluşturduysanız, "YOUR_STRING_SESSION" kısmına oturumunuzu yapıştırın
# Aksi takdirde, oturumu kaydedip buraya yapıştırın ve bir kez çalıştırın


# Matematik işlemlerini yapacak işlev
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Hata: {e}"

@Luna.on(events.NewMessage(pattern='^/calculate .*'))
async def handle_calculate(event):
    expression = event.message.message.replace('/calculate ', '')
    result = calculate(expression)
    await event.respond(f"📊Sonuç: {result}")
    
@Luna.on(events.callbackquery.CallbackQuery(data="math"))
async def math(event):
	await event.edit("🙋‍♂️Salam, Sen Menimle 🔢Matematik İşlerini Yerine Yetire Bilersen,Tek Elemen Gerek /calculate yazıb Işlemi Seçmek🔣, Meselen /calculate 5 + 3 ", buttons=(
	[Button.inline('🔙Geri', data="help")],
	),
	link_preview=False)
	


@Luna.on(events.NewMessage(from_users=SAHIB, pattern='^/ship'))
async def handle_ship(event):
    try:
        participants = await event.client.get_participants(event.chat_id, limit=200)
        members = [user for user in participants if not user.bot]
        random_users = random.sample(members, 2)
        user1, user2 = random_users[0], random_users[1]
        await event.respond(f"@{user1.username} ve @{user2.username} Harika bir çift olabilirsiniz💝🙎‍♂️🙎‍♀️.")
    except Exception as e:
        print("Hata:", e)




#Online Metod
@Luna.on(events.NewMessage(pattern="/online"))
async def handler_online(event):
							sender = await event.get_sender()
							if sender.username == "Dueclaion":
												await event.respond("Salam🙋‍♂️ Dəyərli Sahibim🤩, Necesenn")
							else:
													
													await event.respond("Sen Mənim Sahibim Deyilsen❗, Öz işinle Məşğul Ol❌")
												
@Luna.on(events.ChatAction)

async def handler(event):
  
  
	if event.user_left:
	  
	  await event.reply(f"{random.choice(ayrılan_user)}")
	  
	  
@Luna.on(events.ChatAction)
async def handler(event):
  if event.user_joined:
    await event.reply(f"{random.choice(yeni_user)}")


running = False
@Luna.on(events.NewMessage(pattern='^/hizlitag'))
async def handle_tagall(event):
    global running
    running = True
    participants = await event.client.get_participants(event.chat_id, limit=200)
    for user in participants:
        if not user.bot:
            await event.respond(f"@{user.username or user.first_name}")
            await asyncio.sleep(1)  # 1 saniyelik gecikme ekleyin
            if not running:
                break
              

  


@Luna.on(events.NewMessage(pattern='^/yavastag'))
async def handle_tagall(event):
    global running
    running = True
    participants = await event.client.get_participants(event.chat_id, limit=200)
    for user in participants:
        if not user.bot:
            await event.respond(f"@{user.username or user.first_name}")
            await asyncio.sleep(3)
            
@Luna.on(events.NewMessage(pattern='^/stop'))
async def handle_stop(event):
  global running
  await event.respond("Bot etiketleme işlemini durduruyor❌❌❌")
  running = False
  

# Başlangıç aralığını belirleyin
min_number = 1
max_number = 500
secret_number = random.randint(min_number, max_number)

# Oyun durumunu takip etmek için değişken
game_started = False

# Komutları işleyen fonksiyon
@Luna.on(events.NewMessage(pattern='/oyun'))
async def start(event):
    global secret_number, min_number, max_number, game_started
    if not game_started:
        game_started = True
        min_number = 1
        max_number = 500
        secret_number = random.randint(min_number, max_number)
        await event.respond(f'🔢{min_number} ile {max_number} arasında bir sayı tahmin edin❗')
    else:
        await event.respond('🎮Oyun zaten başlamış. Lütfen bir sonraki oyun için bekleyin❌❌')

@Luna.on(events.NewMessage(pattern=r'\d+'))
async def guess(event):
    global min_number, max_number, secret_number, game_started
    if game_started:
        user_guess = int(event.text)

        if user_guess == secret_number:
            await event.respond('✅Tebrikler, doğru tahmin ettiniz')
            game_started = False  # Oyunu burada bitirin
        elif user_guess < secret_number:
            await event.respond('🔝Daha yüksek bir sayı deneyin❗')
        else:
            await event.respond('⬇️Daha düşük bir sayı deneyin❗')


# 'bot' değişkenini tanımlamak ve başlatmak için gerekli kodları ekleyin

@Luna.on(events.NewMessage(from_users=SAHIB, pattern="^/song ?(.*)"))
async def song(event):
    query = event.pattern_match.group(1)
    search = await event.reply("🔍Musiqi axtarılır...")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            await search.edit("❌Musiqi tapılmadı")
            return

        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:45]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
    except Exception as e:
        await search.edit("❌Musiqi tapılmadı")
        print(str(e))
        return

    await search.edit("⏳Musiqi endirilir...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            text = f"🎤Adı: [{title}]({link})"
            await search.edit("⚡Musiqi göndərilir...")
            await search.delete()
            await Luna.send_file(event.chat_id, audio_file, caption=text, parse_mode='md', quote=False, title=title, duration=duration, thumb=thumb_name, performer="Song Bot")
    except Exception as e:
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
@Luna.on(events.NewMessage(pattern="^/id ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")
									
													
print("Luna Mükemmel Çalışıyorr")
Luna.run_until_disconnected()
