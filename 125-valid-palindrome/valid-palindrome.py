class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_set = 'abcdefghijklmnopqrstuvwxyz0123456789'
        #s_set = list(s)

        start_pointer = 0
        end_pointer = len(s)-1
        len_s = len(s)
        #loop_c = 0

        while (start_pointer <= end_pointer ): #and loop_c < len_s 
       
         #if start_pointer>= 0 and  end_pointer >= 0:  
            if  (s[start_pointer].lower())  not in lower_set:
                start_pointer+=1
                continue
            if  (s[end_pointer].lower())  not in lower_set :
                end_pointer-=1   
                continue
         
         #if start_pointer>= 0 and  end_pointer >= 0: 
            if   (s[start_pointer].lower()) != (s[end_pointer].lower()) :
                return False
                #return end_pointer
            start_pointer+=1
            end_pointer-=1        
                
        #loop_c+=1   
        return  True
        