# GameOfChance
This project combines 4 games:
- Coinflipping to see if heads or tails.  Player needs to respond with "Heads" or "Tails" as well as how much they are going to bet on the coin flip.  If the player wins the game, will return the amount that they won.  If they lost, should return the amount lost as a negative number.
- Cho-Han - Two dice added together to see if total is odd or even and wins if prediction is correct.  The player is expected to guess if result is "Odd" or "Even" as well as amount they are going to bet on this.
- Simulate 2 players picking a card randomly from deck of cards.  The higher number wins.  Once again, this should allow a player to bet an amount of money on whether they have a higher card.  In this game, there can be a tie and if so, player gets 0 (doesn't win or lose money).
- Roulette - Random number should be generated that determines which space the ball lands on.  This allows player to guess if lands at "Odd", "Even", or at 0 or 00 spots.

Player will be asked to select one of 4 games indicated as well as how much they would like to bet for this whole round.  Once that game is done, they will be asked again if would like to carry on and need to input "Yes" or "Y", else game will end and return the money.

This program includes edge checks for the following:
- Flagging up issue when player bets with more money than they have
- Flagging up when player bets with negative money
- If player calls for "heads" or "Heads!" rather than "Heads", that will be flagged up as well
