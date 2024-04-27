import Sound_Recording_Translation as get_command
import String_Comparison as compare
import time
import RobotCalls.Motion_Caller as call

command_list = ["#take steps forward", "#take steps left", "#take steps right",
                "turn left", "turn right", "sit down", "stand up",
                "look up", "look down", "look right", "look left"]


def execute_command(command):
    match command:
        case "#take steps forward":
            call.movement_command('walk_forward_short', 0)
        case "#take steps left":
            call.movement_command('walk_left', 0)
        case "#take steps right":
            call.movement_command('walk_right', 0)
        case "turn left":
            call.movement_command('turn_left', 0)
        case "turn right":
            call.movement_command('turn_right', 0)
        case "sit down":
            call.movement_command('sit_down', 0)
        case "stand up":
            call.movement_command('standing_position', 0)
        case "look up":
            call.movement_command('move_head_up_or_down', 0)
        case "look down":
            call.movement_command('move_head_up_or_down', 0)
        case "look right":
            call.movement_command('move_neck_left_or_right', 0)
        case "look left":
            call.movement_command('move_neck_left_or_right', 0)
        case _:
            print("Unknown command")


if __name__ == "__main__":
    while True:
        user_command = get_command.listen_for_commands()
        command, iterations = compare.get_probability(user_command, command_list)
        print(command, iterations)

        for i in range(iterations):
            execute_command(command)
            time.sleep(3)
