import cv2
import argparse
import os

def encrypt_image(image_path, output_path, key_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read the image file.")
        return
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    with open(key_path, "w") as key_file:
        key_file.write(password)
    
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0
    
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    print(f"Encrypted image saved as {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt a message into an image.")
    parser.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = parser.parse_args()
    
    encrypt_image(args.image, "encImage.png", "key.txt")
