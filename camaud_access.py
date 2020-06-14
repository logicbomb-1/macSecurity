import psutil
import os
import subprocess


# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


# Check process access camera
def check_cam():
    command = "lsof | grep AppleCamera | awk '{print $1,$2}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    print out
    notify(title = 'Warning',
            subtitle = "Process accessing your webcam",
            message = out)
    check_cam()


# Check process accessing audio
def check_audio():
    command = "lsof | grep CoreAudio.component | awk '{print $1,$2}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    print out
    notify(title = 'Warning',
            subtitle = "Process accessing your audio",
            message = out)

if __name__ == '__main__':
    check_cam()
    check_audio()

