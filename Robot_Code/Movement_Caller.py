import requests
from Movement_Commands import *


def movement_command(select_command,position):
    session = requests.Session()  # TODO: Test if this line is needed
    client = session
    ip_address = '10.101.148.223'  # TODO: Always check the IP from the Pi
    port = 50000

    base_http_call = 'http://' + ip_address + ':'+str(port) + '/'

    robot_head = base_http_call + 'motor?id='

    robot_arm = base_http_call + 'motor?id='

    robot_motion = base_http_call + 'motion/'

    if select_command == 'walk_left':
        walk_left(robot_motion)
    elif select_command == 'walk_right':
        walk_right(robot_motion)
    elif select_command == 'walk_forward_short':
        walk_forward_short(robot_motion)
    elif select_command == 'turn_right':
        turn_right(robot_motion)
    elif select_command == 'turn_left':
        turn_left(robot_motion)
    elif select_command == 'sit_down':
        sit_down(robot_motion)
    elif select_command == 'standing_position':
        standing_position(robot_motion)
    elif select_command == 'walking_position':
        walking_position(robot_motion)
    elif select_command == 'move_left_upper_shoulder':
        move_left_upper_shoulder(robot_arm,str(position),robot_motion)
    elif select_command == 'move_right_upper_shoulder':
        move_right_upper_shoulder(robot_arm,str(position),robot_motion)
    elif select_command == 'move_left_lower_shoulder':
        move_left_lower_shoulder(robot_arm,str(position),robot_motion)
    elif select_command == 'move_right_lower_shoulder':
        move_right_lower_shoulder(robot_arm,str(position),robot_motion)
    elif select_command == 'move_neck_left_or_right':
        move_neck_left_or_right(robot_head,str(position),robot_motion)
    elif select_command == 'move_head_up_or_down':
        move_head_up_or_down(robot_head,str(position),robot_motion)
    elif select_command == 'move_right_elbow':
        move_right_elbow(robot_arm,str(position),robot_motion)
