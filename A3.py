def solution(scoville, K):
    answer = 0
    scovile = sorted(scoville)
    while scovile[0] < 7:
        min = scovile.pop(0)
        second = scovile.pop(0)
        shake = min + second*2
        scovile.append(shake)
        scovile = sorted(scovile)
        answer+=1
        
    if any(i<7 for i in scovile):
        return -1
    
    return answer
