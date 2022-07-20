import PIL
from PIL import Image
import os


imgs = r'' #Enter folder location between quotes

for img in os.listdir(imgs):
    print('Starting ', img)
    flat_img= imgs+"/"+img
    ed_img = Image.open(flat_img)
    rs_img = ed_img.resize((450,450))
    rs_img.save(flat_img)
    print('Finished ', img)

