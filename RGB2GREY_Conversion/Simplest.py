import cv2

image = cv2.imread('botrgb.jpg',0) #change png/jpg according to the format
cv2.imshow('My grey bot image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()