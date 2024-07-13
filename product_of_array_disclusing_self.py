def main():
    nums = [1,2,4,6]

    result = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
          result[i] = prefix
          prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) -1, -1, -1):
          result[i] *= postfix
          postfix *= nums[i]
    print(result)
    
   
def main2():
    nums = [1, 2, 4, 6]
      
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n

    for i in range (n):
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

    print([l*r for l, r in zip(l_arr, r_arr)])
    

    
    
if __name__ == "__main__":
       main()
       main2()