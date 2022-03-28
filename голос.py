from gtts import gTTS
import os
from time import sleep

print ("Введите строку для проговаривания: ")
text = input()

print ("Введите количество проговариваний: ")
i = int(input())

print ("Хотите ли Вы добавлять 'хы-хы' в конце? (Введите да/нет):")
choose = input()

#text = 'Даша Косулина, я тебя пуплю!'
for j in range(i):
    if (choose == "да"):
        text += ' хы'
    speech = gTTS(text=text, lang='ru', slow=False)
    speech.save('l.mp3')
    os.system('l.mp3')
    sleep(5)
