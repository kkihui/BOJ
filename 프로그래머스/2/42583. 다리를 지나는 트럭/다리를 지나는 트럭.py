import collections

def solution(bridge_length, weight, truck_weights):
    deque = collections.deque(truck_weights)
    ing = collections.deque()
    done = []
    time = 0
    weight_sum = 0
    
    while len(done) != len(truck_weights):
        if len(ing) > 0:
            if ing[0][0] <= time-bridge_length:
                temp = ing.popleft()
                weight_sum -= temp[1]
                done.append(temp)
                
        if len(deque) != 0 and len(ing) <= bridge_length and weight_sum + deque[0] <= weight:
            temp = deque.popleft()
            ing.append((time,temp))
            weight_sum += temp
            
        
        time += 1
        
    return time