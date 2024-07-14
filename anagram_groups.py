from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list) #Initializes a list that takes dicts as elements
        result = [] 

        for string in strs:
            sorted_str = tuple(sorted(string)) #Tuple for key value as key needs to be immutable
            anagramList[sorted_str].append(string) #Append all anagrams in their base form to the corresponding key, ["a", "e", "t"] -> ["eat", "ate", "tea"]

        for value in anagramList.values():
            result.append(value)

        return result        
