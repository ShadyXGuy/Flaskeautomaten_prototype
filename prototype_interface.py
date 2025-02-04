import automat

# Denne funktion samler al information til brugeren i en tekst
def generer_bruger_info():

    return generer_flaske_info()

# Denne funktion genererer information om sessionens afleverede flasker
def generer_flaske_info():
    return automat.session

# Denne funktion genererer teksten til udskrift på kvittering
def generer_kvittering_tekst():
    out = ''
    for type in automat.pantdata.keys():
        if type in automat.session:
            out += str(automat.pantdata[type]['info'] + ' ')
            out += str(automat.session.count(type)) + 'X' + str(automat.pantdata[type]['takst']) + ' kr.\n'
    out += str(automat.beregn_session_total())

#skal være rekusiv funktion
    out = limitLineLen(out, 50)
def limitLineLen(out, lineLim):
    for line in out.split('\n'):
        if len(line)>lineLim:
            for newBreak in range(lineLim, 0, -1):
                if line[newBreak]==' ':
                    fixedLine=line[:newBreak].strip()+'\n'+line[newBreak:].strip()
                    fixedLine = limitLineLen(fixedLine, lineLim)
                    break
            out = out.replace(line,fixedLine)
    return out


if __name__ == '__main__':
    aktiv = True
    automat.opstart()
    while aktiv:
        print(str(generer_bruger_info())+' I alt er der: '+ str(len(generer_bruger_info())))
        print('Værdi i kr. '+ str(automat.beregn_session_total()))
        # Simuleret pantindkast/udbetal-tryk
        handling = input('Indkast pant eller udbetal. ')

        if handling == 'udbetal':
            #if len(generer_kvittering_tekst()) > 50:
                #False
            #else:
                print(generer_kvittering_tekst())
                automat.udbetal()

        elif (handling.upper() in automat.pantdata.keys()):
            automat.modtag(handling)

        elif handling == 'shutdown':
            if input('Nedlukningskode? ') == automat.nedlukningskode:
                aktiv = False

        elif handling == 'reboot':
            if input('Nedlukningskode? ') == automat.nedlukningskode:
                automat.reboot()

        else:
            print('Handling ikke mulig.')