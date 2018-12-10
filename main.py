
from mss import mss, tools

with mss() as sct:
    monitor = {"top": 0, "left": 0, "width": 960, "height": 1080}

    img = sct.grab(monitor)
    filename = 'monitor-1.png'
    tools.to_png(img.rgb, img.size, output=None)
    print(filename)