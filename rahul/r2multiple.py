class Flipkart:

    def __init__(self):
        self.tickets = "flight tickets"
        self.shoes = "formal"
        
    def filght_ticket(self):
        print("i can book any flight ticket ")

    def formal_shoes(self):
        print(" i cam sell  any type of formal shoes")

class Amazone:
    def __init__(self):
        self.aticket = "flight bus train"
        self.shirts = "casual shirts "

    def ticket_booking(self):
        print("i can book the flight bus and train tickets")

    def casual_shirts(self):
        print("i cam sell the any type of casual shirts")


class Tata_nuv():
    def __init__(self):
        Flipkart. __init__(self)
        Amazone.__init__(self)
        self.lab = "tata Labs"

    def lab_reports(self):
        print("i selll the lab reports ")


t1 = Tata_nuv()
print(t1.tickets)

