import os
import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage.transform import resize

if __name__ == "__main__":
    scale = 8
    img_width = int(1920 / scale)
    img_height = int(1080 / scale)

    resized_images_by_biomes = {}
    biomes = os.listdir("img")
    
    for biome in biomes:
        print("Processing biome: " + biome)
        resized_images_by_biomes[biome] = []
        images = os.listdir("img/" + biome)
        for image in images:
            image_path = "img/" + biome + "/" + image
            img = io.imread(image_path)
            resized_img = resize(img, (img_height, img_width), anti_aliasing=True)
            resized_images_by_biomes[biome].append(resized_img)
        print("Finished processing " + str(len(images)) + " images")	

    # save resized images as object
    np.save("resized_images_by_biomes.npy", resized_images_by_biomes)