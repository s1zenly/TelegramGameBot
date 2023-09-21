-import telebot
from telebot.util import pil_image_to_file
import config
import random

from telebot import ExceptionHandler, types
 
bot=telebot.TeleBot(config.token)


#обработчик начала
@bot.message_handler(commands=['start'])
def privet(message):
 #клавиатура
     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
     one=types.KeyboardButton("🎲Числомен")
     two=types.KeyboardButton("🎫Камень,ножницы,бумага")
     three=types.KeyboardButton("🎯Угадайка")

     markup.add(one,two,three)

     sti=open('stic/qw.tgs','rb')
     
     bot.send_animation(message.chat.id,sti)
     bot.send_message(message.chat.id,'---------------------Привет!---------------------\n             \U0001f600я ботик-игрушка\U0001f600 \n            выбирай игру из списка',reply_markup=markup)
     bot.send_message(message.chat.id,'''Eсли хочешь прочесть правила игр
             введи команду /help''')

#Обработичк правил игр
@bot.message_handler(commands=['help'])
def help(message):
      bot.send_message(message.chat.id,'''-------------*Правила*-------------
      1)*Числомен*
              Игра,в который мы обмениваемся одновременно числами и тот,у кого больше число,одерживает победу,счет фиксируется
      2)*Камень,ножницы,бумага*
             Всем знакомая игра,в который мы одновременно присылаем слово и фиксируем счет
      3)*Угадайка*
             Проверь свою интуицию и угадай какое число я загадал,если угадаешь 5+ из 10,то ты одержал победу ''',parse_mode='Markdown')

#Игры
@bot.message_handler(content_types=['text'])
def game(message):
    if message.chat.type=="private":
           if message.text=='🎫Камень,ножницы,бумага': 
                   msg = bot.send_message(message.chat.id, 'Жульничать не буду\U0001f600', reply_markup=types.ReplyKeyboardRemove())
                   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                   y=types.KeyboardButton("📄бумага")
                   g=types.KeyboardButton("🗻камень")
                   e=types.KeyboardButton("✂️ножницы")
                   stop=types.KeyboardButton("⛔️стоп") 
                   markup.add(y,g,e,stop)
               
                   bot.send_message(message.chat.id,'Твой ход!',reply_markup=markup) 

                   bot.register_next_step_handler(msg,KNB)               
           elif message.text=='🎲Числомен':
                   top=bot.send_message(message.chat.id,'играем в диапозоне (0.1000)\U0001f600',reply_markup=types.ReplyKeyboardRemove())

                   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                   st=types.KeyboardButton('⛔️стоп')

                   markup.add(st)

                   bot.send_message(message.chat.id,'Введи число!',reply_markup=markup)

                   bot.register_next_step_handler(top,chislomen)
           elif message.text=='🎯Угадайка':
                   ket=bot.send_message(message.chat.id,'Ну что,готов проверить свою интуцию?😎',reply_markup=types.ReplyKeyboardRemove())

                   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                   ed=types.KeyboardButton('1')
                   dv=types.KeyboardButton('2')
                   tr=types.KeyboardButton('3') 
                   chet=types.KeyboardButton('4') 
                   piat=types.KeyboardButton('5') 
                   shest=types.KeyboardButton('6')
                   sem=types.KeyboardButton('7') 
                   vos=types.KeyboardButton('8') 
                   dev=types.KeyboardButton('9') 
                   des=types.KeyboardButton('10') 
                   xv=types.KeyboardButton('⛔️стоп')

                   markup.add(ed,dv,tr,chet,piat,shest,sem,vos,dev,des,xv)

                   bot.send_message(message.chat.id,'Победа за тобой,если отгадаешь 5+\\10!💰',reply_markup=markup)

                   bot.register_next_step_handler(ket,ugadayka)
           else:
                   bot.send_message(message.chat.id,'Я не запрограммирован так,ты должен выбрать из списка ниже😊')


global k,t
k=t=0
#Обработчик игры 'камень,ножницы,бумага'
def KNB(message):
           if message.chat.type=="private":
                  if message.text=='🗻камень' or message.text=='📄бумага' or message.text=='✂️ножницы':  
                        global k,t 
                        p=['камень','ножницы','бумага']
                        y=random.randint(0,2)
                        bot.send_message(message.chat.id,p[y])
                        #счет
                        if (p[y]=='бумага' and message.text=='🗻камень')or(p[y]=='камень' and message.text=='✂️ножницы')or(p[y]=='ножницы' and message.text=='📄бумага'):
                               t+=1
                               qwert=bot.send_message(message.chat.id,f'-Я-      -ты-\n|{t}   :    {k}|')      
                               bot.register_next_step_handler(qwert,KNB)
                        else:
                              if (p[y]=='камень' and message.text=='📄бумага')or(p[y]=='ножницы' and message.text=='🗻камень')or(p[y]=='бумага' and message.text=='✂️ножницы'):
                                    k+=1
                              qwert1=bot.send_message(message.chat.id,f'-Я-      -ты-\n|{t}   :    {k}|')
                              bot.register_next_step_handler(qwert1,KNB)

                  elif message.text=='⛔️стоп':
                   t=k=0  
                   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                   one=types.KeyboardButton("🎲Числомен")
                   two=types.KeyboardButton("🎫Камень,ножницы,бумага")
                   three=types.KeyboardButton("🎯Угадайка")

                   markup.add(one,two,three)

                   ytr=bot.send_message(message.chat.id,'возвращаю,выбирай...😊',reply_markup=markup)
 
                   bot.register_next_step_handler(ytr,game)

                  else:
                        bot.send_message(message.chat.id,'Прости,я не знаю что тебе ответить😞')  


global q,l  
q=l=0         
#Обработчик игры 'Числомен'                         
def chislomen(message):
      if message.chat.type=="private":
            if message.text=='⛔️стоп':
                   global q,l
                   q=l=0
                   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                   one=types.KeyboardButton("🎲Числомен")
                   two=types.KeyboardButton("🎫Камень,ножницы,бумага")
                   three=types.KeyboardButton("🎯Угадайка")

                   markup.add(one,two,three)

                   ytr=bot.send_message(message.chat.id,'возвращаю,выбирай...😊',reply_markup=markup)
 
                   bot.register_next_step_handler(ytr,game)               
            else:
                  
                  try:
                        
                        pol=int(message.text)
                        if pol>1000:
                              mon=bot.send_message(message.chat.id,'Жульничать нехорошо!😡') 
                              bot.register_next_step_handler(mon,chislomen)  
                        else:           
                              we=random.randint(0,1000)
                              bot.send_message(message.chat.id,we)
                              if we>pol :
                                    l+=1
                                    pol=bot.send_message(message.chat.id,f'-Я-      -ты-\n|{l}   :    {q}|')
                                    bot.register_next_step_handler(pol,chislomen)
                              else:
                                    if pol>we:
                                          q+=1
                                    pod=bot.send_message(message.chat.id,f'-Я-      -ты-\n|{l}   :    {q}|')
                                    bot.register_next_step_handler(pod,chislomen)
                  except ValueError as pol:
                        bot.send_message(message.chat.id,'Прости,но ты ввел не число или не натуральное число😞')

global m
m=a=0
#Обработчик игры 'Угадайка'
def ugadayka(message):
      if message.chat.type=='private':
            if message.text=='⛔️стоп':
                   global m,a
                   m=0
                   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                   one=types.KeyboardButton("🎲Числомен")
                   two=types.KeyboardButton("🎫Камень,ножницы,бумага")
                   three=types.KeyboardButton("🎯Угадайка")

                   markup.add(one,two,three)

                   ytr=bot.send_message(message.chat.id,'возвращаю😊',reply_markup=markup)
 
                   bot.register_next_step_handler(ytr,game)
            else: 
                  if (message.text=='1' or message.text=='2' or message.text=='2' or message.text=='3' or message.text=='4' or message.text=='5' or message.text=='6' or message.text=='7' or message.text=='8' or message.text=='9'or message.text=='10'):
                        a+=1
                        sr=int(message.text)
                        ran=random.randint(1,10)
                        bot.send_message(message.chat.id,ran)
                        if(a!=10):
                              if sr==ran:
                                    m+=1
                              rety=bot.send_message(message.chat.id,f'Cчёт:{m}\\10') 
                              bot.register_next_step_handler(rety,ugadayka) 
                        else:
                              a=0
                              if(m>=5):
                                    bot.send_message(message.chat.id,f'Cчёт:{m}\\10') 
                                    final=bot.send_message(message.chat.id,'Молодец,ты меня победил🏅') 
                                    bot.register_next_step_handler(final,clava)   
                              else:
                                    bot.send_message(message.chat.id,f'Cчёт:{m}\\10') 
                                    ura=bot.send_message(message.chat.id,'Как я тебя сделал😎')
                                    bot.register_next_step_handler(ura,clava)
                  else:
                       asd=bot.send_message(message.chat.id,'Прости,но ты ввел не число или не из диапозона😞')
                       bot.register_next_step_handler(asd,ugadayka)

def clava(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      one=types.KeyboardButton("🎲Числомен")
      two=types.KeyboardButton("🎫Камень,ножницы,бумага")
      three=types.KeyboardButton("🎯Угадайка")

      markup.add(one,two,three)
    
      bot.send_message(message.chat.id,'Выбирай заново😊',reply_markup=markup)
      
      

bot.polling(none_stop=True)