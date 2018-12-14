# Chess Openings for Beginners

## Quick Stats based ways to improve your first four moves. Examining openings, castling, & checking

When I play chess, I feel that I fall behind early, sometimes after a few moves. Because the start of the game is much less chaotic, I thought the opening would be when low-elo players do best. But my poor early performance indicates that low-elo and high-elo openings are disparate. 

To test this I ran a few chi-square tests. (Specifically, the chi2_contingency test from the scipy library.) I ran the tests for the first white move, first white and black moves, and the first four moves. (Greater t-statistics and p-values closer to 0 indicate two distributions are different.)

1.  First white move: t-statistic of 17,679 and p-value of 0.0
2.  First move both sides: t-statistic of 2,899 and p-value of 0.0
3.  First four moves: t-statistic of 7,790 and p-value 0.0

This analysis shows low-elo players can still learn from the stronger  high-elo openings.

## What are the Strong Openings?

### First Move

We can see that the two classes play e4 and d4 at about the same rate. High-elo players start with Nf3 and c4 twice as much. 

In our database of high-elo openings,  g3 wins 1.41 times, followed by d4 1.36 times, c4 1.32 times, Nf3 1.3 times. e4 only has a win-rate of 1.21:1.

In the 2018 World Chess Championship, Magnus Carlsen played d4 twice, c4 twice, and e4 twice. Fabiano Caruana played e4 six times. All games were drawn. 

In the games released by Google DeepMind, Alpha Zero played d4 58 times winning 19, drawing 38, and losing 1\. AlphaZero played Nf3 23 times winning 12, drawing 11, and losing 0.

### Countering 1\. e4

When countering the most common opening, low-elo players play e5 over half the time. High-elo players play both e5 and c5 about 30% of the time. 

The high-elo opening database shows even stronger players still have a lot to learn. White only wins 1.08 times when black plays c5, but nearly 1.4 times when black plays e5.

           White_odds  
    move1b                       
    c5        1.080567 
    g6        1.111637 
    Nc6       1.206246 
    Nf6       1.209108 

    e5        1.399075 

    Carlsen countered e4 with c5 every time Caruana played it in the championship.

    AlphaZero countered e4 with e5 every time against Stockfish. 

### Countering 1.d4

Low-elo players counter d4 with d5 60% of the time. High-elo players play Nf6 and d5 about 40% and 35% of the time.

In the high-elo opening database, playing d6 actually puts the odds in blacks favor. Playing d5 gives white a huge advantage.

           White_odds  Num Games
    move1b                       
    d6        0.992931      18321
    g6        1.081049      23398
    e6        1.199456      16035
    Nc6       1.236885       1696
    Nf6       1.279563     729601

    d5        1.559140     443203

## Castling within for moves.

Working with these datasets, I noticed players castled early more often than I expected. 

### White Castling

    In the high-elo games, white castled 3.22% of the time with an average score of 0.58
    Not castling produced an average score of 0.52
    In the low-elo games, white castled 1.79% of the time with an average score of 0.57
    Not castling produced an average score of 0.52

    AlphaZero was white 81 times and did not castle once in the first four moves
    Stockfish8 was white 30 times and castled 11 times in the first four  moves. 36.67%
    The average score for Stockfish8 when castling was 0.41\. and 0.47 without castling

### Black Castling

    In the high-elo games, black castled 2.45% of the time with an average score of 0.5
    Not castling produced an average score of 0.48
    In the low-elo games, black castled 1.07% of the time with an average score of 0.55
    Not castling produced an average score of 0.48

    AlphaZero was black 30 times and castled once in the first four moves. 3.33% Stockfish8 was black 81 times and castled 17 times in the first four moves. 20.99%
    AlphaZero had an average score of 0.5 when castling and 0.55 without castling
    The average score for Stockfish8 when castling was 0.32\. and 0.31 without castling

    In total Stockfish8 castled 28 times in the first four moves, winning once, for an average score of 0.36

In the both high and low elo's, castling within the first four moves was stronger than not for black and white.

In computer chess, castling was a disadvantage. 

## Checking the within four moves

In my games, I put my opponents in check early. Is this a rookie mistake?

### Checking as White

    In the high-elo games, white checked 1.63% of the time with an average score of 0.46
    Not checking produced an average score of 0.52
    In the low-elo games, white checked 3.31% of the time with an average score of 0.47
    Not checking produced an average score of 0.52

    Neither AlphaZero nor Stockfish8 checked early as white in their showdown.

### Checking as Black

    In the high-elo games, black checked 2.47% of the time with an average score of 0.45
    Not checking produced an average score of 0.48
    In the low-elo games, black checked 3.31% of the time with an average score of 0.43
    Not checking produced an average score of 0.48

    AlphaZero did not bother checking as black. Stockfish8 put the opponent in check 13.58% of the 
    time with an average score of 0.36 and an average score of 0.3 without checking 

Checking early was a detriment to all human players but helped Stockfish against AlphaZero.