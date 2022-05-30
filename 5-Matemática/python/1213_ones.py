while True:
    numeros = []
    try:
        numeros.append(int(input()))   
    except EOFError:
        for y in range(len(numeros)):    
            x = 0  
            compara = 0 
            while True:
                x += 1
                compara = int(x*'1')
                if compara % numeros[y] == 0:
                    print(len(str(compara)))
                    break