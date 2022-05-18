class Global():
    # 공통 : 약 명칭, 루틴 방식
    medicineName = ''
    routineMethodName = ''
    # 횟수 기반 : 카운트 횟수, 카운트 횟수에 따른 시간, 간격
    routineCount = 0

    # 수면 기반 : 기상 or 취침 설정, 그에 따른 시간, 간격
    setTimeMorningOrNight = ''

    # 식사 기반 : 아침 or 점심 or 저녁 설정, 그에 따른 시간, 간격
    identifyMeal = ''
    checked =[]


    # 시간과 간격을 계산해서 시간에 나타내고, 이름은 약 명칭을 따와서 나타내고, 설명은 루틴 방식 + 간격에 따라 (횟수: 몇 회차, 수면: 취침 30분 전, 식사: 아침 식사 30분 후), 완료는 카운트 횟수만큼 체크박스 생성

