def _parse_float(value):
    value = value.strip()
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


x1 = _parse_float(input("x1: ",))
y1 = _parse_float(input("y1: ",))
x2 = _parse_float(input("x2: ",))
y2 = _parse_float(input("y2: ",))
M1 = _parse_float(input("M1 (falls gegeben): ",))
M2 = _parse_float(input("M2 (falls gegeben): ",))
Fa1 = _parse_float(input("Kraft am Knoten 1: ",))
Fa2 = _parse_float(input("Kraft am Knoten 2: ",))

x = x1, y1
y = x2, y2
M = M1, M2
Fa = Fa1, Fa2
# Spiegelung eines Punktes an einem Mittelpunkt
if y[0] is None and y[1] is None and M is not None and x is not None:
    y = (x[0]+2*(M[0]-x[0]), x[1]+2*(M[1]-x[1]))
elif x[0] is None and x[1] is None and M is not None and y is not None:
    x = (y[0]+2*(M[0]-y[0]), y[1]+2*(M[1]-y[1]))
# Betrag des Vektors berechnen
def betrag1(x1, y1):
    return (x1**2 + y1**2)**0.5
def betrag2 (x2, y2):
    return (x2**2 + y2**2)**0.5
# Addition der Vektoren
def SummeVektoren(x1, x2, y1, y2):
    return (x1 + x2, y1 + y2)
# Subtraktion der Vektoren
def DifferenzVektoren(x1, x2, y1, y2):
    return (x1 - x2, y1 - y2)
# Skalarprodukt der Vektoren
def Skalarprodukt (x1, x2, y1, y2):
    return x1 * x2 + y1 * y2
# Verbindungsvektor 
def Verbindungsvektor(x1,y1,x2,y2):
    return (x2 - x1, y2 - y1)
verbindung = Verbindungsvektor(x[0],x[1],y[0],y[1])
# Mittelpunkt eines Vektors
def MittelpunktVektor(x1,y1,x2,y2,x=None):
    if x is not None:
        verbindung = Verbindungsvektor(x1, y1, x2, y2)
        mittelpunkt1 = x1+ 0.5*(verbindung [0])
        mittelpunkt2 = y1+ 0.5*(verbindung [1])
        mittelpunkt = (mittelpunkt1, mittelpunkt2)
        return mittelpunkt
    else:
        return None

    # Winkel zwischen 2 Vektoren
def WinkelZwischenVektoren(x1,y1,x2,y2):
    from math import acos, degrees
    skalarproduktoben = Skalarprodukt(x1,x2,y1,y2)
    betragunten1 = betrag1(x1,y1)
    betragunten2 = betrag2(x2,y2)
    if betragunten1 == 0 or betragunten2 == 0:
        return None
    cosa= skalarproduktoben / (betragunten1 * betragunten2)
    winkel = degrees(acos(cosa))
    return winkel
# Zug / Druck der Vektoren berechnen

def ZugDruck(x1,x2,y1,y2,Fa1,Fa2):
    betragverbindung = (((verbindung[0])**2)+((verbindung[1])**2))**0.5
    RiVe1 = verbindung[0] / betragverbindung
    RiVe2 = verbindung[1] / betragverbindung
    RiVe = (RiVe1, RiVe2)
    Dot = Fa1 * RiVe[0] + Fa2 * RiVe[1]
    return Dot
    
import matplotlib.pyplot as plt

# Plotten der Spiegelung eines Punktes an einem Mittelpunkt
if M[0] is not None and x[0]is not None and x[1] is not None and y[1] is None and y[0] is None:
    y_spiegel = (x[0]+2*(M[0]-x[0]), x[1]+2*(M[1]-x[1]))
    plt.quiver(0, 0, y_spiegel[0], y_spiegel[1], angles='xy', scale_units='xy', scale=1)
elif M[1] is not None and y[0]is not None and y[1] is not None and x[0]is None and x[1] is None:
    x_spiegel = (y[0]+2*(M[0]-y[0]), y[1]+2*(M[1]-y[1]))
    plt.quiver(0, 0, x_spiegel[0], x_spiegel[1], angles='xy', scale_units='xy', scale=1)
# Plotten der Vektoren

if x[0] is not None and x[1] is not None:
    plt.quiver(0, 0, x[0], x[1], angles='xy',scale_units='xy', scale=1)
if y[0] is not None and y[1] is not None:    
    plt.quiver(0, 0, y[0], y[1], angles='xy', scale_units='xy', scale=1)

# Plotten des Verbindungsvektors    
plt.quiver(x[0], x[1], verbindung[0], verbindung[1], angles='xy', scale_units='xy', scale=1, color='r')
# Plotten des Mittelpunkts
mittelpunkt = MittelpunktVektor(x[0],x[1],y[0],y[1],x)
plt.scatter(mittelpunkt[0], mittelpunkt[1])


    

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.show()

print("Punkt 1:", x)
print("Punkt 2:", y)
print("Betrag Vektor 1:", betrag1(x[0],x[1]))
print("Betrag Vektor 2:", betrag2(y[0],y[1]))
print("Summe der Vektoren:", SummeVektoren(x[0],y[0],x[1],y[1]))
print("Differenz der Vektoren:", DifferenzVektoren(x[0],y[0],x[1],y[1]))
print("Skalarprodukt der Vektoren:", Skalarprodukt(x[0],y[0],x[1],y[1]))
print("Verbindungsvektor XY:", Verbindungsvektor(x[0],x[1],y[0],y[1]))
print("Mittelpunkt des Vektors:", MittelpunktVektor(x[0],x[1],y[0],y[1],x))
print("Winkel zwischen den Vektoren:", WinkelZwischenVektoren(x[0],x[1],y[0],y[1])) 
dot = ZugDruck(x1,x2,y1,y2,Fa1,Fa2)
if dot > 0:
    print("Es herrscht am Stab eine Zugkraft")
elif dot(x1,x2,y1,y2,Fa1,Fa2) < 0:
    print("Es herrscht am Stab eine Druckkraft")
else:
    print("Keine Stabkraft")  
print("Kraft am Stab:", ZugDruck(x[0],x[1],y[0],y[1],Fa[0],Fa[1]))  