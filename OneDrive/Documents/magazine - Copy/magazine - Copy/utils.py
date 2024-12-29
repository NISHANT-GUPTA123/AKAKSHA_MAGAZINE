# utils.py
import os
from PIL import Image
from werkzeug.utils import secure_filename
from flask import current_app

def save_image(form_image, folder='uploads'):
    """Save and resize uploaded image"""
    if not form_image:
        return None
        
    # Create folder if it doesn't exist
    upload_path = os.path.join(current_app.root_path, 'static', folder)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    # Generate secure filename and save path
    filename = secure_filename(form_image.filename)
    file_path = os.path.join(upload_path, filename)
    
    # Resize and save image
    output_size = (800, 800)
    img = Image.open(form_image)
    img.thumbnail(output_size)
    img.save(file_path)
    
    return os.path.join(folder, filename)

def delete_image(image_path):
    """Delete image file"""
    if not image_path:
        return
        
    file_path = os.path.join(current_app.root_path, 'static', image_path)
    if os.path.exists(file_path):
        os.remove(file_path)