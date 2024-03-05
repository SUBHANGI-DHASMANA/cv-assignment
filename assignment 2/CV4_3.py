import cv2
source = 0
cap = cv2.VideoCapture(source)
if not cap.isOpened():
  print("Error opening video stream or file")
win_name = 'Cam preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps=60
out_mp4 = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))
while cv2.waitKey(1) != 27:
  ret, frame = cap.read()
  if ret:
    out_mp4.write(frame)
    cv2.imshow(win_name, frame)
  else:
    break
cap.release()
out_mp4.release()
cv2.destroyWindow(win_name)