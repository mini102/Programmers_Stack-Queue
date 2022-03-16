def solution(prices):
    answer = [0]*len(prices)
    stack = [(idx+1,i) for idx,i in enumerate(prices)]
    #print(stack)
    while len(stack)>0:
        clist = stack.copy()
        top = stack.pop(0)
        # print("top:{}".format(top))
        clist.sort(key=lambda x: x[1])
        # if clist[0][1]<top[1]:
        if clist[0][1]==top[1]:
                answer[top[0]-1] = len(stack)
                continue
        for idx,p in enumerate(stack):
            # print("idx: {}, p:{}".format(idx,p))
            if p[1]<top[1]:
                ans = p[0]-top[0]
                answer[top[0]-1]=ans 
                break
            # if idx == len(stack)-1:
            #     answer[top[0]-1] = len(stack)
    
    return answer

def solution(prices):
    answer = [0]*len(prices)
    stack = [(idx+1,i) for idx,i in enumerate(prices)]
    while len(stack)>0:
        top = stack.pop(0)
        for idx,p in enumerate(stack):
            if p[1]<top[1]:
                ans = p[0]-top[0]
                answer[top[0]-1]=ans 
                break
            if idx == len(stack)-1:
                answer[top[0]-1] = len(stack)
    
    return answer
