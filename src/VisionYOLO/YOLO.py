import time
import cv2
from ultralytics import YOLO
from Controller import PID_Controller

class YOLO_model:
    def __init__(self, camera_index):
        self.model = YOLO("yolov8n.pt")
        self.capture = cv2.VideoCapture(camera_index)
        self.xyxys = []
        self.confidences = []
        self.class_ids = []
        self.annotated_frame = None
        self.results_frame = None
        self.frame = None
        self.switch = 0

        # init controller
        self.vertical_controller = PID_Controller(kp=1, ki=0.001, kd=0.01, T=0.1, tau=0.01, limitMax=500, limitMin=-500, limit_max_int=1, limit_min_int=-1)
        self.vertical_controller.controller_init()  # Maybe this does not belong here
        self.horizontal_controller = PID_Controller(kp=1, ki=0.001, kd=0.01, T=0.1, tau=0.01, limitMax=500, limitMin=-500, limit_max_int=1, limit_min_int=-1)
        self.horizontal_controller.controller_init()  # Maybe this does not belong here

        print("YOLO")

    def center_BB(self):
        for xyxy in self.xyxys:
            # need to calculate the coordinate pairs for the center of the bounded box
            xCenter = (int(xyxy[0]) + int(xyxy[2])) / 2
            yCenter = (int(xyxy[1]) + int(xyxy[3])) / 2
            cv2.circle(self.annotated_frame, center=(int(xCenter), int(yCenter)), radius=10, color=(0, 255, 0),
                       thickness=5)
    def collecting_information(self):
        start = time.perf_counter()
        self.results_frame = self.model(self.frame)
        end = time.perf_counter()
        total_time = end - start
        fps = 1 / total_time
        self.annotated_frame = self.results_frame[0].plot()  # This is where we get the bounded boxes from the model itself


        # displays fps
        cv2.putText(self.annotated_frame, f"FPS: {int(fps)}", (10, 30), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                    fontScale=1, color=(255, 255, 255), thickness=2)

    def testing_aim_bot(self):
        # init variable
        vertical = 50  # set-point or current position
        horizontal = 50

        desired_vertical = (int(self.xyxys[0][1]) + int(self.xyxys[0][3])) / 2  # desired position
        desired_horizontal = (int(self.xyxys[0][0]) + int(self.xyxys[0][2])) / 2
        print(desired_vertical)
        # update coordinates
        vertical = self.vertical_controller.controller_Update(vertical, desired_vertical)
        # print(vertical)
        horizontal = self.horizontal_controller.controller_Update(horizontal, desired_horizontal)
        # print(horizontal)
        # place a point that we will test
        cv2.circle(self.annotated_frame, center=(int(horizontal * -1), int(vertical * -1)), radius=5, color=(255, 0, 0), thickness=5)  # center(horizontal, vertical)
        cv2.circle(self.annotated_frame, center=(50, 50), radius=5, color=(0, 0, 0), thickness=5)  # black circle is the init position

    # vertical motion only for testing
    def robot_aim_bot(self):
        # getting the pixel measurement then translating it to position motions numbers
        set_point_in_position = 50  # Current position
        desired_position = (int(self.xyxys[0][1]) + int(self.xyxys[0][3])) / 2
        print("desired position: " + str(desired_position))   # from top down: it increases so top would be 0 and bottom would be max number
        output = self.vertical_controller.controller_Update(set_point_in_position, desired_position)
        output = output * -1
        print(int(output))

        # now we translate into motions depending on pixel size of the camera we are going to use TODO LOOK AT THIS!!!
        # also I will need to address the coordinate system of the pixels of the camera then map it to the motions



    def bounding_boxes_request(self):
        # Getting the result information
        for result_frame in self.results_frame:
            boxes = result_frame.boxes.cpu().numpy()  # collect the bounding boxes
            # Collecting data
            self.xyxys = boxes.xyxy  # this is a numpy array
            self.confidences.append(boxes.conf)
            self.class_ids.append(boxes.cls)

    def print_detection_info(self):
        if self.results_frame is not None and len(self.results_frame) > 0:
            for result in self.results_frame:
                if result is not None and len(result.names) > 0:
                    print("Detected Objects:")
                    for label, boxes in result.names.items():
                        print(f"{label}: {len(boxes)}")
                else:
                    print("No objects detected.")
        else:
            print("No objects detected.")

    def circles(self):
        cv2.circle(self.annotated_frame, center=(600, 0), radius=5, color=(0, 0, 0), thickness=5)


    def capture_vision(self):
        while self.capture.isOpened():
            success, self.frame = self.capture.read()

            if success:


                self.collecting_information()
                # self.print_detection_info()
                self.bounding_boxes_request()
                self.center_BB()
                self.circles()
                self.robot_aim_bot()
                # self.testing_aim_bot()
                # Display number and types of detections

                cv2.imshow("YOLOv8", self.annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


vision = YOLO_model(0)  # init
vision.capture_vision()
vision.capture.release()
cv2.destroyAllWindows()
