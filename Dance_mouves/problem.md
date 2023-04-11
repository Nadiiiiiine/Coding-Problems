Dancin' back and forth

Paul wants to learn some simple dance moves, and look at a manual with step movements to follow. These are simple movements going backward and forward. For each dance, the manual gives two lines : one with the number of steps to take, and one with the direction to take.

When going forward, Paul's position goes up by one for each step taken, and when going backward, Paul's position goes down by one for each step taken.
The manual also gives moments to clap to match the music. In this case, Paul's position doesn't change.

Help Paul by predicting where he should end its dance depending on his initial position.
Input
Line 1 : init_pos the initial position of Paul and complexity the number of movements there are, separated with a space
Line 2 : A total of complexity movement separated with space, where movement is a positive integer or CLAP
Line 3 : A total of complexity direction NOT separated with space, where direction is either F for forward, B for backward or C for clapping
Output
final_pos the final position of Paul after making all the dance movements
Constraints
-100000 < init_pos < 100000
0 < complexity < 128
0 < movement < 10000 or movement = CLAP
direction is an uppercase character, either F, B or C
Example
Input
0 3
3 CLAP 3
FCB

Output
0
