import os
from PIL import Image

path_images = './images'

for tomo in sorted(os.listdir(path_images), key=lambda x: int(x.split('_')[1])):
    print("Tomo:", tomo)
    path_tomo = os.path.join(path_images, tomo)
    images_tomo = list()
    for n_cap, capitulo in enumerate(sorted(os.listdir(path_tomo), key=lambda x: int(x.split('_')[1]))):
        print("Capitulo:", capitulo)
        path_img = os.path.join(path_tomo, capitulo)
        for i, img in enumerate(sorted(os.listdir(path_img), key=lambda x: int(x.split('.')[0]))):
            if n_cap == 0 and i == 0:
                print("Path img:", os.path.join(path_img, img))
                im_1 = Image.open(os.path.join(path_img, img)).convert('RGB')
            else:
                images_tomo.append(Image.open(os.path.join(path_img, img)).convert('RGB'))
    im_1.save(r'./tomos/{tomo}.pdf'.format(tomo=tomo), save_all=True, append_images=images_tomo)
