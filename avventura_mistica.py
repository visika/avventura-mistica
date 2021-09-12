prompt = "> "

print("Ciao giocatore, benvenuto. Come ti chiami?")

nome = input(prompt)

print("Una bellissima fanciulla!\n")

print("Entri in una stanza oscura con cinque porte.")
print("Attraversi la porta n°1 o la porta n°2 o la porta n°3 o la porta n°4 o la porta n°5?")

porta = input(prompt)

if porta == "1":
    print("C'è un orso gigante qui che sta mangiando una torta. Che fai?")
    print("1. Prendi la torta.")
    print("2. Urla contro l'orso.")

    orso = input(prompt)
    if orso == "1":
        print("L'orso ti strappa via la faccia a morsi. Ottimo lavoro!")
    elif orso == "2":
        print("L'orso ti strappa via le gambe. Ottimo lavoro!")
    else:
        print("Certo, fare %s è sicuramente migliore. L'orso fugge terrorizzato." % orso)

elif porta == "2":
    print("Ti trovi al cospetto dell'occhio di Sauron.")
    print("Sauron ti chiede di offrirgli l'anello del potere. Che fai?")
    print("1. Fruga nelle tasche ed offrigli 50 centesimi.")
    print("2. Mettiti l'anello e tenta una fuga disperata.")
    print("3. Passa al lato oscuro. Dona l'anello e la tua vita all'oscuro signore.")

    anello = input(prompt)
    if anello == "1" or anello == "2":
        print("Non hai scampo contro l'oscuro signore. Non fai in tempo a fare un passo e sei ridotto in cenere. Ottimo lavoro!")
    else:
        print("Saggia scelta, diventerai presto un cavaliere oscuro ed il potere sarà tuo. Ottimo lavoro!")

elif porta == "3":
    print("Attraversata la porta, un uomo con una maschera pedala un triciclo e dice: \"Voglio fare un gioco con te.\nRispondi correttamente alle mie domande e sarai libero di tornare al mondo reale sulle tue gambe:\nQuanti carri armati ci vogliono per uccidere Batman?\"")
    print("1. 1")
    print("2. 2")
    print("3. Solo Jocker può sconfiggere Batman!")

    batman = input(prompt)
    if batman == "1" or batman == "2":
        print('"Credi davvero che sia così facile?"\nJigsaw ti fa a pezzi. Ottimo lavoro!')
    else:
        print('"Che coniglio che sei, affronta la realtà!"\nJigsaw ti libera e torni alla tua vita di sempre.')

elif porta == "4":
    print("""Ti addentri in un luogo non ben definito,
avvolto da una nebbia di un color verde ocra.
I tuoi sensi sono annebbiati ed in questo stato una voce ti dice:
"Giovane, cosa sei?"

    1. Guerriero
    2. Mago
    3. Arciere
    4. Guerriago
    5. Guerciere
    6. Marriero
    7. Marciere
    8. Arciero
    9. Arciago
    """)

    essenza = input(prompt)
    if essenza == "non morto":
        print("Ho sempre odiato gli scheletri.")

    print("""Sono molto soddisfatto, l'avevo previsto. In questo ambiente i tuoi sensi sono annebbiati per permetteri di prendere le scelte direttamente dal tuo inconscio...
Ma come sono stato scortese, non mi sono presentato. Ciao %s, la tua missione è prendere la cappa magica nella cappella di Cappella, un remoto paese nella contea di Bacoli, nel regno di Napoli. Ho fatto anche rima.
Ora va' e non fallire!
    """ % nome)

    print("Ti ridesti assonnato sulle rive di un fiume e guardandoti intorno ti accorgi d'essere nell'Ellesponto.")
    print("1. Segui il fiume.")
    print("2. Vai in città.")
    print("3. Chiedi informazioni ad un pastore.")

    ellesponto = input(prompt)
    if ellesponto == "1":
        print("Cadi nella corrente e resti fulminato perché la tensione era molto alta. Ottimo lavoro!")
    else:
        print("Vieni riconosciuto in poco tempo, e la gente ti mette al rogo come essere immondo. Ottimo lavoro!")

elif porta == "5":
    print("""
Trovi una statua che ti chiede: "Dove devi andare?"

1. Ti do un passaggio?
2. Scappi via.
3. Lo lasci stare.
""")

    statua = input(prompt)
    if statua == "1":
        print("Ti porta a casa sua e ti chiude dentro.")
        print("""
1. Provi a spaccare le finestre.
2. Cerchi un cellulare.
3. Urli affinché qualcuno ti senta.
""")
        casa = input(prompt)
        
        if casa == "1":
            print("Tutto inutile, sono elettrificate, la corrente ti uccide. Ottimo lavoro!")
        elif casa == "2":
            print("Sono tutti rotti, soffochi nella casa. Ottimo lavoro!")
        else:
            print("Se ne sono andati tutti dalla città, è il mostro a sentirti. Ottimo lavoro!")
    elif statua == "2":
        print("Ti insegue fino allo sfinimento.")
        print("""
1. Tu lo trolli portandolo alla stazione della polizia.
2. Gli lanci una granata e lo fai saltare nell'altro mondo.
3. Chiami i tuoi amici e lo incatenate su un palo.
""")
        sfinimento = input(prompt)
        
        if sfinimento == "1":
            print("La stazione della polizia sta in un'altra città. Ottimo lavoro!")
        elif sfinimento == "2":
            print("Hai solo granate fumogene, il mostro ti raggiunge prima che te ne accorga. Ottimo lavoro!")
        else:
            print("I tuoi amici stanno ad una festa. Ottimo lavoro!")
    else:
        print("Ti compaiono tre troll che ti inseguono.")
        print("""
1. Scappi nell'unico spazio libero.
2. Li distrai con indovinelli per poi scappare.
""")
        
        troll = input(prompt)
        
        if troll == "1":
            print("Inciampi su un sasso e ti acchiappano. Ottimo lavoro!")
        else:
            print("Non ti vengono in mente indovinelli. Ottimo lavoro!")

else:
    print("Cammini in giro e cadi su un pugnale e muori. Ottimo lavoro!")
