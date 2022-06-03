import ev, stats, main

otopt = 0

print("POKEMON CALCULATOR\n1. Stats\n2. EV")
opt = int(input(":"))

anostats = ["HP","Attack","Defense","Special Attack","Special Defense","Speed"]

def values():
    global thestat, base, IV, EV, lvl, natures, naku
    base, thestat = 0, 0
    naku = []
    if otopt == 2:
        print("BASE:")
        for a in range (len(anostats)):
            ayo = int(input(anostats[a]))
            naku.append(ayo)     
    else:   
        for b in range (len(anostats)):
            print(b+1,".",anostats[b])
        thestat = int(input(":"))   
        print("\n",anostats[thestat-1].upper())   
        base = int(input("Base: "))
    IV = int(input("IV (1-31): "))
    EV = int(input("EV (1-255): "))
    lvl = int(input("Level: "))

    if thestat > 1 or anostats[thestat-1] != "HP":
        print("What Nature?")
        print("\t1. Hardy       6. Bold        11. Timid       16. Modest       21. Calm")
        print("\t2. Lonely      7. Docile      12. Hasty       17. Mild         22. Gentle")
        print("\t3. Brave       8. Relaxed     13. Serious     18. Quiet        23. Sassy")
        print("\t4. Adamant     9. Impish      14. Jolly       19. Bashful      24. Careful")
        print("\t5. Naughty     10. Lax        15. Naive       20. Rash         25. Quirky")
        natures = int(input("Nature: "))
    else: natures = 0

def mali(): 
    print("bobo amp")
    out()

def out():
    input("Press any key to continue...")
    main

if opt == 1:
    print("\nWelcome to Pokemon Stats Calculator")
    values()
    print(anostats[thestat-1],": ", stats.userstat.stat(thestat,base,IV,EV,lvl,natures), end="\n\n")
    out()
    
elif opt == 2:
    del anostats[0]
    print("\nEV CALCULATOR\n1. Single Stat\n2. All Stats")
    otopt = int(input(":"))
    if(otopt == 1):
        print("\nSINGLE STAT")
        values()
        stat = int(input("Desire Stat: "))
        print("EV Needed on",anostats[thestat-1].upper(),": ", ev.userev.single(thestat,base,IV,EV,lvl,natures,stat), end="\n\n")
    elif(otopt == 2): 
        print("\nALL STAT")
        anostats = [anostats + ": " for anostats in anostats]  
        values()
        desire = []
        print("\nDesire Stats:")
        for b in range (len(anostats)):
            stat = int(input(anostats[b]))
            desire.append(stat)
        print("\nEVs Needed on:")
        for c in range (len(anostats)):
            print(anostats[c],ev.userev.all(desire,naku[c],desire[c],IV,EV,lvl,natures,stat), end="\n")
        print("\n")
    else: mali()
    out()

else: mali()

