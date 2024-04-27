from API_Calls import *
import asyncio

default_torq = 4
allow_output = False


# Left upper shoulder - id:12 ; min: 10 ; max:254 ; default:180 ; inverted:true ; min is slightly behind the user, max is straight up
# Right upper shoulder - id:13 ; min: 1 ; max:254 ; default:180 ; inverted:false ; min is straight up, max is
# Left lower shoulder - id:14 ; min:135 ; max:254 ; default:135 ; inverted:false
# Right lower shoulder - id:15 ; min:1 ; max:120 ; default:120 ; inverted:true


# I don't know what this code is used for, but I will test it.
def pc_control(robot_motion):
    asyncio.run(APICall(robot_motion + 'pc_control'))


def print_info(movement, response):
    if allow_output:
        print('movement: ' + movement)
        print('response: ' + response)


# FEET
# left-foot: min=115, max=140, default=127
def move_left_foot(robot_foot, position, torq=default_torq):
    movement = robot_foot + '0&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-foot: min=110, max=140, default=127
def move_right_foot(robot_foot, position, torq=default_torq):
    movement = robot_foot + '1&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# HEEL
# left-heel: min=77, max=175, default=127
def move_left_heel(robot_heel, position, torq=default_torq):
    movement = robot_heel + '2&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-heel: min=78, max=175, default=127
def move_right_heel(robot_heel, position, torq=default_torq):
    movement = robot_heel + '3&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# KNEE
# left-knee: min=77, max=204, default=204
def move_left_knee(robot_knee, position, torq=default_torq):
    movement = robot_knee + '4&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-knee: min=50, max=180, default=50
def move_right_knee(robot_knee, position, torq=default_torq):
    movement = robot_knee + '5&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# UPPER LEG
# left-front-upper-leg: min=0, max=255, default=127
def move_left_front_upper_leg(robot_upper_leg, position, torq=default_torq):
    movement = robot_upper_leg + '6&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-front-upper-leg: min=0, max=255, default=127
def move_right_front_upper_leg(robot_upper_leg, position, torq=default_torq):
    movement = robot_upper_leg + '7&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# left-back-upper-leg: min=0, max=255, default=127
def move_left_back_upper_leg(robot_upper_leg, position, torq=default_torq):
    movement = robot_upper_leg + '8&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-back-upper-leg: min=0, max=255, default=127
def move_right_back_upper_leg(robot_upper_leg, position, torq=default_torq):
    movement = robot_upper_leg + '9&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# HIP
# left-hip: min=0, max=255, default=127
def move_left_hip(robot_hip, position, torq=default_torq):
    movement = robot_hip + '10&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-hip: min=0, max=255, default=127
def move_right_hip(robot_hip, position, torq=default_torq):
    movement = robot_hip + '11&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# SHOULDER
# left-upper-shoulder: min=10, max=254, default=180
def move_left_upper_shoulder(robot_arm, position, robot_motion, torq=default_torq):
    movement = robot_arm + '12&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-upper-shoulder: min=1, max=254, default=180
def move_right_upper_shoulder(robot_arm, position, torq=default_torq):
    movement = robot_arm + '13&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# left-lower-shoulder: min=135, max=254, default=135
def move_left_lower_shoulder(robot_arm, position, robot_motion, torq=default_torq):
    movement = robot_arm + '14&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# left-lower-shoulder: min=1, max=120, default=120
def move_right_lower_shoulder(robot_arm, position, robot_motion, torq=default_torq):
    movement = robot_arm + '15&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# BICEP
# left-bicep: min=1, max=254, default=127
def move_left_bicep(robot_bicep, position, torq=default_torq):
    movement = robot_bicep + '16&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# right-bicep: min=1, max=254, default=127
def move_right_bicep(robot_bicep, position, torq=default_torq):
    movement = robot_bicep + '17&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# ELBOW
#  left_elbow: min=75, max=210, default=210
def move_left_elbow(robot_arm, position, robot_motion, torq=default_torq):
    movement = robot_arm + '18&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


#  right-bicep: min=40, max=180, default=40
def move_right_elbow(robot_arm, position, robot_motion, torq=default_torq):
    movement = robot_arm + '19&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# WAIST
# waist: min=95, max=165, default=127
def move_waist(robot_waist, position, torq=default_torq):
    movement = robot_waist + '22&position=' + position + '&torq=' + torq
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# NECK
# waist: min=95, max=165, default=127
def move_neck_left_or_right(robot_head, position, robot_motion, torq=default_torq):
    movement = robot_head + '23&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)


# HEAD
# waist: min=100, max=160, default=127
def move_head_up_or_down(robot_head, position, robot_motion, torq=default_torq):
    movement = robot_head + '24&position=' + position + '&torq=' + torq
    pc_control(robot_motion)
    response_body = asyncio.run(APICall(movement))
    print_info(movement, response_body)
