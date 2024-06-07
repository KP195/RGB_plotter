import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image as im  



pic=im.open("Bayern_Simssee_edit.png") #Abbildung 1 einlesen

dimX=pic.size[0]; #Breite bzw. x-Dimension von Abbildung 1
dimY=pic.size[1]; #Höhe bzw. y-Dimension von Abbildung 2

rows=[] #array zur Speicherung der Blau-Werte des RGB-Anteils


# Erstellen von x- und y-Daten
x = np.arange(0,dimX) #Erstellen eines eindimensionalen Arrays der Länge dimX


y = np.arange(0,dimY,1) #Erstellen eines eindimensionalen Arrays der Länge dimY
x, y = np.meshgrid(x, y) #Erstellen zweier zweidimensionaler Arrays, die als Koordinaten für die z-Koordinate, welche dem Blau-Anteil
                        # des RGB-Farbkanals entspricht, dienen. Somit bemisst sich die Position des von matplotlib zu zeichnenden Pixels
                        # anhand der x-y-Position in der xy-Ebene. Die Höhe des zu zeichnenden Elements entspricht dem Blau-Anteil des
                        # Pixel an der entsprechenden x-y-Position der Satellitenaufnahme. 
                        

for i in range(0,dimY): # Die äußere Schleife läuft von 0 bis dimY - Höhe des Bildes.
    
    newXRow=[] # lokae Variable zur Speicherung der jeweils aktuellen Pixelzeile
 
    for j in range(0,dimX): # Die innere Schleife läuft von 0 bis dimX - der Breite des Bildes. Äußere und innere Schleife ermöglichen
                            # ein zeilenweises Abrastern eines jeden Pixel der Satellitenaufnahme.
        
        newXRow.append(pic.getpixel((j,i))[2])  #Blau-Wert aus RGB-Werten extrahieren und newXRow hinzufügen:
                                                # Die RGB-Werte werden als dreitwertiges Tupel von der Funktion getPixel() 
                                                #zurück gegeben, weshalb bei der vorliegende 0-basierenden Arrayreferenzierung mit
                                                # [2] auf den Blau-Wert bzw. dem dritten Wert des Tupels zugegriffen wird. 
                                                
        
    
  
    rows.append(newXRow)# Ein Durchlauf in der äußeren Schleife entspricht einer abgearbeiteten x-Pixelreihe.
   
np_Array_Colors=np.array(rows)#np_Array_Colors enthält ein Array,das die Blau-Werte eines jeden Pixels der Satellitenaufnahme enthält. 


# Korrigieren der Orientierung durch Umdrehen der y-Achse
np_Array_Colors = np.flipud(np_Array_Colors)#

# Erstellen der Figur und der 3D-Achsen
fig = plt.figure()#plt.figure() liefert ein Objekt, welches das Fenster zum Plotten einer oder mehrere Plots repräsentiert. 
ax = fig.add_subplot(111, projection='3d') # ax enthält hier ein Objekt, das den visuellen Bereich repräsentiert, in welchem der Graph gezeichnet wird. 
                                            # Der Parameter "111" steht dafür, dass sich der Plot in einer Reihe
                                            # mit einer Spalte an der Indexposition eins befindet --> "111". 
                                            # Der zweite Parameter meint, dass ein 3D-Plot erstellt wird.


#Erstellen eines 3D-Terrain-Plots
#surface entspricht einem Objekt, welches den Plot selbst repräsentiert, und damit in ax eingebettet ist.
# Das cmap-Argument definiert das zu nutzende Farbschema, edgecolor ermöglch die Angabe einer Kantenfarbe zwischen den einzelnen
#vom Plot zu zeichnenden Datenpunkten.

surface = ax.plot_surface(x, y, np_Array_Colors, cmap='terrain', edgecolor='none')

# Hinzufügen einer Farbleiste für ax: Übergabe der Objekte "surface" und "ax" an die Funktion "colorbar", shrink beschreibt
# die Höhe der Farbleiste im Vergleich zur Höhe der Achse "ax", "aspect" bezieht sich auf das Verhältnis von Höhe zur Breite der Farbleiste.
fig.colorbar(surface, ax=ax, shrink=0.6, aspect=5)


ax.set_title('Simssee') #Titel von ax
ax.set_xlabel('Breite: West-Ost')# Beschriftung der x-Achse von ax
ax.set_ylabel('Länge: Nord-Süd') #Beschriftung der y-Achse von ax
ax.set_zlabel('RGB: Blau') #Beschriftung der z-Achse von x

# Anzeigen des Plots
plt.show()
