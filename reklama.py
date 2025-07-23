from pyrogram import Client
import asyncio

# Константы
SOURCE_CHAT_ID = "me"
TARGET_CHAT_ID = -1001984966725

# Ввод данных
print("авторизация через телеграм. надо ввести данные. Создал @KingOfInsanity")
api_id = int(input("Введи свой API ID: "))
api_hash = input("Введи свой API HASH: ")
session_name = "akkaunt_data"

# Клиент
app = Client(session_name, api_id=api_id, api_hash=api_hash)

# Основная функция
async def forward_last_message():
    async for message in app.get_chat_history(SOURCE_CHAT_ID, limit=1):
        if message:
            await app.forward_messages(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=SOURCE_CHAT_ID,
                message_ids=message.id
            )
            print("сообщение переслано.")
        else:
            print("нет сообщений в избранном.")

# Главный цикл
async def main():
    async with app:
        print("авторизован. рассылка начата.")
        while True:
            await forward_last_message()
            await asyncio.sleep(3600)
