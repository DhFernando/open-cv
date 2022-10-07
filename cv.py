import cv2 as cv

#rescale
def rescaleFrame(frame, scale = 0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimention = (width, height)
    return cv.resize(frame, dimention, interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture('SRCFile/Videos/1.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
    
#     cv.imshow('My video', frame_resized)
#     cv.imshow('My video2', frame)
    
    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

img = cv.imread('SRCFile/Photos/1.jpg')
# cv.imshow('me', img)
frame_resized = rescaleFrame(img)
cv.imshow('me2', frame_resized)
cv.waitKey(0)