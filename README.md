# Road Generator Without Vehicles
This is an implementation of the task provided by SYNERGYLABS, hiring for the post of DL Engineer.

## Problem Statement
Generate road without vehicle by averaging frames of a video footage.

Lets say you want to create a video where Optimus prime is running on a (real) highway, for
that you need a footage where the road doesn’t have any vehicle on it, this is a problem as
the highways are very busy. But as a computer vision expert you say, wait! I can do it using
image processing, just give me a video.

### Test Video
The test video can be downloaded from [here](https://drive.google.com/file/d/1il2yWyr7-t9XfG1nDVL7QlfmnmNDf_9I/view).

## Implementation
I have made use of OpenCV library with medium filtering technique for the implementation of this task.

The test video contains a CCTV footage of a higway with continous moving vehicles on it. The camera is static in the video and hence, every pixel sees the same piece of the background for most of the time. Occasionaly, some pixels gets covered by the moving vehicles, but only for a fraction of time.

Now fisrt, I have randomly selected few frames (30 frames to be exact) from the test video. It gives us 30 estimates of the background for each and every pixel. Since, none of the pixels in that test video is covered by a movinng object or a vehicle for more than just few nano seconds, I applied the median filter on each pixel over these 30 frames and it gave me a really good estimate of the background at those specific pixels.

The same process is repeated for every pixel and from that I recovered the entire background, giving me an image of a higway with no vehicles on it.

From this image we can create a video where Optimus Prime is running on this highway without any fear of hurting any humans.

### Files
1. Test Video: "cut.mp4"
2. Python Script for this task: "RoadWithoutVehicles.py"
3. Output of the program: "Highway.jpeg"
4. Write-up for this task: "README.md"

## References
1. https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html

2. https://stackoverflow.com/questions/25359288/how-to-know-total-number-of-frame-in-a-file-with-cv2-in-python

3. https://stackoverflow.com/questions/45179467/how-to-use-cv2-cap-prop-pos-frames-to-extract-video-frame

4. https://www.geeksforgeeks.org/numpy-median-in-python/#:~:text=axis%20%3D%200%20means%20along%20the,same%20dimensions%20as%20expected%20output.

5. https://stackoverflow.com/questions/39316447/opencv-giving-wrong-color-to-colored-images-on-loading

6. https://html.developreference.com/article/23487587/Why+OpenCV+Using+BGR+Colour+Space+Instead+of+RGB
