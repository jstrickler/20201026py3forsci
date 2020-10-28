
import carddeck

d1 = carddeck.make_deck("Bob")

carddeck.shuffle(d1)

for i in range(5):
    card = carddeck.deal(d1)

