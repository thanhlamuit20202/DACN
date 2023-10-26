import numpy as np

def exe_to_vector(exe_file_path):
    try:
        with open(exe_file_path, "rb") as exe_file:
            # Đọc dữ liệu từ tệp .exe
            exe_data = exe_file.read()
            # Chuyển dữ liệu thành mảng vector
            vector = np.frombuffer(exe_data, dtype=np.uint8)
            return vector
    except FileNotFoundError:
        print("Không tìm thấy tệp .exe.")
        return None

if __name__ == "__main__":
    exe_file_path = "C:\\Users\\Thanh Lam\\Desktop\\f2.exe"
    vector = exe_to_vector(exe_file_path)

    if vector is not None:
        # Lưu vector vào tệp
        np.save("C:\\Users\\Thanh Lam\\Desktop\\exe_vector.npy", vector)
