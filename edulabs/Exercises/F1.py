import re


# 1 Given a word, check whether it's a Capitalized word (starts from upper case, the second char is a lower case)
def is_capitalized(path: str) -> bool:
    pattern: str = r'[A-Z][a-z]'
    if re.match(pattern, path):
        return True
    else:
        return False


# 2 Given a string that represents DNA, check whether a given DNA string contain a TATA-box-like pattern.
def has_tata_box(dna_string):
    pattern: str = r'TATAA[ACGT]{3,4}TT'
    if re.search(pattern, dna_string):
        return True
    else:
        return False


# 3 Use repeats syntax and rewrite previous TATAA - pattern exercise
def has_tata_box_like_pattern(dna_string: str):
    pattern: str = r'TATAA[ACGT]{3,4}TT'
    if re.findall(pattern, dna_string):
        return True
    else:
        return False


# 4 Match two digits then any character then two non digits
def two_dig_any_two_non(path: str) -> bool:
    pattern: str = r'^\d{2}.[$%#@!&*^]{2}'
    if re.match(pattern, path):
        return True
    else:
        return False


# 5 Check whether the given string contains at least two TATA-lke patterns
def least_two_tata_lke(dna_string: str) -> bool:
    pattern: str = r'TATAA[ACGT]{3,4}TT'
    all_list: list = re.findall(pattern, dna_string)
    if len(all_list) >= 2:
        return True
    else:
        return False


# 6 Maximum 2 TATA-like patterns
def max_two_tata_lke(dna_string: str) -> bool:
    pattern: str = r'TATAA[ACGT]{3,4}TT'
    all_list: list = re.findall(pattern, dna_string)
    if len(all_list) <= 2 :
        return True
    else:
        return False


# Write a regular expression to look for 3 digits, possibly separated by whitespace.
def three_dig_sep_white(path: str) -> bool:
    pattern: str = r'\d\s'
    if re.search(pattern, path):
        return True
    else:
        return False


def all_israeli_phone_nums(path: str) -> list[str]:
    pattern = r'^05\d-\d{7}'
    phone_nums = re.findall(pattern, path)
    return phone_nums



if __name__ == '__main__':
    print(is_capitalized("Wdsded"))  # True

    dna1 = "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
    dna2 = "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
    dna3 = "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAAACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
    dna4 = "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAAACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAAA" \
           "CGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAAACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"


    print(has_tata_box(dna1))  # True
    print(has_tata_box(dna2))  # False

    print(has_tata_box_like_pattern(dna1))  # True
    print(has_tata_box_like_pattern(dna2))  # False

    print(two_dig_any_two_non('21f%$'))  # True
    print(two_dig_any_two_non('21f%43'))  # False

    print(least_two_tata_lke(dna3))  # True
    print(least_two_tata_lke(dna1))  # False

    print(max_two_tata_lke(dna1))  # True
    print(max_two_tata_lke(dna3))  # True
    print(max_two_tata_lke(dna4))  # False

    print(three_dig_sep_white(' 3123  434 3 '))  # True
    print(three_dig_sep_white(' fefewg  efe f '))  # False

    print(all_israeli_phone_nums('054-2345445'))

