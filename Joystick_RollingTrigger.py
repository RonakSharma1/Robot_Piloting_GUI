#Written by Ronak Sharma, 08/04/2017

# AIM: This programme collects the information from a flight controller
# and dispays the co-ordinates of the joystick and the power through the throttle
# on the screen. Then UDP communication protocol is used to send the information
#from one server to another

#------------- MODULES USED-----------#
import sys
from PyQt4 import QtGui, QtCore
from functools import partial
import pygame
from time import sleep
import socket
#------------------------------------#


#HOST='192.168.1.5' # Defining the target
#HOST='192.168.1.5'

HOST='localhost'
PORT=5454      # Definig the target port 

instance=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP collection


#-------Initialisation of the Joystick---------#
pygame.init()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock=pygame.time.Clock()
#---------------------------------------------#


app = QtGui.QApplication(sys.argv) # Defining the main window of the GUI


#--------------- MAIN CLASS------------#

#----Defining the windows apperance and callling the main funcitons--------#
class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Joystick Controller")
        self.setStyleSheet("background-color: white")
        self.setGeometry(1000,1000,1000,1000)
        #--Self Parameters of joystick--#
        self.name_joystick()
        self.number_axis()
        self.number_buttons()
        #---------------------------------#
        
        #---------AXIS-------#
        self.label_name()
        self.position_axis_1()
        self.label_position_axis_1()
        self.position_axis_2()
        self.label_position_axis_2()
        self.position_axis_3()
        self.label_position_axis_3()
        self.position_axis_4()
        self.label_position_axis_4()
        self.position_axis_5()
        self.label_position_axis_5()
        #self.string_transition()
        #-------------------#
        
        #--------BUTTONS---------#
        self.button_value_1()
        self.label_button_value_1()
        self.button_value_2()
        self.label_button_value_2()
        self.button_value_3()
        self.label_button_value_3()
        self.button_value_4()
        self.label_button_value_4()
        self.button_value_5()
        self.label_button_value_5()
        self.button_value_6()
        self.label_button_value_6()
        self.button_value_7()
        self.label_button_value_7()
        self.button_value_8()
        self.label_button_value_8()
        self.button_value_9()
        self.label_button_value_9()
        self.button_value_10()
        self.label_button_value_10()
        self.button_value_11()
        self.label_button_value_11()
        self.button_value_12()
        self.label_button_value_12()
        self.thrusters_power()
        #--------------------------#
        
        #------THREADING-----#
        self.thread = Worker()
        self.connect(self.thread, QtCore.SIGNAL('Hello'), self.information)
        self.thread.start()
        #-------------------#    
        
    #-----CREATING LABELS AND TEXT BOXES-----#   
    
    #------Displaying Self Parameters of Joystick-------#
    def name_joystick(self):
        self.txt1 = QtGui.QLineEdit(self)
        self.txt1.resize(self.txt1.sizeHint())
        self.txt1.move(50,100)
    
    def label_name(self):  
        self.label4=QtGui.QLabel("              ",self)
        self.label4.move(100,10)
        self.label4.resize(50,50)
        self.label4.setText("THE JOYSTICK") 
        
    def number_axis(self):
        self.txt2 = QtGui.QLineEdit(self)
        self.txt2.resize(self.txt2.sizeHint())
        self.txt2.move(200,100)
        
    def number_buttons(self):
        self.txt3 = QtGui.QLineEdit(self)
        self.txt3.resize(self.txt3.sizeHint())
        self.txt3.move(400,100)
    #----------------------------------------#
        
    #--------DISPLAYING AXIS CO-ORDINATES--------------#
    def position_axis_1(self):
        self.txt4 = QtGui.QLineEdit(self)
        self.txt4.resize(self.txt4.sizeHint())
        self.txt4.move(50,200)
   
    def label_position_axis_1(self):  
        self.label4=QtGui.QLabel("  ",self)
        self.label4.move(50,180)
        self.label4.resize(self.label4.sizeHint())
        self.label4.setText("X-Axis")
                
    def position_axis_2(self):
        self.txt5 = QtGui.QLineEdit(self)
        self.txt5.resize(self.txt5.sizeHint())
        self.txt5.move(200,200)
    
    def label_position_axis_2(self):
        self.label5=QtGui.QLabel("                  ",self)
        self.label5.move(200,180)
        self.label5.resize(self.label5.sizeHint())
        self.label5.setText("Y-Axis")
        
    def position_axis_3(self):
        self.txt6 = QtGui.QLineEdit(self)
        self.txt6.resize(self.txt6.sizeHint())
        self.txt6.move(400,200)
        
    def label_position_axis_3(self):
        self.label6=QtGui.QLabel("                  ",self)
        self.label6.move(400,180)
        self.label6.resize(self.label6.sizeHint())
        self.label6.setText("Throttle")
        
    def position_axis_4(self):
        self.txt7 = QtGui.QLineEdit(self)
        self.txt7.resize(self.txt7.sizeHint())
        self.txt7.move(600,200)
        
    def label_position_axis_4(self):
        self.label7=QtGui.QLabel("                   ",self)
        self.label7.move(600,180)
        self.label7.resize(self.label7.sizeHint())
        self.label7.setText("Yaw")

    def position_axis_5(self):
        self.txt8 = QtGui.QLineEdit(self)
        self.txt8.resize(self.txt8.sizeHint())
        self.txt8.move(800,200)
        
    def label_position_axis_5(self):
        self.label8=QtGui.QLabel("                   ",self)
        self.label8.move(800,180)
        self.label8.resize(self.label8.sizeHint())
        self.label8.setText("Rudder")
    #-------------------------------------------#
        
    #-----------DISPLAYING BUTTONS-------------------#
    def button_value_1(self):
        self.txt9 = QtGui.QLineEdit(self)
        self.txt9.resize(self.txt9.sizeHint())
        self.txt9.move(50,300)
        
    def label_button_value_1(self):
        self.label9=QtGui.QLabel("                   ",self)
        self.label9.move(50,280)
        self.label9.resize(self.label9.sizeHint())
        self.label9.setText("R1")
        
    def button_value_2(self):
        self.txt10 = QtGui.QLineEdit(self)
        self.txt10.resize(self.txt10.sizeHint())
        self.txt10.move(200,300)
        
    def label_button_value_2(self):
        self.label10=QtGui.QLabel("                   ",self)
        self.label10.move(200,280)
        self.label10.resize(self.label10.sizeHint())
        self.label10.setText("L1")
        
    def button_value_3(self):
        self.txt11 = QtGui.QLineEdit(self)
        self.txt11.resize(self.txt11.sizeHint())
        self.txt11.move(400,300)
        
    def label_button_value_3(self):
        self.label11=QtGui.QLabel("                   ",self)
        self.label11.move(400,280)
        self.label11.resize(self.label11.sizeHint())
        self.label11.setText("R3")
        
    def button_value_4(self):
        self.txt12 = QtGui.QLineEdit(self)
        self.txt12.resize(self.txt12.sizeHint())
        self.txt12.move(600,300)
        
    def label_button_value_4(self):
        self.label12=QtGui.QLabel("                   ",self)
        self.label12.move(600,280)
        self.label12.resize(self.label9.sizeHint())
        self.label12.setText("L3")
        
    def button_value_5(self):
        self.txt13 = QtGui.QLineEdit(self)
        self.txt13.resize(self.txt13.sizeHint())
        self.txt13.move(800,300)
        
    def label_button_value_5(self):
        self.label13=QtGui.QLabel("                   ",self)
        self.label13.move(800,280)
        self.label13.resize(self.label13.sizeHint())
        self.label13.setText("5")
        
    def button_value_6(self):
        self.txt14 = QtGui.QLineEdit(self)
        self.txt14.resize(self.txt14.sizeHint())
        self.txt14.move(50,400)
        
    def label_button_value_6(self):
        self.label14=QtGui.QLabel("                   ",self)
        self.label14.move(50,380)
        self.label14.resize(self.label14.sizeHint())
        self.label14.setText("6")
        
    def button_value_7(self):
        self.txt15 = QtGui.QLineEdit(self)
        self.txt15.resize(self.txt15.sizeHint())
        self.txt15.move(200,400)
        
    def label_button_value_7(self):
        self.label15=QtGui.QLabel("                   ",self)
        self.label15.move(200,380)
        self.label15.resize(self.label15.sizeHint())
        self.label15.setText("7")
        
    def button_value_8(self):
        self.txt16 = QtGui.QLineEdit(self)
        self.txt16.resize(self.txt16.sizeHint())
        self.txt16.move(400,400)
        
    def label_button_value_8(self):
        self.label16=QtGui.QLabel("                   ",self)
        self.label16.move(400,380)
        self.label16.resize(self.label16.sizeHint())
        self.label16.setText("8")
        
    def button_value_9(self):
        self.txt17 = QtGui.QLineEdit(self)
        self.txt17.resize(self.txt17.sizeHint())
        self.txt17.move(600,400)
        
    def label_button_value_9(self):
        self.label17=QtGui.QLabel("                   ",self)
        self.label17.move(600,380)
        self.label17.resize(self.label17.sizeHint())
        self.label17.setText("R2")
        
    def button_value_10(self):
        self.txt18 = QtGui.QLineEdit(self)
        self.txt18.resize(self.txt18.sizeHint())
        self.txt18.move(800,400)
        
    def label_button_value_10(self):
        self.label18=QtGui.QLabel("                   ",self)
        self.label18.move(800,380)
        self.label18.resize(self.label18.sizeHint())
        self.label18.setText("L2")
        
    def button_value_11(self):
        self.txt19 = QtGui.QLineEdit(self)
        self.txt19.resize(self.txt19.sizeHint())
        self.txt19.move(50,500)
        
    def label_button_value_11(self):
        self.label19=QtGui.QLabel("                   ",self)
        self.label19.move(50,480)
        self.label19.resize(self.label19.sizeHint())
        self.label19.setText("SE")
        
    def button_value_12(self):
        self.txt20 = QtGui.QLineEdit(self)
        self.txt20.resize(self.txt20.sizeHint())
        self.txt20.move(200,500)
        
    def label_button_value_12(self):
        self.label20=QtGui.QLabel("                   ",self)
        self.label20.move(200,480)
        self.label20.resize(self.label20.sizeHint())
        self.label20.setText("ST")
    
    def string_transition(self,x):
        for i in range(len(x)):
            if x[i]>=0:
                proxy='+'+str(x[i])
                x[i]=proxy;
            else:
                proxy=str(x[i])
                x[i]=proxy
        return x
        
#----- Below defines the calcualtion undertaken to determine the power to thruster----------#
    def thrusters_power(self):
        #------ Storing the values from the different axis on joystick------#
        self.X_Axis="{:>.2f}".format(my_joystick.get_axis(0))# X_Axis- Axis 0
        self.Y_Axis="{:>.2f}".format(my_joystick.get_axis(1))#Y_Axis - Axis 1
        self.Throttle="{:>.2f}".format(my_joystick.get_axis(2))
        self.Yaw="{:>.2f}".format(my_joystick.get_axis(3))
        self.Rudder="{:>.2f}".format(my_joystick.get_axis(4))
        self.Roll=(my_joystick.get_button(0))
    
        
#--- Based on the experimentation conducted it was concluded that the maximum deviation from the required action is 15%------#
#--- So the error is 0.15----#
#-- Also the thruster are numbered from 1 to 6 and can be seen in the diagram uploaded in the Drive
        # If all the axis are between -0.15 and 0.15 it means that they are not being moved so the system is at rest
        #print(self.Roll)
        if ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Yaw)<0.15) and (-0.15<float(self.Rudder)<0.15) and -0.15<float(self.Y_Axis)<0.15 and int(self.Roll)==0):
            print('System at Rest')
            self.copy_thruster_power=([0.00,0.00,0.00,0.00,0.00,0.00,0.00]) # Thruster are powered zero
            self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        # If all the axis are between -0.15 and 0.15 except Y axis means that Y-Axis is being controlled at the moment
                
        if ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Yaw)<0.15) and (-0.15<float(self.Rudder)<0.15) ):
            # If positive values means that the ROV should go backward 
            #Values are taken after 0.15 and values lower than that are ignored as 15% error was considered in the system
            if(0.15<=float(self.Y_Axis)<=1.00):
                print("Moving Backward")
                self.copy_thruster_power=([(1)*float(self.Y_Axis),(1)*float(self.Y_Axis),(1)*float(self.Y_Axis),(1)*float(self.Y_Axis),0.00,0.00,0.00])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
                #If negative values then ROV moving forward
            elif(-1.00<=float(self.Y_Axis)<-0.15):
                print("Moving Forward")
                self.copy_thruster_power=([(-1)*float(self.Y_Axis),(-1)*float(self.Y_Axis),(-1)*float(self.Y_Axis),(-1)*float(self.Y_Axis),0.00,0.00,0.00])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
                #The above thruster are powered accordingly based on the vectorisation developed previously#
             
        #--- If all axis are between -0.15 and 0.15 except X_axis then it means that ROV want to move in right or left direction
        elif ((-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Y_Axis)<0.15) and (-0.15<float(self.Yaw)<0.15) and (-0.15<float(self.Rudder)<0.15) ):
            # If the values are positive then Right
            if(0.15<=float(self.X_Axis)<=1.00):
                print("Turning Right")  # 0 means that that thruster is not powered
                self.copy_thruster_power=([float(self.X_Axis),0.00,0.00,(-1)*float(self.X_Axis),0.00,0.00,0.00])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
                # If negative values then Turning Left
            elif (-1.00<=float(self.X_Axis)<-0.15):
                print("Turning Left")
                self.copy_thruster_power=([0.00,float(self.X_Axis),(-1)*float(self.X_Axis),0.00,0.00,0.00,0.00])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()                
                     # The combination of which thrusters can be again found by looking at the vectors of the motor
        
        elif ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Y_Axis)<0.15) and (-0.15<float(self.Yaw)<0.15) and (-0.15<float(self.Throttle)<0.15) ):
    
             if(0.15<=float(self.Rudder)<=1.00):
                print("Pitch Down") #According to me power should be greater than half as the forces are not aligned
                self.copy_thruster_power=([0.00,0,00,0.00,0.00,float(self.Rudder),0.00,0.00])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
             elif(-1.00<=float(self.Rudder)<-0.15):
                print("Pitch Up")
                self.copy_thruster_power=([0.00,0,00,0.00,0.00,float(self.Rudder),0.00,0.00])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
        elif ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Y_Axis)<0.15) and (-0.15<float(self.Yaw)<0.15) and (-0.15<float(self.Rudder)<0.15) ):
    
             if(0.15<=float(self.Throttle)<=1.00):
                print("Rise Up") #According to me power should be greater than half as the forces are not aligned
                self.copy_thruster_power=([0.00,0,00,0.00,0.00,float(self.Throttle),round((float(self.Throttle))/2,2),round((float(self.Throttle))/2,2)])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
             elif(-1.00<=float(self.Throttle)<-0.15):
                print("Go Down")
                self.copy_thruster_power=([0.00,0,00,0.00,0.00,float(self.Throttle),round((float(self.Throttle))/2,2),round((float(self.Throttle))/2,2)])
                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
#        elif ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Y_Axis)<0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
#            
#             if(0.15<=float(self.Yaw)<=1.00):
#                print("Rolling Clockwise")
#                self.copy_thruster_power=([0.00,0,00,0.00,0.00,0.00,float(self.Yaw),(-1)*float(self.Yaw)])
#                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
#             
#             elif (-1.00<=float(self.Yaw)<-0.15):
#                print("Rotating Left")
#                self.copy_thruster_power=([float(self.Yaw),(-1)*float(self.Yaw),(-1)*float(self.Yaw),float(self.Yaw),0.00,00,0.00])                           
#                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()

#        elif ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Y_Axis)<0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
#            
#             if(0.15<=float(self.Yaw)<=1.00):
#                print("Rolling Clockwise")
#                self.copy_thruster_power=([0.00,0,00,0.00,0.00,0.00,float(self.Yaw),(-1)*float(self.Yaw)])
#                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
#             
#             elif (-1.00<=float(self.Yaw)<-0.15):
#                print("Rolling Anti-Clockwise")
#                self.copy_thruster_power=([0.00,0,00,0.00,0.00,0.00,float(self.Yaw),(-1)*float(self.Yaw)])                           
#                self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()

        elif ((-0.15<float(self.X_Axis)<0.15) and (-0.15<float(self.Y_Axis)<0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
            
             if(0.15<=float(self.Yaw)<=1.00):
                if(self.Roll==1):
                     print("Rolling - Clockwise") 
                     self.copy_thruster_power=([0.00,0.00,0.00,0.00,0.00,float(self.Yaw),(-1)*float(self.Yaw)])
                     self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
                else:
                    print("Rotating Right")
                    self.copy_thruster_power=([float(self.Yaw),(-1)*float(self.Yaw),(-1)*float(self.Yaw),float(self.Yaw),0.00,0.00,0.00])
                    self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
                 
             elif (-1.00<=float(self.Yaw)<-0.15):
                 if(self.Roll==1):
                     print("Rolling - AntiClockwise") 
                     self.copy_thruster_power=([0.00,0.00,0.00,0.00,0.00,float(self.Yaw),(-1)*float(self.Yaw)])
                     self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
                 else:
                     print("Rotating Left")
                     self.copy_thruster_power=([float(self.Yaw),(-1)*float(self.Yaw),(-1)*float(self.Yaw),float(self.Yaw),0.00,0.00,0.00])                           
                     self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
                
                # For diagonal two axis are looked together , so if the X axis and Y_Axis is out of error area then means that the ROV should move diagonally
        # The direction would depend  on what value + or - would be fed to and also to which motor
        # Again this combination can be found out by referring to thrusters vector
        elif ((0.15<=float(self.X_Axis)<=1) and (-1.00<=float(self.Y_Axis)<=-0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
           print("Diagonal : North - East")
           self.copy_thruster_power=([0.00,float(self.Y_Axis),float(self.X_Axis),float(self.X_Axis),0.00,0.00,0.00])
           self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
        elif ((0.15<=float(self.Y_Axis)<=1) and (-1.00<=float(self.X_Axis)<=-0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
           print("Diagonal : South - West")
           self.copy_thruster_power=([float(self.X_Axis),float(self.Y_Axis),0.00,float(self.X_Axis),0.00,0.00,0.00])
           self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
        elif ((-1.00<=float(self.Y_Axis)<=-0.15) and (-1.00<=float(self.X_Axis)<=-0.15) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
           print("Diagonal : North - West")
           self.copy_thruster_power=([0.00,float(self.X_Axis),(-1)*float(self.X_Axis),(-1)*float(self.X_Axis),0.00,0.00,0.00])
           self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
        elif ((0.15<=float(self.Y_Axis)<=1) and (0.15<=float(self.X_Axis)<=1) and (-0.15<float(self.Throttle)<0.15) and (-0.15<float(self.Rudder)<0.15)):
           print("Diagonal : South - East")
           self.copy_thruster_power=([float(self.Y_Axis),(-1)*float(self.Y_Axis),(-1)*float(self.Y_Axis),0.00,0.00,0.00,0.00])
           self.thruster_power=str(self.string_transition(self.copy_thruster_power)).encode()
        
           #Prints the final thruster_power
        print(self.thruster_power)
        print("\n")
       # print(self.thruster_power)
    #--------------------------------------------#

    #This defines the main fucntion of the program. It caluclates and analyses
    # the differnet paramters obtained on the movement of the controller and
    #then collects and outputs them on the screen
    def information(self):
        #self.comma=","
        #----- Collecting Self Parameters of Joystick----#
        name_joystick=my_joystick.get_name() # Collects the pre-defined name of joystick
        number_axes=my_joystick.get_numaxes() # Collects the pre-defined number of axis 
        number_buttons=my_joystick.get_numbuttons()# Collects the pre-defined number of buttons
        self.txt1.setText(str(name_joystick)) #Displaying the information 
        self.txt2.setText(str(number_axes))   #in the required textboxes
        self.txt3.setText(str(number_buttons))
        instance.sendto((self.thruster_power),(HOST,PORT))
        #instance.sendto(str(self.comma).encode(),(HOST,PORT))
        #-------------------------------------#
        
        #---------Collecting the value of the Axis---------#
        self.txt4.setText(str("{:>.2f}".format(my_joystick.get_axis(0))))
     #   instance.sendto(str("{:>.2f}".format(my_joystick.get_axis(0))).encode(),(HOST,PORT))
        self.txt5.setText(str("{:>.2f}".format(my_joystick.get_axis(1))))
      #  instance.sendto(str("{:>.2f}".format(my_joystick.get_axis(1))).encode(),(HOST,PORT))
        self.txt6.setText(str("{:>.2f}".format(my_joystick.get_axis(2))))
       # instance.sendto(str("{:>.2f}".format(my_joystick.get_axis(2))).encode(),(HOST,PORT))
        self.txt7.setText(str("{:>.2f}".format(my_joystick.get_axis(3))))
       # instance.sendto(str("{:>.2f}".format(my_joystick.get_axis(3))).encode(),(HOST,PORT))
        self.txt8.setText(str("{:>.2f}".format(my_joystick.get_axis(4))))
       #instance.sendto(str("{:>.2f}".format(my_joystick.get_axis(4))).encode(),(HOST,PORT))
       #---------------------------------------------------#
        
        #------------------Collecting the value of Buttons--------------#   
        self.txt9.setText(str(my_joystick.get_button(0)))
        #instance.sendto(str(my_joystick.get_button(0)).encode(),(HOST,PORT))
        self.txt10.setText(str(my_joystick.get_button(1)))
        #instance.sendto(str(my_joystick.get_button(1)).encode(),(HOST,PORT))
        self.txt11.setText(str(my_joystick.get_button(2)))
        #instance.sendto(str(my_joystick.get_button(2)).encode(),(HOST,PORT))
        self.txt12.setText(str(my_joystick.get_button(3)))
        #instance.sendto(str(my_joystick.get_button(3)).encode(),(HOST,PORT))
        self.txt13.setText(str(my_joystick.get_button(4)))
        #instance.sendto(str(my_joystick.get_button(4)).encode(),(HOST,PORT))
        self.txt14.setText(str(my_joystick.get_button(5)))
        #instance.sendto(str(my_joystick.get_button(5)).encode(),(HOST,PORT))
        self.txt15.setText(str(my_joystick.get_button(6)))
        #instance.sendto(str(my_joystick.get_button(6)).encode(),(HOST,PORT))
        self.txt16.setText(str(my_joystick.get_button(7)))
        #instance.sendto(str(my_joystick.get_button(7)).encode(),(HOST,PORT))
        self.txt17.setText(str(my_joystick.get_button(8)))
        #instance.sendto(str(my_joystick.get_button(8)).encode(),(HOST,PORT))
        self.txt18.setText(str(my_joystick.get_button(9)))
        #instance.sendto(str(my_joystick.get_button(9)).encode(),(HOST,PORT))
        self.txt19.setText(str(my_joystick.get_button(10)))
        #instance.sendto(str(my_joystick.get_button(10)).encode(),(HOST,PORT))
        self.txt20.setText(str(my_joystick.get_button(11)))
        #instance.sendto(str(my_joystick.get_button(11)).encode(),(HOST,PORT))
        #----------------------------------------------------------------#
        self.thrusters_power() # Calling the thruster value
#----------------------------------------------------------------------------#


# This class is responsible for threading which means runnin two operations 
#simultaneously. It emits a signal to define when the above program shoudl be
#updated

class Worker(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self, parent=app)
    
    def run(self):
        EXIT=False
        while not EXIT:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    EXIT=True
            self.emit(QtCore.SIGNAL('Hello'))
            clock.tick(5) #This determines how fast the frames change per second
        pygame.quit() # This is used to quit pygame and use any internal program within the python
        quit()
        
        
def main():        
    window = Window()
    window.show()
    sys.exit(app.exec_())
main()