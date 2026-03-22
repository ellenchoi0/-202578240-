from gpiozero import LEDBoard
from time import sleep

# 연결된 LED를 순서대로 묶음
leds = LEDBoard(2,3,4,20,21)

try:
    while 1:
        # 차는 달리고, 사람은 멈춤
        leds.value = (0,0,1,1,0)
        sleep(3.0)
        # 차 멈춤 예고
        leds.value = (0,1,0,1,0)
        sleep(1.0)
        # 차는 멈추고, 사람은 건넘
        leds.value = (1,0,0,0,1)
        sleep(3.0)
    
except KeyboardInterrupt:
    # Ctrl+C를 누르면 프로그램 정지
    pass

# 모든 전등 꺼짐
leds.off()
