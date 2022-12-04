import PySimpleGUI as sg

def error():
    layout = [
        [sg.Text("IP SEARCH")],
        [sg.Text("Something don't work correctly, verify if the ip exists and if you are connected in the internet")],
        [sg.Button("Sair")]
    ]

    window = sg.Window("IP Search", layout, icon="favicon.ico")

    while True:
        event, values = window.read()

        if event == "Sair":
            break

    window.close()