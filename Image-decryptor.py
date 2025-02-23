import cv2
import argparse

def decrypt_image(image_path, key_path=None):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read the image file.")
        return
    
    stored_password = None
    if key_path:
        try:
            with open(key_path, "r") as key_file:
                stored_password = key_file.read().strip()
        except FileNotFoundError:
            print("Error: Key file not found.")
            return
    
    if not stored_password:
        stored_password = input("Enter passcode for Decryption: ")
    
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0
    
    try:
        while True:
            char = c[img[n, m, z]]
            if not char.isprintable():
                break
            message += char
            n += 1
            m += 1
            z = (z + 1) % 3
    except KeyError:
        pass  # Stop when an invalid key is encountered
    except IndexError:
        pass  # Stop when pixel limits are exceeded
    
    print("Decrypted message:", message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt a message from an image.")
    parser.add_argument("-i", "--image", required=True, help="Path to the encrypted image")
    parser.add_argument("-p", "--password", help="Path to the key file")
    args = parser.parse_args()
    
    decrypt_image(args.image, args.password)
