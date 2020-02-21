from my_io import io
from utility import utility

dimensions = [512, 512]

lena = "sources\lena.raw"
lena_edit = "sources\lena_edit.raw"

result = utility.sub(lena, lena_edit, dimensions, "lena_subtraction")

inverse_img = utility.inverse(lena, dimensions, "lena_negative")

trans_img = utility.translation(lena, 5, dimensions, "lena_translation")
