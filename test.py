class tt:
    def __init__(self,va):
        self.n=va
        self.i = 0
    def a(self):
        try:
            self.i = self.n/0
        except Exception as e:
            print(e,'   bindass')

c=tt(1)
c.a()
