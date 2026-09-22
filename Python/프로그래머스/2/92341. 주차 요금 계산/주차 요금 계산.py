import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees

    in_time = {}      # 차량번호별 입차 시각(분) 기록
    total_time = {}   # 차량번호별 누적 주차 시간(분)

    def to_minutes(hhmm):
        # "HH:MM" 형태 문자열을 "자정부터 몇 분 지났는지"로 변환
        h, m = hhmm.split(':')
        return int(h) * 60 + int(m)

    for record in records:
        time_str, car, action = record.split(' ')
        t = to_minutes(time_str)

        if action == 'IN':
            in_time[car] = t                     # 입차 시각 저장
            if car not in total_time:
                total_time[car] = 0                # 처음 등장하는 차라면 누적시간 0으로 초기화
        else:  # OUT
            total_time[car] += t - in_time[car]    # 이번 입차~출차 구간 시간을 누적
            del in_time[car]                        # 출차했으니 입차 기록은 제거

    # 출차 기록이 없는(아직 in_time에 남아있는) 차량은 23:59(1439분)에 출차된 것으로 간주
    for car, t in in_time.items():
        total_time[car] += 1439 - t

    # 차량 번호가 작은 순서대로 정렬해서 요금 계산
    answer = []
    for car in sorted(total_time.keys()):
        minutes = total_time[car]
        if minutes <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((minutes - base_time) / unit_time) * unit_fee
        answer.append(fee)

    return answer