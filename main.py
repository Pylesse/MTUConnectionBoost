from os import system

input("This programm need to be administrator so relaunch in administrator or continue with enter..")
mtu_value = input("Enter your MTU : ")
plat = input("Your connection is in Wifi (w) or in ethernet (e) ? ")
if plat == "w":
    print("Please wait for boost...")
    system(
        f'netsh int ipv4 set subinterface "Wi-Fi" mtu={mtu_value} store=persistent')
elif plat == "e":
    print("Please wait for boost...")
    system(
        f'netsh int ipv4 set subinterface "Ethernet" mtu={mtu_value} store=persistent')
else:
    input("I don't understand please relaunch software...")
    exit(0)

input("Ok. So press enter for reboot your computer..")
system("shutdown -r -t 0")
