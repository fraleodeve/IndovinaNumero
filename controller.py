from view import View
from model import Model
import flet as ft
import math as m

class Controller(object): # metodi che interagiscono con view e modello
    def __init__(self, view: View):
        self._view = view
        self._model = Model()
        self.listaTentativi = []

    def getNmax(self):
        return self._model.Nmax # dopo aver creato property in model

    def getTmax(self):
        return self._model.Tmax

    def modalita(self, e):
        if self._view._modalita.value == "Facile":
            self._model._Nmax = 50
            self._model._Tmax = round(m.log2(50))
            self._model._T = round(m.log2(50))

            self._view.txtNmax.value = 50
            self._view.txtTmax.value = round(m.log2(50))
            self._view.txtT.value = round(m.log2(50))

            self._model.reset()  # resetto stato gioco lato modello
            self._view.update()
            return

        elif self._view._modalita.value == "Medio":
            self._model._Nmax = 100
            self._model._Tmax = round(m.log2(100))
            self._model._T = round(m.log2(100))

            self._view.txtNmax.value = 100
            self._view.txtTmax.value = round(m.log2(100))
            self._view.txtT.value = round(m.log2(100))

            self._model.reset()  # resetto stato gioco lato modello
            self._view.update()
            return

        elif self._view._modalita.value == "Difficile":
            self._model._Nmax = 200
            self._model._Tmax = round(m.log2(200))
            self._model._T = round(m.log2(200))

            self._view.txtNmax.value = 200
            self._view.txtTmax.value = round(m.log2(200))
            self._view.txtT.value = round(m.log2(200))

            self._model.reset()  # resetto stato gioco lato modello
            self._view.update()
            return

    def assistenza(self, e):
        if self._view._assistita.value == "Si":
           self._view.aggiuntaAssistenza()
           return


    def reset(self, e): # e = evento che ha generato pressione pulsante
        # interfaccia tra view e modello (tentativo)

        self._view._modalita.value = None
        self._view._assistita.value = None
        self._view.txtNmax.value = ""
        self._view.txtTmax.value = ""
        self._view.txtT.value = ""
        self._view._pb.value = 0
        self._view._row5.controls.clear()

        # pulire ListView, togliere elementi partita precedente
        self._view._lvoOut.controls.clear()

        # diciamo all'utente che può giocare
        self._view._lvoOut.controls.append(
            ft.Text("Inizia il gioco! Indovina il numero a cui sto pensando.")
        )

        # aggiorno interfaccia grafica
        self._view.update()

    def play(self, e):
        if self._view._modalita.value == None or self._view._assistita.value == None:
            self._view._lvoOut.controls.clear()
            self._view._lvoOut.controls.append(ft.Text("Attenzione! Campo mancante"))
            self._view._lvoOut.update()
            return

        # valore in input
        tentativoStr = self._view._txtInTentativo.value

        # convertire in intero
        try: # tutti i controlli dei dati in input devono essere fatti nel controller
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvoOut.controls.append(
                ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()
            return

        if tentativo in self.listaTentativi:
            self._view._lvoOut.controls.append(ft.Text("Attenzione! Numero già inserito"))
            self._view._lvoOut.update()
            return
        else:
            self.listaTentativi.append(tentativo)

        # aggiornare tentativi rimanenti
        self._view.txtT.value = self._model.T - 1
        self._view._pb.value = (6 - (self._model.T - 1)) / 6
        self._view.update()

        # posso giocare, passo valore a model, che mi restituisce -1, 0, 1, o 2
        risultato = self._model.play(tentativo)
        self._view._txtInTentativo.value = ""

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
            self._view.fine.value = tentativo-1
            self._view.update()
            return

        elif risultato == 1:
            self._view._lvoOut.controls.append(ft.Text(f"Ritenta! Il numero è più grande di {tentativo}"))
            self._view.inizio.value = tentativo+1
            self._view.update()
            return

        else:
            return

