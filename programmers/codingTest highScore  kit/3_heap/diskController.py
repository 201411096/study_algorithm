"""
프로그래머스 -> 코딩테스트 연습 -> 힙(Heap) -> 디스크 컨트롤러


문제 설명
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다.
디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다.
가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
와 같은 요청이 들어왔습니다. 

한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면

- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

입출력 예
jobs	return
[[0, 3], [1, 9], [2, 6]]	9

입출력 예 설명
문제에 주어진 예와 같습니다.

0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.
"""
import heapq

def solution(jobs):
    answer = 0
    time = 0
    
    divAnswer = len(jobs) # 마지막에 평균 구할 때 사용
    currentJob = None
    heap1 = [] # 요청시간 순서대로
    heap2 = [] # 작업시간 순서대로

    for job in jobs:
        heapq.heappush(heap1, job)

    while len(heap1) != 0 or len(heap2) != 0:
        # heap2에 job이 하나도 들어가 있지 않다면 요청시간이 가장 빠른 job을 pop
        # 해당 job의 끝나는 시간대로 이동
        if len(heap2)==0:
            currentJob = heapq.heappop(heap1)
            time = currentJob[0] # 시간대 보정(현재 시간에 맞는 작업이 없으니, 요청시간이 가장 빠른 시간대로 넘어감)
        # heap2에 job이 하나라도 들어있는 상태라면
        elif len(heap2) > 0:
            currentJob = heapq.heappop(heap2)[1]
        
        # 현재 job의 종료 시간대로 이동
        # answer 계산
        time = time + currentJob[1]
        answer = answer + (time - currentJob[0]) # job이 끝난 시간 - job이 요청된 시간

        # 요청이 온 작업들을 heap2에 담는 작업
        while True:
            if len(heap1) == 0:
                break
            if heap1[0][0]>time:
                break
            tempJob = heapq.heappop(heap1)
            heapq.heappush(heap2, (tempJob[1], tempJob))
            
    return int(answer / divAnswer) # 단, 소수점 이하는 버립니다...

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs)) # 9
jobs = [[0, 3], [4, 3], [10, 3]]
print(solution(jobs)) # 3
jobs = [[0, 10], [2, 3], [9, 3]]
print(solution(jobs)) # 9
jobs = [[1, 10], [3, 3], [10, 3]]
print(solution(jobs)) # 9
jobs = [[0, 10]]
print(solution(jobs)) # 10
jobs = [[0, 10], [4, 10], [5, 11], [15, 2]]
print(solution(jobs)) # 15
jobs = [[1, 3],[1, 9], [2, 6]]
print(solution(jobs)) # 9