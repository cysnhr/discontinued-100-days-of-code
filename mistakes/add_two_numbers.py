# 20230112 

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1 = ""
        n2 = ""
        list1 = []
        list2 = []
        list1.append(l1.val)
        while l1.next is not None:
          l1 = l1.next
          list1.append(l1.val)

        list2.append(l2.val)
        while l2.next is not None:
          l2 = l2.next
          list2.append(l2.val)

        for i in range(0,len(list1)):
            i = len(list1) - i - 1 
            n1 += str(list1[i])
        
        for j in range(0,len(list2)):
            j = len(list2) - j - 1 
            n2 += str(list2[j])
        
        n1 = int(n1)
        n2 = int(n2)
        tmp = str(n1 + n2)
        res = []
        for r in range(0,len(tmp)):
            r = len(tmp) - r - 1 
            res.append(tmp[r])
        
        f_res = ListNode(res[0])
        print(f_res)
        o = 1
        
        """
        stuff is wrong here
        """
        
        while o < len(res) - 1:
            f_res.next = res[o]
            f_res.next = res[o+1]
            o += 1

        print(f_res)
