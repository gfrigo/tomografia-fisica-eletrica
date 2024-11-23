#pylint: disable-all
from PIL import Image
import shutil
import os

"""
A classe TransformImages é responsável por:
-> Rotacionar a imagem em 90 graus
-> Obter fotos preto e branco
-> Cortar a foto nos limites do feixe de luz vermelho
"""

class TransformImages():

  def __init__(self) -> None:
    self.__raw_images_path = "./raw_images"
    self.__images_transformed_path = "./images_transformed"
    self.__images_crop_params = (5,195,400,199)
    self.__rotation_angle = 90
    self.__reset_folder(self.__images_transformed_path)
  
  def transform_images(self):
    i = 0
    for img_name in os.listdir(self.__raw_images_path):
      if img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(self.__raw_images_path, img_name)
        with Image.open(img_path) as img:
          img_white_black = img.convert("L")
          crop_image = img_white_black.crop(self.__images_crop_params)
          rotated_image = crop_image.rotate(self.__rotation_angle, expand=True)
          output_path = os.path.join(self.__images_transformed_path, f"transformed_{img_name}")
          rotated_image.save(output_path)
          print(f"Imagem {i} tratada salva em ./images_transformed")
          i += 1

  def __reset_folder(self, path):
    if os.path.exists(path):
      shutil.rmtree(path)
      print(f"O caminho {path} foi excluído.")
    os.makedirs(path)
    print(f"O caminho {path} foi criado.")

# Test
# tranform_images = TransformImages()
# tranform_images.transform_images()