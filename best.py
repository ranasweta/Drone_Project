import torch
from yolov5 import YOLOv5
# Load YOLOv5 model
import pathlib 
temp=pathlib.PosixPath
pathlib.PosixPath=pathlib.WindowsPath
model = torch.hub.load('yolov5', 'custom', path='best.pt', source="local", force_reload=True)
# Perform inference on an image
results = model('topview.jpg')

# Print results
results.print()

# Show results
results.show()  # Displays the image with annotations
pathlib.PosixPath=temp