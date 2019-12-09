# Import the single dependency
import random

# Initialize a dict for a dictionary representation of the flowchart
choices = {}

# Manually enter each flowchart choice
# Each entry is a tuple with two items, a content string and a further tuple enumerating the possible next steps
# End points of the flowchart should have None in place of a next steps' tuple

choices[0] = ('Did you know that', tuple(i for i in range(1, 10)))

choices[1] = ('the', (10, 11))
choices[2] = ('the', (14, 15))
choices[3] = ('the', (19, 20))
choices[4] = ('daylight', (24, 25))
choices[5] = ('leap', (27, 28))
choices[6] = ('Easter', (13,))
choices[7] = ('the', (29, 30, 31))
choices[8] = ('Toyota Truck Month', (13,))
choices[9] = ('Shark Week', (13,))
choices[10] = ('fall', (12,))
choices[11] = ('spring', (12,))
choices[12] = ('equinox', (13,))
choices[14] = ('winter', (16,))
choices[15] = ('summer', (16,))
choices[16] = (None, (17, 18))
choices[17] = ('solstice', (13,))
choices[18] = ('Olympics', (13,))
choices[19] = ('earliest', (21,))
choices[20] = ('latest', (21,))
choices[21] = (None, (22, 23))
choices[22] = ('sunrise', (13,))
choices[23] = ('sunset', (13,))
choices[24] = ('saving', (26,))
choices[25] = ('savings', (26,))
choices[26] = ('time', (13,))
choices[27] = ('day', (13,))
choices[28] = ('year', (13,))
choices[29] = ('Harvest', (32,))
choices[30] = ('Supser', (32,))
choices[31] = ('Blood', (32,))
choices[32] = ('Moon', (13,))

choices[13] = (None, (33, 34, 35))
choices[33] = ('happens', (36, 37, 38))
choices[34] = ('drifts out of sync with the', (41, 42, 43, 44, 45, 46, 47, 48))
choices[35] = ('might', (50, 51))
choices[36] = ('earlier', (39,))
choices[37] = ('later', (39,))
choices[38] = ('at the wrong time', (39,))
choices[39] = ('every year', (40,))
choices[41] = ('Sun', (40,))
choices[42] = ('Moon', (40,))
choices[43] = ('zodiac', (40,))
choices[44] = ('Gregorian', (49,))
choices[45] = ('Mayan', (49,))
choices[46] = ('lunar', (49,))
choices[47] = ('iPhone', (49,))
choices[48] = ('atomic clock in Colorado', (40,))
choices[49] = ('calendar', (40,))
choices[50] = ('not happen', (52,))
choices[51] = ('happen twice', (52,))
choices[52] = ('this year', (40,))

choices[40] = ('because of', (53, 54, 55, 56, 57, 58, 59, 60, 61, 62))
choices[53] = ('time zone legislation in', (63, 64, 65))
choices[54] = ('a decree by the pope in the 1500s', (66,))
choices[55] = ('precession', (67,))
choices[56] = ('libration', (67,))
choices[57] = ('nutation', (67,))
choices[58] = ('libation', (67,))
choices[59] = ('eccentricity', (67,))
choices[60] = ('obliquity', (67,))
choices[61] = ('magnetic field reversal', (66,))
choices[62] = ('an arbitrary decision by', (68, 69, 70))
choices[63] = ('Indiana', (66,))
choices[64] = ('Arizona', (66,))
choices[65] = ('Russia', (66,))
choices[66] = ('?', (79,))
choices[67] = ('of the', (71, 72, 73, 74, 75, 76, 77))
choices[68] = ('Benjamin Franklin', (66,))
choices[69] = ('Isaac Newton', (66,))
choices[70] = ('FDR', (66,))
choices[71] = ('Moon', (66,))
choices[72] = ('Sun', (66,))
choices[73] = ("Earth's axis", (66,))
choices[74] = ('equator', (66,))
choices[75] = ('prime meridian', (66,))
choices[76] = ('international date', (78,))
choices[77] = ('Mason-Dixon', (78,))
choices[78] = ('line', (66,))

choices[79] = ('Apparently', (80, 81, 82, 83, 84, 85))
choices[80] = ('it causes a predictable increase in car accidents.', None)
choices[81] = ("that's why we have leap seconds.", None)
choices[82] = ('scientists are really worried.', None)
choices[83] = ('it was even more extreme during the', (86, 87, 88, 89))
choices[84] = ("there's a proposal to fix it, but it", (90, 91, 92, 93))
choices[85] = ("it's getting worse and no one knows why.", None)
choices[86] = ('Bronze Age.', None)
choices[87] = ('Ice Age.', None)
choices[88] = ('Cretaceous.', None)
choices[89] = ('1990s.', None)
choices[90] = ('will never happen.', None)
choices[91] = ('actually makes things worse.', None)
choices[92] = ('is stalled in Congress.', None)
choices[93] = ('might be unconstitutional.', None)

# There is one more choice in the comic's mousehover text
# It contains an introductory phrase and five possible endings
mousehover_intro = ' While it may seem like trivia, it '
mousehover_options = ('causes huge headaches for software developers',
                      'is taken advantage of by high-speed traders',
                      'triggered the 2003 Northeast Blackout',
                      'has to be corrected for by GPS satellites',
                      'is now recognized as a major cause of World War I')

# Define a function to follow through the resulting flowchart dictionary
def claim(dictionary=choices, start=0, mousehover=False,
          mousehover_intro=mousehover_intro, mousehover_options=mousehover_options):
    """Function to build a calendar claim using the flowchart dictionary.

    Parameters:
        dictionary (dict): the flowchart contents as a Python dict
        start (int): the starting position
        mousehover (bool): whether to include the mousehover bit
        mousehover_intro (str): the introductory phrase of the mousehover text
        mousehover_options (tuple): collection of alternative endings for the moushover text

    Output: a calendar-related claim as a string
    """
    # Initialize starting position on the flowchart dictionary
    key = start
    # Initialize storage space for the sentence components
    record = []
    # Begin a loop over steps in the flowchart
    while True:
        # Read the dictionary contents for the current step
        string, split = dictionary[key]
        # Add content string to storage (unless empty)
        if string is not None:
            record.append(string)
        # If next step selection is None, at the end of flowchart -> exit loop
        if split is None:
            break
        # Otherwise randomly pick the next position from available options
        key = random.choice(split)
    # Afterwards combine all elements into a single long sentence string
    sentence = ' '.join(record)
    # Remove whitespace preceding the question mark
    question_mark = sentence.index('?')
    sentence = sentence[:question_mark-1] + sentence[question_mark:]
    # Add the mousehover bit if appropriate
    if mousehover:
        addition = mousehover_intro
        addition = addition + random.choice(mousehover_options) + '.'
        sentence = sentence + addition
    return sentence
