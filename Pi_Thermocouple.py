import piplates.THERMOplate as THERMO
import time

THERMO.setSCALE('c') 

while(1):
   t1=THERMO.getTEMP(0,1)
   print (time.ctime(),'Temperature on thermocouple 1:',t1)
   THERMO.toggleLED(0) #Blink light when taking readings
   time.sleep(1)