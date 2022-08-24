import time
from datetime import datetime
from urllib.request import urlopen
import smtplib, ssl

def doge():
    global dogeprice
    global timestampStr
    global dogestamp

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    time.sleep(1)
    url = "https://robinhood.com/crypto/DOGE"
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    title_index = html.find("atomic")
    start_index = title_index + len("<span class>")
    end_index = html.find("<span class>")
    title = html[start_index:end_index]

    title = title.replace('"', "")
    title.split(" ")

    dogeprice = title[13:22]
    dogeprice = float(dogeprice)
    print()

    dogestamp = timestampStr, "|", dogeprice
    print(dogestamp)

while True:
    doge()

    if dogeprice >= 0.315000 or dogeprice <= 0.30000:
        import yagmail
        yag = yagmail.SMTP('email@email.com', 'password')
        contents = "Time of DOGE price: " + timestampStr, "DOGE Price: $" +str(dogeprice)
        yag.send('email@email.com', 'subject', contents)
        print("Email alert sent!")
        time.sleep(1800)

  
    else:
        print("Updating price...")
        doge()
