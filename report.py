import PySimpleGUI as sg
import requests
from error import error

def report(ip):
    layout = [
        [sg.Text("IP Search")],
        [sg.Text("IP:"), sg.InputText(f"{ip}")],
        [sg.Text("Categories:"), sg.InputText()],
        [sg.Text("Comment:"), sg.InputText()],
        [sg.Button("Report"), sg.Button("Exit")]
    ]

    window = sg.Window("IP Search", layout, icon="favicon.ico")

    while True:
        event, values = window.read()

        if event == "Report":
            try:
                url = 'https://api.abuseipdb.com/api/v2/report'

                params = {
                    'ip': f'{values[0]}',
                    'categories': f'{values[1].replace(" ", "")}',
                    'comment': f'{values[2]}'
                }

                headers = {
                    'Accept': 'application/json',
                    'Key': '3fe25b75168ddb506e9026fb30db623f9cfaf2fbdbf1567f6ef6735754bf420642f58c0ae853ba2c'
                }

                response = requests.request(method='POST', url=url, headers=headers, params=params)
                print(response)
            except:
                error()

        if event == "Exit":
            break

    window.close()