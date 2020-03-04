class JumbleSolver:
    def __init__(self, words_blanks):
        f = open("/usr/share/dict/words", "r")
        contents = f.read()
        self.words_list = contents.split("\n")
        f.close()
        self.permutation_lookup_table = {}
        letters = []
        for word, blanks in words_blanks:
            word_grams_letters = []
            anagrams = self.anagrams(word)
            print("Solutions for '" + word + "':")
            for anagram in anagrams:
                gram_letters = ""
                print(anagram)
                for blank in blanks:
                    gram_letters += anagram[blank]
                word_grams_letters.append(gram_letters)
            letters.append(word_grams_letters)
        print(letters)
        options = []
        for index, array in enumerate(letters):
            if index == 0:
                for string in array:
                    options.append(str(string))
            else:
                previous_word_options = options
                options = []
                for string in array:
                    for option in previous_word_options:
                        options.append(str(option + string))
        print(options)
        for index, option in enumerate(options):
            print("Set", index, "of possibilities:")
            print(self.permutations(option))


    def is_anagram(self, word1, word2):
        if len(word1) == 1:
            if word1 == word2:
                return True
            else:
                return False
        try:
            two_index = word2.index(word1[0])
            return self.is_anagram(word1[1:], word2[: two_index] + word2 [two_index+1:])
        except:
            return False

    def anagrams(self, text):
        anagram_list = []
        for word in self.words_list:
            if len(text) == len(word):
                if self.is_anagram(text, word):
                    anagram_list.append(word)
        return anagram_list

    def permutations(self, string, n=-1):
        all_perms = []
        if n < 1:
            n = len(string)
        if n == 1:
            all_perms.append(string)
        else:
            for i in range(n):
                if (string, n-1) in self.permutation_lookup_table:
                    new_additions = self.permutation_lookup_table[(string, n-1)]
                else:
                    new_additions = self.permutations(string, n-1)
                for new_string in new_additions:
                    all_perms.append(new_string)
                string = list(string) 
                if n % 2 == 0:
                    # swap elements 0 and n-1
                    string[0], string[n-1] = string[n-1], string[0]
                else: 
                    # swap elements i and n-1
                    string[i], string[n-1] = string[n-1], string[i]
                string = "".join(string)

        self.permutation_lookup_table[(string, n)] = all_perms
        return all_perms

if __name__ == "__main__":
    # jumble = JumbleSolver([("laisa", [1, 2, 3]), ("laurr", [0, 2]), 
    #     ("burreek", [0, 1]), ("prouot", [2, 4, 5])])
    jumble = JumbleSolver([("ulqit", [0]), ("lavees", [5]), ("beeestrmp", [0]),
        ("svrtaeh", [0]), ("tecthuns", [6]), ("aumutn", []), ("atolflob", [5])])