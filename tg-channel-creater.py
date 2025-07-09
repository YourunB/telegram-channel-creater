import sys
import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, CreateForumTopicRequest

load_dotenv()

api_id = int(os.getenv('TG_API_ID'))
api_hash = os.getenv('TG_API_HASH')

client = TelegramClient('session_name', api_id, api_hash)

tour_name = sys.argv[1]
date = sys.argv[2]
group_title = f"{tour_name} {date}"

async def channel_exists(title):
  async for dialog in client.iter_dialogs():
    if dialog.is_channel and dialog.name == title:
      return True
  return False

async def main():
  await client.start()

  if await channel_exists(group_title):
    print(f"Группа '{group_title}' уже существует. Создание отменено.")
    return

  result = await client(CreateChannelRequest(
    title=group_title,
    about="Группа тура",
    megagroup=True,
    forum=True
  ))

  group = result.chats[0]
  
  topics = [
    "💬 Чат",
    "⚠️ Важная информация",
    "📸 Фотофиксация",
    "👍 Отзывы",
    "🕒 Расписание",
    "✈️ Прилёт/вылет"
  ]

  for topic in topics:
    await client(CreateForumTopicRequest(
      channel=group.id,
      title=topic
    ))

with client:
  client.loop.run_until_complete(main())
