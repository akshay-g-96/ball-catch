import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
#from OpenGL.GLUT import *


import random

count=0
drops =0
score = 0

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0), 
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
    (1,0,1),
    (0,0,1),
    (0,1,0),
    (0,0,0),
    (0,1,1),
    (1,0,0),
    
    (1,1,0),
    (1,1,1)
    )

ground_vertices = (
    (-13, -2, -2),
    (-13, -2, -10),
    (13, -2, -10),
    (13, -2, -2)
    )

verti = [
    surfaces[4][0],
    surfaces[4][1],
    surfaces[4][2], 
    surfaces[4][3]
    ]

def ground(x_rev,y_rev,z_rev,sp):
    glBegin(GL_QUADS)

    for vertex in ground_vertices:
        x_new=vertex[0]-x_rev
        z_new=vertex[2]#-z_rev
        y_new=vertex[1]-y_rev
        glColor3fv((0,0.5,0))
        glVertex3fv((x_new,y_new,z_new))
        #if()

        ############################################################print("ground",(x_new,y_new,z_new))
        
    glEnd()
    return ((x_new,y_new,z_new))

def set_vertices(max_distance):
    x_value_change = 0#random.randrange(-10,10)
    y_value_change = 10#random.randrange(-10,10)
    z_value_change = random.randrange(-1*max_distance, -20)

    new_vertices = []
    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

h=0


def Sphere(x_rev,y_rev,z_rev,r,s,t):
    col = []
    p=0
    q=0
    
    glBegin(GL_POINTS)
    for i in range(360):
        glColor3f(1,0,1)
        glVertex3f((.05*math.cos(i*math.pi/180))-x_rev+r,s+(.05*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(1,1,1)
        glVertex3f((.1*math.cos(i*math.pi/180))-x_rev+r,s+(.1*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(0,0,1)
        glVertex3f((.15*math.cos(i*math.pi/180))-x_rev+r,s+(.15*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(1,0,0)
        glVertex3f((.2*math.cos(i*math.pi/180))-x_rev+r,s+(.2*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(1,1,0)
        glVertex3f((.25*math.cos(i*math.pi/180))-x_rev+r,s+(.25*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(0,1,0)
        glVertex3f((.3*math.cos(i*math.pi/180))-x_rev+r,s+(.3*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(0,0,0)
        glVertex3f((.35*math.cos(i*math.pi/180))-x_rev+r,s+(.35*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(0,1,0)
        glVertex3f((.4*math.cos(i*math.pi/180))-x_rev+r,s+(.4*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(0,0,0)
        glVertex3f((.45*math.cos(i*math.pi/180))-x_rev+r,s+(.45*math.sin(i*math.pi/180)),(-t-z_rev))
        glColor3f(0,1,1)
        glVertex3f((.5*math.cos(i*math.pi/180))-x_rev+r,s+(.5*math.sin(i*math.pi/180)),(-t-z_rev))
        
        p=0.5*math.cos(3*math.pi/2)-x_rev+r
        q=s+(0.5*math.sin(3*math.pi/2))#i#180
    glEnd()

    ##############################################################print("sphere",((.5*math.cos(i*math.pi/180))-x_rev+r,s+(.5*math.sin(i*math.pi/180)),t-z_rev))
    
    return (((.5*math.cos(3*math.pi/2))-x_rev+r,s+(.5*math.sin(3*math.pi/2))+y_rev,(-t-z_rev)))


def Cube(x_rev,y_rev,z_rev):
##    x_new=vertex[0]-x_rev
##    z_new=vertex[2]-z_rev
##    y_new=vertex[1]-y_rev
    new_vertices = []
    for vert in vertices:
        new_vert = []

        new_x = vert[0] - x_rev
        new_y = vert[1] - y_rev
        new_z = vert[2] - z_rev

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
        
    glBegin(GL_QUADS)
    for surface in surfaces:
        x=8
        
        for vertex in surface:
            x-=1
            glColor3fv(colors[x]
                       )
            glVertex3fv(new_vertices[vertex])
    glEnd()

    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(new_vertices[vertex])
    glEnd()



def main():

    x_rev=0
    z_rev=0
    y_rev=0
    x_rev1=0
    z_rev1=0
    gr = (0,0,0)
    sp = ()
    
    pygame.init()
    pygame.font.init()
    display = (800,600) #screen size 800 px and 600px
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 60.0)#45 degrees,50 z view port
    #screen.fill((0,0,255))
    glTranslatef(0,-2,-20)#-27  # move y by -2 and z by -35 units
    #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #ground()
    myfont = pygame.font.SysFont("monospace", 16)
    object_passed = False
    z_move=0
    x_move=0
    r=random.randrange(-5,5)
    s=6#random.randrange(4,7)
    t=-10#(random.randrange(0,6))
    
    while not object_passed:
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    if x_rev>=-4:
                    
                        x_move = -0.2#move x by -0.3 units
                        #print("x_rev",x_rev)
                    else:
                        x_move = 0
                        
                if event.key == pygame.K_RIGHT:
                    if x_rev <= 4:
                    
                        x_move = 0.2#move x by 0.3 units
                    else:
                        x_move=0
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    z_move = 0
                    #print("z_rev",z_rev)

                    
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        glClearColor(1.0,0.0,0.0,0.5)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        x_rev+=x_move# on each key press summation of x_move
        z_rev+=z_move# on each key press -35 + (summation of z_move)
        y_rev-=0.12#0.03  # makes fruits fall
        x_rev1-=x_move
        z_rev1-=z_move
        glTranslatef(x_move,0,z_move) # each iteration move 
        glTranslatef(0,-0.12,0)
        sp = Sphere(x_rev,y_rev,z_rev,r,s,t)
        gr = ground(x_rev,y_rev,z_rev,sp)
        sp1 = sp[1] * 100
        gr1 = gr[1] * 100
        ve1 = (vertices[1][1]+y_rev) * 100
        ve2 = int(ve1)
        sp2 = int(sp1)
        gr2 = int(gr1)
        
        
        #print(sp[0],vertices[1][0])
        if(sp2-155<2 and sp[0]<vertices[1][0]  and sp[0]<vertices[5][0]  and sp[0]>vertices[7][0]  and sp[0]>vertices[2][0]):
            object_passed=True
            global count
            count+=1
            print("object caught, total catches",count)
        if(sp2 <= 30):
            object_passed=True
            global drops
            drops+=1
            print("object passed, total drops",drops)
        
        Cube(x_rev1,y_rev,z_rev1)
        #scoretext = myfont.render("Score {0}".format(count), 1, (0,0,0))
        #screen.blit(scoretext, (5, 10))
        #score += 1
        pygame.display.flip()
        #pygame.time.wait(10)
        
for x in range(50):
    main()
    
pygame.quit()
quit()
        
    


