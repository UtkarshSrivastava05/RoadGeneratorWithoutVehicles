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

The camera of the test video is static. Hence, every pixel sees the same piece of the background for most of the time. Occasionaly, some pixels gets covered by the moving vehicles, but only for a fraction of time.

Now fisrt, I have randoly selected few frames (30 frames to be exact) from the test video. It gives us 30 estimates of the background for each and every pixel. Since, none of the pixels in that test video is covered by a movinng object or a vehicle for more than just few nano seconds, I took a median of each pixel over these 30 frames and it gave me a really good estimate of the background at those specific pixels.

The same process is repeated for every pixel and from that I recovered the entire background giving us an image of a higway with no vehicles on it.
