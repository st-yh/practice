import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

video_capture.set(3, 1280)
video_capture.set(4, 720)

face_locations = []

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # resize를해서 하는이유가뭘까

    # face_location = 사람얼굴을 인식하는 좌표값을 알려준다
    face_locations = face_recognition.face_locations(frame, model="cnn")

    # 인식한 얼굴을 박스로 만들고 원본 프레임에 적용하기위해q
    for top, right, bottom, left in face_locations:
        top *= 1
        right *= 1
        bottom *= 1
        left *= 1

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
        cv2.rectangle(frame, (0, 0), (30, 30), (0, 255, 0), 2)
        cv2.rectangle(frame, (20, 20), (30, 30), (255, 0, 0), 2)

    cv2.imshow('df', small_frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()