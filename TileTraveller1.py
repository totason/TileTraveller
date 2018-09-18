#x, y hnit fyrir staðsetningu
#Ef notandi færir sig til norður eða suður þá er það + og - á y hniti
#Austur og vestur eru + og - á x hniti
#Ef x eða y er 1 kemst það ekki lengra í mínus áttina
#Ef x eða y er 3 kemst það ekki lengra í + áttina
#Bæti við þeim upplýsingum að "Veggir" séu á ákveðnum stöðum
#Skilgreini að ekki sé hægt að fara í gegnum þá með if elif 

x = 1
y = 1

print(prufustrengur)
norður = "(N)orth "
austur = "(E)ast "
suður = "(S)outh "
vestur = "(W)est "
eða = "or "
punktur = "."
attir = ""
badspot1, badspot2, badspot3, badspot4 = "2.1", "3.4", "4.3", "4.1"

while (x != 5) and (y != 1):
    n = str(x) + "." + str(y + 1)
    a = str(x + 1) + "." + str(y)
    s = str(x) + "." + str(y - 1)
    v = str(x - 1) + "." + str(y)
    manordur, maaustur, masudur, mavestur = False

    if (n != badspot1) and (n != badspot2) and (n != badspot3) and (n != badspot4) and ((y + 1)!= 6):
        attir += norður
        manordur = True
    if (a != badspot1) and (a != badspot2) and (a != badspot3) and (a != badspot4) and ((x + 1)!= 6):
        attir += austur
        maaustur = True
    if (s != badspot1) and (s != badspot2) and (s != badspot3) and (s != badspot4) and ((y - 1)!= 0):
        attir += suður
        masudur = True
    if (v != badspot1) and (v != badspot2) and (v != badspot3) and (v != badspot4) and ((x - 1)!= 0):
        attir += vestur
        mavestur = True
    print("You can travel: " + attir)
    inp = input("Direction")

    if (inp == "n" or inp =="N") and (manordur == True):
        y += 2
    elif (inp == "a" or inp =="A") and (maaustur == True):
        x += 2
    elif (inp == "s" or inp =="S") and (masudur == True):
        y -= 2
    elif (inp == "w" or inp =="W") and (mavestur == True):
        x -= 2

