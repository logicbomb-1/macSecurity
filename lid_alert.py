import psutil
import os
import subprocess
import requests

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Sms function
def sms():
    headers = {
    'Authorization': 'Bearer c45255********ec3aab38',
    'Content-Type': 'application/json',
    }

    data = '\n  {\n    "from": "447537432321",\n    "to": [ "919650754366" ],\n    "body": "Someone has tried to open your laptop"\n  }'

    response = requests.post('https://sms.api.sinch.com/xms/v1/cba25879c63f4c61a09a6587ef0acb4c/batches', headers=headers, data=data)


def pic():
    command = "/ImageSnap-v0.2.5/imagesnap > /dev/null 2>&1;"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    out = out.strip()
    print out

# Check process access camera
def check_lid():
    FLAG = 0
    outp = "Yes"
    command = "ioreg -r -k AppleClamshellState -d 4 | grep AppleClamshellState  | head -1 | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    out = out.strip()
    if (FLAG == 0 and out == "No"):
        check_lid()
    else:
        if outp == "Yes":
            while outp != "No":
                command = "ioreg -r -k AppleClamshellState -d 4 | grep AppleClamshellState  | head -1 | awk '{print $4}'"
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                outp, err = process.communicate()
                outp = outp.strip()

        notify(title = 'Warning',
            subtitle = "Someone try to open your lid",
            message = "Taking the snap")
        sms()
        pic()
    check_lid()
    
    
if __name__ == '__main__':
    check_lid()
