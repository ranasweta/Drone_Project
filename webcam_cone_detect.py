from ultralytics import YOLO
import cv2

model = YOLO("C:\\Users\\SWETA RANA\\Desktop\\Aero\\my_model\\my_model.pt")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    result = model.predict(frame, device='cpu', conf=0.5)[0]
    cv2.imshow("YOLOv8", result.plot())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
