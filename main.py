import discord

#create the client object, set cache_auth 
client = discord.Client(cache_auth=False)


#on_message event, triggers anytime a message is received on a channel the client can see
#msg - the object representing the message received
@client.event
async def on_message(msg):
	print("Message received")
	
@client.event
async def on_ready():
	print("Client is running as {}".format(client.user.name))
	
print("Starting bot...")
client.run("derpscordbot@gmail.com", "pokemon2010")