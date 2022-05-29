from keep_alive import keep_alive
import BotFuncs
import discord
import os
import datetime
import math

#----------------------------# Discord Bot main function. 
client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you..."))
	print('{0.user}, ready to conquer the world.'.format(client))

#-----------------------------#  Administrator Bot commands.
@client.event
async def on_message(message):
	if message.content.startswith('!echo') == True:
		if message.author.guild_permissions.administrator == True:
			text = message.content.replace('!echo','')
			await message.channel.send(text)
			await message.delete()
		else:
			await message.channel.send('You are not my master.', reference=message)

	if message.content == ('!dailychallenge'):
		if message.author.guild_permissions.administrator == True:
			await message.channel.send(BotFuncs.DailyChallenge())
			BotFuncs.increaseDay()
		else:
			await message.channel.send('You are not my master.', reference=message)
	
	if message.content.startswith('!rules') == True:
		if message.author.guild_permissions.administrator == True:
			text = message.content
			text = text.replace('!rules', '').split("\n")
			embed = discord.Embed(title=text[1], description="", timestamp=datetime.datetime.utcnow())
			for index, content in enumerate(text):
				if int(index) >= 2:
					embed.add_field(name='Rule #'+str(index-1) , value=content)
			await message.channel.send(embed=embed), await message.delete()
		else:
			await message.channel.send('You are not my master.', reference=message)						

#-----------------------------#  User Commands	
	if message.content == ('!hello'):
		await message.channel.send('Dont talk to me, Im being developed.', reference=message)

	if message.content == ('!catfact'):
		await message.channel.send(BotFuncs.catfact(),reference=message)
		
	if message.content == ('!dogfact'):
		await message.channel.send(BotFuncs.dogfact(),reference=message)
		
	if message.content == ('!quote'):
		await message.channel.send(BotFuncs.quote(),reference=message)
		   
	if message.content == ('!joke'):
		await message.channel.send(BotFuncs.joke(),reference=message)

	if message.content.startswith('!google') == True:
		MsgString = str(message.content)
		msg = 'Here, allow me to gooogle that one for you:\nhttps://letmegooglethat.com/?q=' + str(MsgString[8:].strip().replace(" ","+"))
		await message.channel.send(msg, reference=message)
		
	if message.content.startswith('!8ball') == True:
		await message.channel.send('🎱 - ' + BotFuncs.magik(),reference=message)
		
	if message.content == ('!fakeperson'):
		await message.channel.send(BotFuncs.fakePerson(),reference=message)

	if message.content == ('!pugfact'):
		await message.channel.send(BotFuncs.pugFact(), reference=message)
		
	if message.content == ('!taunt'):
		await message.channel.send(BotFuncs.taunt(), reference=message)
		
	if message.content.startswith('!rolldice') == True:
		await message.channel.send('**'+str(message.author.name)+'**' + ' rolled a ' +'**'+BotFuncs.dice()+'**', reference=message)


	# THIS IS TOO DANGEROUS. INTRODUCES VULNERABILITIES IN BOT
	# if message.content.startswith('!math') == True:
	# 	text = message.content
	# 	text = text.replace("!math ", "")
	# 	try:
	# 		await message.channel.send(eval(text), reference=message)
	# 	except:
	# 		await message.channel.send('Sorry, thats not math I know. You must be WAY smarter than me...', reference=message)
			
	if message.content.startswith('!embed') == True:
		text = message.content
		text = text.replace('!embed', '').split("\n")
		embed = discord.Embed(title=text[1], description="", timestamp=datetime.datetime.utcnow())

		if len(text) <= 3:
				embed.add_field(name='Content', value=text[2])
				await message.channel.send(embed=embed), await message.delete()
				
		if len(text) > 3:
				for i in range(2, len(text)):
						if len(text[i]) < 1:
								continue
						else:
								embed.add_field(name=f" ----- ", value=text[i], inline=False)
				embed.set_footer(text=message.author)
				await message.channel.send(embed=embed), await message.delete()

	if message.content.startswith("!zeus") == True:
		link = message.content.split(" ")
		returned = BotFuncs.check_site(url=link[1])
		if returned[1] == "**ONLINE**":
				COLOR = discord.Color.green()
		else:
				COLOR = discord.Color.red()

		embed = discord.Embed(title=f"ZeusTheInvestigator", description="", timestamp=datetime.datetime.utcnow(), color=COLOR)
		embed.add_field(name=f"Checked Link: *{returned[0]}*", value=f"STATUS: {returned[1]}")
		embed.set_footer(text=f"Credit goes to @777advait#6334")
		await message.channel.send(embed=embed)

	if "https://discord.com/channels" in message.content:
		text = message.content
		l = text.replace(", ", " ").split(" ")
		key = "https://discord.com/channels/"
		for item in l:
				if key in item:
						try:
								lilink = l[l.index(item)]
								response = "-**---** Link Preview **---**- \n\n"
								link = lilink.replace("https://discord.com/channels/", "").split("/")
								sourceServer = client.get_guild(int(link[0]))
								sourceChannel = sourceServer.get_channel(int(link[1]))
								sourceMessage = await sourceChannel.fetch_message(int(link[2]))
	
								if len(sourceMessage.content) <= 1000:
										embed = discord.Embed(title=response, description="", timestamp=datetime.datetime.utcnow())
										embed.add_field(name=f"Length: {len(sourceMessage.content)}", value=sourceMessage.content)
										embed.set_footer(text=sourceMessage.author, icon_url=sourceMessage.author.avatar_url)
										await message.channel.send(embed=embed)
	
								if len(sourceMessage.content) > 1000:
										contents = sourceMessage.content
										con2 = []
										splitstr = math.ceil(len(contents) / 1000)
										embed1 = discord.Embed(title=response, description="", timestamp=datetime.datetime.utcnow())
										while contents:
												con2.append(contents[:900])
												contents = contents[900:]
										for feilds in range(0, splitstr):
												embed1.add_field(name="----------------------", value=f"```py\n{con2[feilds]}\n```",
																				 inline=False)
										embed1.set_footer(text=sourceMessage.author, icon_url=sourceMessage.author.avatar_url)
										await message.channel.send(embed=embed1)
						except:
								await message.channel.send(f"-**Cannot** **preview**-\n-"
															f"**Make sure message is in this server,"
															f" and not a text file or image**-")


if __name__ == "__main__":
	keep_alive()
	try:
		client.run(os.environ['TOKEN'])
	except:
	    os.system("kill 1")


