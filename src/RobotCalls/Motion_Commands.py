from API_Calls import APICall
import asyncio

allow_output = False


def print_info(response):
    if allow_output:
        print('movement: ' + response)


def kick_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'kick_right'))
    print_info(response_body)


def kick_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'kick_left'))
    print_info(response_body)


def turn_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_right'))
    print_info(response_body)


def turn_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_left'))
    print_info(response_body)


def walk_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_right'))
    print_info(response_body)


def walk_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_left'))
    print_info(response_body)


def walk_forward_1step(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_forward_short'))
    print_info(response_body)


def walk_forward_4step(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_forward_4step'))
    print_info(response_body)


def walk_forward_6step(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_forward_6step'))
    print_info(response_body)


def sit_down(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'sit_down'))
    print_info(response_body)


def stand_up(robot_motion):
    print(robot_motion + 'reset')
    response_body = asyncio.run(APICall(robot_motion + 'reset'))
    print_info(response_body)


def walking_position(robot_motion):
    print(robot_motion + 'basic_motion')
    response_body = asyncio.run(APICall(robot_motion + 'basic_motion'))
    print_info(response_body)


def demo_introduction(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'demo_introduction'))
    print_info(response_body)


def demo_gangnamstyle(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'dance_gangnamstyle'))
    print_info(response_body)
