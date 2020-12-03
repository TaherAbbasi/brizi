  
# -*- coding: utf-8 -*-

# This work is licensed under the MIT License.
# To view a copy of this license, visit https://opensource.org/licenses/MIT

# Written by Taher Abbasi
# Email: abbasi.taher@gmail.com

import math

optical_zoom = 25 # 25x

# minimum focal length in mm(millimeter)
focal_length_min = 4.8

# image resolution
image_res = (1920, 1080)

image_center = tuple(int(dim/2) for dim in image_res)

# to convert optical zoom handred percent scale to optical zoom scale
oz_factor = 100 / optical_zoom

# the sensor size for 1/2.8" is 0.19×0.14 inch which is 4.826×3.556 mm
# 4.826 mm is for horizental and 3.556 mm is for vertical dimension
sensor_size = (4.826, 3.556)

def pixel_to_steps(roi_pixel_coord, currentZoom: int):
    '''This is used for obtaining the vertical and horizental degrees
    which the camera have to rotate, so the ROI is in the center of the
    frame.
    :roi_pixel_coord: roi center in the image.
    :currentZoom: current zoom of the camera.
    '''
    # difference between ROI center to the image center in pixel
    roi_center_diff = tuple( a - b for a,b in zip(image_center, 
                            roi_pixel_coord))
    
    focal_length_curr = (currentZoom / oz_factor) * focal_length_min
    print(focal_length_curr)
    # current angle view of the camera in degree. Respectively, 
    # horizentally and vertically.
    angle_view_curr = tuple(57.2958 * 2 * math.atan (dim / (2 * 
                            focal_length_curr)) for dim in sensor_size)
    print(angle_view_curr)
    pixel_to_angle_ratio = tuple( a / b for a,b in zip(image_res, 
                            angle_view_curr))
    
    steps = tuple( int(a / b) for a,b in zip(roi_center_diff, 
                                        pixel_to_angle_ratio))
    return steps    
