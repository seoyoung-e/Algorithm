import heapq
def solution(jobs):
    jobs.sort()
    h=[]
    time, i, total_wait = 0, 0, 0
    count = len(jobs)
    
    while h or i<count: 
        while i < count and jobs[i][0] <= time:  # 현재 시간 이하로 요청된 작업을 힙에 넣기
            heapq.heappush(h, (jobs[i][1], jobs[i][0]))  # (소요시간, 요청시간)
            i += 1
        
        if  h:
            a,b=heapq.heappop(h) #소요시간, 요청시간
            time+=a
            total_wait += time - b
        else:
            if i < count: time= jobs[i][0] #가능한 작업 없으면 다음 요청시간으로 이동
            
    return total_wait//count