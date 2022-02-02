from game import Card, Deck, Game


def test_create_deck():
    d = Deck()
    deck = d.create_deck()
    assert deck[0] == ('♠', '2')



def test_create_shuffled_deck():
    d = Deck()
    deck1 = d.create_deck(shuffle = True)
    deck2 = d.create_deck(shuffle = True)

    assert deck1 != deck2

def test_deal_hands():
    d = Deck()
    deck = d.create_deck()
    hands = deal_hands(deck)
    assert len(hands) == 4
    hand = hands[0]
    for card in hand:
        assert card in deck

def test_player_order():
    game = Game()
    result = game.player_order(names = ['fred', 'bob', 'joe'], start = 'joe')
    assert result == ['joe', 'fred', 'bob']
    


