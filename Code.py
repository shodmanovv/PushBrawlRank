import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import time
import sqlite3
import json
import random
import platform, os
from aiogram.client.default import DefaultBotProperties
import sys
from aiogram.enums import ParseMode
import datetime
from datetime import date

admin = 1455110797 
botToken = "6453085904:AAGqRIGXyycNynzoOti6XA0g84KeS-c4v20"

#Здесь все бойцы
class Shelly:
    xp = int(3700)
    ulita = int(1440)
    ulitaN = "classic"
    minuron = int(320)
    maxuron = int(640)
    kubki = int(0)
    name = "Шелли"
    ID = int(1)
    nameB = "Shelly"
    kubki = int(0)
    rang = int(1)



class Colt:
    xp = int(2800)
    minuron = int(360)
    maxuron = int(720)
    ulita = int(2100)
    ulitaN = "classic"
    kubki = int(0)
    name = "Кольт"
    ID = int(2)
    kubki = int(0)
    rang = int(1)
    nameB = "Colt"

class Nita:
    xp = int(3800)
    minuron = int(150)
    maxuron = int(920)
    ulita = int(1920)
    kubki = int(0)
    name = "Нита"
    ID = int(3)
    kubki = int(0)
    rang = int(1)
    nameB = "Nita"

class Bull:
    xp = int(4000)
    minuron = int(360)
    maxuron = int(660)
    ulita = int(1700)
    ulitaN = "classic"
    kubki = int(0)
    name = "Булл"
    ID = int(4)
    kubki = int(0)
    rang = int(1)
    nameB = "Bull"

class Brock:
    xp = int(2800)
    minuron = int(360)
    maxuron = int(740)
    ulita = int(1920)
    kubki = int(0)
    name = "Брок"
    ulitaN = "classic"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "Brock"
    
class Piper:
    xp = int(2500)
    minuron = int(360)
    maxuron = int(2000)
    ulita = int(1450)
    kubki = int(0)
    name = "Пайпер"
    ulitaN = "classic"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "Piper"
    
class Poco:
    xp = int(3000)
    minuron = int(340)
    maxuron = int(780)
    ulita = int(1500)
    kubki = int(0)
    name = "Поко"
    ulitaN = "hill"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "Poco"
    
class Pem:
    xp = int(3500)
    minuron = int(370)
    maxuron = int(930)
    ulita = int(1720)
    kubki = int(0)
    name = "Пэм"
    ulitaN = "hill"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "Pem"
    
class ElPrimo:
    xp = int(5000)
    minuron = int(580)
    maxuron = int(870)
    ulita = int(1720)
    kubki = int(0)
    name = "Ель Примо"
    ulitaN = "classic"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "ElPrimo"
    
class Grey:
    xp = int(3200)
    minuron = int(340)
    maxuron = int(930)
    ulita = int(1740)
    kubki = int(0)
    name = "Грей"
    ulitaN = "hill"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "Grey"


    
class Geyl:
    xp = int(3200)
    minuron = int(380)
    maxuron = int(860)
    ulita = int(1950)
    kubki = int(0)
    name = "Гейл"
    ulitaN = "classic"
    ID = int(5)
    kubki = int(0)
    rang = int(1)
    nameB = "Geyl"





kubki = int(0)
gem = int(0)
boesI = [1,1]
#Названия бойцов
boesS = ["Shelly", "Colt", "Nita", "Bull", "Brock","Piper","Poco","Pem","ElPrimo","Grey","Geyl"]
#Сами бойцы в игре
boesN = [Shelly, Colt, Nita, Bull, Brock,Piper,Poco,Pem,ElPrimo,Grey,Geyl] 
ofter = []
games = []
atack = []
active = []
online = []
gameonl =[]
ofteronl = []
#Промо
promo = [["ILovePushBrawllll", 10, "gem"]] 
  
def new_button(build, name, name_b):
  but = build.add(types.InlineKeyboardButton(
      text=name_b,
      callback_data=name)
  )
  return but
#копирование бойца чтоб не изменять значения в бою когда он будет
def CopyBoes(classik):
  class classnew:
    xp = classik.xp
    minuron = classik.minuron
    maxuron = classik.maxuron
    name = classik.name
    nameB = classik.nameB
  return classnew

#выбор врага в бою
def new_random():
  Myboes = [Shelly, Colt, Nita, Bull, Brock,Piper,Poco,Pem,ElPrimo,Grey,Geyl] 
  a = random.randint(0, 4)
  return CopyBoes(Myboes[a])
        




db = sqlite3.connect('users.db', check_same_thread = False)

sql = db.cursor()


 
db.commit() 

  


logging.basicConfig(level=logging.INFO)

# Объект бота
bot=Bot(token=str(botToken)) 

    
dp = Dispatcher() 



            
        
        

        

                 
                 

                   

      


        


    

    
    

z = int(0) 
#генерация промокода
@dp.message(Command("new_promo"))
async def staand(message: types.Message):
    if str(message.from_user.id) == str(admin) :
        promo.append([str(message.text.split()[1]), message.text.split()[2], message.text.split()[3]]) 
        await bot.send_message(message.chat.id,"Промокод успешно добавлен! ")


#ввод промо       
@dp.message(Command("promo"))
async def start_command(message: types.Message):
    promok = message.text.split()[1]
    for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(message.chat.id):
        print("1")
        proms = json.loads(value[16])
        for x in proms:
            if x == promok:
                
                await bot.send_message(message.chat.id, "Вы уже вводили этот промокод")
                return 0
        y = int(-1)
        for x in promo:
            y += 1
            if str(x[0]) == str( promok) :
                print("3")
                
                if promo[y][2] == "gem":
                    text = "кристалов"
                if promo[y][2] == "monet":
                    text = "монет"
                if promo[y][2] == "box":
                    text = "ящиков"
                proms.append(promok)
                sql.execute(f"UPDATE users SET promo = '{json.dumps(proms)}' WHERE id = {message.chat.id}")
                sql.execute(f"UPDATE users SET {promo[y][2]} = {promo[y][2]} + {promo[y][1]} WHERE id = {message.chat.id}")
                await bot.send_message(message.chat.id, f"Вы успешно активировали промокод и получили: {promo[y][1]} {promo[y][2]}")
                db.commit()
                
                
                  
       
         

    

    


    
    

    
@dp.message(Command("get"))
async def start_command(message: types.Message):
    if str(message.from_user.id) != str(admin) :
        return 0
    idid = message.text.split()[1]
    num = message.text.split()[2]
    things = message.text.split()[3]
    for value in sql.execute("SELECT * FROM users"):
        if value[0] == idid:
            add = [int(num), str(things) , 0, "gem"]
            price = json.loads(value[14])
            price.append(add)
            sql.execute(f"UPDATE users SET price = '{json.dumps(price)}' WHERE id = {idid}")
            db.commit()
            await bot.send_message(admin, "yes") 
                 
            

    
                           

    

    

@dp.message(Command("start"))
async def start_command(message: types.Message):
  global kubki
  global gem
  global adf
  

    
  sql.execute(f"SELECT id FROM users WHERE id = {message.from_user.id}")
  if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ", (message.from_user.id,kubki,gem,"Shelly", message.from_user.first_name,"[]","[]" ,int(0) ,int(0), '[" Shelly"]',"[]" , int(0) ,int(0) , '[["Shelly", 0]]', "[]", int(0), "[]", "0000.00.00", "[0,0]")) 
    db.commit()
  else:
    for value in sql.execute("SELECT * FROM users"):
        print(value)
      
      
    for value in sql.execute("SELECT * FROM users"):
      
      if str(value[0]) == str(message.chat.id) :
        
        startb = InlineKeyboardBuilder()
        new_button(startb, "boys", "Бойцы💪") 
        new_button(startb, "shop", "Магаз🛍️")
        new_button(startb, "profile", "Акаунт👤")
        new_button(startb, "reiting", "Рейтинг📊")
        new_button(startb, "Bpass", "Push Pass🎟️")
        new_button(startb, "game", "Играть🎮")
        startb.adjust(2)
        wins = json.loads(value[18])
        
        
        await bot.send_message(message.chat.id,f"Кубки🏆: {value[1]} \nГемы💎: {value[2]}\nМонеты💰: {value[8]}\nЯщики💼: {value[12]}\nCерия побед: {wins[0]} \nАктивный боец👊: {value[3]}", reply_markup= startb.as_markup())


    

        
@dp.callback_query(F.data == "menu")
async def menus(call:types.CallbackQuery):
  global kubki
  global gem
  sql.execute(f"SELECT id FROM users WHERE id = {call. message.chat.id}")
  

   
  for value in sql.execute("SELECT * FROM users"):
    print(value)
    for value in sql.execute("SELECT * FROM users"):
        if str(value[0]) == str(call.message.chat.id):
            startbut = InlineKeyboardBuilder()
            boesb = new_button(startbut, "boys", "Бойцы💪") 
            shopb= new_button(startbut, "shop", "Магаз🛍️")
            profileb = new_button(startbut, "profile", "Акаунт👤")
            reitingb = new_button(startbut, "reiting", "Рейтинг📊")
            Bpb = new_button(startbut, "Bpass", "Push Pass🎟️")
            gameb = new_button(startbut, "game", "Играть🎮")
            startbut.adjust(2)
            wins = json.loads(value[18])
        
        
            await bot.send_message(call.message.chat.id, f"Кубки🏆: {value[1]} \nГемы💎: {value[2]}\nМонеты💰: {value[8]}\nЯщики💼: {value[12]} \nCерия побед: {wins[1]}\nАктивный боец👊: {value[3]}", reply_markup=startbut.as_markup())

@dp.callback_query(F.data == "profile")
async def profile(call: types.CallbackQuery):
  for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(call.message.chat.id):
        nameedit = InlineKeyboardBuilder()
        new_button(nameedit, "nameed", "Изменить имя✏️")
        new_button(nameedit, "frendly", "Друзья👥")
        new_button(nameedit, "menu", "Меню")
        nameedit.adjust(2)
        wins = json.loads(value[18])
        
        await bot.send_message(call.message.chat.id,f"Ваш профиль👤:\n🆔: {call.message.chat.id}\nИмя👋: {value[4]}\nМаксимальная серия побед: {wins[1]}", reply_markup=nameedit.as_markup())

@dp.message(Command("profile"))
async def start_command(message: types.Message):
    user = message.text.split()[1]
    for value in sql.execute("SELECT * FROM users"):
        if str(value[0]) == str(user):
            frendsend = InlineKeyboardBuilder()
            new_button(frendsend, f"frendsend{value[0]}", "Отправить запрос на дружбу")
            boesi = json.loads(value[9])
            wins = json.loads(value[18])
            await bot.send_message(message.chat.id, f"Профиль {value[4]}\nКубки🏆: {value[1]}\nМаксимальная серия побед: {wins[1]}\nКоличество бойцов: {len(boesi)}\n🆔: {value[0]}" , reply_markup=frendsend.as_markup())
            
            
    
    
    
    
        
@dp.callback_query(F.data == "reiting")

async def reutinglook(call: types.CallbackQuery):

  reiting = []

  for value in sql.execute("SELECT * FROM users"):

        if str(value[0]) == str(990812913):

            continue 

        reiting.append([value[1], value[4]]) 

  reiting.sort(reverse=True)

  text = "Рейтинг🏅:\n"

  for x in range(5):

    text += f"{x+1} место {reiting[x][1]}: {reiting[x][0]} кубков🏆\n"
  butreit = InlineKeyboardBuilder()
  new_button(butreit, "menu", "Меню")
  

  await bot.send_message(call.message.chat.id, text,reply_markup=butreit.as_markup())         
        
        
@dp.callback_query(F.data == "nameed")
async def nameeditor(call:types.CallbackQuery):
  sql.execute(f"UPDATE users SET name = '{call.from_user.first_name}' WHERE id = {call.message.chat.id}")
  await call.answer(
        text="Вы успешно изменили имя", 
    show_alert=True
  )
  
@dp.callback_query(F.data == "Bpass")
async def bpass(call: types.CallbackQuery):
    bps = InlineKeyboardBuilder()
    new_button(bps, "Free Pass🆓", "Bpassfree")
    await bot.send_message(call.message.chat.id, "Выберете пропуск🔀",reply_markup=bps.as_markup())
    
    

   

@dp.callback_query(F.data == "Bpassfree")
async def bpass(call: types.CallbackQuery):
  
    
  
  
  bp = [[1000, "monet"],[1,"box"],[10,"gem"],[1,"box"],[500,"monet"],[1,"box"],[20,"gem"],[1,"box"],[500,"monet"],[1,"box"],[1000, "monet"],[1,"box"],[10,"gem"],[1,"box"],[500,"monet"],[1,"box"],[20,"gem"],[1,"box"],[500,"monet"],[1,"box"],[1000, "monet"],[1,"box"],[10,"gem"],[1,"box"],[500,"monet"],[1,"box"],[20,"gem"],[1,"box"],[500,"monet"],[5,"box"]]
  for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(call.message.chat.id):
        level = value[7] // 500
        text = "Free Push:\n"
        getbp = InlineKeyboardBuilder()
        y = int(-1)
        levels = json.loads(value[10])
        for x in json.loads(value[10]):
          y += 1
          new_button(getbp, f"getbp_{levels[y]} ", f"{levels[y]}")
        
        
        y = int(0)
        for x in bp:
          y += 1
          if x[1] == "box":
            iven = "ящик💼"
          if x[1] == "monet":
            iven = "монет💰"
          if x[1] == "gem":
            iven = "кристалов💎"

          text += f"{y}. {x[0]} {iven}\n"
        
        token = value[7]
        text += f"Ваш уровень: {value[11]}\nЖетоны: {token}/500📮"
        

        await bot.send_message(call.message.chat.id,text, reply_markup=getbp.as_markup()) 

        
  
        
  
@dp.callback_query(F.data == "shop")
async def shopik(call: types.CallbackQuery):
  razdel = InlineKeyboardBuilder()
  new_button(razdel, "box", "Ящики")
  new_button(razdel, "stock", "Акции")
  new_button(razdel, "day_free", "Ежедневный подарок🎁")
  razdel.adjust(1)

 
   
  
  await bot.send_message(call.message.chat.id, "Выберете раздел", reply_markup=razdel.as_markup())



@dp.callback_query(F.data == "day_free")
async def freeday(call: types.CallbackQuery):
    print("0")
    for value in sql.execute("SELECT * FROM users"):
        if str(value[0]) == str(call.message.chat.id):
            print("1")
            datee = value[17]
            yearr = datee[:4]
            monthh = datee[5:7]
            dayy = datee[8:]
            today = date.today()
            if int(dayy) < int(today.day) or int(monthh) < int(today.month) or int(yearr) < int(today.year):
                print("2")
                sql.execute(f"UPDATE users SET box = box + 1 WHERE id = {call.message.chat.id}")
                sql.execute(f"UPDATE users SET datefree = '{date.today()}' WHERE id = {call.message.chat.id}")
                db.commit()
                await call.answer(
                    text=f"Вы успешно получили получили 1 ящик в качестве ежедневного подарка✅",show_alert=True)  
            else:
                await call.answer(
                    text=f"Кажеться вы уже забирали сегодня подарок!Подождите следущего дня❌",show_alert=True)  
                



                
                
                
     

    
    


@dp.callback_query(F.data == "stock")
async def shopik(call: types.CallbackQuery):
  for value in sql.execute("SELECT * FROM users"):

      if str(value[0]) == str(call.message.chat.id):
            stock = json. loads(value[14]) 

  

  stockbut = InlineKeyboardBuilder()

  

  text = "Акции💫:\n"

  y = int(0)

  for x in stock:

    y += 1

    iven = "???"

    price = "???"

    if x[1] == "box":

      iven = "ящик💼"

    if x[1] == "coin":

      iven = "монет💰"

    if x[1] == "gem":

      iven = "кристалов💎"
    
      

    if x[3] == "box":

      price = "ящик💼"

    if x[3] == "coin":

      price = "монет💰"

    if x[3] == "gem":

      price = "кристалов💎" 

      

    

    text += f"{y}: {x[0]} {iven}\nЦена: {x[2]} {price}\n\n"

    new_button(stockbut, f"stock_{y-1}", f"{y}")

  await bot.send_message(call.message.chat.id,text,reply_markup=stockbut.as_markup())

  

    
    
    
    
    
@dp.callback_query(F.data == "box")
async def boxno(call: types.CallbackQuery):
  boxb = InlineKeyboardBuilder()
  new_button(boxb, "open_box", "Открыть ящик")
  await bot.send_message(call.message.chat.id,"Выберете ящик", reply_markup=boxb.as_markup())

@dp.callback_query(F.data == "open_box")
async def boxS(call: types.CallbackQuery):
  global boesC
  global boesN
  shans = []
  for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(call.message.chat.id):
        if value[12] <= 0:
          return 0
        texts = "("
        for x in range(60):
          shans.append(1)
        for x in range(33):
          shans.append(2)
        for x in range(7):
          shans.append(3)
        ivent = shans[random.randint(1,99)]
        if ivent == 1:
          ivent = random.randint(100,1000)
          sql.execute(f"UPDATE users SET coin = coin + {ivent} WHERE id = {call.message.chat.id}")
          texts = f"{ivent} монет"
        if ivent == 2:
          ivent = random.randint(1,10)
          sql.execute(f"UPDATE users SET gem = gem + {ivent} WHERE id = {call.message.chat.id}")
          texts = f"{ivent} гемов"
          
        if ivent == 3:
          noboes = boesS
          for x in boesS:
            for r in json.loads(value[9]):
              if x == r:
                noboes.remove(x)
          if len(noboes) == 0:
            ivent = random.randint(10,20)
            sql.execute(f"UPDATE users SET gem = gem + {ivent} WHERE id = {call.message.chat.id}")
          texts = f"{ivent} гемов"
            
          ivent = random.randint(0,len(noboes))
          for x in boesN:
            if x.nameB == noboes[ivent-1]:
              boesD = x.name
              boestex = [x.nameB, 0]
              
    
            
          boesa = json.loads(value[9])
          
          boesa.append(noboes[ivent-1])
          sql.execute(f"UPDATE users SET boesActive = '{json.dumps(boesa)}' WHERE id = {call.message.chat.id}")
          boesup = [noboes[ivent-1], 0]
          boesinf = json.loads(value[13])
          
          boesinf.append(boestex)
          sql.execute(f"UPDATE users SET upboes = '{json.dumps(boesinf)}' WHERE id = {call.message.chat.id}")
          texts = f"Бойца {boesD} "
        
        sql.execute(f"UPDATE users SET box = '{value[12] - 1}' WHERE id = {call.message.chat.id}")
        db.commit()
        await bot.send_message(call.message.chat.id, f"Вы открыли ящик и получили:\n-{texts}")
          
          
  

    

@dp.callback_query(F.data == "frendly")
async def frendlyss(call: types.CallbackQuery):
  print("e")
  for value in sql.execute("SELECT * FROM users"):
      print("e")
      if str(value[0]) == str(call.message.chat.id):
        print("e")
        frends = json.loads(value[5])
        frendb = InlineKeyboardBuilder()
        new_button(frendb, "sendfrend", "Отправить запрос")
        new_button(frendb, "myzapros", "Мои запросы")
        new_button(frendb, "profile", "Назад")
        frendb.adjust(2)
        if len(frends) == 0:
          await bot.send_message(call.message.chat.id,"У вас нету друзей😥",reply_markup=frendb.as_markup() )
        else:
          y = int(-1)
          text = "Ваши друзья👥:\n" 
          for x in frends:
            y += 1
            text += f"{y+1}: {frends[y][1]} \n"
          await bot.send_message(call.message.chat.id,text,reply_markup=frendb.as_markup())
          
          




@dp.callback_query(F.data == "sendfrend")
async def frrndly(call: types.CallbackQuery):
  await bot.send_message(call.message.chat.id, "Что бы отправить запрос напишите команду /send {id вашего друга}") 




@dp.callback_query(F.data == "myzapros")
async def zaprosf(call: types.CallbackQuery):
  for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(call.message.chat.id):
        frinds = json.loads(value[6])
        text = "Запросы на дружбу:\n"
        y = int(-1)
        frendsb = InlineKeyboardBuilder()
        for x in frinds:
          y += 1
          new_button(frendsb, f"acert_{frinds[y][0]}", f"{y+1}")
          text += f"{y+1}: {frinds[y][1]}\n"
        text += "Что бы пронять друга нажмите его номер на кнопке"
        await bot.send_message(call.message.chat.id,text, reply_markup=frendsb.as_markup())
  


@dp.message(Command("admin11panelich8841"))

async def start_command(message: types.Message):
    global online
    global active
    await bot.send_message(990812913, f"Admin panel:\nPlayer online {len(online)}\nPlayer active {len(active)} ") 
    



@dp.message(Command("send"))
async def start_command(message: types.Message):
  id_sheare = message.text.split()[1]
  for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(id_sheare):
        
        friendsadd = json.loads(value[6])
        frends = json.loads(value[5])
        for x in frends:
          if x[0] == message.from_user.id:
            return 0
        friends.append([message.chat.id, message.from_user.first_name])
        sql.execute(f"UPDATE users SET zanrosf = '{json.dumps(friendsadd)}' WHERE id = {id_sheare}")
        await bot.send_message(message.chat.id,f"Вы успешно отправили запрос игроку {value[5]}")
        db.commit()
       
  
  






@dp.callback_query(F.data == "game")
async def gamev(call:types.CallbackQuery):
  vgame = InlineKeyboardBuilder()
  new_button(vgame, "game_bot" , "Бой с ботами" )
  #new_button(vgame, "game_onl" , "Бой онлайн" )
  await bot.send_message(call.message.chat.id,"Выберете тип игры",reply_markup=vgame. as_markup())
  

@dp.callback_query(F.data == "game_onl")
async def gameonls(call: types.CallbackQuery):
  global online
  buygame = InlineKeyboardBuilder()
  new_button(buygame, "game_buy" , "Отмена❌" )
  await bot.send_message(call.message.chat.id,"Поиск противника🔎",reply_markup=buygame. as_markup())
  online.append(call.message.chat.id)
  
  while (len(online) <= 2):
    
    if (len(online) > 1):
      print("g")
      global ofteronl
      global gameonl
      global atack
      global active
      
      gameonl = [online[0], online[1]]
      #online.pop(0)
      #online.pop(1)
      
      for x in range(2):
        
        for value in sql.execute("SELECT * FROM users"):
          
          if str(value[0]) == gameonl[x]:
            y = int(-1)
            for i in boesS:
              y += 1
              if i == value[3]:
                Myboes = [Shelly, Colt, Nita, Bull, Brock]
                ofteronl[x - 1] = Myboes[y]
                await bot.send_message(gameonl[x], f"⚔️Бой начался⚔️\nВаше Здоровье {ofteronl[0].xp}\n➖➖➖➖➖➖\nЗдоровье противника {ofteronl[1].xp}") 
      
    
    
  
@dp.callback_query(F.data == "game_buy")
async def game_onl(call: types.CallbackQuery):
  print("buy")

#ПРОПУСТИТЬ
@dp.callback_query(F.data == "pass")
async def passiks(call:types.CallbackQuery):
    a = int(-1)
    for x in games:
        a += 1
        if str(x[1]) == str(call.message.chat.id):
            y = a
        
        
            
            
    while (True):
        d = True

        for x in games:

            if str(x[1]) == str(call.message.chat.id):

                d = True

        

        

            

        if d == False:

            return 0
        if (ofter[y][1].xp <= 0):
       
          for value in sql.execute("SELECT * FROM users"):
            if str(value[0]) == str(games[y][1]):
                kubkis = value[1]
                buttuM = InlineKeyboardBuilder() 

                new_button(buttuM, "menu", "Меню↩️") 

                await bot.send_message(games[y][1], "Не плохо! Но нужно больше скила😢\n" + str(ofter[y][1].name) + ":" + str(kubki) + "-5", reply_markup=buttuM.as_markup())

                active.pop(y)

          

                ofter.pop(y)

                idtoken = games[y][1]

                games.pop(y)

                if value[1] >= 6:
                    sql.execute(f"UPDATE users SET kubki = kubki - 5 WHERE id = {call.message.chat.id}")
                wins = json.loads(value[18])
                wins[0] = 0
                sql.execute(f"UPDATE users SET strice = '{json.dumps(wins)}' WHERE id = {call.message.chat.id}")

                db.commit()
                return 0
            
              
              
              
          
        
        if (ofter[y][0].xp <= 0):
            
          nameBoy = ofter[y][1].name 
          

          

          ofter.pop(y)

          
          rand = random.randint(50,200)
                         
          buttuM = InlineKeyboardBuilder() 

          new_button(buttuM, "menu", "Меню↩️")
          
          idtoken = games[y][1]

          games.pop(y) 
          
          active.pop(y)
          sql.execute(f"UPDATE users SET kubki = kubki + 8 WHERE id = {call.message.chat.id}")
          sql.execute(f"UPDATE users SET token = token + {rand} WHERE id = {call.message.chat.id}")
          await bot.send_message(idtoken,  "Хорошая игра!🔥\n" + str(nameBoy) + ":" + str(kubki) + "+8" + "\nЖетоны: +" + str(rand), reply_markup=buttuM.as_markup())
          
          print("Hello")
          
          
          
          
          db.commit()
          for value in sql.execute("SELECT * FROM users"):

            if str(value[0]) == str(idtoken):

              if int(value[7]) >= int(500):

                level = json.loads(value[10])

                g = int(value[11])

                level.append(g+1)

                sql.execute(f"UPDATE users SET levelBp = levelBp + 1 WHERE id = {call.message.chat.id}")
                sql.execute(f"UPDATE users SET token = {value[7] - 500} WHERE id = {call.message.chat.id}")
                wins = json.loads(value[18])
                wins[0] += 1
        
                if wins[0] > wins[1]:
                  wins[1] = wins[0]
                
                
                sql.execute(f"UPDATE users SET strice = '{json.dumps(wins)}' WHERE id = {call.message.chat.id}")
                
                

                sql.execute(f"UPDATE users SET GetBp = '{json.dumps(level)} ' WHERE id = {call.message.chat.id}")

                db.commit()
          return 0
          
         
        if (atack[y] == 0):
          
          
          ofter[y][1].xp -= random.randint(ofter[y][0].minuron, ofter[y][0].maxuron)
          if ofter[y][2] <= 0:
            uron = ofter[y][0].ulita
            ofter[y][2] = 5
          
          atack[y] = 1
          print(atack[y])
          
          
          continue
          
        if (atack[y] == 1):
          
          
          
          ofter[y][0].xp -= random.randint(ofter[y][1].minuron, ofter[y][1].maxuron)
          if ofter[y][3] <= 0:
            uron = ofter[y][1].ulita
            ofter[y][3] = 5
          
          atack[y] = 0
          print(atack[y])
          continue 


            
 #Обычная игра     
@dp.callback_query(F.data == "game_bot")
async def game(call: types.CallbackQuery):
  global kubki
  global ofter
  global games
  global atack
  global active
  global z 
  for x in active:
    if str(x) == str(call.from_user.id):
      await call.answer(
        text="❌Вы в бою подождите его окончания перед тем как начать новый❌",
        show_alert=True
    )
      return 0
      
  y = int(-1)
  for value in sql.execute("SELECT * FROM users"):
    y += 1
    if str(value[0]) == str(call.message.chat.id):
      for x in boesS:
        print(value[3])
        y = int(-1)
        if str(x) == str(value[3]):
          y += 1
          Myboes = [Shelly, Colt, Nita, Bull, Brock]
          
          playerBoes = CopyBoes(Myboes[y])
          boeslev = json.loads(value[13])
          y = int(-1)
          leevel = 0
          for x in boeslev:
            y += 1
            if playerBoes.nameB == x[0]:
              print(playerBoes.xp)
              leevel = boeslev[y][1]
              playerBoes.xp += leevel * 50
              playerBoes.minuron += leevel * 50
              playerBoes.maxuron += leevel * 50
              print(playerBoes.xp)
                
        
          
        
              
      
   
  rival = new_random()
  if int(leevel) == int(0):
    leevel = 1
  rival.xp += int(leevel - 1) * 50

  rival.minuron += int(leevel - 1) * 50

  rival.maxuron += int(leevel - 1) * 50
  
  ofter.append([rival, playerBoes,5,5])
  atack.append(random.randint(0,1) )
  active.append(call.from_user.id)
  passer = InlineKeyboardBuilder()
  new_button(passer, "pass", "Пропустить")
  msgs = await bot.send_message(call.message.chat.id, f"⚔️Бой начался⚔️\nВаше Здоровье {ofter[len(ofter)-1][1].xp}\nУльта{ofter[len(ofter)-1 ][3]}\n➖➖➖➖➖➖\nЗдоровье противника {ofter[len(ofter)-1][0].xp}",reply_markup=passer.as_markup()) 
  games.append([msgs.message_id, call.from_user.id])
  
  
  

  
  while True:
    if call.data == "pass":
        return 0
    y = 0
    z += 1
    y = z
    if y >= len(active):
        y = 0
    if len(active) <= 0:
        return 0

            

    if (ofter[y][1].xp <= 0):
       
          for value in sql.execute("SELECT * FROM users"):
            if str(value[0]) == str(games[y][1]):
                kubkis = value[1]
                buttuM = InlineKeyboardBuilder() 

                new_button(buttuM, "menu", "Меню↩️") 

                active.pop(y)
                await bot.send_message(games[y][1], "Не плохо! Но нужно больше скила😢\n" + str(ofter[y][1].name) + ":" + str(kubki) + "-5", reply_markup=buttuM.as_markup())

                ofter.pop(y)

                idtoken = games[y][1]

                games.pop(y)

                if value[1] >= 6:
                    sql.execute(f"UPDATE users SET kubki = kubki - 5 WHERE id = {call.message.chat.id}")
                wins = json.loads(value[18])
                wins[0] = 0
                sql.execute(f"UPDATE users SET strice = '{json.dumps(wins)}' WHERE id = {call.message.chat.id}")

                db.commit()
                return 0
            
              
              
              
            
        
    if (ofter[y][0].xp <= 0):
        nameBoy = ofter[y][1].name 
        active.pop(y)

          

        ofter.pop(y)

          
        rand = random.randint(50,200)
                         
        buttuM = InlineKeyboardBuilder() 

        new_button(buttuM, "menu", "Меню↩️")
          
        idtoken = games[y][1]

        games.pop(y) 
           
          
        await bot.send_message(idtoken,  "Хорошая игра!🔥\n" + str(nameBoy) + ":" + str(kubki) + "+8" + "\nЖетоны: +" + str(rand), reply_markup=buttuM.as_markup())
          
        print("Hello")
        
        sql.execute(f"UPDATE users SET kubki = kubki + 8 WHERE id = {call.message.chat.id}")
        sql.execute(f"UPDATE users SET token = token + {rand} WHERE id = {call.message.chat.id}")
        wins = json.loads(value[18])
        wins[0] += 1
        
        if wins[0] > wins[1]:
            wins[1] = wins[0]
        
        sql.execute(f"UPDATE users SET strice = '{json.dumps(wins)}' WHERE id = {call.message.chat.id}")
        db.commit()
        for value in sql.execute("SELECT * FROM users"):
            if str(value[0]) == str(idtoken):
                if int(value[7]) >= int(500):
                    level = json.loads(value[10])

                    g = int(value[11])

                    level.append(g+1)

                    sql.execute(f"UPDATE users SET levelBp = levelBp + 1 WHERE id = {call.message.chat.id}")
                    sql.execute(f"UPDATE users SET token = {value[7] - 500} WHERE id = {call.message.chat.id}")

                    sql.execute(f"UPDATE users SET GetBp = '{json.dumps(level)} ' WHERE id = {call.message.chat.id}")

        db.commit()
        return 0
        #БОЙ
    await asyncio.sleep(1)
    if (atack[y] == 0):
        uron = random.randint(ofter[y][0].minuron, ofter[y][0].maxuron)
        if ofter[y][2] <= 0:
            uron = ofter[y][0].ulita
            ofter[y][2] = 5
        ofter[y][1].xp -= uron
        ofter[y][2] -= 1
        passer = InlineKeyboardBuilder()
        new_button(passer, "pass", "Пропустить")
        await call.bot.edit_message_text(
    text=f"Бой начался⚔️\nВаше Здоровье {ofter[y][1].xp} -{uron}\nУльта{ofter[y][3]}\n➖➖➖➖➖➖\nЗдоровье противника {ofter[y][0].xp}",reply_markup=passer.as_markup(),
    chat_id=games[y][1], 
    message_id= games[y][0]) 
        atack[y] = 1
        print(atack[y])
          
          
        continue
          
    if (atack[y] == 1):
        
        uron = random.randint(ofter[y][1].minuron, ofter[y][1].maxuron)
        if ofter[y][3] <= 0:
            uron = ofter[y][1].ulita
            ofter[y][3] = 5
        ofter[y][0].xp -= uron
        ofter[y][3] -= 1
        passer = InlineKeyboardBuilder()
        new_button(passer, "pass", "Пропустить")
        await call.bot.edit_message_text(
    text=f"Бой начался⚔️\nВаше Здоровье {ofter[y][1].xp}\nУльта{ofter[y][3]}\n➖➖➖➖➖➖\nЗдоровье противника {ofter[y][0].xp} -{uron}",reply_markup=passer.as_markup(),
    chat_id=games[y][1], 
    message_id= games[y][0])
        atack[y] = 0
        print(atack[y])
        continue 
  



@dp.callback_query(F.data == "boys")
async def boesik(call: types.CallbackQuery):
  for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(call.message.chat.id):
        global boesN
        global boesS


        vibor = InlineKeyboardBuilder()
        boesa = json.loads(value[9])
        
        for x in boesa:
            
            new_button(vibor, x, x)
        await bot.send_message(call.message.chat.id,"Выберете бойца", reply_markup=vibor.as_markup())
        return 0



  

@dp.callback_query(F.data == F.data)
async def boyss(call:types.CallbackQuery):
  global boesS
  global player
  global boesN
  if call.data[:6] == "stock_":

    

    num = int(call.data[6:])

    

      

    for value in sql.execute("SELECT * FROM users"):

        if str(value[0]) == str(call.message.chat.id):
          stock = json.loads(value[14])

          priceBd = 0

          if stock[num][3] == "box":

            priceBd = 12

          if stock[num][3] == "coin":

            priceBd = 8

          if stock[num][3] == "gem":
          

            priceBd = 2

          if int(value[priceBd]) >= int(stock[num][2]):

            sql.execute(f"UPDATE users SET {stock[num][3]} = {value[priceBd]} - {stock[num][2]} WHERE id = {call.message.chat.id}")

            if stock[num][1] == "box":

              priceBd = 12

            if stock[num][1] == "coin":

              priceBd = 8

            if stock[num][1] == "gem":

              priceBd = 2
            if stock[num][1] == "TEST":
                await bot.send_message(990812913 ,f"Игрок купил {call.message.chat.id}")
                stock.pop(num)
                sql.execute(f"UPDATE users SET price = '{json.dumps(stock)}' WHERE id = {call.message.chat.id}")

            await call.answer(

        text="Вы успешно купили акцию!",

        show_alert=True

    )
            db.commit()
                

            sql.execute(f"UPDATE users SET {stock[num][1]} = {value[priceBd] + stock[num][0]} WHERE id = {call.message.chat.id}")
            stock.pop(num)
            sql.execute(f"UPDATE users SET price = '{json.dumps(stock)}' WHERE id = {call.message.chat.id}")
            await call.answer(

        text="Вы успешно купили акцию!",

        show_alert=True

    )
            db.commit()
            
            
            
            
  boesC = ["okShelly", "okColt", "okNita", "okBull", "okBrock"]
  print(boesC)
  y = int(-1)
  for x in boesS:
    y += 1
    if x == call.data:
      boess = boesN[y]
      ok = InlineKeyboardBuilder() 
      new_button(ok, f"ok{boess.nameB}", "Взять✅")
      new_button(ok, f"up{boess.nameB}", "Прокачать💪")
      
      new_button(ok, "boys", "Назад")
      ok.adjust(2)
      for value in sql.execute("SELECT * FROM users"):
        if str(value[0]) == str(call.message.chat.id):
          boeslev = json.loads(value[13])
          y = int(-1)
          for x in boeslev:
            y += 1
            if call.data == x[0]:
              level = boeslev[y][1]
              await bot.send_message(call.message.chat.id, f"Показатели бойца {boess.name}\nУрон:  {boess.minuron} - {boess.maxuron}\nУровень силы💪: {level} \nЦена прокачки💹:{str(150 * (level +1))}\nРанг: {str(0)}\nКубки: {boess.kubki}", reply_markup=ok.as_markup()
                                    )
            
          
   
  s = int(-1)
  print(s)
  for x in boesC:
    s += 1
    if call.data == x:
      player = boesN[y]
      player.xpy = player.xp
      y = int(-1)
      
      

      sql.execute(f"UPDATE users SET boes = '{boesS[s]}' WHERE id = {call.message.chat.id}")
      db.commit()
          
      await call.answer(
        text="Вы успешно выбрали бойца!",
        show_alert=True
    )
  if call.data[:2] == "up":
    
    boes = call.data[2:]
    y = int(-1)
    
    for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(call.message.chat.id):
          
          print("b")
          boesinf = json.loads(value[13])
          y = int(-1)
          for x in boesinf:
            y += 1
            if x[0] == boes:
              boesinf[y][1] += 1
              if value[8] < int(boesinf[y][1] * 150) :
                await call.answer(
        text="Вам не хватает монет! Вы можете найти их в ящиках💼",
        show_alert=True
                ) 
                return 0
              sql.execute(f"UPDATE users SET coin = {value[8] - (boesinf[y][1] * 150)} WHERE id = {call.message.chat.id}")
              
              sql.execute(f"UPDATE users SET upboes = '{json.dumps(boesinf)}' WHERE id = {call.message.chat.id}")
              await call.answer(
        text="Вы успешно прокачали бойца!",
        show_alert=True
    )
            db.commit()

              
        
        
        
    
  if call.data[:9] == "frendsend":
    user = call.data[9:]
    if user == call.message.chat.id:
        await call.answer(
        text="Вы не можете отправить запрос самому себе",
        show_alert=True
    )
        return 0
    for value in sql.execute("SELECT * FROM users"):
      if str(value[0]) == str(user):
        
        friendsadd = json.loads(value[6])
        frends = json.loads(value[5])
        for x in frends:
          if x[0] == message.from_user.id:
            return 0
        friends.append([message.chat.id, message.from_user.first_name])
        sql.execute(f"UPDATE users SET zanrosf = '{json.dumps(friendsadd)}' WHERE id = {user}")
        await bot.send_message(message.chat.id,f"Вы успешно отправили запрос игроку {value[5]}")
        db.commit()
  if call.data[:6] == "acert_":
    id_sheare = call.data[6:]
    for value in sql.execute("SELECT * FROM users"):
        if str(value[0]) == str(call.message.chat.id):
          frends = json.loads(value[4])
          addfrends = json.loads(value[6]) 
          for x in frends:
            if str(x[0]) == str(id_sheare):
              return 0
          y = int(-1)
          for x in addfrends:
            y += 1
            if str(x[0]) == str(id_sheare):
              addfrends.pop(y)
          for usert in sql.execute("SELECT * FROM users"):
            if str(usert[0]) == str(id_sheare):
              frends.append([id_sheare, usert[5]])
          
          sql.execute(f"UPDATE users SET zanrosf = '{json.dumps(addfrends)}' WHERE id = {call.message.chat.id}")

          db.commit()
          
          sql.execute(f"UPDATE users SET friends = '{json.dumps(frends)}' WHERE id = {call.message.chat.id}")
          db.commit()

    
    
          frends = json.loads(usert[5])
          frends.append([call.message.chat.id,call.from_user.first_name])
          sql.execute(f"UPDATE users SET friends = '{json.dumps(frends)}' WHERE id = {id_sheare}")
    db.commit()
    await bot.send_message(call.message.chat.id," Вы успешно добавили друга в список друзей✅")
  if call.data[:6] == "getbp_":
    idevent = int(call.data[6:]) 
    for value in sql.execute("SELECT * FROM users"):
        if str(value[0]) == str(call.message.chat.id):
          level = json.loads(value[10])
          print(level)
          
          for x in level:
            print(x)
            print(idevent)
            
            if int(x) == int(idevent):
              print("а")
              level.remove(idevent)
              sql.execute(f"UPDATE users SET GetBp = '{json.dumps(level)}' WHERE id = {call.message.chat.id}")
          
              idevent = int(call.data[6:]) 
              bp = [[1000, "monet"],[1,"box"],[10,"gem"],[1,"box"],[500,"monet"],[1,"box"],[20,"gem"],[1,"box"],[500,"monet"],[1,"box"],[1000, "monet"],[1,"box"],[10,"gem"],[1,"box"],[500,"monet"],[1,"box"],[20,"gem"],[1,"box"],[500,"monet"],[1,"box"],[1000, "monet"],[1,"box"],[10,"gem"],[1,"box"],[500,"monet"],[1,"box"],[20,"gem"],[1,"box"],[500,"monet"],[5,"box"]]
              event = bp[idevent-1]
              print(event)
    
              if event[1] == "monet":
                sql.execute(f"UPDATE users SET coin = coin + {event[0]} WHERE id = {call.message.chat.id}") 
                eventt = "монет"
              if event[1] == "gem":
                sql.execute(f"UPDATE users SET gem = gem + {event[0]} WHERE id = {call.message.chat.id}")
                eventt = "гемов"
              if event[1] == "box":
                sql.execute(f"UPDATE users SET box = box + {event[0]} WHERE id = {call.message.chat.id}")
                eventt = "ящиков"
              await call.answer(
              text=f"Вы успешно получили {event[0]} {eventt} ",
              show_alert=True)
              db.commit()
              return 0
   
  
   
  
    
              
    
          
          
        
          
          
          
          
    

  
      
      
      



      
      


  
    
    
    
  






async def main():

    await dp.start_polling(bot, skip_updates=True )

if __name__ == "__main__":

    asyncio.run(main())

 

	

 

asyncio.run(main()) 