class Global:
    # 공통 : 약 명칭, 루틴 방식
    medicineName = ''
    routineMethodName = ''

    # 횟수 기반 : 카운트 횟수, 카운트 횟수에 따른 시간
    routineCount = 0
    countTimeList = []  # 카운트 횟수에 따른 시간을 담은 리스트

    # 수면 기반 : 기상 or 취침 설정, 그에 따른 시간, 간격
    setTimeMorningOrNight = ''
    sleepCount = 0  # 기상 취침 중 하나만 선택하면 1, 둘다 선택하면 2 -> setRowCount에 사용, 체크박스 만들어야하는 갯수에도 사용
    sleepInterval = ''  # 간격 콤보박스 내용 그대로 저장 -> 설명 칸에 그대로 넣으면 됨
    sleepIntervalTime = ''  # 간격 시간을 받아서 숫자만 문자열로 받아놓음
    morningTime = ''  # 아침 기상 시간
    nightTime = ''  # 저녁 취침 시간
    sleepTimeList = [] # 수면 시간을 담은 리스트

    # 식사 기반 : 아침 or 점심 or 저녁 설정, 그에 따른 시간, 간격
    identifyMeal = ''
    checked = []  # len(checked) 이용해서 setRowcount에 사용 , 체크박스 만드는 갯수에도 사용
    mealInterval = ''  # 간격 콤보박스 내용 그대로 저장 -> 설명 칸에 그대로 넣으면 됨
    mealIntervalTime = ''  # 간격 시간을 받아서 숫자만 문자열로 받아놓음
    breakfastTime = ''  # 아침식사 시간
    lunchTime = ''  # 점심식사 시간
    dinnerTime = ''  # 저녁식사 시간간
    # 시간과 간격을 계산해서 시간에 나타내고, 이름은 약 명칭을 따와서 나타내고, 설명은 루틴 방식 + 간격에 따라 (횟수: 몇 회차, 수면: 취침 30분 전, 식사: 아침 식사 30분 후), 완료는 카운트 횟수만큼 체크박스 생성

    # Row 갯수 : 횟수 기반 - 사용자 입력, 수면 기반 - 기상, 취침 설정에 따라 다름, 식사 기반 - 아침, 점심, 저녁 설정에 따라 다름.
    # 그러면 저장된 루틴 방식을 확인하고, 횟수 기반이면 카운트를 그대로 넣고, 수면, 식사기반이면 사용자의 체크박스 클릭 갯수대로

    #Main 다이얼로그
    mainDlg = None

