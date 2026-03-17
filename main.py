import flet as ft
from controller import Controller
from view import View

def main(page: ft.Page):
    v = View(page) # crea view
    c = Controller(v) # crea controller
    v.setController(c) # fa comunicare view e controller
    v.caricaInterfaccia() # scrive controlli interaccia

ft.app(target=main)