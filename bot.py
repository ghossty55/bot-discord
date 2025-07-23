#discord meme bot
import os # se importa el modulo os para que pueda manejar las variables del sistema digase el token en este caso pero puede interactuar con archivos del sistema en genral digase carpetas textos etc
import discord # permite interactuar con la api de discord
from dotenv import load_dotenv # se importa dotenv para que pueda manejar la variable .env en conjunto con el modulo os y load_dotenv para cargarla como indica su nombre

import requests # se utiliza para descargar archivos de internet, enviar datos a un servidor o interactuar con una api
import json # se utiliza para convertir los archivos tipo diccionario a json y viceversa la mayoria de archivos en internet estan en json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


#carga las variables de entorno desde .env
load_dotenv()
TOKEN= os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))



#configuracion de los permisos del bot (intents)
intents = discord.Intents.default()
intents.message_content = True #habilita que el bot pueda leer mensajes

#definir la clase del bot
class MyClient(discord.Client):
  async def on_ready(self):#se ejecuta cuando el bot se conecta 
    print('Logged on as {0}!'.format(self.user))
    channel= self.get_channel(941081153127989340)  
    await channel.send("Estoy en linea!")
    
  async def on_message(self, message):#se ejecuta cuando alguien envia un mensaje
    if message.author == self.user:
      return  #evita que el bot se responda a si mismo
   
    if message.content.startswith("$hello"):
      await message.channel.send("Hello World!")#responde con hello world 

    if message.content.startswith("$bye"):
      await message.channel.send("Good Bye!")

    
    if message.content.startswith("$meme"):
      await message.channel.send(get_meme())# devuelve la funcion get meme la cual esta detallada mas arriba de donde recoge un meme aleatorio de la api que indicamos

    if  message.content.startswith("$exit"):
      if message.author.id== OWNER_ID:
        await message.channel.send("👋 Good bye")
        await self.close()
        
      else:
        await message.channel.send("❌ You don't have permission to shut down the bot.")


# crea la instancia del bot con los permisos correctos 
client = MyClient(intents=intents)
client.run(TOKEN) #corre el discord token o digase el archivo .env que tenemos en la misma carpeta del proyecto 