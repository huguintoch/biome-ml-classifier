import numpy as np
from skimage import io

# import np file
resized_images_by_biomes = np.load("resized_images_by_biomes.npy", allow_pickle=True).item()

print(type(resized_images_by_biomes))
for biome in resized_images_by_biomes:
    io.imshow(resized_images_by_biomes[biome][0])
    io.show()