import PySimpleGUI as sg
import requests
from error import error
from response import main

sg.change_look_and_feel("Black")

user_ip = requests.get("https://api.ipify.org/").text
print("User ip: {}".format(user_ip))

layout = [
    [sg.Text("IP SEARCH")],
    [sg.Text("API provided by: www.abuseipdb.com")],
    [sg.Text("Write the IP: "), sg.InputText()],
    [sg.Text("Your ip: {}".format(user_ip))],
    [sg.Button("Search"), sg.Button("Create txt", key="txt"), sg.Button("Exit")],
    [sg.Text("")],
    [sg.Text("Dev: PHC")]
]

window = sg.Window("IP Search", layout, icon="favicon.ico")

while True:
    event, values = window.read()

    if event == "Exit":
        break

    if event == "Search":
        try:
            url = 'https://api.abuseipdb.com/api/v2/check'

            querystring = {
                'ipAddress': values[0],
                'maxAgeInDays': '90'
            }

            headers = {
                'Accept': 'application/json',
                'Key': '3fe25b75168ddb506e9026fb30db623f9cfaf2fbdbf1567f6ef6735754bf420642f58c0ae853ba2c'
            }

            response = requests.request(method='GET', url=url, headers=headers, params=querystring).json()["data"]

            # formating datas (ignore)
            if response["isPublic"] == True:
                response["isPublic"] = "Yes"
            else:
                response["isPublic"] = "No"

            if response["isWhitelisted"] == None:
                response["isWhitelisted"] = "No"
            else:
                response["isWhitelisted"] = "Yes"

            main(response)
        except:
            error()

    if event == "txt":
        try:
            url = 'https://api.abuseipdb.com/api/v2/check'

            querystring = {
                'ipAddress': values[0],
                'maxAgeInDays': '90'
            }

            headers = {
                'Accept': 'application/json',
                'Key': '3fe25b75168ddb506e9026fb30db623f9cfaf2fbdbf1567f6ef6735754bf420642f58c0ae853ba2c'
            }

            response = requests.request(method='GET', url=url, headers=headers, params=querystring).json()["data"]

            # formating datas (ignore)
            if response["isPublic"] == True:
                response["isPublic"] = "Yes"
            else:
                response["isPublic"] = "No"

            if response["isWhitelisted"] == None:
                response["isWhitelisted"] = "No"
            else:
                response["isWhitelisted"] = "Yes"

            txt = open(str(response["ipAddress"]) + ".txt", "w").write(f"IP SEARCH\n===\nIP: {response['ipAddress']}\nPublic: {response['isPublic']}"
            f"\nVersion: {response['ipVersion']}\nWhite listed: {response['isWhitelisted']}\nAbuse confidence store: {response['abuseConfidenceScore']}\nCountry code: {response['countryCode']}\nUsage type: {response['usageType']}\nISP: {response['isp']}\nDomain: {response['domain']}\nHost names: {response['hostnames']}\nTotal reports: {response['totalReports']}\nNumbers of distinct users: {response['numDistinctUsers']}\nLast report at: {response['lastReportedAt']}")
        except:
            error()

window.close()
