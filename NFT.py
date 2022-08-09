import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def nft(ctx,   keko):
    await ctx.message.delete()
    await ctx.send("Generando NFT...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   
    
    habbo = response.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=2&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 1
    
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    ###

    textogafas = ["gafascorazon","gafasestrellas"]
    gafas = Image.open(r"imagenes/" +random.choice(textogafas)+ ".png").convert("RGBA") #imagen de la trozo
    img1 = gafas.resize((64,110), Image.Resampling.LANCZOS)#tamaño de la pompa

    tirantes = Image.open(r"imagenes/tirantes.png").convert("RGBA") #imagen de la trozo
    img1 = tirantes.resize((64,110), Image.Resampling.LANCZOS)#tamaño de la pompa

    
    

 

 
    img1.paste(img2,(0,0), mask = img2) #Posicion del keko 1
    
    
    img1.paste(tirantes,(0,0), mask = tirantes) #Posicion de la tirantes
    ### 

    
    img1.paste(gafas,(0,0), mask = gafas) #Posicion de la gafas
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   