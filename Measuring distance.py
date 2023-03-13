#SOURCE CODE OF MEASURING DISTANCE,SEGREGATING WASTE,  DETECTING OBSTACLE AND PROMPTING MESSAGE:


#!/usr/bin/python
import RPi.GPIO as GPIO #Import GPIO library
import time
#Import time library
GPIO.setwarnings(False)
#set GPIO numbering mode and define output pins
S1 = 32
S2 = 36
S3 = 21

SM = 29
SW = 23

M11 = 31
M12 = 33
M21 = 35
M22 = 37

U_T = 38
U_E = 40
SVO = 12 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(M11,GPIO.OUT,initial=0)  GPIO.setup(M12,GPIO.OUT,initial=0) GPIO.setup(M21,GPIO.OUT,initial=0) GPIO.setup(M22,GPIO.OUT,initial=0) 
GPIO.setup(S1,GPIO.IN) #IR_1 GPIO.setup(S2,GPIO.IN) #IR_2 GPIO.setup(S3,GPIO.IN) #IR_3 GPIO.setup(SM,GPIO.IN) #Moisture 
GPIO.setup(SW,GPIO.IN) #Switch 
GPIO.setup(U_T,GPIO.OUT) # Trigger GPIO.setup(U_E,GPIO.IN) # Echo 
GPIO.setup(SVO,GPIO.OUT) 
#Defining PWM 
SV = GPIO.PWM(SVO, 50) 
SV.start(7) 
time.sleep(1)
SV.ChangeDutyCycle(7) 
#motor1GPIO.start(20) 
#motor2GPIO = GPIO.PWM(35, 100) #motor2GPIO.start(20) 
time.sleep(0.1) 
print("Ultrasonic Measurement") #GPIO.output(37, False) 
def measure(): 
 time.sleep(0.333) 
 GPIO.output(U_T, True) 
 time.sleep(0.00001) 
 GPIO.output(U_T, False) 
 start = time.time() 
 while GPIO.input(U_E)==0:  start = time.time() 
 while GPIO.input(U_E)==1:  stop = time.time() 
 elapsed = stop-start 
 distance = (elapsed * 34300)/2
def stop(): 
 GPIO.output(M11,False)  GPIO.output(M12,False)  GPIO.output(M21,False)  GPIO.output(M22,False) def forward(): 
 GPIO.output(M11,True)  GPIO.output(M12,False)  GPIO.output(M21,True)  GPIO.output(M22,False) def back(): 
 GPIO.output(M11,False)  GPIO.output(M12,True)  GPIO.output(M21,False)  GPIO.output(M22,True) def left(): 
 GPIO.output(M11,True)  GPIO.output(M12,False)  GPIO.output(M21,False)  GPIO.output(M22,True) def right(): 
 GPIO.output(M11,False)  GPIO.output(M12,True)  GPIO.output(M21,True)  GPIO.output(M22,False)
try: 
while True: 
 dis = measure() 
 print("Distance : %.1f" % dis) 
 V_S1 = GPIO.input(S1) 
 V_S2 = GPIO.input(S2) 
 V_S3 = GPIO.input(S3) 
 V_SM = GPIO.input(SM) 
 V_SW = GPIO.input(SW) 
# print("V_Sw ", V_SW) 
# print("V_S2 ", V_S2) 
#  
# time.sleep(0.01) 
  
# stop() 
 if V_S3 == 0: 
 stop() 
 print("Stop") 
 else:  
 if V_S1 == 0 and V_S2==0: #IR1 & IR2   forward() 
 elif V_S1 == 0 and V_S2 == 1: #IR1  right()  
 elif V_S1 == 1 and V_S2 == 0: #IR2
stop() left()  
 else: 

 if V_SW == 0: 
 if V_SM == 1: 
 SV.ChangeDutyCycle(2.5) # turn towards 0 degree (WET is Right  CONTAINER) 
 time.sleep(4) # sleep 1 second 
 SV.ChangeDutyCycle(7) # turn towards 90 degree  time.sleep(1) # sleep 1 second 
 else: 
 SV.ChangeDutyCycle(12.5) # turn towards 180 degree  time.sleep(4) # sleep 1 second 
 SV.ChangeDutyCycle(7) # turn towards 90 degree  time.sleep(1) # sleep 1 second 
  
 if dis >19 and dis <25: 
 print("dustbin is empty") 
 elif dis > 17 and dis <19: 
 print("dustbin 20% filled") 
 elif dis > 15 and dis <17: 
 print("dustbin 30% filled") 
 elif dis > 13 and dis <15: 
 print("dustbin 50% filled")
 elif dis > 7 and dis <13: 
 print("dustbin 70% filled")  elif dis < 7 or dis >100: 
 print("dustbin 100% filled")   
except KeyboardInterrupt: 
 #cleanup the GPIO pins before ending  SV.stop() 
 GPIO.cleanup()
