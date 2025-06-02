import pyautogui
import keyboard
import time
import os

def capture_and_trigger():
    # 1. 獲取完整螢幕的截圖
    screenshot = pyautogui.screenshot()
    # 建立螢幕截圖檔案的存放路徑
    screenshot_folder = "screenshots"
    os.makedirs(screenshot_folder, exist_ok=True)  # 如果目錄不存在則創建
    screenshot_filename = os.path.join(screenshot_folder, "screenshot.png")
    screenshot.save(screenshot_filename)
    print(f"螢幕截圖已儲存到: {screenshot_filename}")

    # 2. 模擬按下空白鍵
    keyboard.press_and_release('space')  # 按下並釋放空白鍵 
    print("空白鍵被按下")

def main():
    print("程式啟動中，請按下 'ctrl+c' 結束程式...") 
    while True:
        try:
            # 每隔10秒執行一次截圖並按下空白鍵
            capture_and_trigger()
            time.sleep(10)
        except KeyboardInterrupt:
            print("程式已結束")
            break

if __name__ == "__main__":
    main()