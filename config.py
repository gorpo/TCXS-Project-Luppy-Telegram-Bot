# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]

import amanobot
import amanobot.aio
import asyncio
import os



#LOCAL CONFIG rodar em local host use as linhas abaixo--->
token =  "token pego no botfather colocar dentro das aspas"
token_dropbox = 'token pego no dropbox colocar dentro das aspas utilizado pelo sistema de backup e upload manual'
token_imgur =  "token do imageur entre aspas utilizado pelo sistema de criar sites"
#https://api.hgbrasil.com/weather
token_weather = 'token do weather entre aspas utilizado pelo sistema de pesquisa do clima'






#em logs colocar sua id ou id de um canal para ele enviar logs de erros e outros
logs = 12341234
#em sudoers colocar quem tera acesso full ao bot e comandos especiais na maquina que o bot esta rodando, separe os usuarios por virgula dentro da lista colocando sua id do telegram (cuidado a pessoa tera total acesso a sua maquina que hospeda o bot)
sudoers = [12341234,]








#HEROKU CONFIG - rodar no heroku use as linhas abaixo descomentando elas, comente as linhas acima, o heroku nao permite escrita portanto usar o dropbox la nao é possivel------->
#token = os.environ['TELEGRAM_TOKEN']
#logs = os.environ['LOGS']
#sudoers = os.environ['SUDOERS']





#----------------------------------------------------
loop = asyncio.get_event_loop()  # Do not change this
bot = amanobot.aio.Bot(token)
na_bot = amanobot.Bot(token)
me = loop.run_until_complete(bot.getMe())
bot_username = me['username']
bot_id = me['id']
keys = dict(
    here = {'app_id': 'key_id_here', 'app_code': 'key_code_here'},  # https://here.com
    yandex = 'trnsl.1.1.20190asde811T18qwe4100Z.f3e1e6d6d3507525.7ea9c78123123123123123123',# pegue seu token em https://tech.yandex.com/translate
    giphy = '7f6ws7EvslO9BuaccaAKie9BasdieyYnD3OkaskT',# Pegue seu token em https://developers.giphy.com
)





backups_chat = 522523410051  #insira a id do canal, grupo ou administrador que ira receber os backups no horario agendado, troque o horario abaixo
backup_hours = ['15:56']




git_repo = ('https://github.com/gorpoorko/Manicomio-Bot-IA', 'master') #repositorio para upgrade do bot
max_time = 60
version = '7.0'




enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'shorten',
    'kibe',
    'translate',
    'rextester',
    'inlines',
    'welcome',
    'admins',
    'warns',
    'prints',
    'pypi',
    'weather',
    'youtube',
    'ping',
    'gif',
    'git',
    'reddit',
    'coub',
    'sudos',
    'ids',
    'ip',
    'jsondump',
    'dice',
    'misc',
    'tcxs',
    'hora_data',
    'trollagens',
    'randomicas',
    'calculadora',
    'users',
    'inteligencia',
    'permanencia',
    'dropbox_upload',
    'link_direto',
    'antiflood',
    'avatar',
    'notepad_telegraph',
    'cria_site_telegraph',
    'qrcode',

]
