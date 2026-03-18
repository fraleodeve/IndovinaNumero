from view import View
from model import Model
import flet as ft

class Controller(object): # metodi che interagiscono con view e modello
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNmax(self):
        return self._model.Nmax # dopo aver creato property in model

    def getTmax(self):
        return self._model.Tmax

    def reset(self, e): # e = evento che ha generato pressione pulsante
        self._model.reset() # resetto stato gioco lato modello

        # interfaccia tra view e modello (tentativo)
        self._view.txtT.value = self._model.T # potrei mettere anche 6

        # pulire ListView, togliere elementi partita precedente
        self._view._lvoOut.controls.clear()

        # diciamo all'utente che può giocare
        self._view._lvoOut.controls.append(
            ft.Text("Inizia il gioco! Indovina il numero a cui sto pensando.")
        )

        # aggiorno interfaccia grafica
        self._view.update()

    def play(self, e):
        # valore in input
        tentativoStr = self._view._txtInTentativo.value

        # aggiornare tentativi rimanenti
        # self._view.txtT.value = self._model.T

        # convertire in intero
        try: # tutti i controlli dei dati in input devono essere fatti nel controller
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvoOut.controls.append(
                ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()
            return

        # posso giocare, passo valore a model, che mi restituisce -1, 0, 1, o 2
        risultato = self._model.play(tentativo)

        # gestisco risultato
        if risultato == 0:
            self._view._lvoOut.controls.append(ft.Text(f"Hai vinto! Il valore corretto era: {tentativo}", color = "green"))
            self._view.update()
            return

        elif risultato == 2:
            self._view._lvoOut.controls.append(ft.Text(f"Hai perso! Il valore corretto era: {self._model.segreto}", color = "red"))
            self._view.update()
            return

        elif risultato == -1:
            self._view._lvoOut.controls.append(ft.Text(f"Ritenta! Il numero è più piccolo di {tentativo}"))
            self._view.update()
            return

        elif risultato == 1:
            self._view._lvoOut.controls.append(ft.Text(f"Ritenta! Il numero è più grande di {tentativo}"))
            self._view.update()
            return

        else:
            return

