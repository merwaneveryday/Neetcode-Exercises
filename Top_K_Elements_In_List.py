class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count = {} #Key : nombre d'occurences -> Value : num(s)
        freq = [[] for i in range(len(nums) + 1)] #Crée une liste avec autant de [] qu'il y a de nums + 1 (pour la frequence 0)

        for n in nums:
            count[n] = count.get(n, 0) + 1 #A la key n, incrémente la value actuelle. Si pas de value, crée une value 0 et ajoute 1

        for n, c in count.items(): #Pour chaque key-value pair
            freq[c].append(n) #Dans l'emplacement c (occurences par l'index) de l'array freq, ajoute la value n
            #L'index devient le nombre d'occurences, par ex. tous les nombres qui apparaissent une fois seront dans freq[1]

        result = []
        for i in range(len(freq) - 1, 0, -1): #len(freq) - 1 = dernier index de len(freq), fin à 0, step -1
            for n in freq[i]: - freq[6], freq[5], freq[4], etc.
                result.append(n) #On append les values qui arrivent en premier car on cherche les plus hautes
                if len(result) == k: #Des que la longueur de result est égale à K, on est bon
                    return result 
        

