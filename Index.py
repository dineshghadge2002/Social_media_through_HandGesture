import os
import cv2
from cvzone.HandTrackingModule import HandDetector

def linkdin():
    linkedin_url = "https://www.linkedin.com/in/vitthal-shinde-a50628227/"
    os.system(f"start {linkedin_url}") 
def Kaggle():
    Kaggle_url = "https://www.kaggle.com/dineshghadge"
    os.system(f"start {Kaggle_url}") 
def github():
    github_url = "https://github.com/dineshghadge2002"
    os.system(f"start {github_url}") 
def facebook():
    Facebook_url = "https://www.facebook.com/vitthal.shinde.52438174"
    os.system(f"start {Facebook_url}")
def instagram():
    instagram_url = "https://www.instagram.com/vithu_shinde_07/"
    os.system(f"start {instagram_url}")
def snap():
    snap_url = "https://www.snapchat.com/add/v_shinde88?share_id=EzTz1KyU0Mc&locale=en-GB"
    os.system(f"start {snap_url}")
    
cap = cv2.VideoCapture( 0 )

from cvzone.HandTrackingModule import HandDetector
detector = HandDetector()


while True:
    print("""========================================================================
    1)Open My linkedin account thumbsUp.
    2)Open Kaggle account up only index finger.
    3)Open github up middile finger.
    4)Open Facebook up ring finger.
    5)Open Instagram up middile finger. 
    6)Open snap up all finger""")
    status , photo = cap.read()
    cv2.imshow("my photo" , photo)
    if cv2.waitKey(100) == 13:
        break
    
    handphoto = detector.findHands(photo , draw=False)
    
    if handphoto:
        lmlist = handphoto[0]
        fingerstatus = detector.fingersUp(lmlist)

        if fingerstatus == [1,0,0,0,0]:
            print("Thumb is up")
            linkdin()
    
        elif fingerstatus == [ 0 ,1 ,0 , 0, 0]:
            print("index finger up")
            Kaggle()
            
    
        elif fingerstatus == [ 0 , 0, 1, 0 , 0 ]:
            print("Middle finger up")
            github()
    
        elif fingerstatus == [ 0 , 0, 0, 1, 0 ]:
            print("Ring finger up")
            facebook()
            
        elif fingerstatus == [ 0 , 0, 0, 0, 1 ]:
            print("Little finger up")
            instagram()
            
        elif fingerstatus == [ 1, 1, 1, 1, 1 ]:
            print("All fingers up")
            snap()
        else:
            print("Finger not found")
             
cv2.destroyAllWindows()
cap.release()