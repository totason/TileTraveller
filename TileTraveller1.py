#x, y hnit fyrir staðsetningu
#Ef notandi færir sig til norður eða suður þá er það + og - á y hniti
#Austur og vestur eru + og - á x hniti
#Ef x eða y er 1 kemst það ekki lengra í mínus áttina
#Ef x eða y er 3 kemst það ekki lengra í + áttina
#Bæti við þeim upplýsingum að "Veggir" séu á ákveðnum stöðum
#Skilgreini að ekki sé hægt að fara í gegnum þá með if elif 

x = 1
y = 1
norður = "(N)orth "
austur = "(E)ast "
suður = "(S)outh "
vestur = "(W)est "
eða = "or "
punktur = "."
attir = ""
attir = norður + eða + austur + eða + suður + punktur
attir -= austur
print(attir)
while (x != 3) and (y != 1):
    if x == 1:
        attir = norður + eða + austur + eða + suður, punktur

    
