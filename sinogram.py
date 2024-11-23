#pylint: disable-all
from PIL import Image
import shutil
import os

"""
A classe Sinogram é responsável por:
-> Formar colagens (sinogramas) de 99 imagens agrupagas de forma horizontal
-> Um grupo de imagens terá menos de 99 imagens e será descartado
-> Algumas imagens foram registradas incorretamente (terminadas pelo numero par), 
desta forma, o sinograma ficou invertido e a função rotate_images() inverte para a posição correta. 
"""

class Sinogram():

  def __init__(self, group_size) -> None:
    self.__images_transformed_path = "./images_transformed"
    self.__sinogram_path = "./sinogram"
    self.__group_size = group_size
    self.__reset_folder(self.__sinogram_path)

  def get_image_paths(self):
    image_paths = [
      os.path.join(self.__images_transformed_path, img)
      for img in os.listdir(self.__images_transformed_path)
      if img.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    return image_paths   

  def create_sinogram(self, images, group_index):
    image_width, image_height = images[0].size
    collage_width = image_width * len(images)
    collage_height = image_height 

    collage = Image.new("RGB", (collage_width, collage_height))

    x_offset = 0
    for img in images:
      collage.paste(img, (x_offset, 0))
      x_offset += image_width

    collage_path = os.path.join(self.__sinogram_path, f"sinogram_{group_index + 1}.jpg")
    collage.save(collage_path)
    print(f"Colagem salva: {collage_path}")
  
  def process_images(self):
    image_paths = self.get_image_paths()
    total_images = len(image_paths)
    for i in range(0, total_images, self.__group_size):
      group = image_paths[i:i + self.__group_size]
      if len(group) < self.__group_size:
        print("Há um grupo que não fará parte do sinograma, pois, possui menos de 99 fotos.")
        continue
      images = [Image.open(img_path) for img_path in group]
      self.create_sinogram(images, i//self.__group_size) 

  def rotate_images(self):
    sinogram_images = [
      img for img in os.listdir(self.__sinogram_path)
      if img.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]

    i = 1
    for img_name in sinogram_images:
      try:
        number = int(img_name.split("_")[-1].split(".")[0])
        if (number % 2 == 0):
          img_path = os.path.join(self.__sinogram_path, img_name)
          with Image.open(img_path) as img:
            rotated_img = img.rotate(180)
            rotated_img.save(img_path)
          print(f"Imagem {i} invertidas foram corrigidas.")
          i += 1
      except ValueError:
        print(f"Nome do arquivo inválido. Arquivo {img_name} ignorada.")

  def __reset_folder(self, path):
    if os.path.exists(path):
      shutil.rmtree(path)
      print(f"O caminho {path} foi excluído.")
    os.makedirs(path)
    print(f"O caminho {path} foi criado.")

# Test
# sinogram = Sinogram(99)
# sinogram.process_images()
# sinogram.rotate_images()