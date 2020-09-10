- This code is very simple and fast. you just need to add the path to your images folder and give the size of the output images!

```
import PIL
import os
import os.path
from PIL import Image

f = r'Address of input folder of images' # for example C:/Myimages
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((48,48))  $ the needed size of images. here we needed 48*48
    img.save(f_img)
```
