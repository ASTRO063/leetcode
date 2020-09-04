class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack) <=0:
                    return False
                if s[i]==')':
                    if stack[len(stack)-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif s[i]==']':
                    if stack[len(stack)-1]=='[':
                        stack.pop()
                    else:
                        return False
                elif s[i]=='}':
                    if stack[len(stack)-1]=='{':
                        stack.pop()
                    else:
                        return False
            # print("i=",i,stack)
        if len(stack)==0:
            return True
        else:
            return False
            
        