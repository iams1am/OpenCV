import cv2
import os
import matplotlib.pyplot as plt
import glob

def show_grayscale_comparison(input_directory):
    """
    Read images from the input directory, convert to grayscale, and show
    side-by-side comparisons using matplotlib.
    
    Args:
        input_directory (str): Directory containing the input images
    """
    # Get all image files from the input directory
    image_paths = []
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.bmp']:
        image_paths.extend(glob.glob(os.path.join(input_directory, ext)))
    
    # Exit if no images found
    if not image_paths:
        print(f"No images found in {input_directory}")
        return
    
    print(f"Found {len(image_paths)} images")
    
    # Process each image
    for img_path in image_paths:
        # Read the original image
        original = cv2.imread(img_path)
        
        # Check if image was read successfully
        if original is None:
            print(f"Could not read {img_path}")
            continue
        
        # Convert BGR to RGB for matplotlib display
        original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
        
        # Create grayscale version
        grayscale = cv2.imread(img_path, 0)  # 0 flag loads directly as grayscale
        
        # Display side by side comparison
        plt.figure(figsize=(10, 5))
        
        # Show original image
        plt.subplot(1, 2, 1)
        plt.imshow(original_rgb)
        plt.title('Original')
        plt.axis('off')
        
        # Show grayscale image
        plt.subplot(1, 2, 2)
        plt.imshow(grayscale, cmap='gray')
        plt.title('Grayscale')
        plt.axis('off')
        
        # Set the window title to the image filename
        plt.suptitle(os.path.basename(img_path))
        plt.tight_layout()
        plt.show()

# Replace this with your input directory
input_dir = "input_directory"  # Change this to your folder path

# Call the function to show the comparisons
show_grayscale_comparison(input_dir)