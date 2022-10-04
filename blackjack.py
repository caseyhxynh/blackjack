import random
FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


def deal_card():
   
   playing_card = random.choice(CARD_LABELS)
   return playing_card
def get_card_value(card_label):
   
   if card_label == 'A':
       return ACE_VALUE
   elif card_label == '2':
       return 2
   elif card_label == '3':
       return 3
   elif card_label == '4':
       return 4
   elif card_label == '5':
       return 5
   elif card_label == '6':
       return 6
   elif card_label == '7':
       return 7
   elif card_label == '8':
       return 8
   elif card_label == '9':
       return 9
   elif card_label == '10':
       return 10
   elif card_label == "J" or card_label == "Q" or card_label == "K":
       return FACE_CARD_VALUE
def deal_cards_to_player():
   
   card_1 = deal_card()
   card_2 = deal_card()
   total_value = get_card_value(card_1) + get_card_value(card_2)
   print("Player drew {} and {}.".format(card_1, card_2))
   print("Player's total is {}.".format(total_value))
   print('')
   hit_or_stay = None
   while hit_or_stay != 's':
       hit_or_stay = input("Hit (h) or Stay (s)? ")
       print('')
       if hit_or_stay == "h":
           added_card = deal_card()
           total_value = total_value + get_card_value(added_card)
           print("Player drew {}.".format(added_card))
           print("Player's total is {}.".format(total_value))
           print('')
       if total_value >= BLACKJACK:
           hit_or_stay = 's'

   return total_value
def deal_cards_to_dealer():
   
   card_3 = deal_card()
   card_4 = deal_card()
   total_value = get_card_value(card_3) + get_card_value(card_4)
   print("The dealer has", card_3, "and", card_4 + ".")
   print("Dealer's total is", str(total_value) + ".")
   print('')
   while not total_value > DEALER_THRESHOLD:
       added_card = deal_card()
       print("Dealer drew {}.".format(added_card))
       total_value = total_value + get_card_value(added_card)
       print("Dealer's total is {}.".format(total_value))
       print('')
   return total_value
def determine_outcome(player_total, dealer_total):

   if dealer_total == BLACKJACK:
       print("YOU LOSE!")
       print('')
   elif player_total > BLACKJACK:
       print("YOU LOSE!")
       print('')
   elif dealer_total > BLACKJACK:
       if player_total <= BLACKJACK:
           print("YOU WIN!")
           print('')
       else:
           print("YOU LOSE!")
           print('')
   elif player_total > dealer_total:
       print("YOU WIN!")
       print('')
   elif dealer_total > player_total:
       print("YOU LOSE!")
       print('')
   elif dealer_total == player_total:
       print("YOU LOSE!")
       print('')

def play_blackjack():
   
   play_again = "Y"
   print("Let's Play Blackjack!")
   print('')
   while play_again != "N":
       if play_again == "Y":
           player_total = deal_cards_to_player()
           if player_total > BLACKJACK:
               determine_outcome(player_total, dealer_total = 0)
           else:
               dealer_total = deal_cards_to_dealer()
               determine_outcome(player_total, dealer_total)
       play_again = input("Play again (Y/N)? ")
       print('')
   print("Goodbye.")

def main():
  
   play_blackjack()



main()
