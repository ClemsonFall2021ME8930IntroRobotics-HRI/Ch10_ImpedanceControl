# Ch10_ImpedanceControl


Select a admittance control for a two-join (three-linkage) robot with a force sensor installed on the manipulator. 


Steps in python code:
1. Get all the components as hangle that we can define each component of the robot including each joint and link as well as the manipulator. 
2. Set the positions of all the components of the robot including each joint and link as well as the manipulator. 
3. Set the coefficients of the damping and stiffness.
4. Set the mass of the manipulator. 

![pic_manipulator](https://user-images.githubusercontent.com/44584200/146103520-21598930-4e5f-481c-84ad-0002fa54f238.PNG)


5. Set the desired position and velocity of the manipulator.
6. Based on the control law equation, to get the acceleration of the manipulator. 
7. Set for the external force (sensed by the force sensor).  

![parameters](https://user-images.githubusercontent.com/44584200/146104405-adad3c37-9418-40ad-96e9-085062d24c43.PNG)


8. Based on the admittance control law, get the acceleration of the manipulator.
![law](https://user-images.githubusercontent.com/44584200/146104450-cde52cff-553b-4819-9d12-4cbeba12d85b.PNG)

