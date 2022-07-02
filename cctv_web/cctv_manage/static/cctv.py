import cv2
import mediapipe as mp
import time,os
from datetime import datetime
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

none_time = -100
recording = False
isclean = False
saved_day = datetime.now()

'''주간 파일 정리'''
def clean_file(now):
    files = os.listdir(BASE_DIR + "/videos")
    for file in files:
        f_day = datetime.strptime(file[0:4] + file[5:7] + file[8:10], "%Y%m%d")
        print((f_day - now).days)
        if ((now - f_day).days > 7):
            os.remove(BASE_DIR + '/videos/' + file)

'''새로운 날인지 확인'''
def isNewday(now):
    if((now - saved_day).days > 0):
        return True
    else:
        False

'''카메라 인식'''
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    now = datetime.now()

    if(isNewday(now)):
        clean_file(now)

    success, image = cap.read()
    will_save = image.copy()
    if not success:
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    if(results.pose_landmarks):
        none_time = time.time()

    if(time.time()-none_time<10):
        if(recording==False):
            # print("start")
            recording=True
            date = datetime.today().strftime("%Y%m%d%H%M%S")
            name = f"{date[0:4]}{date[4:6]}{date[6:8]}_{date[8:10]}h{date[10:12]}m"
            cv2.imwrite(f'/images/{name}.jpg', will_save)
            video = cv2.VideoWriter(f"files/{name}.mp4", fourcc, fps, (will_save.shape[1], will_save.shape[0]))
        else:
            video.write(will_save)

    else:
        if(recording==True):
            # print("end")
            recording=False
            video.release()
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()