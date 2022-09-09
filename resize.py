from PIL import Image
image = Image.open('video2.png')
image.thumbnail((220, 220))
image.save('video.png')

image = Image.open('exit2.png')
image.thumbnail((220, 220))
image.save('exit.png')

image = Image.open('maps2.png')
image.thumbnail((220, 220))
image.save('maps.png')

image = Image.open('reporte_formulario2.png')
image.thumbnail((220, 220))
image.save('reporte_formulario.png')

image = Image.open('reporte_CovidDB2.png')
image.thumbnail((220, 220))
image.save('reporte_CovidDB.png')

image = Image.open('password2.png')
image.thumbnail((220, 220))
image.save('password.png')

image = Image.open('formulario2.png')
image.thumbnail((220, 220))
image.save('formulario.png')