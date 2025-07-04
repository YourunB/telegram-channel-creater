from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, CreateForumTopicRequest

api_id = 11111111
api_hash = '111aaa111aaa111aaa111aaa'

client = TelegramClient('session_name', api_id, api_hash)

tour_name = "Сёрф-Кемп"
date = "02.07.2025"
group_title = f"{tour_name} {date}"

async def main():
  await client.start()
  # cоздание форум-группы
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

