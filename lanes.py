# Importing necessary libraries
import cv2
import numpy as np

# Define a function to apply Canny edge detection
def canny(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply Canny edge detection
    canny = cv2.Canny(blur, 50, 150)
    return canny

# Define a function to mask the region of interest
def region_of_interest(image):
    # Get the height of the image
    height = image.shape[0]
    # Define the vertices of a polygon to mask
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    # Create a mask that is the same size as the image
    mask = np.zeros_like(image)
    # Fill the defined polygon area with white color in the mask
    cv2.fillPoly(mask, polygons, 255)
    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

# Main part of the script

# Read an image from file
image = cv2.imread('test_image.jpg')
# Create a copy of the image to preserve the original
lane_image = np.copy(image)
# Apply the Canny edge detection
canny = canny(lane_image)
# Crop the image to the region of interest
cropped_image = region_of_interest(canny)
# Display the resulting image
cv2.imshow("result", cropped_image)
# Wait for a key press before closing the window
cv2.waitKey(0)

