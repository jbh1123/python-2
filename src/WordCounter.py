class WordCounter:

    def __init__(self, sentence):
        self.__sentence = sentence
    
    def count_words(self):
        self.__word_count = len(self.__sentence.split(' '))
    
    def get_shortest_word(self):
        return len(min(self.__sentence.split(' '), key=len))

    def get_longest_word(self):
        return len(max(self.__sentence.split(' '), key=len))

    def get_word_count(self):
        return int(self.__word_count)
