import discord
from time import sleep
from sms import SendSms

TOKEN = ""

adet = 20
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name="Sms Botu ~ omicr0n")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == ".sms":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="SMS Bomber (+90)", description=(f"{adet} adet SMS Gönderiliyor -->\n{message.author.mention}"), color=0x001eff)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(" --> "+str(sms.adet)+f" adet SMS gönderildi.\n{message.author.mention}")                        
        else:
            await message.channel.send(f"Geçerli komut yazınız! yardım için .help yazabilirsiniz.{message.author.mention}")
    elif ".help" == message.content:
        await message.channel.send(f"Sms göndermek için komutu aşağıdaki gibi yazınız.\n```.sms 5051234567```\n.sms (telefon numarası)\n{message.author.mention}")
    else:
        pass
  
client.run("MTEwODQzNTYwNjkxNDIwMzc3MA.GN03V6.ak4tQ1pco7HanhGvmlPVGt6VGmPbfhKPZ1_6LQ")
