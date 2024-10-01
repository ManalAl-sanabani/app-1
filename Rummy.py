from deck import DeckOfCards

class RummyGame:
    def __init__(self):
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.player1_hand = [self.deck.deal_card() for _ in range(7)]
        self.player2_hand = [self.deck.deal_card() for _ in range(7)]
        self.discard_pile = [self.deck.deal_card()]

    def display_hand(self, player_hand, player_name):
        print(f"{player_name}'s hand: {[str(card) for card in player_hand]}")

    def draw_card(self, player_hand):
        player_hand.append(self.deck.deal_card())

    def discard_card(self, player_hand):
        card_to_discard = player_hand.pop(0)
        self.discard_pile.append(card_to_discard)
        return card_to_discard

    def check_for_sets(self, player_hand):
        face_counts = {}
        for card in player_hand:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1
        sets = [face for face, count in face_counts.items() if count >= 3]
        return sets

    def play_turn(self, player_hand, player_name):
        self.display_hand(player_hand, player_name)
        print(f"Top card on discard pile: {self.discard_pile[-1]}")
        action = input(f"{player_name}, do you want to draw a card or take the top discard? (draw/take): ").lower()
        if action == 'draw':
            self.draw_card(player_hand)
        else:
            player_hand.append(self.discard_pile.pop())

        self.display_hand(player_hand, player_name)
        discarded_card = self.discard_card(player_hand)
        print(f"{player_name} discarded: {discarded_card}")

        sets = self.check_for_sets(player_hand)
        if sets:
            print(f"{player_name} has a set: {sets}")
            for face in sets:
                player_hand[:] = [card for card in player_hand if card.face != face]

    def play_game(self):
        while self.player1_hand and self.player2_hand:
            print("\nPlayer 1's turn:")
            self.play_turn(self.player1_hand, "Player 1")
            if not self.player1_hand:
                break

            print("\nPlayer 2's turn:")
            self.play_turn(self.player2_hand, "Player 2")
            if not self.player2_hand:
                break

        if not self.player1_hand:
            print("\nPlayer 1 wins!")
        else:
            print("\nPlayer 2 wins!")

if __name__ == "__main__":
    game = RummyGame()
    game.play_game()
