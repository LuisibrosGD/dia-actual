from datetime import datetime, timezone, timedelta
from fechas import efemerides, dias_espaniol, meses_espaniol
zona_horaria_lima = timezone(timedelta(hours=-5))
ahora_en_lima = datetime.now(zona_horaria_lima)
print(f"Zona horaria de Lima: {zona_horaria_lima}")
print(f"Hora actual en Lima: {ahora_en_lima}")

# esto es para buscar la frase en el diccionario
mes_y_dia = ahora_en_lima.strftime("%m-%d")

# esto es para usarlo en la fecha actual
dia = ahora_en_lima.strftime("%d")
mes = ahora_en_lima.strftime("%m")
anio = ahora_en_lima.strftime("%Y")

numero_dia = ahora_en_lima.weekday() 
nombre_dia = dias_espaniol[numero_dia]

nombre_mes = meses_espaniol[mes]

fecha_hoy = f"{nombre_dia}, {dia} de {nombre_mes} del {anio}"

print(nombre_mes)
print(f"Mes y día actual en Lima: {mes_y_dia}")

frase_hoy = ""

if mes_y_dia in efemerides:
    frase_hoy = efemerides[mes_y_dia]
else: 
    frase_hoy = "No hay frase hoy dia (ya que estoy cansado :c)"

# Leemos el index.html y lo guardamos en una variable
with open('plantilla.html', 'r', encoding='utf-8') as archivo:
    contenido_html = archivo.read()

contenido_html = contenido_html.replace('{{FECHA_HOY}}', fecha_hoy)
contenido_html = contenido_html.replace('{{FRASE_HOY}}', frase_hoy)

# Sobreescribimos el archivo index.html con contenido_html
with open('index.html', 'w', encoding='utf-8') as archivo:
    archivo.write(contenido_html)