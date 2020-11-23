class Card:
    k1 = 1
    k2 = 2
    k3 = 3
    k4 = 4
    k5 = 5
    values = [k1, k1, k1, k2, k2, k3, k3, k4, k4, k5]
    suits = ["R", "W", "B", "G", "Y"]

    def __init__(self, idx):
        self.idx = idx # 0 - 49

    def GetValue(self):
        return self.values[int(self.idx%10)]

    def GetSuit(self):
        return self.suits[int(self.idx/10)]

    def GetCode(self):
        return str(self.GetSuit()) + str(self.GetValue())

if __name__ == "__main__":
    c = Card(18)
    print(c.GetCode())
