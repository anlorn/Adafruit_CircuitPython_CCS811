import time
import board
import busio
import adafruit_ccs811

i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c)

try:
    f = open("baseline", "r")
    current_baseline = int(f.read())
except:
    current_baseline = 99999999

# Wait for the sensor to be ready
while not ccs811.data_ready:
    pass

while True:
    print("CO2: {} PPM, TVOC: {} PPB".format(ccs811.eco2, ccs811.tvoc))
    time.sleep(0.5)
    new_baseline = ccs811.baseline
    if new_baseline < current_baseline:
        f = open("baseline", "w")
        f.write(str(new_baseline))
        f.close()
        current_baseline = new_baseline
        print("write")
    print(current_baseline)
