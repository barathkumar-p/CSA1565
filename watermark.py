import cv2

# Load the original image
img1 = cv2.imread('original.jpg')

# Load the watermark image with transparency (PNG format)
img2 = cv2.imread('watermark.png', cv2.IMREAD_UNCHANGED)

# Decide where you want to put the watermark (coordinates)
x = 20  # X-coordinate
y = 20  # Y-coordinate

# Overlay the watermark on the original image
for c in range(0, 3):
    img1[y:y+img2.shape[0], x:x+img2.shape[1], c] = \
    (img1[y:y+img2.shape[0], x:x+img2.shape[1], c] * (1 - img2[:, :, 3] / 255.0) +  img2[:, :, c] * (img2[:, :, 3] / 255.0))

# Save the watermarked image
cv2.imwrite('watermarked.jpg', img2)

# Show the watermarked image (optional)
cv2.imshow('Watermarked Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
