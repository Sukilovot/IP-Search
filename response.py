import PySimpleGUI as sg

def main(response):
    layout = [
        [sg.Text("IP: {}".format(response["ipAddress"]))],
        [sg.Text("Public: {}".format(response["isPublic"]))],
        [sg.Text("Version: {}".format(response["ipVersion"]))],
        [sg.Text("Is in white list: {}".format(response["isWhitelisted"]))],
        [sg.Text("Abuse confidence store: {}".format(response["abuseConfidenceScore"]))],
        [sg.Text("Contry code: {}".format(response["countryCode"]))],
        [sg.Text("Usage type: {}".format(response["usageType"]))],
        [sg.Text("Internet service provider: {}".format(response["isp"]))],
        [sg.Text("Domain: {}".format(response["domain"]))],
        [sg.Text("Hostnames: {}".format(response["hostnames"]))],
        [sg.Text("Total reports: {}".format(response["totalReports"]))],
        [sg.Text("Numbers of distinct users: {}".format(response["numDistinctUsers"]))],
        [sg.Text("Last reported at: {}".format(response["lastReportedAt"]))],
        [sg.Button("Sair")]
    ]

    window = sg.Window("IP Search", layout, icon="favicon.ico")

    while True:
        event, values = window.read()

        if event == "Sair":
            break

    window.close()