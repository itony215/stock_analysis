import pyautogui

import time 
#'1605','1795','2002','2303','2313','2317','2327','2330','2340','2344','2368','2379','2409','2453','2481','2497','2498','2603','2606','2618',
                # '3006','3008','3034','3035','3037','3141','3169','3189','3228','3406',
                # '3443',
stock_list = [
                '3532','3558','3653','3675','3680','3707','4162','4755','4768','4919',
                '5269','5425','5483','6104','6138','6182','6187','6217','6231','6469',
                '6488','6515','6531','6719','8028','8046','8069','8299','8478','9945']
#time.sleep(5)
#暫停10秒，等待網頁視窗安置好
#pyautogui.PAUSE=10
#滑鼠移動到註冊
#移動到 1951 , 792 花 1 秒的時間移動過去
for item in stock_list:
    pyautogui.moveTo(1225,50,1)
    #滑鼠左鍵點擊一下
    pyautogui.click()
    #print('click')
    pyautogui.typewrite(item)
    pyautogui.hotkey('enter')  
    pyautogui.moveTo(71,952,1)
    pyautogui.click()
    pyautogui.moveTo(93,803,1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(120,809,1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(197,950,1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(33,187,1)
    pyautogui.rightClick()
    pyautogui.moveTo(112,597,1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1627,1054,2)
    pyautogui.click()
    time.sleep(4)
    
    while True:
        try:
            if(pyautogui.pixelMatchesColor(71, 343, (255, 255, 255))==False):
                print('done!')
                break
            time.sleep(4)
        except:
            pass


    pyautogui.moveTo(1871,24,2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('enter') 
    time.sleep(1)
    pyautogui.typewrite(item)
    time.sleep(1)
    pyautogui.hotkey('enter') 
    #pyautogui.moveTo(33,187,1)
    #暫停1秒，等待網頁載入
    pyautogui.PAUSE=1