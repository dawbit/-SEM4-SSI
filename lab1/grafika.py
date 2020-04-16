from PIL import Image

class Grafika:
    def __init__(self, filename):
        self.filename = filename
        im = Image.open(filename)
        self.width, self.height = im.size
        self.rgb = im.split()


    def gauss(self):
        kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
        processed_img = Image.new("RGB",(self.width, self.height),color=None)
        for i in range(0, self.width):
            for j in range(0, self.height):
                if (i == 0) or (i == self.width - 1) or (j == 0) or (j == self.height - 1):
                    processed_img.putpixel((i, j), (self.rgb[0].getpixel((i, j)), self.rgb[1].getpixel((i, j)), self.rgb[2].getpixel((i, j))))
                else:
                    tmpR = 0
                    tmpG = 0
                    tmpB = 0
                    for k in range (0, 3):
                        for l in range(0, 3):
                            tmpR += kernel[k][l] * self.rgb[0].getpixel((i-1+k, j-1+l))
                            tmpB += kernel[k][l] * self.rgb[1].getpixel((i-1+k, j-1+l))
                            tmpG += kernel[k][l] * self.rgb[2].getpixel((i-1+k, j-1+l))

                    tmpR = (int)(tmpR/16)
                    tmpG = (int)(tmpG/16)
                    tmpB = (int)(tmpB/16)
                    processed_img.putpixel((i, j), (tmpR, tmpB, tmpG))

        processed_img.save(self.filename.split(".")[0]+"_filtr_gauss."+self.filename.split(".")[1])

    def blur(self):
        kernel = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        processed_img = Image.new("RGB",(self.width, self.height),color=None)
        for i in range(0, self.width):
            for j in range(0, self.height):
                if (i == 0) or (i == self.width - 1) or (j == 0) or (j == self.height - 1):
                    processed_img.putpixel((i, j), (self.rgb[0].getpixel((i, j)), self.rgb[1].getpixel((i, j)), self.rgb[2].getpixel((i, j))))
                else:
                    tmpR = 0
                    tmpG = 0
                    tmpB = 0
                    for k in range (0, 3):
                        for l in range(0, 3):
                            tmpR += kernel[k][l] * self.rgb[0].getpixel((i-1+k, j-1+l))
                            tmpB += kernel[k][l] * self.rgb[1].getpixel((i-1+k, j-1+l))
                            tmpG += kernel[k][l] * self.rgb[2].getpixel((i-1+k, j-1+l))

                    tmpR = (int)(tmpR/9)
                    tmpG = (int)(tmpG/9)
                    tmpB = (int)(tmpB/9)
                    processed_img.putpixel((i, j), (tmpR, tmpB, tmpG))

        processed_img.save(self.filename.split(".")[0]+"_filtr_blur."+self.filename.split(".")[1])

    def sharpen(self):
        kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
        processed_img = Image.new("RGB",(self.width, self.height),color=None)
        for i in range(0, self.width):
            for j in range(0, self.height):
                if (i == 0) or (i == self.width - 1) or (j == 0) or (j == self.height - 1):
                    processed_img.putpixel((i, j), (self.rgb[0].getpixel((i, j)), self.rgb[1].getpixel((i, j)), self.rgb[2].getpixel((i, j))))
                else:
                    tmpR = 0
                    tmpG = 0
                    tmpB = 0
                    for k in range (0, 3):
                        for l in range(0, 3):
                            tmpR += kernel[k][l] * self.rgb[0].getpixel((i-1+k, j-1+l))
                            tmpB += kernel[k][l] * self.rgb[1].getpixel((i-1+k, j-1+l))
                            tmpG += kernel[k][l] * self.rgb[2].getpixel((i-1+k, j-1+l))

                    tmpR = (int)(tmpR)
                    tmpG = (int)(tmpG)
                    tmpB = (int)(tmpB)
                    processed_img.putpixel((i, j), (tmpR, tmpB, tmpG))

        processed_img.save(self.filename.split(".")[0]+"_filtr_sharpen."+self.filename.split(".")[1])


obraz = Grafika('base.jpg')
obraz.gauss()
obraz.blur()
obraz.sharpen()