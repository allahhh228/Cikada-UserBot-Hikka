#meta developer: @moduleslist

from .. import loader, utils

import random
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from telethon.tl.functions.channels import JoinChannelRequest


bullr = [
    "WIN WITH PLUTONIUM!",
    "Хочешь глобала? Но как бро щас столько читеров,что это невозможно(",
    "Братан,есть же Plutonium, качай его и апай глобала без рута и бана",
    "Надоело проигрывать читерам? Скачивай Plutonium и уничтажай всех своих врагов.",
    "Aimbot, WH, Invisible и всё это БЕЗ БАНА и БЕЗ РУТ ПРАВ",
]


@loader.tds
class CikadaMod(loader.Module):
    strings = {
        "name": "☠️ Cikada"
    }
    
    async def client_ready(self, client, db):
        self.db = db
        self.users = self.db.get("cikada", "users", [])
        self.phrases = self.db.get("cikada", "phrases", [])
        
        await client(JoinChannelRequest("@moduleslist"))
    
    def add_phrase(self, phrase: str):
        self.phrases.append(phrase)
        self.db.set("cikada", "phrases", self.phrases)
    
    def add_user(self, user_id: int):
        self.users.append(user_id)
        self.db.set("cikada", "users", self.users)
    
    def remove_user(self, user_id: int):
        self.users.remove(user_id)
        self.db.set("cikada", "users", self.users)
    
    async def clearbullcmd(self, message):
        """Никого не буллить"""
        
        self.users = []
        self.db.set("cikada", "users", self.users)
        
        await utils.answer(
            message=message,
            response="<b>Больше я никого не унижаю</b>"
        )
        
    
    async def cikadatcmd(self, message):
        """Добавить фразу | .cikadat <фраза>"""
        
        args = utils.get_args_raw(message)
        
        if not args:
            return await utils.answer(
                message=message,
                response="<b>🚫 Не указан аргумент</b>"
            )
        
        self.add_phrase(args)
        
        await utils.answer(
            message=message,
            response="<b>Фраза добавлена</b>"
        )
    
    async def cikadarcmd(self, message):
        """Вкинуть рандомное оскорбление"""
        
        await utils.answer(
            message=message,
            response=random.choice(bullr + self.phrases)
        )
    
    async def cikadacmd(self, message):
        """Буллить человека. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            if reply.from_id is not None:
                await utils.answer(
                    message=message,
                    response="<b>я те мать ебал</b>"
                )

                self.add_user(reply.from_id)
            
            else:
                await utils.answer(
                    message=message,
                    response="<b>🚫 Модуль не работает на анонимных администраторах или каналах</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🚫 Нужен реплай</b>"
            )
    
    async def cikadarmcmd(self, message):
        """Не буллить человека. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            await utils.answer(
                message=message,
                response="<b>отсосал ты сын шлюхи</b>"
            )
            
            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<b>💀 Я и так не унижаю этого человека</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🚫 Нужен реплай</b>"
            )
    
    async def watcher(self, message):
        if getattr(message, "from_id", None) in self.users:
            await message.reply(random.choice(bullr + self.phrases))