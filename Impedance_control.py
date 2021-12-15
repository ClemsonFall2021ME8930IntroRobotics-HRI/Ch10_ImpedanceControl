# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')
    
import math
import time

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')


#Getting object handlle
opMode=sim.simx_opmode_blocking
errorCode,base=sim.simxGetObjectHandle(clientID,"Base",opMode)
errorCode,link1=sim.simxGetObjectHandle(clientID,"Link1",opMode)
errorCode,link2=sim.simxGetObjectHandle(clientID,"Link2",opMode)
errorCode,tip=sim.simxGetObjectHandle(clientID,"Dummy",opMode)
errorCode,ForceSensor=sim.simxGetObjectHandle(clientID,"ForceSensor",opMode)


errorCode,J1=sim.simxGetObjectHandle(clientID,"Revolute_joint1",opMode)
errorCode,J2=sim.simxGetObjectHandle(clientID,"Revolute_joint2",opMode)

# Set the position of the components (manipulator and force sensor)
errorCode, tip_position= sim.simxGetObjectPosition(clientID,tip,base,sim.simx_opmode_oneshot_wait)
print("Manipulator_Position = ",tip_position)
errorCode, ForceSensor_position= sim.simxGetObjectPosition(clientID,ForceSensor,base,sim.simx_opmode_oneshot_wait)
print("ForceSensor_Position =",ForceSensor_position)

a1 = 0.8; #Link 1 length
a2 = 0.6; #Link 2 length

#parameters' values，one degree of freedom, so the matrix size is 1x1
mass = 10
stiffness = 10
damping = 600

# External force is 10 N to the y-axis, horizontal relation to the ground
ForceSensor = 10 

# Set a real position of the tip
errorCode, tip_position= sim.simxGetObjectPosition(clientID,tip,base,sim.simx_opmode_oneshot_wait)
print("Manipulator_Position = ",tip_position)

ye = tip_position[1]; #Target Position
# How to set a desired position? What operator should I use? 

# set the real velocity of the tip unit
errorcode, tip_vel= sim.simxSetJointTargetVelocity(clientID, tip,0.3,sim.simx_opmode_streaming )

# set the desired velocity 
tip_vel_d = 0.2


# haven't figured out how to set a desired position 
tip_acc = (-damping*(tip_vel_d-tip_vel)-stiffness*(tip_position-tip_position_d)+ForceSensor)/mass






    







