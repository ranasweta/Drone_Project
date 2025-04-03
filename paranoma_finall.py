import cv2
import os
import cv2 
file_path = "C:/Users/SWETA RANA/Desktop/Aero/pointer.txt"  # File containing the integer

try:
    # Read the integer from the file
    with open(file_path, "r") as file:
        number = int(file.read().strip())
except (FileNotFoundError, ValueError):
    number = 0  # Default to 0 if file does not exist or contains invalid data

# Increment the number
number += 1

# Write the updated number back to the file
with open(file_path, "w") as file:
    file.write(str(number))
print(f"Updated number: {number}")


# Create the frames folder if it doesn't exist
frames_folder = "frames"+str(number)
os.makedirs(frames_folder, exist_ok=True)

# Initialize video capture
cap = cv2.VideoCapture(0)  # 0 for default webcam
fps = 5  # Frames per second
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object
video_path = os.path.join(frames_folder, "output.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

frame_count = 0
total_frames = fps * 100  # Record for 5 seconds

while frame_count < total_frames:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    frame_count += 1
    cv2.imshow('Recording...', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video saved at {video_path}")
# Program To Read video 
# and Extract Frames 


# Function to extract frames 
def FrameCapture(path): 
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
    
    # Used as counter variable 
    count = 0
    
    # checks whether frames were extracted 
    success, image = vidObj.read()
    
    while success: 
        # Saves the frames with frame-count 
        frame_filename = f"frames{number}/frame{count}.jpg"
        cv2.imwrite(frame_filename, image) 
        count += 1
        success, image = vidObj.read()
    return count
    
x = FrameCapture(f"C:/Users/SWETA RANA/Desktop/Aero/frames{number}/output.mp4") 


# Path to your frames folder
frames_folder = 'frames'+str(number)

# Initialize an array to store image paths
image_paths = []

# Loop through all files in the frames folder
for i in range(x):
    image_paths.append(f'{frames_folder}/frame{i}.jpg')


# Initialize a list to store images
imgs = []

# Read all the images from the image_paths list
for i in range(0,len(image_paths),5):
    imgs.append(cv2.imread(image_paths[i]))
    # imgs[-1] = cv2.resize(imgs[-1], (0, 0), fx=0.4, fy=0.4)  # Resize for performance if needed


# Create a stitcher object
stitcher = cv2.Stitcher.create()

# Perform the stitching
dummy, output = stitcher.stitch(imgs)

# Check if the stitching was successful
if dummy != cv2.STITCHER_OK:
    print("Stitching wasn't successful")
else:
    print('Your Panorama is ready!!!')

    # Define the frame filename for the panorama result
    count = len(os.listdir(frames_folder))  # Assuming count is the number of files in the folder
    frame_filename = os.path.join(frames_folder, f"panorama{count}.jpg")

    # Save the final panorama image in the frames folder
    cv2.imwrite(frame_filename, output)

    # Display the final panorama
    cv2.imshow('Final Panorama', output)

# Wait until any key is pressed to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

