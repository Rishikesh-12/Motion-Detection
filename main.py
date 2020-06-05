import cv2, time

first_frame=None

video=cv2.VideoCapture(0)
 
while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue
        
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0),3)

    cv2.imshow("capturing gray frame",gray)
    cv2.imshow("capturing blur frame",delta_frame)
    cv2.imshow("capturing threshold frame",thresh_frame)
    cv2.imshow("color frame", frame)
    
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

    print(status)
    
video.release()
cv2.destroyAllWindows