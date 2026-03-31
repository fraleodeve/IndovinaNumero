import flet as ft

class View(object): # campi necessari, crea pagina con titolo
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2026 - Indovina il Numero" # titolo in alto alla pagina
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None # fissata a None, poi dopo la carica

    def caricaInterfaccia(self): # definizione oggetti grafici (pulsanti, textField, ...)
        self._titolo = ft.Text("Indovina il numero", color="blue", size=24)

        # dobbiamo mettere 4 caselle di testo (alcune modificabili, altre no) e 2 pulsanti

        # visualizza numero massimo
        self.txtNmax = ft.TextField(label = "Numero massimo",  # label è ciò che visualizzo sopra
                                    # value = self._controller.getNmax(), # chiedo a controller, non può parlare direttamente con model
                                    disabled = True # serve affinché non sia modificabile
                                    )

        # visualizza numero tentaivi massimo
        self.txtTmax = ft.TextField(label = "Numero tentativi massimo",
                                    # value = self._controller.getTmax(),
                                    disabled = True
                                    )

        # visualizza tentativi rimanenti
        self.txtT = ft.TextField(label = "Tentativi rimanenti", # value non lo sappiamo ancora
                                 disabled = True
                                 )


        # metto elementi su una riga
        #self._row1 = ft.Row(controls = [self.txtNmax, self.txtTmax, self.txtT]) # si aspetta lista di controlli

        # inserire il tentativo
        self._txtInTentativo = ft.TextField(label = "Valore") # non sappiamo valore; di default disabled è false

        # pulsanti, bottoni
        self._btnReset = ft.ElevatedButton(text = "Nuova partita",
                                           on_click = self._controller.reset)
        # on click serve per chiamare funzione, senza le parentesi tonde (nome metodo, non chiamata)

        self._btnPlay = ft.ElevatedButton(text = "Indovina",
                                          on_click = self._controller.play)

        # metto elementi su una riga
        #self._row2 = ft.Row(controls = [self._txtInTentativo, self._btnReset, self._btnPlay])

        # devo inserire stringhe che dicono se maggiore o minore -> listView (contenitore in cui si stampano stringhe)
        self._lvoOut = ft.ListView(expand = True) # true così si può scrollare
        # al momento vuoto, lo riempio dopo

        # aggiungo elementi alla pagina
        #self._page.add(self._row1) # add sia aggiunge alla pagina sia la aggiorna
        #self._page.add(self._row2) # volendo anche nello stesso add
        #self._page.add(self._lvoOut)

        # progressBar
        self._pb = ft.ProgressBar(width=500, value = 0, color = "red")

        # modalita
        self._modalita = ft.Dropdown(label="Selezionare il livello di difficoltà", options=[
            ft.dropdown.Option("Facile"),
            ft.dropdown.Option("Medio"),
            ft.dropdown.Option("Difficile")
        ], on_change=self._controller.modalita,
                                     width=300)

        # assistenza
        self._assistita = ft.Dropdown(label="Modalità assistita", options=[
            ft.dropdown.Option("Si"),
            ft.dropdown.Option("No"),
        ], on_change=self._controller.assistenza,
                                     width=300)

        self._row = ft.Row(controls=[self._btnReset], alignment="center")
        self._row0 = ft.Row(controls=[self._modalita, self._assistita], alignment="center", spacing=100)
        self._rowspazio = ft.Row(controls=[], height = 25)
        self._row1 = ft.Row(controls=[self.txtNmax], alignment="center")
        self._row2 = ft.Row(controls=[self.txtT, self.txtTmax], alignment="center")
        self._row3 = ft.Row(controls=[self._txtInTentativo, self._btnPlay], alignment="center")
        self._row4 = ft.Row(controls=[self._pb], alignment="center")
        self._row5 = ft.Row(controls=[], alignment="center")
        self._page.add(self._row, self._row0, self._rowspazio,
                       self._row1, self._row2, self._row4, self._rowspazio,
                       self._row3, self._rowspazio,
                       self._row5, self._rowspazio,
                       self._lvoOut)


        self._page.update() # aggiorna

    def setController(self,controller): # far conoscere view e controller
        self._controller = controller

    def update(self): # aggiorna interfaccia grafica e modifica contenuto
        self._page.update() # solo dentro view -> per passare a controller

    def aggiuntaAssistenza(self):
        self.inizio = ft.TextField(label="Da",
                                   value="1",
                                   disabled=True
                                   )
        self.fine = ft.TextField(label="A",
                                 value=self.txtNmax.value,
                                 disabled=True
                                 )
        self._row5.controls.append(self.inizio)
        self._row5.controls.append(self.fine)
        self.update()