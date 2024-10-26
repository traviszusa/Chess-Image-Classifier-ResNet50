import streamlit as st
import torch
from torchvision import transforms, models
from PIL import Image

# Load the best trained model
model_path = './model/best-model-resnet.pth'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize model and load trained weights
model = models.resnet50(weights=None)  # Use weights=None to avoid warnings
model.fc = torch.nn.Linear(model.fc.in_features, 6)  # Change to number of classes
model.load_state_dict(torch.load(model_path, map_location=device))
model = model.to(device)
model.eval()

# Define transformation for the input image
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Define class names (as per your ImageFolder class names)
class_names = ['Bishop', 'King', 'Knight', 'Pawn', 'Queen', 'Rook']  # Adjust as necessary

st.title("Chess Piece Classification")
st.write("Take a photo of a chess piece, and the model will classify it!")

# Capture image from the camera
img_file = st.camera_input("Take a photo")

if img_file:
    # Convert the image to PIL format
    image = Image.open(img_file)
    
    # Apply transformations
    img = transform(image).unsqueeze(0)  # Add batch dimension
    img = img.to(device)
    
    # Predict
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
        class_idx = predicted.item()
    
    # Display result
    st.image(image, caption=f"Predicted: {class_names[class_idx]}", use_column_width=True)
    st.success(f"**Classified as:** {class_names[class_idx]}")