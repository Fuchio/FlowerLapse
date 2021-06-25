from pathlib import Path
import os

PATH = Path().resolve()
PATH = PATH / '8f6bb7ee' / '25_06'

img_list = Path(PATH).rglob('*.jpg')
img_list = sorted(img_list, key=os.path.getmtime)
for img_path in img_list:
    print(img_path)

# for path in Path(PATH).rglob('*.jpg'):
#     print(path)
