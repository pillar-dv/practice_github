import os
import random
import time
import shutil

def clear_screen():
    """터미널 화면 지우기 (Windows, Mac, Linux 지원)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def shooting_star():
    # 터미널 크기 가져오기
    cols, rows = shutil.get_terminal_size((80, 20))
    
    try:
        while True:
            clear_screen()
            # 랜덤 위치에서 별 시작
            x = random.randint(0, cols - 1)
            y = 0
            trail = []

            # 별이 아래로 떨어지는 애니메이션
            while y < rows:
                clear_screen()
                trail.append((x, y))
                for tx, ty in trail:
                    print("\033[%d;%dH*" % (ty + 1, tx + 1), end="")  # 별 출력
                y += 1
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n종료합니다.")

if __name__ == "__main__":
    shooting_star()