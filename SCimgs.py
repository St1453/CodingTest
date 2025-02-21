'''
Codes for slicing an image.
지정 장소(C:/Users/MG/Projects/Images)에 있는 임의의 이미지 origin.png을 12등분 해 'C:/Users/MG/Projects/Images/cuts'에 저장합니다.
'''

from PIL import Image
import os

def slice_image(image_path, output_folder):
    # Open the original image
    with Image.open(image_path) as img:
        img_width, img_height = img.size

        # Calculate slice dimensions
        slice_width = img_width // 6
        slice_height = img_height // 2

        # Number of slices
        num_slices_x = img_width // slice_width
        num_slices_y = img_height // slice_height

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        slice_index = 0
        for y in range(num_slices_y):
            for x in range(num_slices_x):
                left = x * slice_width
                upper = y * slice_height
                right = left + slice_width
                lower = upper + slice_height

                # Crop the image to the slice dimensions
                img_slice = img.crop((left, upper, right, lower))

                # Save the cropped slice
                slice_filename = os.path.join(output_folder, f'slice_{slice_index}.png')
                img_slice.save(slice_filename)
                print(f'Saved: {slice_filename}')
                slice_index += 1

if __name__ == "__main__":
    # Input parameters
    input_image_path = 'C:/Users/MG/Projects/Images/origin.png'  # Replace with the path to your image
    output_directory = 'C:/Users/MG/Projects/Images/cuts'

    slice_image(input_image_path, output_directory)



'''
Codes to compare images.
코사인 유사도를 이용해 slice_0과 slice_0부터 slice_11까지 비교합니다.
'''

import os
import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

def extract_features(image_path, size=(128, 128)):
    """Extracts feature vector from an image using PIL."""
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    img = img.resize(size)  # Resize to fixed dimensions
    img = np.array(img).flatten()  # Flatten to 1D vector
    img = img / np.linalg.norm(img)  # Normalize
    return img

def compare_images(main_image_path, folder_path):
    """Compares main image to images in a folder using cosine similarity."""
    main_features = extract_features(main_image_path)
    similarities = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.lower().endswith(('png', 'jpg', 'jpeg')):
            sliced_features = extract_features(file_path)
            similarity = cosine_similarity([main_features], [sliced_features])[0][0]
            similarities.append((file, similarity))
    
    # Sort images by similarity (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities

# Example usage
main_image = "C:/Users/MG/Projects/Images/cuts/slice_0.png"
sliced_folder = "C:/Users/MG/Projects/Images/cuts"

results = compare_images(main_image, sliced_folder)
for filename, score in results:
    print(f"{filename}: {score:.4f}")
