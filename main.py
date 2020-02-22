from my_io import io
from utility import utility
import math
dimensions = [512, 512]

lena = "input/lena.raw"
lena_edit = "input/lena_edit.raw"

# result = utility.sub(lena, lena_edit, dimensions, "lena_subtraction")
#
# inverse_img = utility.inverse(lena, dimensions, "lena_negative")
#
# trans_img = utility.translation(lena, 5, dimensions, "lena_translation")
# utility.histogram(lena, dimensions, "lena_histequal")

# x = utility.smooth(lena, dimensions, "lena_smooth")
utility.unsharp(io.read(lena, dimensions), utility.smooth(lena, dimensions), dimensions)

io.write(utility.sharpening(lena, dimensions), "lena_sharpening")