from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 28348304
API_HASH = "99275a99d9d593fd50ecf6127f0ac312" 
bot_token = "6687245954:AAHjw3ifmApIGOtbBJfzEOvxZ2oWqE52Yo4"
string_session = "1ApWapzMBu4kSSgh-dBnaJEcjHvO2a_QtFjsvcv9fD4sJ1Stq_RzgMu44Q8ub9FnRnj1qTNkTPki1YpR2B_yKj3RuICOqnjVjroq6zxvKIcCvtIzs0EpogwJRYHooHU-j2YLvnVyjbb6oXA5FWqTbwTMn6PXLTyDYHgb93abvAiWCVOD0LaOCW6FuK6DYONHDqoJoiNR-1foBK4jvbjq8lQGrVNC4MqknKve38RCFXJbR0wzPKEpSUrX6iymCvX04OpFQRoFb5tDjzmk-YS0akmolQkOMfURyrfZsTetNxrAep4JdUJRko1hF5oPTk-e4059WozF9oSDcAxjVgEZT8N-JUEJyKEA="

Luna = TelegramClient(StringSession(string_session), API_ID, API_HASH).start(bot_token=bot_token)

print("Modul Yüklendi")
