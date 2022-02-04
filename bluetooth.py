import bluetooth as bt
import time

def scan():

    print("Scanning for bluetooth devices:")

    devices = bt.discover_devices(lookup_names = True, lookup_class = True)

    number_of_devices = len(devices)

    print(number_of_devices,"devices found")

    for addr, name, device_class in devices:

        print("\n")

        print("Device:")

        print("Device Name: %s" % (name))

        print("Device MAC Address: %s" % (addr))



scan()

socket = bt.BluetoothSocket(bt.RFCOMM)
socket.connect(("08:DF:1F:BD:D0:98", 1)) ## Changer l'addresse MAC pour celle de l'enceinte que l'on veut connecter