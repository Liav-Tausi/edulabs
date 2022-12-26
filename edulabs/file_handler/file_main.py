from file_Interpreter import CsvFile, JsonFile, TxtFile


if __name__ == "__main__":
    csv_file1 = CsvFile("f_h_files/email-password-recovery-code.csv", ";")
    csv_file2 = CsvFile("f_h_files/csv_combine_test.csv", ",")
    json_file = JsonFile("f_h_files/json_ex.json")
    json_file2 = JsonFile("f_h_files/json_ex2.json")
    txt_file1 = TxtFile("f_h_files/alice_in_wonderland.txt")
    txt_file2 = TxtFile("f_h_files/alice_in_wonderland2.txt")
    txt_file3 = TxtFile("f_h_files/alice_in_wonderland.txt_alice_in_wonderland2.txt")

    # json_file1 + json_file2
    # print(csv_file2.delimiter())
    # print(csv_file1.delimiter())
    # csv_file2 + csv_file1

    # files = [csv_file1, json_file1, txt_file1]
    # for i in files:
    #     print(i.content())

    # print(csv_file1.file_size())
    # print(csv_file1.file_size_unit("terabytes"))
    # print(csv_file1.columns())
    # print(csv_file1.rows())
    # print(csv_file1.by_row(6))
    # print(csv_file1.by_column(3))
    # print(csv_file1.by_cell(0, 3))

    # print(txt_file1.avg_word_len())
    # print(json_file.is_list())
    # print(json_file.is_object())
    # print()
    # print(txt_file2.words_amount()+txt_file1.words_amount())
    # print(txt_file3.words_amount())
