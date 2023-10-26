import cv2
import numpy as np

def vector_to_image(vector, output_image_path, image_shape):
    # Tạo mảng hình ảnh từ vector
    image = vector.reshape(image_shape)

    # Lưu mảng hình ảnh thành tệp ảnh
    cv2.imwrite(output_image_path, image)

if __name__ == "__main__":
    vector_file = "C:\\Users\\Thanh Lam\\Desktop\\giam2.npy"  
    output_image_path = "C:\\Users\\Thanh Lam\\Desktop\\giam2.jpg"  
    image_shape = (582, 582, 3)  

    vector = np.load(vector_file)
    
    vector_to_image(vector, output_image_path, image_shape)
