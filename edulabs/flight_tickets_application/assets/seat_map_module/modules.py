def file_open(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                print(line.rstrip())
    except:
        print("NO FILE FOUND, CHECK PATH")

def print_seats_map(value: int):
    ''''DESC: FUNCTION PRINTING SEATS LAYOUT ON CMD
    1 for first class
    2 for biz class
    3 for eco class                            '''''
    try:
        match value:
            case 1:
                file_open('asciis/first_class.txt')
            case 2:
                file_open('asciis/biz_class.txt')
            case 3:
                file_open('asciis/eco_class.txt')
    except:
        print("RANGE ACCEPTED ONLY 1-3.")
