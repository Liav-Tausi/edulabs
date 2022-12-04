'''EXAMPLE FOR USE'''''

from modules import print_seats_map

# try to handle out of range / error input
'''PRINT OUT LAYOUT OF CLASS
    1 for first class
    2 for biz class
    3 for eco class         '''''
try:
    print_seats_map(2)
except:
    print("Accepting only range 1-3.")