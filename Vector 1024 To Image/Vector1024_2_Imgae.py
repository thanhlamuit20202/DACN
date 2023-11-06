import cv2
import numpy as np
import re

def vector_to_image(vector, output_image_path, image_shape):
    # Tạo mảng hình ảnh từ vector
    image = vector.reshape(image_shape)

    # Lưu mảng hình ảnh thành tệp ảnh
    cv2.imwrite(output_image_path, image)

def read_vector_from_txt(txt_file):
    with open(txt_file, 'r') as file:
        content = file.read()
        # Tìm và trích xuất các dãy số từ nội dung tệp
        number_lists = re.findall(r'\[([^]]+)\]', content)
        vectors = []
        for number_list in number_lists:
            numbers = [float(num) for num in number_list.split(', ')]
            vectors.append(numbers)
        vector_array = np.array(vectors)
    return vector_array

if __name__ == "__main__":
    vector_file = "C:\\Users\\Thanh Lam\\Desktop\\vector1024.txt"  # Đường dẫn đến tệp chứa vector.txt
    output_image_path = "C:\\Users\\Thanh Lam\\Desktop\\vec1024.jpg"  
    #Set kích thước cho hình ảnh (1x1024 và 1 chiều)
    image_shape = (1, 1024, 1)  

    vector = read_vector_from_txt(vector_file)
    
    vector_to_image(vector, output_image_path, image_shape)
