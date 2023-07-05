import cv2

cap = cv2.VideoCapture(0)
FPS = 30.0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('Application check.avi', 
                         fourcc, 
                         FPS,
                         (640,480))

# tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()

success , frame = cap.read()

bbox = cv2.selectROI('Tracking', frame, False)
tracker.init(frame, bbox)




def drawBox(frame, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame, 
                  (x, y), 
                  (x + w, y + h), 
                  (255, 0, 255),
                  3, 
                  1)
    cv2.putText(frame,
                "Tracking", 
                (75, 75), 
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2)

while cap.isOpened():
    timer = cv2.getTickCount()
    success , frame = cap.read()
    
    success, bbox = tracker.update(frame)

    if success:
        drawBox(frame, bbox)
        output.write(frame)
    else:
        cv2.putText(frame, 
                    "Loss",
                    (75, 75), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.7, 
                    (0, 0, 255),
                    2)
    
    fps = cv2.getTickCount()/(cv2.getTickCount() - timer)
    cv2.putText(frame,
                str(int(fps)),
                (50,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0,0),
                2)
        
    
    cv2.imshow("Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break                
    
cap.release()
output.release()
cv2.destroyAllWindows()