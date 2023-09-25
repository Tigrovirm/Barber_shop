from typing import Any
from django.core.management.base import BaseCommand
from telegram.management.commands.config import bot
from services.models import Client
import random


@bot.message_handler(commands=['start'])
def start(message):
    try:
        client = Client.objects.get(telegram_id=message.from_user.id)
        text = f"Ваш уникальныфй ID: {client.uniq_id}"
        bot.send_message(chat_id = message.from_user_id, text = text, parse_mode="html")
    except:
        client = None
        uniq_id = random.randint(100000, 999999)
        bot.send_message(message.from_user.id, text="Работает")
        while len(Client.objects.filter(uniq_id=uniq_id)) > 0:
            uniq_id = random.randint(100000, 999999)
        client = Client.objects.create(uniq_id=uniq_id, telegram_id=message.from_user.id)
        client.save()
        text = f"Спасибо за регестрацию,Ваш уникальныфй ID: {client.uniq_id}"
        bot.send_message(chat_id=message.from_user_id, text = text, parse_mode="html")

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        print("RUN BOT . . .")
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling(timeout=60, none_stop=True)
        print("STOP BOT . . .")
