from game import SUITS, RANKS, Card, Deck, create_deck,deal_hands, choose, player_order, play


def test_create_deck():
    deck = create_deck()
    assert deck[0] == ('♠', '2')


def test_deck_noshuffle():
    deck1 = create_deck(shuffle = False)
    deck2 = create_deck(shuffle = False)
    assert deck1 == deck2


def test_create_shuffled_deck():
    deck1 = create_deck(shuffle = True)
    deck2 = create_deck(shuffle = True)

    assert deck1 != deck2

def test_deal_hands():
    deck = create_deck()
    hands = deal_hands(deck)
    assert len(hands) == 4
    hand = hands[0]
    for card in hand:
        assert card in deck

def test_choose():
    items = ['Doug', 'Bob', "Jiminy Cricket"]
    choice = choose(items)
    assert choice in items


def test_player_order():
    result = player_order(names = ['fred', 'bob', 'joe'], start = 'joe')
    assert result == ['joe', 'fred', 'bob']
    


