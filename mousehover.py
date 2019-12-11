import random

# It contains an introductory phrase and five possible endings
mousehover_intro = 'While it may seem like trivia, it '
mousehover_options = ('causes huge headaches for software developers',
                      'is taken advantage of by high-speed traders',
                      'triggered the 2003 Northeast Blackout',
                      'has to be corrected for by GPS satellites',
                      'is now recognized as a major cause of World War I')

def add_mousehover(claim, intro=mousehover_intro, options=mousehover_options, separator='\n\n', ending='.'):
    """Function to add a mousehover bit to a pre-existing claim.
    
    Inputs the claim as a string,
    and outputs the claim with an added mousehover bit also as a string."""
    addition = separator + intro + random.choice(options) + ending
    return claim + addition
