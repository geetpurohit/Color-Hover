<H1 align="center">
    Color Hover
</H1>

<H5 align="center">
    Get the RGBA (Red, Blue, Green, Alpha) value of any pixel in any image by just hovering over the image:
</H5>

<p align="center">
  <img src="https://user-images.githubusercontent.com/68968629/143863898-559a9ed6-744a-4826-a9dd-74e9bbaef7a4.gif" />
</p>



# INSTRUCTIONS



### Step 1 : Download and unzip the code


<img src="https://user-images.githubusercontent.com/68968629/143865600-5ca0219c-3b04-4a3a-b106-cf9e65d008f3.jpg" width=70% height=70%>


### Step 2 : Make sure main.py and target image is in the same folder


![Capture](https://user-images.githubusercontent.com/68968629/143866358-92da08f7-d04e-4062-a657-4f4d8bf63160.PNG)


### Step 3 : Run the main.py through your preferred choice of editor. It doesn't matter which IDE you choose. (hint: VScode is the right choice).


https://user-images.githubusercontent.com/68968629/143867288-8418c887-c6f6-4963-b93f-85e876cffc55.mp4


### Step 4 : Enjoy!


* Possible Bugs and solutions
1. Library issues -> ```pip install``` the required libaries
2. Python Interpreter issue (VSCode Specific) -> Check if you have selected an interpreter. Press Ctrl + Shift + P then Enter and then choose
3. tkinter canvas issues -> image needs to always be in PNG format. Easily change it using Pillow. JPG to PNG example below:
```
from PIL import Image

img = Image.open("target.jpg")
temp = im.convert('RGB')
temp.save('target.jpg')

```



