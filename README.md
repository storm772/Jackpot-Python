# Jackpot Python
### What is that
A little project just to learn Python<br>
It's Y-Independent because im bored to make every single row slot independent and because i did it faster i can<br>

### Y-Independent? what is that
The code will only check if Y axis is the same, Example:<br>
<ins>**X**</ins> Y Y <br>
<ins>**X**</ins> Y Y <br>
<ins>**X**</ins> Y Y

It's so simple, like, very very simple, dont judge me 😢<br>
I plan on improving it and probably in future create a pygame or tkinter gui for that, on console looks really ugly!

__By the way, I created a video doing this game from scratch, go check it out! https://youtu.be/Csyg3R8NMV0__

### How to play
`python3 game.py`, the jackpot will start at 0 in each slot, if you say `y` or `yes`, it will re-roll the jackpot, if you say `n` or `no`, it will exit the program!<br>
Player wins when they get 3 same slots in Y-axis

### How does it works?
First of all, sets three (3) emojis: <br>
```
boom = '💥'
money = '💲'
trident = '⚜'
``` 
Then put them on a charList, which will replace row1/2/3 with their respective emojis.<br>
After that, sets the function `game()` which is the main core of the game, it beings saying what is the initial state of the Jackpot, which (ever) will probably show `[ 0 ]` in every single slot.<br>
Then, it asks what you want to do, if you want to re-roll or just quit the game. <br>
If you chose re-roll, it will trigger the `randomize()` function, which does: <br>
1. Shuffle each char list and replace all the rows with the new char list.
2. Trigger `checkSame()` function, which simple check if a row has the same emoji in every Y-axis row. If it does, just tell you!


