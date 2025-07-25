from PIL import Image
import numpy as np
import os

def encode_lsb(image, message):
    """
    Encodes a user-specified message into an image using LSB steganography.
    
    :param image: PIL.Image object, the input image.
    :param message: str, the user-provided message to encode.
    """
    # Convert the image to a numpy array for manipulation
    image_array = np.array(image)

    # Append a unique delimiter to the message to signal its end during decoding
    delimiter = "###END###"
    message += delimiter

    # Convert the message into a binary string
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Ensure the message fits within the image
    if len(binary_message) > image_array.size:
        raise ValueError("Message too large to encode in the given image!")

    # Encode the binary message into the least significant bits of the image
    binary_index = 0
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(image_array.shape[2]):  # RGB channels
                if binary_index < len(binary_message):
                    # Modify the least significant bit
                    image_array[i, j, k] = (image_array[i, j, k] & ~1) | int(binary_message[binary_index])
                    binary_index += 1
                else:
                    break
            if binary_index >= len(binary_message):
                break
        if binary_index >= len(binary_message):
            break

    # Convert the array back to a Pillow image
    encoded_image = Image.fromarray(image_array)

    # Save the encoded image to the desktop
    save_path = r"C:\Users\Venkatesh UR\Downloads\ISencoded_image.png"
    encoded_image.save(save_path)
    print("Encoded image saved successfully ")


def decode_lsb(image):
    """
    Decodes a message from an image using LSB steganography.
    
    :param image: PIL.Image object, the encoded image.
    :return: str, the decoded message.
    """
    # Convert the image to a numpy array for manipulation
    image_array = np.array(image)

    # Extract the least significant bits to reconstruct the binary message
    binary_message = ""
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(image_array.shape[2]):  # RGB channels
                binary_message += str(image_array[i, j, k] & 1)

    # Decode the binary message
    decoded_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        char = chr(int(byte, 2))
        decoded_message += char
        if "###END###" in decoded_message:
            # Stop when the delimiter is detected
            break

    # Remove the delimiter and return the message
    return decoded_message.replace("###END###", "")
