class NN:
    hw11 = 0  # hw - hidden weight
    hw12 = 0
    hw21 = 0
    hw22 = 0
    ow11 = 0  # ow - output weight
    ow21 = 0
    lr = 0.05

    def __init__(self):
        self.hw11 = 0.11
        self.hw12 = 0.21
        self.hw21 = 0.12
        self.hw22 = 0.08
        self.ow11 = 0.14
        self.ow21 = 0.15

    def train(self, ins, target):
        in1 = ins[0]
        in2 = ins[1]
        h1 = in1 * self.hw11 + in2 * self.hw21
        h2 = in1 * self.hw12 + in2 * self.hw22
        out = h1 * self.ow11 + h2 * self.ow21
        print(out)
        print("Before: ")
        self.show()

        error = (target - out)**2

        error_h1 = self.ow11 / (self.ow11 + self.ow21) * error
        error_h2 = self.ow21 / (self.ow11 + self.ow21) * error

        self.ow11 += self.lr * error * h1
        self.ow21 += self.lr * error * h2

        self.hw11 += self.lr * error_h1 * in1
        self.hw12 += self.lr * error_h2 * in1
        self.hw21 += self.lr * error_h1 * in2
        self.hw22 += self.lr * error_h2 * in2
        print("After: ")
        self.show()

    def show(self):
        print(self.hw11)
        print(self.hw12)
        print(self.hw21)
        print(self.hw22)
        print(self.ow11)
        print(self.ow21)


ins = [1, 3]
target = 1
nn = NN()
nn.train(ins, target)
ins = [2, 3]
nn.train(ins, target)
