def solution(order):
    n = len(order)
    sub_belt = []       # 보조 컨테이너 벨트 (스택 구조: 맨 뒤가 "맨 앞"이자 꺼낼 수 있는 곳)
    answer = 0
    idx = 1              # 기존 컨테이너 벨트에서 지금 몇 번 상자까지 내렸는지 (1번부터 순서대로)

    for want in order:   # order를 순서대로 확인 (지금 트럭에 실어야 하는 번호)
        # want 번호가 나올 때까지, 기존 벨트에서 상자를 계속 내려서 보조 벨트에 쌓는다
        while idx <= want:
            sub_belt.append(idx)
            idx += 1

        # 지금 필요한 상자(want)가 보조 벨트의 맨 위(가장 최근에 넣은 것)와 같다면
        if sub_belt and sub_belt[-1] == want:
            sub_belt.pop()   # 꺼내서 트럭에 싣는다
            answer += 1
        else:
            # 보조 벨트 맨 위도 아니고, 기존 벨트로도 이미 다 확인했는데 못 찾았다면
            # 더 이상 순서를 맞출 수 없으므로 종료
            break

    return answer