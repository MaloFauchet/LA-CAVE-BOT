import datetime

import discord
import logging
import random

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(name='Being Racist is Fun', type=discord.ActivityType.competing,
                            created_at=datetime.date.today())
client = discord.Client(intents=intents, activity=activity)

help_message = '- Yohan\n- Daniel\n- Irving\n- Igor\n- Titouan\n- Nolo'

yohan_list = ['https://cdn.discordapp.com/attachments/956556924076298240/1033787679642505256/unknown.png',
              'https://tenor.com/view/oh-no-anime-stop-this-weeb-shit-weeb-shit-gif-13706746']

daniel_list = ['chan', 'UwU', '#RTXMaker', 'https://tenor.com/view/daniel-iland-daniel-iland-daniel-kim-gif-18126267']

hoyeon_list = ['시작이 반이다.', '열번찍어 안넘어가는 나무 없다.', '시작이 반이다.', '열흘 붉은 꽃이 없다.',
               '하늘이 무너져도 솟아날 구멍이 있다', '빈 수레가 요란하다.', '공자 앞에서 문자 쓴다', '오늘 걷지 않으면 내일은 뛰어야 한다',
               '등잔 밑이 어둡다', '치지 않은 공은 100% 골인되지 않는다.', '나무를 심는데 가장 좋았던 때는 20년 전이었다. 두 번째로 좋은 때는 지금이다.']
# 어떻게 알았어?
nolo_list = ['https://tenor.com/view/its-very-tiny-emma-engvid-its-so-small-its-so-little-gif-25786614',
             'https://tenor.com/view/monster-hunter-palico-monster-hunter-rise-monster-hunter-world-mh-gif-25184238']

igor_list = ['https://tenor.com/view/soviet-cat-sovicat-soviet-ussr-cat-gif-21826197',
             'https://tenor.com/view/igor-vs-error-gif-18579238',
             'https://tenor.com/view/stalin-locket-russia-ussr-gif-23370601']

feur_list = ['FEUR', 'chi', 'FEUSE',
             'https://cdn.discordapp.com/attachments/943910110399447080/1033790112359780512/unknown.png']

a_list = ['a', 'A', 'ah', 'Ah', 'aH', 'AH']


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Help':
        await message.channel.send(help_message)

    if message.content == 'Yohan':
        await message.channel.send(yohan_list[random.randint(0, len(yohan_list))])
    if message.content == 'Daniel':
        await message.channel.send(daniel_list[random.randint(0, len(daniel_list))])
    if message.content == 'Hoyeon':
        await message.channel.send(hoyeon_list[random.randint(0, len(hoyeon_list))])
    if message.content == 'Irving':
        await message.channel.send('https://tenor.com/view/hmm-suspect-gif-22611582')
    if message.content == 'Igor':
        await message.channel.send(igor_list[random.randint(0, len(igor_list))])
    if message.content == 'Nolo':
        await message.channel.send(nolo_list[random.randint(0, len(nolo_list))])
    if message.content == 'Titouan':
        await message.channel.send('.')

    if (('quoi ' or 'Quoi ') in message.content) or (message.content.endswith('quoi')):
        await message.channel.send(feur_list[random.randint(0, len(feur_list))])
    if message.content in a_list:
        await message.channel.send('B')
    if message.content == 'feur' or message.content == 'Feur':
        await message.channel.send('Bien vu')
    if message.content == 'Bambou':
        await message.channel.send('Là.')
    if message.content == 'chien':
        await message.channel.send('Chienne')

    if message.content == 'simp':
        await message.channel.send('Yohan')

    if message.content == 'Ping':
        await message.channel.send('Pong')
    if message.content == 'Ching':
        await message.channel.send('Chong')
    if message.content == 'Da':
        await message.channel.send('niel')

    if message.content == 'No':
        await message.channel.send('lol')

    if message.content.startswith('.d'):
        print('good')
        if not message.author.voice:
            await message.channel.send(f"{message.author} is not connected to a voice channel")
        else:
            print('regood')
            channel = message.author.voice.channel
            await channel.connect()

    if message.author == 'Malo_F#9314':
        print(message.id)
        await message.channel.send(client.get_emoji(1))

    if message.content.startswith('Supprime-moi'):
        await message.channel.send('I will delete myself now...', delete_after=3.0)


client.run('', log_handler=handler)
