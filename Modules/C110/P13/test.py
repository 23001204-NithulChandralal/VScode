import cv2
faces = cv2.imread('multiplefaces.jfif')
# normally, an open source pre-defined face recognition 
# library has a method that can provide this data
# as we assume such data already as a nested List 
boxList = [[[20,100],[80,25]],[[120,100],[180,25]],[[220,100],[280,25]]]
for box in boxList: #There 3 items in boxList.
    # last 2 parameters is color (bgr) and thickness of box drawn
    cv2.rectangle(faces, box[0], box[1], (0, 0, 255), 2)
cv2.imshow("Nested List - Bounding Box", faces)
cv2.waitKey(0)
cv2.destroyAllWindows()