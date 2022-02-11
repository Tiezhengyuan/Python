from typing import List
'''
binary search on ascending sorted list
prerequisite:
1. data type: array or list
2. ascedning sorted
3. at least one element
4. no duplicates.If there is, one of index would be returned. 
'''
class BinarySearch:
    def __init__(self):
        pass

    def get_mid(self, L: int, M: int, R: int) -> tuple:
        """
        get middle point
        1. args: R>L, R>=0, L>=0
        2. args: M should be any value between L and R-1
            could be None: return midpoint of L-R
            or postive:  return midpoint of (M+1)-R
            or negative: return midpoint of L-(M-1)
        3. return: 
            Usually: L<=M<R
            if M==None, then L>=R.  NO midpoint is detected
            Note: not change on L, M, R if M=0, and L-R = [0,0] or [0,1] 
        """
        if L < R:
            if M is None:
                return L, int(L/2+R/2), R
            if M < 0:
                R = abs(M)
                if L < R:
                    return L, int(L/2+R/2), R
            elif M > 0:
                L = M + 1
                if L < R:
                    return L, int(L/2+R/2), R
        return L, None, R
    
    def search(self, nums: List[int], target: int) -> int:
        """
        return index if target exists or -1 if not
        """
        L, M, R = 0, None, len(nums)
        while R >= L:
            #print("<<input: ", L, M, R)
            L, M, R=self.get_mid(L, M, R)
            #print("mid: ", L, M, R)
            #the order of if-statement matters
            if M is None:
                return -1
            if target == nums[M]:
                return M
            if target < nums[M]:
                M = -abs(M)
            #print("after: ", L, M, R)
        return -1


    def search_insert(self, nums: List[int], target) -> int:
        """
        return index if target exists or
        insertion index if that doesn't exist
        """
        L, M, R = 0, None, len(nums)
        while R >= L:
            #print("\n<<: ", L, M, R)
            L, M, R=self.get_mid(L, M, R)
            #print("\tafter: ", L, M, R)
            #the order of if-statement matters
            if M is None: return L
            if target == nums[M]: 
                while M > 0 and target == nums[M-1]:
                    M-=1
                return M
            elif target < nums[M]:
                if M==0: return 0;
                M = -abs(M)
            else:
                if M==0: return 1
            #print("\t>>: ", L, M, R)
        return 0


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        return the index of two elements if sum of them are equal to target
        """
        #detect the split point
        mid_index = self.search_insert(numbers, target/2)
        if numbers[mid_index] == target/2: mid_index += 1 
        # print(f"left point falls in[0, {mid_index})\n")
        L1, R1 = 0, mid_index

        #detect the most right point
        right_index = self.search_insert(numbers, target)
        while right_index<len(numbers)-1 and numbers[right_index]<=target:
            right_index+=1
        if right_index == mid_index: right_index += 1
        # print(f"right point falls in [{mid_index}, {right_index})\n")

        while L1 < R1:
            # print(">>left value: ", numbers[L1])
            right_target = target - numbers[L1]
            L2, M2, R2 = mid_index, None, right_index
            while True:
                L2, M2, R2= self.get_mid(L2, M2, R2)
                if M2 is None: break
                # print("right value: ", numbers[M2])
                if right_target == numbers[M2]:
                    return [L1+1, M2+1]
                elif right_target < numbers[M2]:
                    M2 = -abs(M2)
            L1 += 1
        return None
            
