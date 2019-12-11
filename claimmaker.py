import random

# Define a function to follow through the resulting flowchart dictionary
def claim(dictionary, start=0, mousehover=True):
    """Function to build a calendar claim using the flowchart dictionary.

    Parameters:
        dictionary (dict): the flowchart contents as a Python dict
        start (int): the starting position

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
    # Remove a space before question mark and replace the one following it with a line break
    question_mark = sentence.index('?')
    end, start = question_mark - 1, question_mark + 2
    sentence = sentence[:end] + '?\n' + sentence[start:]

    return sentence
