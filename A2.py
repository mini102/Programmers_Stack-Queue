def solution(priorities, location):
    answer = 0
    queue = []
    
    for index,i in enumerate(priorities):
        waiting = {}
        waiting[index] = i
        queue.append(waiting)
        
    #print(queue)
    top = queue.pop(0)
    

    index = 0
    while index < len(queue):
        if list(queue[index].values())[0] > list(top.values())[0]:
            queue.append(top)
            top = queue.pop(0)
            index = 0
            continue
        index+=1
    queue.insert(0,top)
    
    ## answer 구하기
    for index,q in enumerate(queue):
        if list(q.keys())[0] == location:
            answer = index+1
    
    return answer
