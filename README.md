# Intelligent-CCTV
사람인식 상황에만 녹화하는 CCTV
![System Architecture](https://user-images.githubusercontent.com/13642330/176994409-57b99e85-0a67-491b-a14a-38ff0ed1966f.png)

사용법
1. python 환경에서 mediapipe, opencv, django 설치
2. cmd1 > python cctv/cctv_web/manage.py runserver
3. cmd2 > python cctv/cctv_web/cctv_manage/static/cctv.py

2번과 3번은 다른 터미널에서 각각 실행시켜줘야한다
두개가 모두 실행이 되었다면 카메라 앞에 내 모습을 비춰보자
cctv/cctv_web/cctv_manage/static/image
cctv/cctv_web/cctv_manage/static/files
두개의 폴더에 영상과 이미지가 저장이 된다

이 시스템을 라즈베리 파이에 올릴 예정
