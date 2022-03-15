def solution(prices):
    answer = []
    stack = [(idx+1,i) for idx,i in enumerate(prices)]
    #print(stack)
    while len(stack)!=0:
        clist = stack.copy()
        top = stack.pop(0)
        clist.sort(key=lambda x: x[1])
        if clist[0][1]<top[1]:
            ans = stack[stack.index(clist[0])][0]-top[0]
            #print(ans)
            answer.append(ans)
        else:
            #print(len(stack))
            answer.append(len(stack))
    
    return answer
