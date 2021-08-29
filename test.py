import utilities.io
import utilities.subtract
import utilities.utility as utility
from models.image import Image


finderprint = "input/fingerprint.raw"
img = Image("fingerprint_erosion", [315, 238], finderprint)
img.matrix = utility.e(img)
io.write(img, "uint8")