from PIL import Image

class Grafika:
    def __init__(self, filename):
        self.filename = filename
        im = Image.open(filename)
        self.width, self.height = im.size
        self.rgb = im.split()


    def sharp(self):
        kernel = [[0, -2, 0], [-2, 11, -2], [0, -2, 0]]
        processed_img = Image.new("RGB",(self.width, self.height),color=None)
        for i in range(0, self.width):
            for j in range(0, self.height):
                if (i == 0) or (i == self.width - 1) or (j == 0) or (j == self.height - 1):
                    processed_img.putpixel((i, j), (self.rgb[0].getpixel((i, j)), self.rgb[1].getpixel((i, j)), self.rgb[2].getpixel((i, j))))
                else:
                    red = 0
                    green = 0
                    blue = 0
                    for k in range (0, 3):
                        for l in range(0, 3):
                            red += kernel[k][l] * self.rgb[0].getpixel((i-1+k, j-1+l))
                            blue += kernel[k][l] * self.rgb[1].getpixel((i-1+k, j-1+l))
                            green += kernel[k][l] * self.rgb[2].getpixel((i-1+k, j-1+l))

                    red = (int)(red)
                    green = (int)(green)
                    blue = (int)(blue)
                    processed_img.putpixel((i, j), (red, blue, green))

        processed_img.save(self.filename.split(".")[0]+"_filtr_wyostrzanie."+self.filename.split(".")[1])


obraz = Grafika('obraz.jpg')
obraz.sharp()