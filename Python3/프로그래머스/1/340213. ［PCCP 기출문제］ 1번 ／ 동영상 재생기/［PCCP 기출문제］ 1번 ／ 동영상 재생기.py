def solution(video_len, pos, op_start, op_end, commands):    
    m_video_len = string_to_time(video_len)
    m_pos = string_to_time(pos)
    m_op_start = string_to_time(op_start)
    m_op_end = string_to_time(op_end)
    
    for command in commands:
        # 오프닝 넘기기 체크
        if m_op_start <= m_pos <= m_op_end:
            m_pos = m_op_end
        
        # 커맨드 실행
        if command == "next":
            # 끝점 체크
            if m_pos + 10 >= m_video_len:
                m_pos = m_video_len
            else:
                m_pos += 10
        elif command == "prev":
            # 시작점 체크
            if m_pos - 10 <= 0:
                m_pos = 0
            else:
                m_pos -= 10
    
    # 최종 오프닝 넘기기 체크
    if m_op_start <= m_pos <= m_op_end:
        m_pos = m_op_end
    
    answer = time_to_string(m_pos)
    return answer


def string_to_time(string):
    hour, minute = map(int, string.split(":"))
    return (hour * 60) + minute


def time_to_string(time):
    hour = time // 60
    minute = time % 60
    
    s_hour = ""
    s_minute = ""
    
    if hour < 10:
        s_hour = f"0{hour}"
    else:
        s_hour = str(hour)
    
    if minute < 10:
        s_minute = f"0{minute}"
    else:
        s_minute = str(minute)
    
    return s_hour + ":" + s_minute
        
        