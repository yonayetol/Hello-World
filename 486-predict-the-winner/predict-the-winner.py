class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right, turn):
            if left == right: # the base case when there is only one number left in the array
                got = [0,0]
                endNum = nums[left]
            else:
                # we can toggle the next turn using (turn+1)%2 which will give us 0 for 1 and 1 for 0
                # we are just being greedy and fair not biased to make one player winner so lets take left and give the rest array to the other guy
                scoreusingleft = helper(left+1, right, (turn+1)%2)
                # the same thing now what if should take the right and leave the rest array for the other guy
                scoreusingright = helper(left, right-1, (turn+1)%2)

                # it is our turn so we have to take the best one, we don't care abt the other guy but nums[left] and nums[right] have to be considered
                if scoreusingleft[turn] + nums[left] > scoreusingright[turn] + nums[right]:
                    got = [scoreusingleft[0], scoreusingleft[1]]
                    endNum= nums[left]
                else:
                    got = [scoreusingright[0], scoreusingright[1]]
                    endNum = nums[right]

            got[turn] += endNum
            # the calculation ends here, now got is the a list containing the maximum player one can got and the maximum player 2 can got (this is not unfair since the first boy is greedy he will try to take the upper hand if he can(always))
            return got

        answer = helper(0,len(nums)-1,0) # player one plays first
        
        return answer[0] >= answer[1]