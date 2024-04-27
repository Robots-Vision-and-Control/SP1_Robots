from fuzzywuzzy import fuzz


def get_probability(user_input, predetermined_commands):
    iterations = 1
    stripped_command_list = [label.lstrip('#') for label in predetermined_commands]
    command_index = exact_matching(user_input, stripped_command_list)
    if command_index is None:
        command_index = probabilistic_matching(user_input, stripped_command_list)

    result = predetermined_commands[command_index]

    if '#' in result:
        iterations = extract_number(user_input)
    return result, iterations


# Function to match the recognized string against a list of commands
def exact_matching(user_input, predetermined_commands):
    for index, command in enumerate(predetermined_commands):
        if command.lower() in user_input.lower():
            return index
    return None


# Function to perform probabilistic matching
def probabilistic_matching(user_input, predetermined_commands):
    max_similarity = 0
    best_match_index = None

    for index, command in enumerate(predetermined_commands):
        similarity = fuzz.ratio(user_input, command)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match_index = index

    return best_match_index


def extract_number(input_string):
    # Regular expression to find one or more digits
    number = None
    for i in input_string.split():
        if i.isdigit():
            return int(i)
