import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                string = file.read()
            _words = re.split('[^a-zа-яё\']+', string.lower())
            all_words[file_name] = _words
        return all_words

    def find(self, word):
        _word = word.lower()
        result = {}
        words_in_files = self.get_all_words()
        for file in words_in_files.keys():
            index = 0
            if _word in words_in_files[file]:
                index = words_in_files[file].index(_word)
            if index > 0:
                result[file] = index
                break
        return result

    def count(self, word):
        _word = word.lower()
        result = {}
        words_in_files = self.get_all_words()
        for file in words_in_files.keys():
            count = 0
            for one_word in words_in_files[file]:
                if one_word == _word:
                    count += 1
            if count > 0:
                result[file] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


