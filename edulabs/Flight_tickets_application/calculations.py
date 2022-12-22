import random


# over all input calculations:
def luggage_calc(area_class: str,luggage_kg: int=0) -> float:
    luggage_price = 0
    if area_class == 'first':
        pass
    elif area_class == 'biz':
        if luggage_kg > 50:
            luggage_price = 10
    else:
        if luggage_kg > 20:
            luggage_price = 10
    return (luggage_price*luggage_kg)
# seat-line input calculations
def seat_calc(seat_class:str,seat_char: str=None,seat_line: str=None) -> int:
    price = 0
    # if first class price = 4000
    if seat_class == 'first':
        price += 4000
    # if biz class depending on the seat and line choice
    elif seat_class == 'biz':
        #for lins 5 - 7 base price = 3000
        if seat_line >= '5' and seat_line <= '7':
            price += 3000
        # for all ather lines base price = 2300
        else:
            price += 2300
        # for window seats price is $55
        match seat_char:
            case 'A' | 'D':
                price += 55
    # if economy class depending on the seat and line choice
    else:
        # for lins 11 - 20 base price = 1700
        if seat_line >= '11' and seat_line <= '20':
            #if special seat + $15
            if seat_line == 12:
                price += 15
            price += 1700
        # for lins 21 - 21 base price = 1500
        elif seat_line >= '21'and seat_line <= '40':
            # if special seat + $15
            if seat_line == 22:
                price += 15
            price += 1500
        # for all ather lines base price = 1200
        else:
            # if special seat + $15
            if seat_line == 42:
                price += 15
            price += 1200
        # for window seats price is $10
        match seat_char:
            case 'A' | 'F':
                price += 10
    # over all seat price
    return price

# meal price calculations
def meal_price(meal_class: str) -> int:
    match meal_class:
        # Luxury meal
        case '1':
          return 42
        # biz meal
        case '2':
          return 22
        # eco meal
        case '3':
          return 7

def lottery(full_name: str, num_choice: int) -> int:
    name_length: int = len(full_name)
    rand_num: int = random.randrange(1,5)
    result: int = (name_length*rand_num) % num_choice
    if result <= 5:
        return result
    else:
        return 0