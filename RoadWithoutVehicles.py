# Importing the required libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Open the video file
video = cv2.VideoCapture('cut.mp4')

# Calculate the total number of frames in the video
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Select 30 frames from the video randomly
RandFrames = length * np.random.uniform(size=30)

# Store selected frames in an array
frames = []
for f in RandFrames:
    video.set(cv2.CAP_PROP_POS_FRAMES, f)
    ret, frame = video.read()
    frames.append(frame)
    
# Calculate the median frame along the time axis
median = np.median(frames, axis=0).astype(dtype=np.uint8)   

# Save the median frame to a file in jpeg format
cv2.imwrite("Highway.jpeg", median)

# Change the colorspace of median frame from BGR to RGB
medianFrame = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)

# Display median frame
plt.rcParams["figure.figsize"]=50,50
plt.axis('off')
plt.imshow(medianFrame)