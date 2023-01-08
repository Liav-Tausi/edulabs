from vt_api_key_for_test import *
from vt_file import *
from vt_url import *




if __name__ == '__main__':

    url = VTUrl(url=r'https://edulabs.co.il/', vt_key=vt_key)
    print(url.post_get_url())


    url = VTUrl(url=r'https://www.ynet.co.il/', vt_key=vt_key)
    print(url.post_get_url())


    url = VTUrl(url=r'https://mixedanalytics.com/', vt_key=vt_key)
    print(url.post_get_url())


    file = VTFile(file=r'C:\Users\liavt\PycharmProjects\LernningPython\edulabs\file_handler\f_h_files\csv_ex.csv',
                  vt_key=vt_key)
    print(file.post_get_file())


    file = VTFile(file=r'C:\Users\liavt\PycharmProjects\LernningPython\edulabs\file_handler\f_h_files\json_ex.json',
                  vt_key=vt_key)
    print(file.post_get_file())
