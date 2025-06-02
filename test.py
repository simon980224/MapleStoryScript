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
    1. 捕捉螢幕畫面，2. 圖像處理 ，3. 模擬 z 鍵按下
    """
    # 1. 使用 pyautogui 捕捉螢幕畫面
    screenshot = pyautogui.screenshot()
    # 將螢幕截圖轉換為 OpenCV 格式的圖像（NumPy 陣列）
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 2. 圖像處理
    processed_image = process(frame)

# ========================================輸出========================================
keyboard = Controller()
def attack(seconds):
    """
    模擬攻擊
    """
    print("執行 attack 函數：模擬攻擊")
    # 放雙飛閃
    keyboard.press('z')
    time.sleep(seconds)
    keyboard.release('z')

def speed():
    """
    模擬加速
    """
    print("執行 speed 函數：模擬加速")
    # 放速度激發
    keyboard.press('x')
    time.sleep(0.5)
    keyboard.release('x')

def hide():
    """
    模擬隱身術
    """
    print("執行 hide 函數：模擬隱身術")
    # 放隱身術
    keyboard.press('a')
    time.sleep(0.5)
    keyboard.release('a')

def restore():
    """
    角色回原始位置
    """
    print("執行 restore 函數：角色回到原始位置")
    # 放速度激發
    speed()
    time.sleep(0.1)
    # 放隱身術
    hide()
    # 走到右底
    keyboard.press(Key.right)
    time.sleep(10)
    keyboard.release(Key.right)
    # 轉向左面
    keyboard.press(Key.left)
    # time.sleep(0.1)
    keyboard.release(Key.left)

def climeb():
    """
    模擬爬牆
    """
    print("執行 climb 函數：模擬爬牆")
    # 放爬牆鍵
    keyboard.press(Key.space)
    keyboard.press(Key.up)
    time.sleep(2)
    keyboard.release(Key.space)
    keyboard.release(Key.up)

def step1row():
    """
    模擬走到第一排
    """
    print("執行 step1row 函數：模擬走到第一排")
    # 放速度激發
    speed()
    time.sleep(0.1)
    # 放隱身術
    hide()
    keyboard.press(Key.left)
    time.sleep(5.4)
    keyboard.release(Key.left)
    # 轉向右面
    keyboard.press(Key.right)
    time.sleep(0.1)
    keyboard.release(Key.right)
# ========================================測試========================================

if __name__ == "__main__":
    for i in range(2):
        print(f"程式將在 {2 - i} 秒後啟動...")
        time.sleep(1)

    for i in range(3):
        restore()
        attack(10)
        step1row()
        climeb()
        attack(10)
        restore()