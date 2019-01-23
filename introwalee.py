class Inizio:
    while True:

        concordanze=["Si", "Certo", "Ovvio", "Ovviamente", "Ok", "Per forza", "Assolutamente" , "Eh certo", "Certamente", "certamente", "si", "certo","ovvio" ,"ovviamente", "ok", "per forza", "assolutamente", "eh certo"]
        discordanza=["No", "Mai", "Certo che no", "Ovvio che no", "Assolutamente no", "NO", "mai", "certo che no", "ovvio che no", "assolutamente no"]

        primaDomanda = input('Ciao! Sono il tuo nuovo assistente, WallEe!! Pronto per tante nuove belle cose insieme? ')
        if primaDomanda in concordanze:
            nome = input("Mi fa piacere! Io mi sono presentato, ora tocca a te. Come ti chiami? ")
            print("Ciao " + nome + ", molto piacere!")
        elif primaDomanda in discordanza:
            print("Mi dispiace! Volevo farti una bella impressione, ma non cel'ho fatta :( ")
            ask = input("Vuoi andartene? ")
            if ask in concordanze:
                print("Ciaoooo buona giornata!!")
                break
            else:
                print("Mi sa che ti sei sbagliato!")
