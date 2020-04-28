import CC
import CorrelationCoefficient
import DU
import my_io
import utility
from MyImage import MyImage
from utility import erosion
from utility import dilation
from utility import boundaryExtraction
from edgeDetection import gradient
from edgeDetection import derivX
from edgeDetection import derivY
from texture import co_Occurrence

# finderprint = "input\\fingerprint.raw"
# x = "input\\lena.raw"
#
# img = MyImage("fingerprint_erosion", [315, 238], finderprint)
# img.matrix = erosion(img)
# my_io.write(img, "8")
#
# img = MyImage("fingerprint_dilation", [315, 238], finderprint)
# img.matrix = dilation(img)
# my_io.write(img, "8")
#
# lincoln = "input\\lincoln.raw"
# img2 = MyImage("lincoln_boundary", [221, 269], lincoln)
# img2.matrix = boundaryExtraction(img2)
# my_io.write(img2, "8")
#
# lena_derivX = "input\\lena.raw"
# img2 = MyImage("lena_derivX", [512, 512], lena_derivX)
# img2.matrix = derivX(img2)
# my_io.write(img2, "int16")
#
# lena_derivY = "input\\lena.raw"
# img2 = MyImage("lena_derivY", [512, 512], lena_derivY)
# img2.matrix = derivY(img2)
# my_io.write(img2, "int16")
#
# lena_gradient = "input\\lena.raw"
# img2 = MyImage("lena_gradient", [512, 512], lena_gradient)
# img2.matrix = gradient(img2)
# my_io.write(img2, "uint16")
#
# cktboard_texture = "input\\cktboard.raw"
# img3 = MyImage("cktboard_texture", [365, 120], cktboard_texture)
# dimensions = [256, 256]
# img3.matrix = co_Occurrence(img3, dimensions)
# my_io.customised_matrix_write8(img3, dimensions)


flowers = "input\\flowers.raw"
img1 = MyImage("flowers", [400, 300], flowers)
flowers_template = "input\\flowers-template.raw"
img2 = MyImage("flowers_template", [42, 45], flowers_template)

img3 = MyImage("flowers_correlation_coefficient", [358, 255])
img3.matrix = CorrelationCoefficient.CC(img1, img2)
# my_io.write(img3, "int8")
img3.matrix = utility.normalize(img3.matrix, [358, 255])
# my_io.write(img3, "int8")
my_io.customised_matrix_write8(img3, [358, 255])


# lena = "input\\lena.raw"
# img3 = MyImage("lena_resampling", [512, 512], lena)
# img3.matrix = DU.down(img3)
# img3.matrix = DU.up(img3)
# my_io.write(img3, "int8")

# lena = "input\\lena_resampling2.raw"
# img3 = MyImage("lena_resampling", [256, 256], lena)
# # img3.matrix = DU.down(img3)
# img3.matrix = DU.up(img3)
# # my_io.write(img3, "int8")
# my_io.customised_matrix_write8(img3, [512, 512])
