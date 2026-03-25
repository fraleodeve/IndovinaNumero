import random

class Model(object): # implementa logica (fatta nei laboratori precedenti)

    # due possibilità: nuova partita o verifica numero
    def __init__(self):
        self._Nmax = None # valore massimo da indovinare
        self._Tmax = None # numero max tentatuvi
        self._T = None # tentativi rimanenti
        self._segreto = None # numero da indovinare (cambia ogni partita)

        #sei un bullo! (oggi no) Grazie, non ancora, ah ecco, mi sembrava strano

    def reset(self): # per creare partita (setta la scelta), resetta stato gioco
        """
        Questo metodo resetta stato del gioco. Imposta il numero da indovinare e ripristina numero di tentativi
        :return:
        """
        self._segreto = random.randint(1, self._Nmax) # crea valore randomico, da indovinare
        # self._T = self._Tmax # tutti tentativi rimasti (vite tutte); ripristina tentativi
        print(f"Il numero segreto è: {self._segreto}") # importante fare prove intermedie

    def play(self, tentativo): # prende in input tentativo dell'utente
        """
        Questo metodo riceve come argomento un valore intero, che sara il tentativo del giocatore,
        e lo confronta con il segreto
        :return:
        -1 se il segreto è più piccolo del tentativo
        0 se il tentativo è uguale al segreto
        1 se segreto è più grande del tentativo
        2 se non ho più tentativi disponibili
        """

        self._T -= 1

        if tentativo == self._segreto: # ho indovinato
            """ho vinto!"""
            return 0 # esco

        if self._T == 0: # prima verifico che ci sia ancora tentativi possibili
            """allora non ho più vite, non posso più giocare"""
            return 2 # esco

        if tentativo > self._segreto:
            """il tentativo dell'utente è più grande del segreto"""
            return -1
        else:
            return 1

    @property # dobbiamo chiamare Nmax in controller ma ha l' underscore -> quindi creo getter
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto


# testo metodo, faccio prova intermedia per verificare che reset funzioni
if __name__ == '__main__':
    m = Model()
    m.reset() # resetto modello
    print(m.play(50))
    print(m.play(30))
    print(m.play(20))
    print(m.play(10))
    print(m.play(5))
    print(m.play(3))
    print(m.play(4)) # ne metto più di 6 per verificare
