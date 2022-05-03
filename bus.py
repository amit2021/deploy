from Vehicle import Vehicle


class Bus(Vehicle):

    def seating_capacity(capacity):
         return super().seating_capacity(capacity=50)


    def fare(self):
        amount=super().fare()
        amount=amount+(.1*amount)
        return  amount

