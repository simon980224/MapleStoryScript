from pynput.keyboard import Controller, Key  # 修改部分：從 pynput 引入 Key 模塊
import pyautogui
import cv2
import numpy as np
import time

# ========================================輸入========================================
def process(image):
    """
    圖像處理函數：執行基礎圖像處理，例如灰階和模糊處理
    """
    # 將圖像轉換為灰階
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 應用高斯模糊（可選，用於降噪處理）
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 展示處理後的圖片（若不需要展示，可省略）
    cv2.imshow("Processed Image", blurred_image)  # 顯示處理後的圖片
    cv2.waitKey(1)  # 短暫等待（避免視窗無回應）

    return blurred_image

def recognize():
    """
    1. 捕捉螢幕畫面，2. 圖像處理
    """
    # 1. 使用 pyautogui 捕捉螢幕畫面
    screenshot = pyautogui.screenshot()
    # 將螢幕截圖轉換為 OpenCV 格式的圖像（NumPy 陣列）
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 2. 圖像處理
    processed_image = process(frame)

# ========================================輸出========================================
keyboard = Controller()
def attack(sec):
    """
    雙飛斬
    """
    print("雙飛斬")
    # 放雙飛斬
    keyboard.press('z')
    time.sleep(sec)
    keyboard.release('z')
    # 等待後搖
    time.sleep(1)

def attackSpeed():
    """
    急速暗殺
    """
    print("急速暗殺")
    # 放攻擊速度
    keyboard.press('c')
    time.sleep(0.1)
    keyboard.release('c')
    # 等待後搖
    time.sleep(0.5)

def speed():
    """
    速度激發
    """
    print("速度激發")
    # 放速度激發
    keyboard.press('x')
    time.sleep(0.1)
    keyboard.release('x')
    # 等待後搖
    time.sleep(0.5)

def hide():
    """
    隱身術
    """
    print("隱身術")
    # 平a取消隱身術
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    # 等待後搖
    time.sleep(0.5)

    # 放隱身術
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')
    # 等待後搖
    time.sleep(0.5)

def moveLeft(sec):
    """
    向左移動
    """
    print("向左移動")
    # 放向左鍵
    keyboard.press(Key.left)
    time.sleep(sec)
    keyboard.release(Key.left)

def moveRight(sec):
    """
    向右移動
    """
    print("向右移動")
    # 放向右鍵
    keyboard.press(Key.right)
    time.sleep(sec)
    keyboard.release(Key.right)

def restore():
    """
    角色回原始位置
    """
    print("執行 restore 函數：角色回到原始位置")
    # 放速度激發
    speed()
    # 放隱身術
    hide()
    # 走到右底
    moveRight(15)
    # 轉向左面
    moveLeft(0.1)

# ========================================測試========================================

if __name__ == "__main__":
    for i in range(2):
        print(f"程式將在 {2 - i} 秒後啟動...")
        time.sleep(1)

    direction = "left"
    # direction  = "right"
    while True:
        speed()
        for _ in range(3):  # 每個方向執行重複的攻擊和移動
            attackSpeed()
            attack(8)
            if direction == "left":
                moveLeft(2)
            elif direction == "right":
                moveRight(2)
        if direction == "left":
            # 轉向右面之後，接續右方向的動作
            moveRight(0.1)
            direction = "right"
        elif direction == "right":
            # 轉向左面之後，接續左方向的動作
            moveLeft(0.1)
            direction = "left"
