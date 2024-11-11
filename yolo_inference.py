from ultralytics import YOLO

model = YOLO('models/best.pt')

result = model.predict('input_videos/match.mp4', save = True )
print(result[0])

print('***********************************')
for box in result[0].boxes:
    print(box)