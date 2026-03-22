#'gpiozero' 라이브러리에서 'LED' 클래스를 가져옴
from gpiozero import LED # LED 제어하기 위한 도구 
# 'time' 라이브러리에서 'sleep' 함수를 가져옴
from time import sleep # 전구를 켜고 기다리는 기능

# 다양한 LED 핀의 핀 번호를 변수로 정의함
carLedRed = 2 
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    while 1: # 참이면 무한히 반복
        # 차는 달리고, 사람은 멈춰 서 있는 상태
        carLedRed.value = 0 # 자동차 빨간불 꺼짐
        carLedYellow.value = 0 # 자동차 노란불 꺼짐
        carLedGreen.value = 1 # 자동차 초록불 켬
        humanLedRed.value = 1 # 보행자 빨간불 켬
        humanLedGreen.value = 0 # 보행자 초록불 꺼짐
        sleep(3.0) # 이 상태 3초 유지
        # 차가 멈출 준비를 하는 상태
        carLedRed.value = 0 
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0) # 1초 동안 노란불 유지
        # 차는 멈추고, 사람이 건너는 상태
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0) # 사람이 건널 시간 3초
    
except KeyboardInterrupt:
    # Ctrl+C를 누르면 프로그램 정지
    pass

# 모든 전등 꺼짐
carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0