from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
from graphics.circle import area as circle_area,perimeter as circle_perimeter
from graphics_3d.cuboid import area as cuboid_area,volume as cuboid_volume
from graphics_3d.sphere import area as sphere_area,volume as sphere_volume
rect_length,rect_width=5,10
circle_radius=7
cuboid_length,cuboid_width,cuboid_height=3,4,5
sphere_radius=6
print("rectangle area:",rect_area(rect_length,rect_width))
print("rectangle perimeter:",rect_perimeter(rect_length,rect_width))
print("circle area:",circle_area(circle_radius))
print("circle perimeter:",circle_perimeter(circle_radius))
print("cuboid area:",cuboid_area(cuboid_length,cuboid_width,cuboid_height))
print("cuboid volume:",cuboid_volume(cuboid_length,cuboid_width,cuboid_height))
print("sphere area:",sphere_area(sphere_radius))
print("sphere volume:",sphere_volume(sphere_radius))
from graphics.rectangle import *
from graphics.circle import *
from graphics_3d.cuboid import *
from graphics_3d.sphere import *
rect_length,rect_width=5,10
circle_radius=7
cuboid_length,cuboid_width,cuboid_height=3,4,5
sphere_radius=6
print("rectangle area:",rect_area(rect_length,rect_width))
print("rectangle perimeter:",rect_perimeter(rect_length,rect_width))
print("circle area:",circle_area(circle_radius))
print("circle perimeter:",circle_perimeter(circle_radius))
print("cuboid area:",cuboid_area(cuboid_length,cuboid_width,cuboid_height))
print("cuboid volume:",cuboid_volume(cuboid_length,cuboid_width,cuboid_height))
print("sphere area:",sphere_area(sphere_radius))
print("sphere volume:",sphere_volume(sphere_radius))
