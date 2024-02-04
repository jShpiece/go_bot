This is a bot capable of playing the game Go. 

dlgo //
    Agent // 
        base:
        helpers: FUnctions used for strategy - locating eyes on the board, or good point to play
        naive: a bot capable of playing by the rules - makes its moves entirely at random. 
    goboard_slow: Defines the go board and everything on it - functions that define groups on the board, tracking their positions and liberties, etc. Essentially, this contains the rules of the game. 
    gotypes:
    utils: Holds helper functions (mostly visualization)
bot_v_bot: Run to have two bots play against each other
bot_v_humanL: Run to have a bot play against human