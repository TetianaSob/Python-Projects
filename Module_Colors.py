# Module_Colors.py

#import the module
import colorsys

print(dir(colorsys))

'''['ONE_SIXTH', 'ONE_THIRD', 'TWO_THIRD', '__all__', '__builtins__', 
'__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', '_v', 'hls_to_rgb', 'hsv_to_rgb', 
'rgb_to_hls', 'rgb_to_hsv', 'rgb_to_yiq', 'yiq_to_rgb'] '''

print(help(colorsys))

'''
Help on module colorsys:

NAME
    colorsys - Conversion functions between RGB and other color systems.

MODULE REFERENCE
    https://docs.python.org/3.8/library/colorsys

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This modules provides two functions for each color system ABC:

-- More  --
'''

text = colorsys.colorsys("HI THERE!", color = "cyan", on_color = "on_magenta", attrs= ["blink"])
print(text)
