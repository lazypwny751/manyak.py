#!/bin/python3

#    Manyak bot pandemi döneminde can sıkıntısından yağıldı - manyak.py yoksa sh mı demeliydim
#    Copyright (C) 2022  lazypwny751
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import time
import random
import discord
import os
from discord.ext import commands
from termcolor import colored, cprint

token = ""

async def start_bot():
    await client.start('token')
cprint('\t\t\t Bot Çalışıyor\n', 'blue', attrs=['blink'])

bot = commands.Bot(command_prefix='$')

bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="$help / $yardım", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('------------------------------------------------------------\n$help veya $yardım ile mevcut komutları görüntüleyebilirsin.\n------------------------------------------------------------')

@bot.command()
async def test(ctx):
    await ctx.send('manyaqmısın olm')
    cprint('test komutu çalıştırıldı', 'red')


#@bot.command()
#async def spam(ctx):
#    cprint('spam komutu çalıştırıldı', 'red')
#    while True:
#        await ctx.send('@admin')
#        cprint('spam atıldı +1', 'yellow')
#    cprint('spam komutu durdulurdu?', 'red')

@bot.command()
async def spam(ctx):
    incprint = 0
    cprint('spam komutu çalıştırıldı', 'red')
    while True:
        incprint+=1
        await ctx.send(str(incprint) + ' @everyone spam atma la **Melkor**')
        cprint('spam atıldı +1', 'yellow')
    cprint('spam komutu durdulurdu?', 'red')

@bot.command()
async def spam5(ctx):
    cprint('spam komutu çalıştırıldı', 'red')
    count = 0
    while count < 5:
        await ctx.send('manyaqmısın olm')
        count += 1
        cprint('spam atıldı +1', 'yellow')
    await ctx.send('5 adet spam atıldı' )
    cprint('spam komutu durdulurdu +', 'green')

#@bot.command()
#async def send_dm(ctx, member: discord.Member, *, content):
#    channel = await member.create_dm()
#    await channel.send(content)
#    print(member, 'bir direkt mesaj gönderildi')

@bot.command()
async def dm(ctx, member: discord.Member, *, content, amount=1):
    await ctx.channel.purge(limit=amount +0)
    channel = await member.create_dm()
    await channel.send(content)
    print(member, 'kullanıcısına bir direkt mesaj gönderildi')

@bot.command("cowsay")
async def cowsay(ctx, *, content):
    os.system("cowsay " + content + " > cowsay.txt")
    cowfile = open("cowsay.txt","r")
    embed = discord.Embed(
    description = ("```" + str(cowfile.read()) + "```"),
    colour = discord.Colour.red()
    )
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    await ctx.send(embed=embed)
    print('bir cow gönderildi')

@bot.command("Eryaman!")
async def Eryaman(ctx):
    eryamansiir = open("eryamansiir.txt", "r")
    embed = discord.Embed(
    title = "yaşasın Eryaman",
    description = ("```" + str(eryamansiir.read()) + "```"),
    colour = discord.Colour.red()
    )
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    embed.set_image(url='https://cdn.discordapp.com/attachments/708309578458202174/742067149291388948/WhatsApp_Image_2020-08-05_at_13.07.36_1.jpeg')
    await ctx.send(embed=embed)
    print('Eryaman Mesajı Gönderildi')

@bot.command("AbdulhamidHan!")
async def Abdulhamid(ctx):
    abdulhamidhan = open("abdulhamidhan.txt", "r")
    embed = discord.Embed(
    title = "Ruhun Şaad Olsun Abdulhamid Han.",
    description = ("```" + str(abdulhamidhan.read()) + "```"),
    colour = discord.Colour.green()
    )
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    embed.set_thumbnail(url='https://img-s1.onedio.com/id-55fd382a5ad3bd3c10a5d702/rev-0/w-500/s-77b6884a59fdca21806645b9c4fae6c8f729edc3.jpg')
    embed.set_image(url='https://www.bayrakreyonu.com/wp-content/uploads/osmanli-arma-bayrak-fiyat.jpg')
    await ctx.send(embed=embed)
    print('Abdulhamid Han +')

#@bot.command("Atatürk!")
#async def Atatürk(ctx):
#   embed = discord.Embed(yakında)
#   title = "Saygı ile anıyoruz seni Atatürk."
#   description = "yakında"
#   ... # yakında

@bot.command()
async def geçicimesaj(ctx):
    await ctx.send('5 saniye sonra silincek', delete_after=5)
    cprint('geçici mesaj komutu çalıştırıldı', 'red')

@bot.command()
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    #cprint(amount, 'adet mesaj silindi +', 'yellow')
    print(amount, 'adet mesaj silindi +')


@bot.command("covid19")
async def covid19(ctx):
    #print(str(ctx.author)+" > "+str(ctx.channel) + " > " + str(ctx.command))
    await ctx.send('Biraz Bekleyin Bu İşlem BirKaç Saniye Alacak Gibi Görünüyor', delete_after=1)
    os.system("./bilgi-covid19 -od")
    covidfile = open("covidtoday.txt","r")
    embed = discord.Embed(
    title = 'Güncel Covid 19 Tablosu:',
    description = (str(covidfile.read())),
    colour = discord.Colour.green()
    )
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    embed.set_thumbnail(url='https://n11scdn.akamaized.net/a1/org/kozmetik-kisisel-bakim/tek-kullanimlik-urunler/3-katli-lastikli-cerrahi-yuz-maskesi-koruyucu-maske-50-adet__1568451563194940.png')
    embed.set_image(url='https://media-cdn.t24.com.tr/media/library/2020/06/1592942506957-fah.png')
    await ctx.send(embed=embed)
    cprint('Güncel Covid19 tablosu komutu çalıştırıldı +', 'green')
    #if os.path.isfile("covidtoday.txt"):
    #    os.system("rm covidtoday.txt")

@bot.command("doviz")
async def doviz(ctx):
    print(str(ctx.author) + ">"+str(ctx.channel) + ">" + str(ctx.command))
    await ctx.send('Biraz Bekleyin Bu İşlem BirKaç Saniye Alacak Gibi Görünüyor', delete_after=2)
    os.system("./doviz")
    doviz = open("doviz.txt","r")
    embed = discord.Embed(
    title = 'Güncel Doviz Tablosu:',
    description = (str(doviz.read())),
    colour = discord.Colour.red()
    )
    embed.set_image(url='https://upload.wikimedia.org/wikipedia/commons/6/64/1TL_obverse.png') #https://upload.wikimedia.org/wikipedia/commons/6/64/1TL_obverse.png
    embed.set_thumbnail(url='https://www.millionbebe.com/images/borsa.png')
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    await ctx.send(embed=embed)
    cprint('Güncel Doviz tablosu komutu çalıştırıldı +', 'green')

@bot.command("sondakika")
async def sondakika(ctx):
    await ctx.send('Biraz Bekleyin Bu İşlem BirKaç Saniye Alacak Gibi Görünüyor', delete_after=1)
    print(str(ctx.author) + ">"+str(ctx.channel) + ">" + str(ctx.command))
    os.system("./sondakika")
    sondakika = open("sondakika.txt","r")
    embed = discord.Embed(
    title = 'Son Dakika Haberleri:',
    description = (str(sondakika.read())),
    colour = discord.Colour.red()
    )
    embed.set_thumbnail(url='https://www.pinclipart.com/picdir/middle/361-3617622_humanity-news-globe-logo-png-clipart.png')
    embed.set_image(url='https://www.rujmuj.com/wp-content/uploads/2020/06/son-dakika-hakkaride-3-terorist-etkisiz-hale-getirildi-tym5rReH.gif') # https://iprgezgini.org/wp-content/uploads/2019/07/cropped-son-dakika.png
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    await ctx.send(embed=embed)
    cprint('Güncel Son Dakika Haberleri Gösterildi +', 'green')

@bot.command("espri")
async def espri(ctx):
    #await ctx.send('Biraz Bekleyin Bu İşlem BirKaç Saniye Alacak Gibi Görünüyor', delete_after=1)
    print(str(ctx.author) + ">"+str(ctx.channel) + ">" + str(ctx.command))
    os.system("./espiri espiri")
    espiri = open("espiri.txt","r")
    embed = discord.Embed(
    title = 'Buz Gibi Bir Espri :)',
    description = ("```" + str(espiri.read()) + "```" + "a script by lazy-pwny: https://github.com/lastpingu"),
    colour = discord.Colour.orange()
    )
    embed.set_thumbnail(url='https://p.kindpng.com/picc/s/10-100233_facebook-haha-emoji-png-transparent-png.png')
    embed.set_image(url='https://media1.tenor.com/images/274de584e24b65e772a330c217e917d1/tenor.gif')
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    await ctx.send(embed=embed)
    cprint('Buz Gibi Soğuk Bir Espiri Yapıldı +', 'green')

@bot.command("atasözü")
async def atasözü(ctx):
    #await ctx.send('Biraz Bekleyin Bu İşlem BirKaç Saniye Alacak Gibi Görünüyor', delete_after=1)
    print(str(ctx.author) + ">"+str(ctx.channel) + ">" + str(ctx.command))
    os.system("./espiri atasoz")
    linuxatasozu = open("atasozu.txt","r")
    embed = discord.Embed(
    title = 'Güzel Bir Linux Atasözü:',
    description = ("```" + str(linuxatasozu.read()) + "```" + "a script by lazy-pwny: https://github.com/lastpingu"),
    colour = discord.Colour.orange()
    )
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/527560284928213021/7c0a001eb6c8545b91651d04c8668448.jpg')
    embed.set_image(url='https://i.pinimg.com/originals/68/5e/b4/685eb4a66bfe809067fc677bb2a361ea.gif')
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    await ctx.send(embed=embed)
    cprint('Atasözü Yazdırıldı +', 'green')

@bot.command("yak")
async def yak(ctx):
    #await ctx.send('Biraz Bekleyin Bu İşlem BirKaç Saniye Alacak Gibi Görünüyor', delete_after=1)
    print(str(ctx.author) + ">"+str(ctx.channel) + ">" + str(ctx.command))
    os.system("./espiri dolaryak")
    dolaryak = open("dolaryak.txt","r")
    embed = discord.Embed(
    title = 'Zengin Bir Babayiğit Dolar Yaktı(tamamen eğlence amaçlıdır ciddiye almayın):',
    description = ("```" + str(dolaryak.read()) + "```" + "a script by lazy-pwny: https://github.com/lastpingu"),
    colour = discord.Colour.green()
    )
    embed.set_thumbnail(url='https://static8.depositphotos.com/1008522/993/v/450/depositphotos_9938782-stock-illustration-rich-business-man-with-money.jpg')
    embed.set_image(url='https://thumbs.gfycat.com/MiserableHiddenAfricanmolesnake-max-1mb.gif')
    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')
    await ctx.send(embed=embed)
    cprint('Dolar Yakıldı +', 'green')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'Komutlar Hakkında genel bilgi almak için $help, daha detaylı bilgi almak için $yardım yazın',
        value = 'default prefix: $',
        colour = discord.Colour.purple()
    )
    embed.add_field(name='$test', value='test komutudur çet`e basit bir mesaj gönderir', inline=True)
    #embed.add_field(name='$spam', value='araklıklı spam atar(test hariç kullanma)', inline=True)
    #embed.add_field(name='$spam5', value='5 adet spam gönderir ve durur', inline=True)
    embed.add_field(name='$dm', value='"$dm @kullanıcı mesaj" şeklinde bahsi geçen kullanıcıya dm atar', inline=True)
    #embed.add_field(name='$sil', value='mesajları siler', inline=True)
    embed.add_field(name='$covid19', value='Güncel Covid19 tablosu', inline=True)
    embed.add_field(name='$sondakika', value='Son Dakika Haberleri', inline=True)
    embed.add_field(name='$doviz', value='Güncel Döviz Durumu(Dolar, Euro, CHF, CAD)', inline=True)
    embed.add_field(name='$espri', value='Buz Gibi Bir Espri :)', inline=True)
    embed.add_field(name='$atasözü', value='Güzel Bir Linux Atasözü Yazdırır', inline=True)
    embed.add_field(name='$cowsay', value='argüman olarak yazdığınız kelime veya cümleyi bir inek tekrar eder', inline=True)
    embed.add_field(name='$Eryaman!', value='Yaşasın Eryaman', inline=True)

    embed.set_author(name=(ctx.author), icon_url='https://www.oli.org.in/wp-content/uploads/2019/11/author-icon-8.png')

    await ctx.send(embed=embed)
    cprint('Help menusu komutu girildi gerekli içeriki ilgili kanala gönderildi [*]', 'blue')

@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CheckFailure):
        await ctx.send(str(ctx.author) + ' Ne dediğini anlayamadım ab, komutlarımı görmek için **$help** yada **$yardım** komutunu yazmayı deneyebilirsin (^-^)')
        print(str(ctx.author) + ">" + str(ctx.channel)+'-> ¿bilinmeyen komut?')

bot.run(token)

#https://discord.com/api/oauth2/authorize?client_id=741153957099077652&permissions=8&scope=bot
