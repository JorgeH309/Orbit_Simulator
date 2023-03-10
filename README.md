The program is supposed to open a GUI using Tkinter and provide a summary on the context
behind the simulator. The GUI contains widgets such as Labels, Entries, and Buttons. The label that
contains the summary actually retrieves the paragraph from a separate text file. A label in the bottom of
the GUI also retrieves an image from outside the program. In the simulator, there is a spacecraft that
has been launched from Earth and when it reaches “free flight” or the end of its burn time, it will be
located at a point far above the atmosphere. At this point, the trajectory of the spacecraft can be found
only using the velocities of the spacecraft in all directions. Hence why the GUI contains three entry
widgets that allow the user to input the x, y, and z velocities of the spacecraft when reaching free flight.
In the program, I also imported the module Scipy, since it contains the function odeint which takes in an
equation of a mathematical function’s derivative, initial values and range of the interval and it returns
the value of the function throughout the entire range. I found the equations for the acceleration of an
object in orbit and using the initial coordinate, user’s initial velocities, and an array of time intervals
created by Numpy, the odeint returned an array of all the coordinates of the object’s trajectory. Once
the user has input their velocities, they shall click the button on the GUI. If the input values are invalid
such as if they contain special characters or letters, then an error message will display on the GUI asking
them to input numerical values. If the values are valid however, then a 3D plot in matplotlib will be
displayed in a new window, showing a sphere resembling Earth and the trajectory of the spacecraft. I
used the spherical coordinates equations to get all the coordinates of a sphere with radius of 6378.4 km.
Matplotlib contains a function called ‘surface’ which allowed the code run quicker by only plotting the
surface of the sphere.
