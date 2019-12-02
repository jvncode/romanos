valores = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
valores5 = { 'V': 5,  'L': 50,  'D': 500 } 
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano: 
        #incrementamos el valor del número arábigo con el valor numérico del símbolo romano
        if letra in valores:
            numArabigo += valores[letra]
            if ultimoCaracter == '':
                pass
            elif ultimoCaracter == "(":
                ultimoCaracter = 0
            elif ultimoCaracter == ")":
                ultimoCaracter = 0
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1
                if letra in valores5:
                    return 0

                if numRepes > 3:
                    return 0


            elif valores[ultimoCaracter] < valores[letra]:
                if numRepes > 1: # No permite repeticiones en las restas
                    return 0

                if ultimoCaracter in valores5: #No permite restas de valores de 5 (5, 50, 500)
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de más de un orden
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter]*2
                numRepes = 1
        elif letra == "(":
            pass
        elif letra == ")":
            numArabigo = numArabigo*1000
            numRepes = 1
            
        else:  #si el simbolo romano no es permitido devolvemos error (0)
            return 0
        ultimoCaracter = letra

    return numArabigo

def arabigo_a_romano(numArabigo):

    numArabigo = str(numArabigo)
    numDigit = len(numArabigo)
    
    numRomano = []
 
    for digit in numArabigo:
        digit = int(digit)
        if numDigit == 1:
            if digit <= 3:
                numRomano.append(int(digit)*"I")
            elif digit == 4:
                numRomano.append("IV")
            elif digit == 5:
                numRomano.append("V")
            elif digit >= 6 and digit <=8:
                numRomano.append("V"+int(digit-5)*"I")
            elif digit == 9:
                numRomano.append("IX")
            numDigit -= 1
            
        if numDigit == 2:
            if digit <= 3:
                numRomano.append(int(digit)*"X")
            elif digit == 4:
                numRomano.append("XL")
            elif digit == 5:
                numRomano.append("L")
            elif digit >= 6 and digit <=8:
                numRomano.append("L"+int(digit-5)*"X")
            elif digit == 9:
                numRomano.append("XC")
            numDigit -= 1
        
        if numDigit == 3:
            if digit <= 3:
                numRomano.append(int(digit)*"C")
            elif digit == 4:
                numRomano.append("CD")
            elif digit == 5:
                numRomano.append("D")
            elif digit >= 6 and digit <=8:
                numRomano.append("D"+int(digit-5)*"C")
            elif digit == 9:
                numRomano.append("CM")
            numDigit -= 1
        
        if numDigit == 4:
            numRomano.append(int(digit)*"M")
            numDigit -= 1
            
        if numDigit == 0:
            numRomanoCont = "".join(numRomano)
            return numRomanoCont