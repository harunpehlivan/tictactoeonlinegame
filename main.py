import time
from os import system
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 
from termcolor import colored
from time import time as tm


firebase_sdk =credentials.Certificate("venv/include/scoreboard-bb61f-firebase-adminsdk-gptsj-33f4d9658e (1).json")

firebase_admin.initialize_app(firebase_sdk,{"databaseURL":"https://scoreboard-bb61f-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/3EnRayaOnline")
"""ref.push({"Casillas":[[" "," "," "],[" "," "," "],[" "," "," "]]})"""

ref = db.reference("3EnRayaOnline")
casilla_ref=ref.child("-NFPEbKeBFWDRrnmRup8")
"""for i in range(1,10):
    casilla_ref.update({"Casillas"+str(i):[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})"""

lobby="1"
casilla=casilla_ref.child("Casillas"+lobby)
casillas=casilla.get()

print(".\n\n\nType 'server' to see the lobbys, you can join or spectate the one you like. Type 'play' to directly be in a lobby.'server'/'play'")
debut=str(input())

while debut!="play" and debut!="server":
    print(".\n\n\nType 'server' to see the lobbys, you can join or spectate the one you like. Type 'play' to directly be in a lobby. 'server'/'play'")
    debut=str(input())
    
start=1
end=11
elegido=0
while debut=="server":
    color_server=""

    for i in range(start,end):
        casilla=casilla_ref.child("Casillas"+str(i))
        casillas=casilla.get()
        if casillas[8]==0:
            color_server="green"
        if casillas[8]==1:
            color_server="blue"
        if casillas[8]>=2:
            color_server="red"
        print(colored("Lobby nº"+str(i)+": ",color_server),casillas[8],"/2 players.")
    
    print("Press 'enter' to refresh, type 'play x' to play on one server, type 'join x' to spectate a game and type '+' or '-' to see more or less servers: (replace 'x' by the number of the server.)\n'play x'/'join x'/'+'/'-'.")
    join=str(input())
    system("clear")
    count_letra=1
    for letra in join:
        if letra =="+":
            start=start+10
            end=end+10
        if letra =="-":
            if start>1:
                start=start-10
                end=end-10
        if letra =="p":
            for i in join:
                if count_letra==6:
                    lobby=str(i)
                    elegido=1
                    debut="ok"
                count_letra+=1
        if letra=="j":
            for j in join:
                if count_letra==6:
                    lobby=str(j)
                    elegido=1
                    debut="ok"
                    
                    while True:
                        casilla=casilla_ref.child("Casillas"+lobby)
                        casillas=casilla.get()
                        system("clear")
                        color_join="blue"
                        print(colored(casillas[5],"red"),"is playing against",colored(casillas[6],"red"),"!\n")
                        for i in range(len(casillas[0])):
                            for j in range(len(casillas[0])):
                                if j==0:
                                    print("     ",i+1,"|  ",end="")
                                if j<2:
                                    print(colored(casillas[i][j],color_join),"|",end="")
                                else:
                                    print(colored(casillas[i][j],color_join),end=" \n")
                            if i<2:
                                print("           ",end="")
                                print("--------")
                        print("            _  _  _ ")
                        print("            1  2  3 ")
                        time.sleep(1)
                        
                count_letra+=1

                
if debut=="play" and elegido==0:
    while casillas[8]>=2:
        lobby=str(int(lobby)+1)
        casilla=casilla_ref.child("Casillas"+lobby)
        casillas=casilla.get()
    

    
casilla=casilla_ref.child("Casillas"+lobby)
casillas=casilla.get()
game_is_over=False
true_red=2
emoji="x"
username=""
empezaste=0
while casillas[8]>=2:
        lobby=str(int(lobby)+1)
        casilla=casilla_ref.child("Casillas"+lobby)
        casillas=casilla.get()
casilla=casilla_ref.child("Casillas"+lobby)
casillas=casilla.get()    
if casillas[3]==0:
    casillas[3]=1
    username=os.environ['REPL_OWNER']
    casillas[5]=username
    username=casillas[6]
else:
    username=os.environ['REPL_OWNER']
    casillas[6]=username
    true_red+=1
    username=casillas[5]
    empezaste+=1
    
if casillas[5]==casillas[6]:
    true_red=2
    username=""
    empezaste=0
    casilla_ref.update({"Casillas"+lobby:[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})
    if casillas[3]==0:
        casillas[3]=1
        username=os.environ['REPL_OWNER']
        casillas[5]=username
        username=casillas[6]
    else:
        username=os.environ['REPL_OWNER']
        casillas[6]=username
        true_red+=1
        username=casillas[5]
        empezaste+=1
    
casillas[0]=[" "," "," "]
casillas[1]=[" "," "," "]
casillas[2]=[" "," "," "]
casillas[8]=casillas[8]+1
casilla_ref.update({"Casillas"+lobby:casillas})
casillas=casilla.get()

if casillas[5]==casillas[6]:
    true_red=2
    username=""
    empezaste=0
    casilla_ref.update({"Casillas"+lobby:[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})
    casillas=casilla.get()
    if casillas[3]==0:
        casillas[3]=1
        username=os.environ['REPL_OWNER']
        casillas[5]=username
        username=casillas[6]
    else:
        username=os.environ['REPL_OWNER']
        casillas[6]=username
        true_red+=1
        username=casillas[5]
        empezaste+=1
    
    casillas[0]=[" "," "," "]
    casillas[1]=[" "," "," "]
    casillas[2]=[" "," "," "]
    casillas[8]=casillas[8]+1
    casilla_ref.update({"Casillas"+lobby:casillas})
    casillas=casilla.get()

def display():
    color="red"
    for i in range(len(casillas[0])):
        for j in range(len(casillas[0])):
            if casillas[i][j]=="x" and empezaste==1:
                color="red"
            if casillas[i][j]=="o" and empezaste==1:
                color="green"
            if casillas[i][j]=="x" and empezaste==0:
                color="green"
            if casillas[i][j]=="o" and empezaste==0:
                color="red"
            if j==0:
                print("     ",i+1,"|  ",end="")
            if j<2:
                print(colored(casillas[i][j],color),"|",end="")
            else:
                print(colored(casillas[i][j],color),end=" \n")
        if i<2:
            print("           ",end="")
            print("--------")
    print("            _  _  _ ")
    print("            1  2  3 ")
def play(x,y):
    global username
    if casillas[4]%2==0:
        emoji="x"
    else:
        emoji="o"
    casillas[x][y]=emoji
    casillas[4]+=1
    if empezaste==1:
        casillas[7]=casillas[6]
    else:
        casillas[7]=casillas[5]
    casilla_ref.update({"Casillas"+lobby:casillas})

def ask_case():
        global x,y,game_is_over
        print("\nChoose case between '1,1' and '3,3': (Press 'q' to quit the game.)\n")
        answer=str(input())
        if answer=="q":
            game_is_over=True
            
            rep=5+(casillas[4]%2)
            print("\nGame finished! One of the players gave up and",colored(casillas[7],"blue"),"won!")
            casillas[9]=1
            casilla_ref.update({"Casillas"+lobby:casillas})
            exit()
        if game_is_over==False:    
            count=0
            for letter in answer:
                if count==0:
                    x=int(letter)-1
                if count==2:
                    y=int(letter)-1
                count+=1
            
empate=0          
def game_over():
    global game_is_over,empate
    acabao=0
    for i in range(3):
        for j in range(3):
            if casillas[i][j]==" ":
                acabao+=1
    if acabao==0:
        empate=1
        game_is_over=True
    if casillas[0][0]==casillas[0][1]and casillas[0][1]==casillas[0][2] and casillas[0][2]!=" ":
        game_is_over=True
    if casillas[1][0]==casillas[1][1]and casillas[1][1]==casillas[1][2]and casillas[1][2]!=" ":
        game_is_over=True
    if casillas[2][0]==casillas[2][1] and casillas[2][1]==casillas[2][2]and casillas[2][2]!=" ":
        game_is_over=True
    if casillas[0][0]==casillas[1][0] and casillas[1][0]==casillas[2][0] and casillas[2][0]!=" ":
        game_is_over=True
    if casillas[0][1]==casillas[1][1]and casillas[1][1]==casillas[2][1]and casillas[2][1]!=" ":
        game_is_over=True
    if casillas[0][2]==casillas[1][2]and casillas[1][2]==casillas[2][2]and casillas[2][2]!=" ":
        game_is_over=True
    if casillas[0][0]==casillas[1][1]and casillas[1][1]==casillas[2][2]and casillas[2][2]!=" ":
        game_is_over=True
    if casillas[0][2]==casillas[1][1]and casillas[1][1]==casillas[2][0]and casillas[2][0]!=" ":
        game_is_over=True

        
puntos=[".","..","..."]
contadorpuntos=0


timeout=False
while game_is_over==False:
    system("clear")
    while username=="":
        system("clear")
        print("Waiting for oponent (1/2) in lobby nº"+lobby,puntos[contadorpuntos%3],"\nPlease be patient, it could take a while.")
        casillas=casilla.get()
        if empezaste==0:
            username=casillas[6]
        else:
            username=casillas[5]
        time.sleep(1)
        contadorpuntos+=1
    system("clear")
    print("You are playing against",colored(username,"red"),"!! You have 30seconds to choose.\n")
    display()
    if true_red%2==0:
        starting=tm()
        x=0
        y=0
        ask_case()
        while(x>2 or x<0 or y>2 or y<0 or casillas[x][y]!=" "):
            y=0
            x=0
            ask_case()
        play(x,y)
    else:
        starting=tm()
        timeleft=0
        while casillas==casilla.get():
          system("clear")
          print("You are playing against",colored(username,"red"),"!!\n")
          display()
          ending=tm()
          timeleft=30-round(ending-starting)
          print("\nYour oponent is choosing his play!",timeleft,"seconds left.")
          time.sleep(1)
          
          if round(ending-starting)>30:
            print("\nGame finished! One of the players took to long to choose!")
            casilla_ref.update({"Casillas"+lobby:[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})
            exit()
    ending=tm()
    
    if round(ending-starting)>30:
            print("\nGame finished! One of the players took to long to choose!")
            casilla_ref.update({"Casillas"+lobby:[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})
            exit()
        
    casillas=casilla.get()
    if casillas[9]!=0:
            game_is_over=True
            print("\nGame finished! One of the players gave up and",colored(casillas[7],"blue"),"won!")
            casilla_ref.update({"Casillas"+lobby:[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})
            exit()
    
    game_over()        
    true_red+=1
time.sleep(1)
system("clear")
print("You were playing against",colored(username,"red"),"!!\n")
display()

if empate==1:
    print("\nGame finished! It's a draw!")
else:
    print("\nGame finished!",colored(casillas[7],"blue"),"won!")
    
casilla_ref.update({"Casillas"+lobby:[[" "," "," "],[" "," "," "],[" "," "," "],0,0,"","","",0,0]})