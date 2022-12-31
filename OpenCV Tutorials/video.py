import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# FourCC is a 4-byte code used to specify the video codec. 
# List of codes can be obtained at Video Codecs by FourCC. 
# The codecs for Windows is DIVX and for OSX is avc1, h263. 
# FourCC code is passed as cv2.VideoWriter_fourcc(*’MJPG’) for MJPG and 
# cv2.VideoWriter_fourcc(*’XVID’) for DIVX.

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280, 720)) # (width, height)
# Has to be the same size as captured video size
# cv2.VideoWriter(filename,fourcc,fps,framesize,apiPreference)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

#print(frame.shape)
