from Motion_Commands import *
from Motor_Comands import *
import requests


def movement_command(select_command, position):
    session = requests.Session()  # TODO: Test if this line is needed
    client = session
    ip_address = '10.101.148.223'  # TODO: Always check the IP from the Pi
    port = 50000

    base_http_call = 'http://' + ip_address + ':' + str(port) + '/'

    robot_motor = base_http_call + 'motor?id='

    robot_motion = base_http_call + 'motion/'

    match select_command:
        case 'walk_left':
            walk_left(robot_motion)
        case 'walk_right':
            walk_right(robot_motion)
        case 'walk_forward_short':
            walk_forward_1step(robot_motion)
        case 'turn_right':
            turn_right(robot_motion)
        case 'turn_left':
            turn_left(robot_motion)
        case 'sit_down':
            sit_down(robot_motion)
        case 'standing_position':
            stand_up(robot_motion)
        case 'walking_position':
            walking_position(robot_motion)
        case 'dance_gangnamstyle':
            demo_gangnamstyle(robot_motion)
        case 'move_left_upper_shoulder':
            move_left_upper_shoulder(robot_motor, str(position), robot_motion)
        case 'move_right_upper_shoulder':
            move_right_upper_shoulder(robot_motor, str(position), robot_motion)
        case 'move_left_lower_shoulder':
            move_left_lower_shoulder(robot_motor, str(position), robot_motion)
        case 'move_right_lower_shoulder':
            move_right_lower_shoulder(robot_motor, str(position), robot_motion)
        case 'move_neck_left_or_right':
            move_neck_left_or_right(robot_motor, str(position), robot_motion)
        case 'move_head_up_or_down':
            move_head_up_or_down(robot_motor, str(position), robot_motion)
        case 'move_right_elbow':
            move_right_elbow(robot_motor, str(position), robot_motion)
