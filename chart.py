#pylint: disable-all

import os
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ChartTomography:
  def __init__(self) -> None:
    self.__radon_path = "./radon"

  def plot_radon_stack_3d(self):
    image_files = sorted([f for f in os.listdir(self.__radon_path) 
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    if not image_files:
      print("Nenhuma imagem encontrada na pasta fornecida.")
      return
    
    stack = []
    for img_file in image_files:
      image_path = os.path.join(self.__radon_path, img_file)
      image = imread(image_path, as_gray=True)
      stack.append(image)
    volume = np.array(stack)

    z_dim, y_dim, x_dim = volume.shape
    z, y, x = np.meshgrid(
      np.arange(z_dim), 
      np.arange(y_dim), 
      np.arange(x_dim), 
      indexing='ij'
      )

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    step = max(1, z_dim // 30)
    for i in range(0, z_dim, step):
      ax.contourf(x[i], y[i], volume[i], zdir='z', offset=i, cmap='gray', alpha=0.8)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Empilhamento 3D de Imagens (Transformada de Radon)")
    plt.show()

# Test
# chart_tomography = ChartTomography()
# chart_tomography.plot_radon_stack_3d()