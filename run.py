#pylint: disable-all
from sinogram import Sinogram
from transform import TransformImages
from radon import RadonTransformer

"""
Arquivo principal de inicialização da tomografia com Python
"""

tranform_images = TransformImages()
tranform_images.transform_images()
sinogram = Sinogram(99)
sinogram.process_images()
sinogram.rotate_images()
radon_transform = RadonTransformer()
radon_transform.radon_transform()