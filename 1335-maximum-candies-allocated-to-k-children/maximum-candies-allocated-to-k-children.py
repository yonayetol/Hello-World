class Solution:
    def maximumCandies(self, candies, k):
        def isGood(candy):
            haveGot = 0
            for candie in candies:
                haveGot += candie//candy
            return haveGot >= k


        minicandy = 1
        maxicandy = 10**12
        while minicandy <= maxicandy:
            midcandy = (maxicandy + minicandy)//2
            if isGood(midcandy):
                minicandy = midcandy + 1
            else:
                maxicandy = midcandy - 1

        return maxicandy
