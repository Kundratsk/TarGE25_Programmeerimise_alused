"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialize a card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Return a string representation of the card."""
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    value_order = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }

    def __init__(self):
        """Initialize the hand."""
        self.cards_in_hand = []

    def can_add_card(self, card: Card) -> bool:
        """Check card validity."""
        if card.suit not in self.suits:
            return False

        if card.value not in self.values:
            return False

        if len(self.cards_in_hand) >= 5:
            return False

        for existing_card in self.cards_in_hand:
            if existing_card.suit == card.suit and existing_card.value == card.value:
                return False

        return True

    def add_card(self, card: Card):
        """Add a card to the hand."""
        if self.can_add_card(card):
            self.cards_in_hand.append(card)
        else:
            print("Käsi on täis või kaart on vale")

    def can_remove_card(self, card: Card):
        """Check if a card can be removed from the hand."""
        for removable_card in self.cards_in_hand:
            if removable_card.suit == card.suit and removable_card.value == card.value:
                return True
        return False

    def remove_card(self, card: Card):
        """Remove a card from the hand."""
        if self.can_remove_card(card):
            self.cards_in_hand.remove(card)

    def get_cards(self):
        """Return cards as objects."""
        return self.cards_in_hand

    def is_straight(self):
        """Check if the hand is a straight."""
        if len(self.cards_in_hand) != 5:
            return False

        sorted_cards = sorted(self.cards_in_hand, key=lambda x: self.value_order[x.value])

        for i in range(len(sorted_cards) - 1):
            if self.value_order[sorted_cards[i + 1].value] != self.value_order[sorted_cards[i].value] + 1:
                return False

        return True

    def is_flush(self):
        """Check if all cards have the same suit."""
        if len(self.cards_in_hand) != 5:
            return False

        suits = [card.suit for card in self.cards_in_hand]
        return len(set(suits)) == 1

    def is_straight_flush(self):
        """Check for straight flush."""
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        """Check for full house."""
        counts = {}
        for card in self.cards_in_hand:
            counts[card.value] = counts.get(card.value, 0) + 1

        return sorted(counts.values()) == [2, 3]

    def is_four_of_a_kind(self):
        """Check for four of a kind."""
        counts = {}
        for card in self.cards_in_hand:
            counts[card.value] = counts.get(card.value, 0) + 1

        return 4 in counts.values()

    def is_three_of_a_kind(self):
        """Check for three of a kind."""
        counts = {}
        for card in self.cards_in_hand:
            counts[card.value] = counts.get(card.value, 0) + 1

        return 3 in counts.values() and not self.is_full_house()

    def is_pair(self):
        """Check for a pair."""
        counts = {}
        for card in self.cards_in_hand:
            counts[card.value] = counts.get(card.value, 0) + 1

        return list(counts.values()).count(2) == 1

    def get_hand_type(self):
        """Return the poker hand type."""
        if len(self.cards_in_hand) != 5:
            return None

        if self.is_straight_flush():
            return "straight flush"
        if self.is_four_of_a_kind():
            return "four of a kind"
        if self.is_full_house():
            return "full house"
        if self.is_flush():
            return "flush"
        if self.is_straight():
            return "straight"
        if self.is_three_of_a_kind():
            return "three of a kind"
        if self.is_pair():
            return "pair"

        return "high card"

    def __repr__(self):
        """Return a string representation of the hand."""
        cards_str = ", ".join(str(card) for card in self.cards_in_hand)
        hand_type = self.get_hand_type()

        if hand_type:
            return f"I got a {hand_type} with cards: {cards_str}"
        else:
            return f"I'm holding {cards_str}"