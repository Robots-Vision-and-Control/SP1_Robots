import time
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

capture = cv2.VideoCapture(0)

xyxys = []
confidences = []
class_ids = []

while capture.isOpened():
    success, frame = capture.read()

    if success:
        start = time.perf_counter()
        results = model(frame)
        end = time.perf_counter()
        total_time = end - start
        fps = 1 / total_time

        annotated_frame = results[0].plot()  # This is where we get the bounded boxes from the model itself

        # Getting the result information
        for result in results:
            boxes = result.boxes.cpu().numpy()
            # Collecting data
            xyxys = boxes.xyxy
            # xyxys.append(boxes.xyxy)
            confidences.append(boxes.conf)
            class_ids.append(boxes.cls)

            for xyxy in xyxys:

                # need to calculate the coordinate pairs for the center of the bounded box
                xCenter = (int(xyxy[0]) + int(xyxy[2])) / 2
                yCenter = (int(xyxy[1]) + int(xyxy[3])) / 2
                cv2.circle(annotated_frame, center=(int(xCenter), int(yCenter)), radius=10, color=(0, 255, 0), thickness=5)

        # cv2.circle(annotated_frame, center=(100, 100), radius=10, color=(0, 255, 0), thickness=10)
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 30), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                    fontScale=1, color=(255, 255, 255), thickness=2)

        cv2.imshow("YOLOv8", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


capture.release()
cv2.destroyAllWindows()
