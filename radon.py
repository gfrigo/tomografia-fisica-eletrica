#pylint: disable-all
import os
import shutil
import numpy as np
from skimage.io import imread, imsave
from skimage.transform import radon

class RadonTransformer:

  def __init__(self) -> None:
    self.__sinogram_path = "./sinogram"
    self.__radon_path = "./radon"
    self.__reset_folder(self.__radon_path)

  def radon_transform(self):
    i = 1
    for img_name in os.listdir(self.__sinogram_path):
      if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(self.__sinogram_path, img_name)
        image = imread(image_path, as_gray=True)
        theta = np.linspace(0., 180., max(image.shape), endpoint=False)
        sinogram = radon(image, theta=theta, circle=True)
        sinogram_normalized = 255 * (sinogram - np.min(sinogram)) / (np.max(sinogram) - np.min(sinogram))
        sinogram_uint8 = sinogram_normalized.astype(np.uint8)
        image_name = os.path.basename(image_path).split(".")[0]
        output_path = os.path.join(self.__radon_path, f"{image_name}_radon.png")
        imsave(output_path, sinogram_uint8)  # Salvar o sinograma normalizado
        print(f"Sinograma {i} após transformada de Radon salvo em: {output_path}")
        i += 1

  def __reset_folder(self, path):
    if os.path.exists(path):
      shutil.rmtree(path)
      print(f"O caminho {path} foi excluído.")
    os.makedirs(path)
    print(f"O caminho {path} foi criado.")

# Teste
# radon_transform = RadonTransformer()
# radon_transform.radon_transform()
