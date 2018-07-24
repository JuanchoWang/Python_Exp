import os
from shutil import copyfile
from PoseboxGen import DrawPosebox

# Change the following path
root_path = '/mnt/Projects/CV-008_Students/wan4hi/DukeMTMC-reID'
if not os.path.isdir(root_path):
    print('Please enter a correct path to original dataset')

part_path = os.path.join(root_path, 'bounding_box_test_par_cropped_body_parts') # CHANGE
img_path = os.path.join(root_path,'bounding_box_test') # CHANGE
save_path = os.path.join(root_path,'bounding_box_test_pbx_clean')
if not os.path.isdir(save_path):
    os.mkdir(save_path)

crop_list = os.listdir(part_path)
num = 0

for root, dirs, files in os.walk(img_path, topdown=True):
    for name in files:
        ID = name.split('_')
        num += 1
        print('ID {} {}/{}'.format(ID[0], num, len(files)))

        if name[0:-4] in crop_list:
            PBox = DrawPosebox(os.path.join(part_path, name[0:-4]))
            PBox.save(os.path.join(save_path, name))
        # Comment the following lines when clean posebox set wanted
        # else:
        #     src_path = os.path.join(img_path, name)
        #     copyfile(src_path, os.path.join(save_path, name))
