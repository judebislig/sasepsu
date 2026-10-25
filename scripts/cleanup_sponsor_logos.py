from PIL import Image, ImageDraw
import os

base = r'C:\Users\jdw64\Downloads\sasepsu2\sasepsu\images\sponsors'
files = [
    'sponsor-lockheed.jpg',
    'sponsor-wabtec.png',
    'sponsor-whiting.png',
    'blue origin logo.png',
]

for name in files:
    path = os.path.join(base, name)
    if not os.path.exists(path):
        continue

    img = Image.open(path).convert('RGBA')
    w, h = img.size
    pixels = img.load()

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            if r > 245 and g > 245 and b > 245:
                pixels[x, y] = (255, 255, 255, 0)

    mask = Image.new('L', (w, h), 0)
    draw = ImageDraw.Draw(mask)
    radius = min(w, h) // 12
    draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)

    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask=mask)

    if name.lower().endswith('.png'):
        out.save(path)
    else:
        new_path = os.path.splitext(path)[0] + '.png'
        out.save(new_path)
        os.remove(path)

print('processed sponsor logos')
