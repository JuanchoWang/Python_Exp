import os
from PIL import Image

def DrawPosebox(img_dir):
    #img_dir = '/mnt/Projects/CV-008_Students/wan4hi/VIPeR_data/Test_Sequence_2/cropped_body_parts/000066_00000001_0000/'
    hd_part = Image.open(os.path.join(img_dir, 'Head.jpg'))
    ts_part = Image.open(os.path.join(img_dir, 'Torso.jpg'))
    luA_part = Image.open(os.path.join(img_dir, 'LeftUpperArm.jpg'))
    ruA_part = Image.open(os.path.join(img_dir, 'RightUpperArm.jpg'))
    llA_part = Image.open(os.path.join(img_dir, 'LeftLowerArm.jpg'))
    rlA_part = Image.open(os.path.join(img_dir, 'RightLowerArm.jpg'))
    luL_part = Image.open(os.path.join(img_dir, 'LeftUpperLeg.jpg'))
    ruL_part = Image.open(os.path.join(img_dir, 'RightUpperLeg.jpg'))
    llL_part = Image.open(os.path.join(img_dir, 'LeftLowerLeg.jpg'))
    rlL_part = Image.open(os.path.join(img_dir, 'RightLowerLeg.jpg'))

    pbx = Image.new('RGB', (100, 210))
    pbx.paste(hd_part,(30,0))
    pbx.paste(ruA_part,(0,40))
    pbx.paste(ts_part,(20,40))
    pbx.paste(luA_part,(80,40))
    pbx.paste(rlA_part,(0,72))
    pbx.paste(llA_part,(90,72))
    pbx.paste(ruL_part,(25,120))
    pbx.paste(luL_part,(50,120))
    pbx.paste(rlL_part,(30,165))
    pbx.paste(llL_part,(50,165))
    #pbx.save(os.path.join(img_dir, 'Posebox.jpg'))
    return pbx
