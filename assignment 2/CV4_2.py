########## Read a video
import cv2
source= 'C:\\Users\\subha\\OneDrive\\Desktop\\video.mp4'# source = 0 for webcam
cap = cv2.VideoCapture (source)
if not cap.isOpened():
  print("Error opening video stream or file")
#Read and display one frame
ret, frame = cap.read()
import matplotlib.pyplot as plt
plt.imshow(frame [...,:: -1])
plt.show()
######### Read the whole video
win_name = 'Camera Preview'
cv2.namedWindow (win_name, cv2.WINDOW_NORMAL) #cv2.WINDOW_FULLSCREEN)
while cv2.waitKey(1) != 27: # Escape
  has_frame, frame =cap.read()
  if not has_frame:
    break
  cv2.imshow(win_name, frame)
cap.release()
cv2.destroyWindow (win_name)



# import cv2

# # Create a VideoCapture object and read from input file
# # If the input is taken from the camera, pass 0 instead of the video file name.
# cap = cv2.VideoCapture('video.mp4')

# while True:
#     ret, frame = cap.read()  # Read a frame
#     if not ret:
#         break  # Break the loop if no frame is read
#     cv2.imshow('Video', frame)  # Display the frame
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break  # Press 'q' to exit the loop

# cap.release()  # Release the VideoCapture object
# cv2.destroyAllWindows()  # Close all windows
