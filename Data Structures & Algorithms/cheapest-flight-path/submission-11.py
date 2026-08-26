class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # bell-man ford algorithm
        prices = [float("inf")] * n
        prices[src] = 0

        while k >= 0:
            tempPrices = prices.copy()
            for s, d, p in flights:  # s=source, d=destination, p=prices
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p

            prices = tempPrices
            k -= 1

        return prices[dst] if prices[dst] != float("inf") else -1
