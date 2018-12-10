from mss import mss, tools
import ctypes


with mss() as sct:
    # The screen part to capture
    monitor = {"top": 140, "left": 75, "width": 520, "height": 520}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    tools.to_png(sct_img.rgb, sct_img.size, output=output)
    
