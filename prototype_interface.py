import automat

# Denne funktion samler al information til brugeren i en tekst
def generer_bruger_info():

    return generer_flaske_info()

# Denne funktion genererer information om sessionens afleverede flasker
def generer_flaske_info():
    return automat.session

# Denne funktion genererer teksten til udskrift på kvittering
def generer_kvittering_tekst():
    for type in automat.pantdata.keys():
        if type in automat.session:
            print(automat.pantdata[type]['info'] + ' ' + str(automat.session.count(type)) + ' x ' + str(automat.pantdata[type]['takst']) + 'kr.')
    out = ''
    for type in automat.pantdata.keys():
        out += type
        out += str(automat.session.count(type))
        out += automat.session.count(type) * str(automat.pantdata[type]['takst'])
    return print('total værdi udbetalt ' + str(automat.beregn_session_total()) + 'kr.')


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