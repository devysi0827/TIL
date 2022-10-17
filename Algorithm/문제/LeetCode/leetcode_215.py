class Solution(object):
    from collections import deque
    def findKthLargest(self,nums, k):
        # nums.sort(reverse=True)
        # return nums[k-1]
        global answer
        answer = []
        num_queue = deque()
        for i in nums:
            num_queue.append(i)

        def divide_sort(my_queue):
            global answer
            number = my_queue.popleft()


            low_q = deque()
            high_q = deque()
            for i in range(len(my_queue)):
                now_num = my_queue.popleft()
                if now_num > number:
                    high_q.append(now_num)
                else:
                    low_q.append(now_num)

            if len(high_q) >= 2:
                divide_sort(high_q)
            elif len(high_q) == 1:
                answer.append(high_q.popleft())
            answer.append(number)
            if len(low_q) >= 2:
                divide_sort(low_q)
            elif len(low_q) == 1:
                answer.append(low_q.popleft())

        divide_sort(num_queue)
        
        return answer[k-1]

        
        