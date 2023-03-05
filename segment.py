import cv2
from yolo_segmentation import YOLOSegmentation

# Segmentation detector
ys = YOLOSegmentation("C:/Users/lenovo/Desktop/YOLO v8/segmentation/yolov8_segmentation-pysource.com/yolov8s-seg.pt")

# Capture video from default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame
    frame = cv2.resize(frame, None, fx=0.9, fy=0.9)

    # Detect objects and segment them
    bboxes, classes, segmentations, scores = ys.detect(frame)

    # Loop through each detection and draw bounding box and segmentation mask
    for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
        (x, y, x2, y2) = bbox
        if class_id == 67:
            cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 2)
            cv2.polylines(frame, [seg], True, (0, 0, 255), 4)
            #print(seg)
            area = cv2.contourArea(seg)
            print("Segmentation mask area:", area," pixel square")
            cv2.putText(frame, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    cv2.imshow("frame", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
