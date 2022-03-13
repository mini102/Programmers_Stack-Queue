def solution(progresses, speeds):
    answer = []
    #map = {}
    daylist =[]
    
    for index,pro in enumerate(progresses):
        day=0
        speed = 0 
        while pro+speed < 100:
            day+=1
            speed = speeds[index]*day
        #map[pro] = day
        daylist.append(day)
        
    #print(map)
    
    #vlist = list(map.values())
    
    for index,v in enumerate(daylist):
        if index!=0 and v<daylist[index-1]:
            daylist[index] = daylist[index-1]
    
    #print(daylist)
    
#     for index,k in enumerate(list(map.keys())):
#         map[k] = vlist[index]
        
#     print(map)
    
    count={}
    # lists = list(map.values())
    for i in daylist:
        try: count[i] += 1
        except: count[i]=1
    #print(count)
    
    answer = list(count.values())
    return answer
