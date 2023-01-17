"""
===============================================================================
ENGR 13300 Fall 2022

Program Description
    This is an interactive simulator in which the user can input a spacecraft's velocities when it
    reaches free flight, and it will plot its trajectory. A GUI will be prompted for the user's inputs.

Assignment Information
    Assignment:     Individual Project: Orbit Simulator
    Author:         Jorge Hernandez, herna647@purdue.edu
    Team ID:        LC5

Contributor:
    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
from intersection import *
from tkinter import*
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from PIL import ImageTk, Image

root = Tk()
root.title('Orbital Mechanics')
root.configure(background='black')
# builds the GUI and makes the background black and adds a title

def equation(cond, t):
    mu = 3.986004418E+05
    x = cond[0]
    y = cond[1]
    z = cond[2]
    x_vel = cond[3]
    y_vel = cond[4]
    z_vel = cond[5]
    x_sder = -mu * x / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    y_sder = -mu * y / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    z_sder = -mu * z / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    forms_dt = [x_vel, y_vel, z_vel, x_sder, y_sder, z_sder]
    # these are the equations to find the acceleration at each point of an orbit
    return forms_dt

def export(x, y, z):
    newfile = open('coordinates.txt', 'w')
    newfile.write('X-Coordinate:   Y-Coordinate:   Z-Coordinate:\n')
    index = 0
    while index < len(x):
        newfile.write(f'{round(x[index], 3):>13}   {round(y[index], 3):>13}   {round(z[index], 3):>12}\n')
        index += 1
    newfile.close()
    # This will open a new file and put all the coordinates of the orbit in it

def graph_sphere():
    # This plots the sphere in 3D
    fig = plt.figure(facecolor="White")
    ax = plt.axes(projection="3d")
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    radius = 6378.14

    x = radius * np.outer(np.cos(theta), np.sin(phi))
    y = radius * np.outer(np.sin(theta), np.sin(phi))
    z = radius * np.outer(np.ones(np.size(theta)), np.cos(phi))
    # These are the spherical equations used to plot the sphere
    ax.plot_surface(x, y, z, rstride=2, cstride=2)
    ax.tick_params(labelsize=8, rotation=0)
    ax.set_title('Your Trajectory')
    ax.set_xlabel('X-Axis [km]')
    ax.set_ylabel('Y-Axis [km]')
    ax.set_zlabel('Z-Axis [km]')
    return ax, radius

def graph():
    try:
        # Initial coordinate of the trajectory
        x_i = 6000
        y_i = -5500
        z_i = -3300
        vel_x = float(x_vel_input.get())
        vel_y = float(y_vel_input.get())
        vel_z = float(z_vel_input.get())
        # grabs the input velocities and uses it
        ax, radius = graph_sphere()
        # retrieves the function to graph the sphere
        initial_cond = [x_i, y_i, z_i, vel_x, vel_y, vel_z]
        t = np.linspace(0, 6 * 3600, 200)
        coords = odeint(equation, initial_cond, t)
        # the odeint function from Scipy gets the acceleration equations and integrates
        # them to get the velocities and the coordinates; only the coordinates are retrieved
        x_coord = coords[:, 0]
        y_coord = coords[:, 1]
        z_coord = coords[:, 2]
        x_coord, y_coord, z_coord = intersection(radius, x_coord, y_coord, z_coord)
        export(x_coord, y_coord, z_coord)
        ax.plot(x_coord, y_coord, z_coord, 'r', label='trajectory')
        ax.plot(x_i, y_i, z_i, 'b.', label='start of free-flight')
        ax.set_aspect('equal')
        ax.legend(bbox_to_anchor=(1.2, 0.05))
        plt.show()
        # plots the orbit
    except:
        ButtonLabel = Label(root, background='black', foreground='white')
        ButtonLabel.grid(row=18, column=2)
        ButtonLabel['text'] = 'Please input a numerical value'
        # if the numbers inputted aren't valid, then it will print this message

# These functions are retrieved to clear the entry widgets
def entry_clicked(event):
    x_vel_input.configure(state=NORMAL)
    x_vel_input.delete(0, END)
    x_vel_input.unbind('<Button-1>', clicked)
def entry_clicked2(event):
    y_vel_input.configure(state=NORMAL)
    y_vel_input.delete(0, END)
    y_vel_input.unbind('<Button-1>', clicked2)
def entry_clicked3(event):
    z_vel_input.configure(state=NORMAL)
    z_vel_input.delete(0, END)
    z_vel_input.unbind('<Button-1>', clicked3)

# This opens the jpg image placed in the GUI. Everything after are widgets
image1 = ImageTk.PhotoImage(Image.open('spacepic.jpg').resize((450, 300)))
imagelabel = Label(root, image=image1, bg='black', anchor='center')
myLabel = Label(root, width=20, text=' ', background='black', fg='white')
myLabel2 = Label(root, width=20, text=' ', background='black', fg='white')
x_vel_input = Entry(root, width=50, borderwidth=10, background='black', fg='white')
y_vel_input = Entry(root, width=50, borderwidth=10, background='black', fg='white')
z_vel_input = Entry(root, width=50, borderwidth=10, bg='black', fg='white')
# this opens the text file that contains the introduction paragraph
para = open('introduction.txt', 'r')
file = []
for line in para:
    file.append(line)
intro = Label(root, width=80, text=' '.join(file), highlightthickness=2, highlightbackground='red', bg='black', fg='white')
para.close()
Title = Label(root, text='Welcome to Orbit Simulator!', font=18, foreground='white', background='black')
filler = Label(root, width=50, text=' ', bg='black', fg='white')
filler2 = Label(root, width=50, text=' ', bg='black', fg='white')
fillerx = Label(root, width=50, text=' ', bg='black', fg='white')
filler3 = Label(root, width=50, text=' ', bg='black')
filler4 = Label(root, width=50, text=' ', bg='black')
filler5 = Label(root, width=50, text= ' ', bg='black')
myButton = Button(root, text='Click here!', padx=50, command=graph)
# Once the widgets are created, they are placed in the GUI using a grid system
myLabel.grid(row=0, column=0)
myLabel2.grid(row=0, column=3)
Title.grid(row=2, column=2)
filler.grid(row=3, column=2)
intro.grid(rowspan=2, column=2)
fillerx.grid(row=6, column=2)
x_vel_input.grid(row=7, column=2)
filler2.grid(rowspan=2, column=2)
y_vel_input.grid(row=10, column=2)
filler3.grid(rowspan=2, column=2)
z_vel_input.grid(row=14, column=2)
filler4.grid(rowspan=2, column=2)
x_vel_input.insert(0, "Enter x-velocity")
y_vel_input.insert(0, 'Enter y-velocity')
z_vel_input.insert(0, 'Enter z-velocity')
clicked = x_vel_input.bind('<Button-1>', entry_clicked)
clicked2 = y_vel_input.bind('<Button-1>', entry_clicked2)
clicked3 = z_vel_input.bind('<Button-1>', entry_clicked3)
myButton.grid(row=17, column=2)
filler5.grid(row=18, column=2)
imagelabel.grid(row=19, column=2)

# This ensures that the GUI remains open until it is manually closed by the user
root.mainloop()
