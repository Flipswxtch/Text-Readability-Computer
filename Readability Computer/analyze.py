"""The analyze module uses the Flesch-Kincaid readability test to analyze text and 
then produces a readability score. The resulting score is then equated to a grade-based
reading category.
"""

import ch1text

def count_syllables(words):
    """Takes a list of words and returns a total count of syllables
        across all words in the list"""
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count

def count_syllables_in_word(word):
    """Takes a word in the form of a string and returns the number 
        of syllables in that word. As this function is a heuristic, it is not 
        100% accurate."""
    count = 0

    endings = '.,;!?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]
    
    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word: 
        if char in vowels:
            if not prev_char_was_vowel:
                 count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if processed_word[-1] in 'yY':
        count = count + 1
    
    return count

def count_sentences(text):
    """Counts the number of sentences in a string of text using period,
    semicolon, question mark, and exlamation marks as terminals."""
    count = 0

    punctuation = '.;?!'
    for char in text:
        if char in punctuation:
            count = count + 1
    return count

def output_results(score):
    """Takes Flesch-Kincaid score and prints the corresponding reading level."""
    if score >= 90:
        print('Reading level of 5th grade')
    elif score >= 80:
        print('Reading level of 6th grade')
    elif score >= 70:
        print('Reading level of 7th grade')
    elif score >= 60:
        print('Reading level of 8-9th grade')
    elif score >= 50:
        print('Reading level of 10-12th grade')
    elif score >= 30:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')





def compute_readability(text):
    """Takes a string of any length and prints out a grade-based readability score."""
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    score = (206.835 - 1.015 * (total_words / total_sentences)
                        - 84.6 * (total_syllables / total_words))

    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')
    print(score, 'reading ease score')
    output_results(score)

if __name__ == "__main__":
    import ch1text
    print('Chapter1 Text:')
    compute_readability(ch1text.text)