import numpy as np

data = np.load('C:\\Users\\Thanh Lam\\Desktop\\exe_vector.npy')

# size moi
data = data[:1016172] # chia hết cho 3 hoặc 2 và căn đẹp

np.save('C:\\Users\\Thanh Lam\\Desktop\\giam2.npy', data)
