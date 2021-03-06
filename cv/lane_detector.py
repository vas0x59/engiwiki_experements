import cv2
import numpy as np

lane = cv2.imread("demo_lane.png")
out = lane.copy()
gray = cv2.cvtColor(lane, cv2.COLOR_BGR2GRAY)

lines = cv2.HoughLines(gray,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(out,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("out", out)

cv2.waitKey(0)