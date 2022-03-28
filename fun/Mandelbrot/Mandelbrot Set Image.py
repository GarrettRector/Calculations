from numba import jit
from PIL import Image


@jit(nopython=True, parallel=True)
def mandelbrot_set(j, k) -> int:
    c1 = complex(j, k)
    c2 = 0
    for n in range(1, 900):
        if abs(c2) > 2:
            return int(n)
        c2 = c2 ** 2 + c1
    return 0


def generate(width):
    image = Image.new('RGB', (width, int(width / 2)))
    pixels = image.load()
    for x in range(image.size[0]):
        print("%.2f %%" % (x / width * 100.0))
        for y in range(image.size[1]):
            pixels[x, y] = mandelbrot_set((x - (0.75 * width)) / (width / 4),
                                          (y - (width / 4)) / (width / 4))
    image.save(f"Mandelbrot Set {width}.png")


w = 8000 # Width of image
generate(w)
