import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.figsize'] = (8, 8)
mpl.rcParams['axes.grid'] = False


#### Get the image #################################################

image_path = './esca_dataset/esca/esca_000_cam1.jpg'
image_raw = tf.io.read_file(image_path)
image = tf.image.decode_image(image_raw)


plt.figure()
plt.imshow(image)  # To change [-1, 1] to [0,1]
plt.show()

##################################################################