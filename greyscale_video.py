import cv2
def greyscale(img, height, width):
    resized_img = cv2.resize(img,(height,width),interpolation=cv2.INTER_CUBIC)
    return cv2.cvtColor(resized_img,cv2.COLOR_RGB2GRAY)

# img = cv2.imread('image.jpg')
# img = greyscale(img, 64,64)
# cv2.imwrite('test.jpg',img)

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('voice.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame_original', frame)
    frame = greyscale(frame, 128,128)
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()