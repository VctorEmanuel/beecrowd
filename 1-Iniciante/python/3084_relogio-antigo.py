while True:
    try:
        horas, minutos, distanciah, distanciam, limiteh, limitem = [], [], [], [], 0, 0
        for angulos in range(0, 360):
            distanciah.append(angulos), distanciam.append(angulos)
            limiteh, limitem = limiteh + 1, limitem + 1
            if limiteh == 30:
                horas.append(distanciah)
                limiteh, distanciah = 0, []
            if limitem == 6:
                minutos.append(distanciam)
                limitem, distanciam = 0, []
        entrada = input().split()
        h, m = int(entrada[0]), int(entrada[1])
        for x in range(12):
            if h in horas[x]:  
                saidaH = horas.index(horas[x])
        for x in range(60):
            if m in minutos[x]:  
                saidaM = minutos.index(minutos[x])
        saidaH = "0"+ str(saidaH) if len(str(saidaH)) == 1 else str(saidaH) #adiciona o 0 na frente para numero entre 0 e 9
        saidaM = "0"+ str(saidaM) if len(str(saidaM)) == 1 else str(saidaM)
        print(f"{saidaH}:{saidaM}")
    except EOFError:
        break