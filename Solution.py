from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Count the occurrences of each word in the first sentence
        word_count_1 = Counter(s1.split())
        
        # Count the occurrences of each word in the second sentence
        word_count_2 = Counter(s2.split())

        # List to store the uncommon words
        uncommon_words = []

        # Iterate through the words and their counts in the first sentence
        for word, count in word_count_1.items():
            # Add the word to the result if it appears exactly once in s1 and not in s2
            if count == 1 and word not in word_count_2:
                uncommon_words.append(word)

        # Iterate through the words and their counts in the second sentence
        for word, count in word_count_2.items():
            # Add the word to the result if it appears exactly once in s2 and not in s1
            if count == 1 and word not in word_count_1:
                uncommon_words.append(word)

        # Return the list of uncommon words
        return uncommon_words
