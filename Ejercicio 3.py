v1= float(input("Ingrese el voltaje 1: "))
v2= float(input("Ingrese el voltaje 2: "))
v3= float(input("Ingrese el voltaje 3: "))

promedio= (v1+ v2+ v3)/3

if promedio < 115: 
    print("Voltaje Correcto")

elif promedio > 115 and promedio < 220:
    print ("Alto Voltaje")

else: 
    print("Peligro")
    
