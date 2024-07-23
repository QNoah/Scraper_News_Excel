import requests
from bs4 import BeautifulSoup

cookies = "authId=bcc6b354-2e6e-433d-825a-0574cca5abf3; authId=bcc6b354-2e6e-433d-825a-0574cca5abf3; temptationTrackingId=ts-6666ccd8-7846-4ce7-ab55-55a873cee014; ak_bmsc=3BF77DCB2CBC48DC8B57E3AD37670CE6~000000000000000000000000000000~YAAQFSjdF9QgrruQAQAAj+XV4BjfN6aEi6MjsFtpPmuK3h/IyA1y2zM4EMSeTcZhDPJKFtoT7J5wu1KbGUnyv+jlsddwuWF7Igo5GNK6VSif2sJsv3C4yLBjfEqFcSU6IIIFe+ZoBt6Myj0Th3pk9wA33IQW0kyhdmrAJ9S/zU3qaba3gApFRjpC0vNv5JCsMCzuUWDGiE6w1tmpKbgXUZAt+Fn/Le67DYk331tIj72ltmoQDXgudDW5rjvkej2q2G9xlViOK4TE40TXW//metKPGfA23Sm7+PO1QXo+knHDmk0Kvomrool2znNX875B/1mHZF+nKCjaSKwp4y143RRt6kaRFoAwMuTe5hBsuXZrKHtYVvZVrCATWtNVKKFRONfsS1lJd8MnDgyfS5QQXOKpMw01suiUDd0a9YdyLBknXBU=; bm_sv=40F2C4707CFB9F3F374E43B218A86CB8~YAAQCijdF+Flbb+QAQAAHYnb4BiZm3fpeal5SgHEzyPKzMCjM9DFskeXzlw9gByJGzUrOFwgfRfuhFwCH9IZIj1uro7tA3iXz7fm1/AauvQHgtlytEdnIES36pM+f3ceJLfAOUadUGwOaB5MDrjSginGrYUUSDlHWFK2Lfuq7A18/Yn2GxNXhj/qCw/REHZptsdp8MfrIDVbgztSZ0PnbK/Vy7QR5M2E4YCK/00lc7joJRbjSJrp94f+BEbVQng=~1"

headers = {
    "Cookie": cookies.strip()
}

req = requests.get('https://www.ad.nl/net-binnen', headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')

print(soup)