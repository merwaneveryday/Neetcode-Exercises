def main():
    prices = [10,1,5,6,7,1]

    left_pointer, right_pointer = 0, 1
    maxProfit = 0

    while right_pointer < len(prices):
        if prices[left_pointer] < prices[right_pointer]:
            profit = prices[right_pointer] - prices[left_pointer]
            maxProfit = max(profit, maxProfit)
        else:
            left_pointer = right_pointer
        right_pointer += 1

    print(maxProfit)

if __name__ == "__main__":
    main()
