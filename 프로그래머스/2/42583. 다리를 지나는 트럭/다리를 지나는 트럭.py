from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    waiting_truck = deque(truck_weights)
    total_weight = 0
    while bridge or waiting_truck:
        time+=1
        if bridge:
            for i in range(len(bridge)):
                w,t = bridge.popleft()
                t-=1
                if t > 0:
                    bridge.append([w,t])
                else:
                    total_weight -= w
            if waiting_truck:
                if total_weight+waiting_truck[0]<= weight and len(bridge)+1 <= bridge_length:
                    temp = waiting_truck.popleft()
                    bridge.append([temp,bridge_length])
                    total_weight+=temp
        else:
            if waiting_truck:
                temp = waiting_truck.popleft()
                bridge.append([temp,bridge_length])
                total_weight += temp
                    
    answer = time
    return answer