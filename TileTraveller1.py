#x, y hnit fyrir stadsetningu
#Ef notandi færir sig til nordur eda sudur þá er þad + og - á y hniti
#Austur og vestur eru + og - á x hniti
#Ef x eda y er 1 kemst þad ekki lengra í mínus áttina
#Ef x eda y er 3 kemst þad ekki lengra í + áttina
#Bæti vid þeim upplýsingum ad "Veggir" séu á ákvednum stödum
#Skilgreini ad ekki sé hægt ad fara í gegnum þá med if elif 

x = 1
y = 1
nordur = "(N)orth"
austur = " (E)ast"
sudur = " (S)outh"
vestur = " (W)est"
eda = " or"
punktur = "."

badspot1, badspot2, badspot3, badspot4 = "2.1", "3.4", "4.3", "4.1"
operator = (x != 5) and (y != 1)


while True:
    n = str(x) + "." + str(y + 1)
    a = str(x + 1) + "." + str(y)
    s = str(x) + "." + str(y - 1)
    v = str(x - 1) + "." + str(y)
    manordur, maaustur, masudur, mavestur = False, False, False, False
    attir = ""
    edaeftirfyrsta = False
    if (n != badspot1) and (n != badspot2) and (n != badspot3) and (n != badspot4) and ((y + 1)!= 6):
        attir += nordur
        manordur = True
        edaeftirfyrsta = True
    if (a != badspot1) and (a != badspot2) and (a != badspot3) and (a != badspot4) and ((x + 1)!= 6):
        if edaeftirfyrsta:
            attir = attir + eda + austur
        else:
            attir += austur
        maaustur = True
        edaeftirfyrsta = True
    if (s != badspot1) and (s != badspot2) and (s != badspot3) and (s != badspot4) and ((y - 1)!= 0):
        if edaeftirfyrsta:
            attir = attir + eda + sudur
        else:
            attir += sudur
        masudur = True
        edaeftirfyrsta = True
    if (v != badspot1) and (v != badspot2) and (v != badspot3) and (v != badspot4) and ((x - 1)!= 0):
        if edaeftirfyrsta:
            attir = attir + eda + vestur
        else:
            attir += vestur
        masudur = True
    attir += punktur

    virkadi = False
    while virkadi == False:
        print("You can travel: " + attir)
        inp = input("Direction: ")
        virkadi = True
        if (inp == "n" or inp =="N") and (manordur == True):
            y += 2
        elif (inp == "e" or inp =="E") and (maaustur == True):
            x += 2
        elif (inp == "s" or inp =="S") and (masudur == True):
            y -= 2
        elif (inp == "w" or inp =="W") and (mavestur == True):
            x -= 2
        else:
            print("Invalid direction!")
            virkadi = False
    if (x == 5) and (y == 1):
        print("Victory Royale")
        break

