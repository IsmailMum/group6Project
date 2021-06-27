import math
import xml.etree.ElementTree as ET

tree = ET.parse('/home/grup6/Desktop/group6Project/maze.svg')
coordinates = []

with open("/home/grup6/Desktop/group6Project/coordinates.txt",'w') as f:
    for coordinate in tree.getroot()[0]:
        if coordinate.get('x1') is not None:
            f.write(str(math.floor(float(coordinate.get('x1'))))+ ' '+ str(math.floor(float(coordinate.get('x2'))))+ ' '+ str(math.floor(float(coordinate.get('y1'))))+ ' '+ str(math.floor(float(coordinate.get('x1'))))+ '\n')