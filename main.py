import array as arr
import random
import os

def erasekey():
  for x in range(9):
    msgkey[x] = 0
  print("memory clear")
  return;

def enterkey():
  for xint in range(10):
    manualkey = int(input("Enter a key(0-25): "))
    if manualkey >= 0 and manualkey < 26:
      msgkey[xint] = manualkey
    else:
      print("invalid key")
      quit()
  print('MSGKEY: ', end = '')
  for x in range(9):
    print(msgkey[x],' ' ,end = '')
  print('')
  return;print(msgkey)
  return;

def creatkey():
  print('New key: ', end = '')
  for xint in range(10):
    msgkey[xint] = random.randint(0,25)
    print(msgkey[xint], ' ', end = '')
  print()
  return;

def dispkey():
  print('MSGKEY: ', end = '')
  for x in range(10):
    print(msgkey[x],' ' ,end = '')
  print('')
  return;

def decrypt():
  dec = [92,92]
  for x in range(maxlen):
    dec.append(92)
  #Dekryptering, börja med att nollställa nyckeln
  PosA = msgkey[0]
  PosB = msgkey[1]
  PosC = msgkey[2]
  PosD = msgkey[3]
  PosE = msgkey[4]
  PosF = msgkey[5]
  PosG = msgkey[6]
  PosH = msgkey[7]
  PosI = msgkey[8]
  PosJ = msgkey[9]

  print()
  #Läs in kodad text från kodat till enc, kontrollera tecknen
  kodat = input("Enter coded text: ")
  spaces = 0
  
  for xent in range(len(kodat)):
    if ord(kodat[xent]) == 32:
      spaces = spaces + 1
    elif ord(kodat[xent]) > 64 and ord(kodat[xent]) < 91:
      enc[xent-spaces] = ord(kodat[xent])-65
    elif ord(kodat[xent]) > 96 and ord(kodat[xent]) < 123:
      enc[xent-spaces] = ord(kodat[xent])-97
    else:
      print('character error!')
      #exit()
  #for x22 in range(len(kodat)):
  
  yent = 0
  #Dekryptera, baklänges genom hjulen

  for y in range(len(kodat)-spaces):
    for x in range(26):
      if j[x] == enc[y]:
          valJ = (x-PosJ)%26
    for x in range(26):
      if i[x] == valJ:
          valI = (x-PosI)%26
    for x in range(26):
      if h[x] == valI:
        valH = (x-PosH)%26
    for x in range(26):
      if g[x] == valH:
        valG = (x-PosG)%26
    for x in range(26):
      if f[x] == valG:
        valF = (x-PosF)%26
    for x in range(26):
      if e[x] == valF:
        valE = (x-PosE)%26
    for x in range(26):
      if d[x] == valE:
        valD = (x-PosD)%26
    for x in range(26):
      if c[x] == valD:
        valC = (x-PosC)%26
    for x in range(26):
      if b[x] == valC:
        valB = (x-PosB)%26
    for x in range(26):
      if a[x] == valB:
        valA = (x-PosA)%26
        dec[y] = valA
      #Rotera hjulen efter pinkey    
    PosA = PosA + pinkey[0]
    PosB = PosB + pinkey[1]
    PosC = PosC + pinkey[2]
    PosD = PosD + pinkey[3]
    PosE = PosE + pinkey[4]
    PosF = PosF + pinkey[5]
    PosG = PosG + pinkey[6]
    PosH = PosH + pinkey[7]
    PosI = PosI + pinkey[8]
    PosJ = PosJ + pinkey[9]
  #Skriv ut den dekrypterade texten
  #print("Dekrypterat: ",dec)
  
  print('Decrypted text: ', end ='' )
  for bx in range(len(dec)):
    if dec[bx] == 25:
      print(' ', end = '')
    elif dec[bx] == 92:
      return;
    else:
      print(chr(dec[bx]+65), end = '')
  return;

def encrypt():
  #Läs in meddelandet
  message = input("Enter message: ")
  buff = 0;
  buffmsg = "XXXX"
  #räkna ut hur många tecken som ska läggas till för att få 5 div
  while (len(message) + buff) % 5 != 0:
    buff = buff + 1
  if len(message) > maxlen:
    print('Message too long')
    exit()
  #Kontrollera så att meddelandet inte innehåller förbjudna tecken
  for xy in range(len(message)):
    if ord(message[xy]) > 32 and ord(message[xy]) < 65:
      print('Forbidden characters!')
      exit()
    if ord(message[xy]) > 90 and ord(message[xy]) < 97:
      print('Forbidden characters!')
      exit()
    if ord(message[xy]) > 122:
      print('Forbidden characters!')
      exit()
  for xy in range(len(message)):
    if ord(message[xy]) == 32:
      msg[xy] = 25
    elif ord(message[xy]) > 96 and ord(message[xy]) < 123:
      msg[xy] = ord(message[xy])-97
    else:
      msg[xy] = ord(message[xy])-65

  #Kodinställning, startpossition per hjul
  PosA = msgkey[0]
  PosB = msgkey[1]
  PosC = msgkey[2]
  PosD = msgkey[3]
  PosE = msgkey[4]
  PosF = msgkey[5]
  PosG = msgkey[6]
  PosH = msgkey[7]
  PosI = msgkey[8]
  PosJ = msgkey[9]
  #Kyptering
  count = 0
  print('Encrypted text: ', end = '')
  for x in range(len(message)):
    count = count + 1
    PosY = (PosA+msg[x])%26
    outbyte = a[PosY]
    PosX = (PosB+outbyte)%26
    outbyte = b[PosX]
    PosZ = (PosC+outbyte)%26
    outbyte = c[PosZ]
    PosY1 = (PosD+outbyte)%26
    outbyte = d[PosY1]
    PosY2 = (PosE+outbyte)%26
    outbyte = e[PosY2]
    PosY3 = (PosF+outbyte)%26
    outbyte = f[PosY3]
    PosY4 = (PosG+outbyte)%26
    outbyte = g[PosY4]
    PosY5 = (PosH+outbyte)%26
    outbyte = h[PosY5]
    PosY6 = (PosI+outbyte)%26
    outbyte = i[PosY6]
    PosY7 = (PosJ+outbyte)%26
    outbyte = j[PosY7]
    enc[x] = outbyte
    print(chr(outbyte+65), end = '')
    if count > 4:
      print(' ', end = '')
      count = 0
      
    #Rotering av hjul, efter pinkey.
    PosA = PosA + pinkey[0]
    PosB = PosB + pinkey[1]
    PosC = PosC + pinkey[2]
    PosD = PosD + pinkey[3]
    PosE = PosE + pinkey[4]
    PosF = PosF + pinkey[5]
    PosG = PosG + pinkey[6]
    PosH = PosH + pinkey[7]
    PosI = PosI + pinkey[8]
    PosJ = PosJ + pinkey[9]
#skapa femställiga bokstadskombinationer
  for x in range(buff):
    count = count + 1
    PosY = (PosA+25)%26
    outbyte = a[PosY]
    PosX = (PosB+outbyte)%26
    outbyte = b[PosX]
    PosZ = (PosC+outbyte)%26
    outbyte = c[PosZ]
    PosY1 = (PosD+outbyte)%26
    outbyte = d[PosY1]
    PosY2 = (PosE+outbyte)%26
    outbyte = e[PosY2]
    PosY3 = (PosF+outbyte)%26
    outbyte = f[PosY3]
    PosY4 = (PosG+outbyte)%26
    outbyte = g[PosY4]
    PosY5 = (PosH+outbyte)%26
    outbyte = h[PosY5]
    PosY6 = (PosI+outbyte)%26
    outbyte = i[PosY6]
    PosY7 = (PosJ+outbyte)%26
    outbyte = j[PosY7]
    enc[x] = outbyte
    print(chr(outbyte+65), end = '')
    if count > 4:
      print(' ', end = '')
      count = 0
      
    #Rotering av hjul, efter pinkey.
    PosA = PosA + pinkey[0]
    PosB = PosB + pinkey[1]
    PosC = PosC + pinkey[2]
    PosD = PosD + pinkey[3]
    PosE = PosE + pinkey[4]
    PosF = PosF + pinkey[5]
    PosG = PosG + pinkey[6]
    PosH = PosH + pinkey[7]
    PosI = PosI + pinkey[8]
    PosJ = PosJ + pinkey[9]

  print()
  return;

#Detta är kodhjulen, 10st. Byt ordning på dessa enligt schema
#Hjul 1
d = arr.array('l', [12,24,16,3,11,4,7,21,19,22,6,1,20,14,15,9,10,25,5,13,23,2,8,17,18,0])
#Hjul 2
i = arr.array('l', [4,9,18,10,8,13,24,7,5,2,22,14,3,1,25,11,20,0,19,6,15,16,21,23,12,17])
#Hjul 3
j = arr.array('l', [10,14,4,11,25,17,5,21,23,0,13,18,24,7,1,15,22,20,16,2,6,8,9,3,19,12])
#Hjul 4
c = arr.array('l', [6,21,19,1,22,18,10,7,3,14,11,15,16,0,8,20,24,25,5,9,23,2,17,13,4,12])
#Hjul 5
e = arr.array('l', [12,24,16,3,11,4,7,21,19,22,6,1,20,14,15,9,10,25,5,13,23,2,8,17,18,0])
#Hjul 6
a = arr.array('l', [1,11,17,7,13,16,21,2,24,23,12,4,20,19,15,6,25,14,10,0,18,8,5,22,9,3])
#Hjul 7
b = arr.array('l', [19,13,22,17,14,16,8,12,15,4,2,3,10,9,23,20,0,18,21,11,25,1,6,5,24,7])
#Hul 8
f = arr.array('l', [24,6,19,16,13,8,0,14,17,23,2,15,4,12,7,25,9,21,22,3,1,20,5,10,18,11])
#Hjul 9
g = arr.array('l', [16,19,4,10,25,5,8,14,2,21,15,18,9,13,12,0,3,1,11,20,7,6,24,22,17,23])
#Hjul 10
h = arr.array('l', [5,2,23,25,16,6,8,14,18,11,12,22,9,17,10,7,4,19,24,3,21,15,13,20,1,0])

#Maxlängd på text
maxlen = 2000
#Meddelandenyckel, mellan 0 och 25
msgkey = arr.array('l', [21,5,21,13,6,3,22,13,8,21])
#Number of turns each wheel takes each letter
pinkey = arr.array('l', [1,3,5,7,9,11,17,19,23,25])
#För kopiering


#Skapa listor för meddelandena
msg = [1,1]
for x in range(maxlen):
  msg.append(1)
#det krypterade meddelandet
enc = [92,92]
for x in range(maxlen):
  enc.append(92)
dec = [92,92]
for x in range(maxlen):
  dec.append(92)

print('68-bit rotary substitution cipher version 1.7')

while 1:
  print()
  print('1: ENCRYPT')
  print('2: DECRYPT')
  print('')
  print('3: DISPLAY KEY IN MEMORY')
  print('4: CREATE RANDOM KEY')
  print('5: ENTER KEY MANUALLY')
  print('6: ERASE KEY IN MEMORY')
  print('E: EXIT')
  option = input("")
  if option == '1':
    encrypt()
  elif option == '2':
    decrypt()
  elif option == '3':
    dispkey()
  elif option == '4':
    creatkey()
  elif option == '5':
    enterkey()
  elif option == '6':
    erasekey()
  elif option == 'E' or option == 'e':
    break
  #Läs in meddelandet

 