Like Minded Weirdo's project for 2024-2025 First Lego League season - Submerged!

Similar to the game of life, the team build a model of the ocean using a cellular automata style game.  There are 4 main rules:

1) At the beginning of the game, pollution is randomly distributed across the top and bottom of the game board (lines 76/83 set percentage).
2) Every turn of the game, all life squares randomly 'drive' in the ocean current up to one position away in any of 8 adjacent spaces.
3) If there is pollution in any neighboring square, the life is killed.
4) If there is already life in the destination square, the alive square does not move.

red = pollution
green = life
purple = background color

That's it! 

Line 142 sets board size and size of each cells
line 123 sets game speed
Line 141 has the ability to loop the game on repeat for display purposes.
