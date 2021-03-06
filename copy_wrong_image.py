""""
the file path of wrong sample is at result_model_name/test_flow_from_directory_cp_xx/wrong_sample_path.txt
the path is saved as 
    ...
    live/A3_30000666_crop_3.jpeg
    live/A3_30000674_crop_1.jpeg
    live/A3_30000677_crop_1.jpeg
    ...
this script will read path from file txt and copy image into new folder 
then we will research why model predict wrong these images
"""

import os
import numpy as np
from config import work_place
from tqdm import tqdm
import shutil


def make_dir(path):
    if not os.path.isdir(path):
        # os.makedirs(path)
        pass

def copy_wrong_image(model_name='', cp_index='', base_data=crop_folder_test, number_img_copy=100):
    wrong_path_file = resize_all_folder + '/' + model_name  + '/test_'  + cp_index[:-3] + '/wrong_sample_path.txt'
    wrong_image_folder_all_model = work_place + '/wrong_image_folder'
    make_dir(wrong_image_folder_all_model)

    wrong_image_folder = wrong_image_folder_all_model + '/' + model_name
    make_dir(wrong_image_folder)
    live_wrong = wrong_image_folder + '/live'
    make_dir(live_wrong)
    spoof_wong = wrong_image_folder + '/spoof'
    make_dir(spoof_wong)

    with open(wrong_path_file) as f:
        path_list = f.read().splitlines()

    count = 0
    for item in tqdm(path_list):
        origin_image = os.path.join(base_data, item)
        new_destination = os.path.join(wrong_image_folder, item)
        shutil.copy2(origin_image, new_destination)
        count += 1
        if count >= number_img_copy:
            break
    return count


if __name__ == '__main__':

    copy_wrong_image(model_name='b4_ver_1', cp_index='cp_03.h5')


