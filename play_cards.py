"""
Script to play a game of cards.

Well, OK, really just to demo the CardDeck and JokerDeck classes.
"""
from carddeck import CardDeck   # import CardDeck class from carddeck module
from jokerdeck import JokerDeck

# module: snake case      my_module_name or mymodulename
# class: Pascal case      MyClassName

# camelCase   myClassName
# kebab case  my-class-name

def main():
    """
    Program entry point

    :return: None
    """
    deck1 = CardDeck('Nellie')  # instantiate
    print(deck1)

    deck2 = CardDeck('Andy')
    deck3 = CardDeck('Rosie')

    # deck1.some_method()
    # deck1.some_property

    print(deck1.dealer)  # deck1.dealer() line 9

    deck1.dealer = "Frodo"  # deck1.dealer() line 13

    print(deck1.dealer)

    try:
        deck1.dealer = 1234
    except TypeError as err:
        print(err)

    print(deck1.dealer, deck2.dealer, deck3.dealer)

    deck1.shuffle()
    print(deck1.cards)
    print()

    for _ in range(5):
        rank, suit = deck1.draw()
        print(f"{rank} of {suit}")

    jokerdeck1 = JokerDeck("Alicia")
    jokerdeck2 = JokerDeck("Ferdinand")

    print(jokerdeck1)
    jokerdeck1.shuffle()
    print(jokerdeck1.cards)
    print(jokerdeck1.draw())

    print(deck1)  # print(str(deck1))
    print(jokerdeck1, deck1, jokerdeck2, deck2)

if __name__ == '__main__':
    main()
