import time
from zmqRemoteApi import RemoteAPIClient

# CoppeliaSim과의 Remote API 연결 설정
client = RemoteAPIClient()
sim = client.getObject('sim')

# 비전 센서 핸들 가져오기
vision_sensor_handle = sim.getObject('/Vision_sensor')

# 시뮬레이션 시작
sim.startSimulation()

try:
    while True:
        # 비전 센서로부터 데이터 읽기
        result, packet1, packet2 = sim.readVisionSensor(vision_sensor_handle)
        if result >= 0:  # 센서 데이터가 유효한 경우
            avg_red = packet1[11]  
            avg_green = packet1[12]
            avg_blue = packet1[13]


            print(f"Average Red Value: {avg_red}")
            print(f"Average green Value: {avg_green}")
            print(f"Average blue Value: {avg_blue}")
        else:
            print("Failed to read vision sensor data")

        time.sleep(0.01)  # 10ms 주기로 데이터 읽기

except KeyboardInterrupt:
    # Ctrl+C로 스크립트를 중지했을 때 예외 처리
    pass

finally:
    # 시뮬레이션 정지
    sim.stopSimulation()
    print("Simulation stopped.")