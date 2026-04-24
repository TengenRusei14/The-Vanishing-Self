# Black Jack for Ren'Py by PerssonTM

Adding this to your game will allow you to play blackjack anywhere in your scripts.

## Usage
You can start playing blackjack anywhere in your script by using `call blackjack`
After the player has finished playing, their game will continue from the point blackjack was called.


## Example
```py

eileen "Wow look a blackjack table, lets play!"

call blackjack

eileen "Yipii, I won so much money!"
eileen "Lets move on to other business."

```

## Variables

- You can change the bet amounts, the sounds and the player starting money.

- If you already have a money variable in your game, there is an option to sync it.

- You can also adjust if the players are allowed to roll back during the minigame.

You can find these options in the `bj.variables.rpy` file.
