def get_valid_input(input_string, valid_options):
    input_string += ' ({}) '.format(', '.join(valid_options))
    while True:
        response = input(input_string)
        if response.lower() in valid_options:
            break
    return response

def get_valid_no(input_string,lowerRange,upperRange):
    arr = []
    for i in range(lowerRange,upperRange+1):
        arr.append(i)

    while True:
        response = input(input_string)
        if int(response) in arr:
            break
    return int(response)

def print_menu():
    print(f'\n1. Add new property\n2. Show specific property\n3. Show all property')
    print(f'4. Modify property\n5. Quit from system')
