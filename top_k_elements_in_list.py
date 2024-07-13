
def main():
        nums = [1,2,2,2,3,3,4,4]
        k = 3
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return(result)

def main2():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    count = {}
    freq = [[] for x in range(0, len(nums) + 1)]
    result = []

    for n in nums:
        count[n] = count.get(n, 0) + 1

    for i, n in count.items():
        freq[i].append(n)

    for i in range (len(freq) -1, 0, -1):
         for n in freq[i]:
              result.append(n)
              if len(result) == k:
                   print(result)
                
if __name__ == "__main__":
     main2()
