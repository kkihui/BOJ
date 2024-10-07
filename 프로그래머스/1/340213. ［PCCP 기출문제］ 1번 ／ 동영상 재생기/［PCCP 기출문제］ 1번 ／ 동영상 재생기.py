def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        sec = int(pos[:2])*60 + int(pos[3:])
        length = int(video_len[:2])*60 + int(video_len[3:])
        op_start_sec = int(op_start[:2])*60 + int(op_start[3:])
        op_end_sec = int(op_end[:2])*60 + int(op_end[3:])
        
        if op_start_sec <= sec and sec <= op_end_sec:
            sec = op_end_sec
            
        if command == "next":
            sec += 10
            sec = min(sec,length)            
        else:
            sec -= 10
            sec = max(sec,0)
            
        if op_start_sec <= sec and sec <= op_end_sec:
            sec = op_end_sec
        
        mm = sec // 60
        ss = sec % 60
            
        if mm > 9:
            pos = str(mm) + ':'
        else:
            pos = '0' + str(mm) + ':'
        if ss > 9:
            pos += str(ss)
        else:
            pos += '0' + str(ss)
        print(pos)
    answer = pos
    return answer