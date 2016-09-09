# Practice with text justification
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

# Given a sentence and an n by m grid, print out that sentence repeatedly within that grid.
# The words should not get split up at the end of a line. Fill with spaces if there's leftover space.
# We'll print this out but also return a list of lists

def justify_line(incoming_index, index_count, words, num_columns):
    """
    incoming_index: the next word in the sentence to print
    index_count: dict containing counts of words on index
    words: dict containing indexed words
    num_columns: number of characters per line
    """
    char_sum = 0
    line_out = []
    while char_sum + index_count[incoming_index] <= num_columns:
        char_sum += (index_count[incoming_index] + 1) 
        line_out.append(words[incoming_index])
        incoming_index += 1
        incoming_index = incoming_index % len(words)
    print ' '.join(str(w) for w in line_out)
    assert(len(line_out) <= num_columns)
    return incoming_index, line_out

def text_justification(sentence, num_rows, num_columns):
    # Want a dict of word index to charcter count
    words = sentence.split(' ')
    index_count = {}
    words_index = {}
    for idx, word in enumerate(words):
        words_index[idx] = word
        index_count[idx] = len(word)

    incoming_index = 0
    paragraph = []
    line_out = []
    for line in range(0, num_rows):
        # For each line, we need to know the incoming position
        incoming_index, line_out = justify_line(incoming_index, index_count, words_index, num_columns)
        paragraph.append(line_out)
    return paragraph

sentence = "The thick red brick jumps through Reed Dame\'s barbershop window."
num_rows = 10
num_columns = 40

print text_justification(sentence, num_rows, num_columns)


