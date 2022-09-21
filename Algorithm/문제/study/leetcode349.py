
def intersection(self, nums1, nums2):
    def delete_overlap(arr):
        return list(set(nums1))
        
    answer = []
    first_arr = delete_overlap(nums1)
    second_arr = delete_overlap(nums2)
    for num in first_arr:
        if num in second_arr:
            answer.append(num)
    
    print(sorted(answer))


def canFinish(numCourses, p):
    
    if p == []:
        return True
    
    def find_number(arr,num):
        for num_idx in range(len(arr)):
            if arr[i] == num:
                return num_idx
            
    class_order = p[0]
    for i in range(1,len(p)):
        now_prereq = p[i]

        for j in range(len(now_prereq)):
            if now_prereq[j] in class_order:
                class_order_idx = find_number(class_order,now_prereq[j])
                
                class_left_order = class_order[:class_order_idx]
                now_prereq_right_order = now_prereq[j:]
                
                for num in class_left_order:
                    if num in now_prereq_right_order:
                        return False
                    
                for k in range(len(now_prereq_right_order)):
                    class_order.insert(j,now_prereq_right_order[k])
    return True
print(canFinish())
                    
                    
                
                        
                        
                
                
            
        