from API_Calls import *
import asyncio


def walk_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_left'))
    if response_body:
        print(f"Response Body: {response_body}")


def walk_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_right'))
    if response_body:
        print(f"Response Body: {response_body}")


def walk_forward_short(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_forward_short'))
    if response_body:
        print(f"Response Body: {response_body}")


def turn_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_right'))
    if response_body:
        print(f"Response Body: {response_body}")


def turn_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_left'))
    if response_body:
        print(f"Response Body: {response_body}")


def sit_down(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'sit_down'))
    if response_body:
        print(f"Response Body: {response_body}")


def standing_position(robot_motion):
    print(robot_motion + 'reset')
    response_body = asyncio.run(APICall(robot_motion + 'reset'))
    if response_body:
        print(f"Response Body: {response_body}")


def walking_position(robot_motion):
    print(robot_motion + 'basic_motion')
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(robot_motion + 'basic_motion'))
    if response_body:
        print(f"Response Body: {response_body}")


# Left upper shoulder - id:12 ; min: 10 ; max:254 ; default:180 ; inverted:true ; min is slightly behind the user, max is straight up
# Right upper shoulder - id:13 ; min: 10 ; max:254 ; default:180 ; inverted:false ; min is straight up, max is
# Left lower shoulder - id:14 ; min:135 ; max:254 ; default:135 ; inverted:false
# Right lower shoulder - id:15 ; min:1 ; max:120 ; default:120 ; inverted:true

def move_left_upper_shoulder(robot_arm,position,robot_motion):
    movement = robot_arm + '12&position=' + position + '&torq=4'
    print(movement)
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(movement))
    if response_body:
        print(f"Response Body: {response_body}")


def move_right_upper_shoulder(robot_arm,position,robot_motion):
    movement = robot_arm + '13&position=' + position + '&torq=4'
    print(movement)
    response_body = asyncio.run(APICall(movement))
    if response_body:
        print(f"Response Body: {response_body}")


def move_left_lower_shoulder(robot_arm,position,robot_motion):
    movement = robot_arm + '14&position=' + position + '&torq=4'
    print(movement)
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(movement))
    if response_body:
        print(f"Response Body: {response_body}")


def move_right_elbow(robot_arm,position,robot_motion):
    movement = robot_arm + '19&position=' + position + '&torq=4'
    print(movement)
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(movement))


def move_right_lower_shoulder(robot_arm,position,robot_motion):
    movement = robot_arm + '15&position=' + position + '&torq=4'
    print(movement)
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(movement))
    if response_body:
        print(f"Response Body: {response_body}")


def move_neck_left_or_right(robot_head,position,robot_motion):
    movement = robot_head + '23&position='+ position + '&torq=4'
    print(movement)
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(movement))
    if response_body:
        print(f"Response Body: {response_body}")


def move_head_up_or_down(robot_head,position,robot_motion):
    movement = robot_head + '24&position=' + position + '&torq=4'
    print(movement)
    response_body1 = asyncio.run(APICall(robot_motion + 'pc_control'))
    response_body = asyncio.run(APICall(movement))
    if response_body:
        print(f"Response Body: {response_body}")
