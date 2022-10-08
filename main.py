from rembg import remove
from PIL import merge


inputh_path = 'cl.jpg' # inserir a imagem que será alterada
output_path = 'output.png'

img_input = Image.open(inputh_path)
output = remove(img_input)
output.save(output_path)