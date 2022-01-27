
from HTU2X import HTU21D
import time

htu = HTU21D(22,21)

while True:
    messwertTemperatur = round(htu.temperature,1)
    print("Aktuelle Temperatur:", messwertTemperatur, "gradC")

    messwerteLuftfeuchte = round(htu.humidity,1)
    print("Aktuelle Luftfeuchigkeit:", messwerteLuftfeuchte, "%")

    time.sleep(5)