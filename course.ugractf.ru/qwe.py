from PIL import Image
import os.path

size = 592

new_img = Image.new("RGB", (size, size))

for i in range(size+1):
    for j in range(385):
        file = f"{i}_{j}.jpg"
        if os.path.exists(file):
            img = Image.open(f"{i}_{j}.jpg")
            new_img.paste(img, (i, j))

new_img.show()


