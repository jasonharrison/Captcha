import random

import Image
import ImageFont
import ImageDraw
import ImageFilter


def gen_captcha(text, fnt, fnt_sz, file_name, fmt='JPEG'):
    fgcolor = random.randint(0, 0xffff00)
    bgcolor = fgcolor ^ 0xffffff
    font = ImageFont.truetype(fnt, fnt_sz)
    dim = font.getsize(text)
    im = Image.new('RGB', (dim[0] + 5, dim[1] + 5), bgcolor)
    d = ImageDraw.Draw(im)
    x, y = im.size
    print "X: " + str(x) + ", Y: " + str(y)
    r = random.randint
    for num in range(random.randint(20, 999)):
        d.rectangle((r(0, x), r(0, y), r(0, x), r(0, y)), fill=r(0, 0xffffff))
    for num in range(random.randint(1, 50)):
        d.line((r(0, x), r(0, y), r(0, x), r(0, y)), fill=r(0, 0xffffff))
    for num in range(random.randint(20, 99)):
        d.ellipse((r(0, x), r(0, y), r(0, x), r(0, y)), fill=r(0, 0xffffff))
    d.text((3, 3), text, font=font, fill=fgcolor)
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im.save(file_name, format=fmt)
    return text


def getCaptcha():
    letters = "abcdefghjklmnpqrstuvwxyz234578".upper()
    word = ""
    i = 0
    for x in range(random.randint(5, 10)):
        word += letters[random.randint(0, len(letters) - 1)]
    text = gen_captcha(word, 'porkys.ttf', 100, "tmp.jpg")
    r = open("tmp.jpg", "r").read()
    return [r, text]