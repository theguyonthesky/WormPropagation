import random
import numpy as np
import matplotlib.pyplot as plt


Totvulnip = 1000
totsimsteps = 10000 
runs = 3
OMEGA = 100000
SCAN_RATE = 3

#define the initip function
def initip():
    addressspcip = ['immune' for i in range(OMEGA+1)]
    for i in range(int(1000/10)):
        for j in range(1, 11):
            addressspcip[j + (i * 1000)] = 'vulnerable'
    return addressspcip

#define the getlocip function
def getlocip(addressstip):
    localip = []
    for ip in range(OMEGA):
        if addressstip[ip] == 'infected':
            for _ in range(SCAN_RATE):
                if ip <= 10:
                    rule = np.random.choice(['rule1', 'rule2'], 1, p=[0.8, 0.2])
                    if rule == 'rule1':
                        infctip = random.sample(range(1, ip + 1 + 10), 1)
                    elif rule == 'rule2':
                        infctip = random.sample(range(1, OMEGA + 1), 1)
                elif ip >= (OMEGA - 10):
                    rule = np.random.choice(['rule1', 'rule2'], 1, p=[0.8, 0.2])
                    if rule == 'rule1':
                        infctip = random.sample(range(ip - 10, OMEGA + 1), 1)
                    elif rule == 'rule2':
                        infctip = random.sample(range(1, OMEGA + 1), 1)
                else:
                    rule = np.random.choice(['rule1', 'rule2'], 1, p=[0.8, 0.2])
                    if rule == 'rule1':
                        infctip = random.sample(range(ip - 10, ip + 1 + 10), 1)
                    elif rule == 'rule2':
                        infctip = random.sample(range(1, OMEGA + 1), 1)
                localip.append(infctip[0])
    return localip

#define the worm_propogation function
def worm_propagation(addressstip, mainMethod):
    infctipCntDscrt = []
    numofinfctips = 1
    for tick in range(totsimsteps):
        numOfIpsForScan = numofinfctips * SCAN_RATE
        if mainMethod == 'random_scan':
            infectedIps = random.sample(range(1, OMEGA + 1), numOfIpsForScan)
        elif mainMethod == 'local_preference':
            infectedIps = getlocip(addressstip)
        for ip in infectedIps:
            if addressstip[ip] == 'vulnerable':
                addressstip[ip] = 'infected'
                numofinfctips += 1
                if numofinfctips == Totvulnip:
                    break

        if (tick + 1) % 100 == 0:
            print("Time steps: {0} ---- Infected IPs: {1}".format(tick + 1, numofinfctips))
        infctipCntDscrt.append(numofinfctips)
        if numofinfctips == Totvulnip:
            print("Time steps: {0} ---- Infected IPs: {1}. \nAll IPs infected!!!".format(tick + 1,
                                                                                              numofinfctips))
            break
    return infctipCntDscrt

#define the plotsim function
def plotsim(count, run):
    plt.plot(count, "-", label="Run #{}".format(run + 1)) 

#define the worm_propogation_simulation function
def worm_propagation_simulation(mainMethod, plot=False):
    for run in range(runs):
        print("\n ****** {} Scan Worm Propagation: Run{} ******".format(mainMethod, run+1))
        addressstip = initip()
        addressstip[1001] = 'infected'
        infctipCntDscrt = worm_propagation(addressstip, mainMethod)
        if plot:
            plotsim(infctipCntDscrt, run)
    if plot:
        plt.xlabel("Time tick")
        plt.ylabel("Number of infected computers")
        plt.title("{}: 3 Simulation Runs of Worm Propagation".format(mainMethod))
        plt.legend()
        plt.show()

#define the main function
def main():
    random.seed(1)
    mainMethods = ['random_scan']
    for mainMethod in mainMethods:
        worm_propagation_simulation(mainMethod, plot=False)


main()