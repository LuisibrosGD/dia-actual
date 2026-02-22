# 📅 Página del Día Automatizada

Una página web estática y minimalista que muestra la fecha actual y una efeméride o mensaje festivo diario. El proyecto se actualiza completamente solo todos los días mediante un flujo de Integración Continua (CI).

## 🚀 Características
* **Automatización Total:** No requiere intervención manual. Se actualiza todos los días a las 00:00 (Hora de Lima).
* **Mensajes Personalizados:** Incluye un diccionario de fechas personalizadas orientadas a la tecnología, cultura peruana y vida universitaria.
* **Efecto de Escritura (Typewriter):** La frase del día se revela con un efecto visual animado usando JavaScript puro.
* **Diseño Responsivo:** Interfaz limpia que se adapta a cualquier pantalla (móviles y escritorio).

## ⚙️ Arquitectura y Flujo de Trabajo
Este proyecto no utiliza bases de datos ni servidores activos. Funciona con la siguiente lógica:
1. **El Disparador (GitHub Actions):** Todos los días a las 05:00 UTC, el archivo `actualizar.yml` enciende una máquina virtual.
2. **El Motor (Python):** Se ejecuta el script `actualizar_fecha.py`. Este programa calcula la hora exacta en Lima, busca si hay una celebración para el día de hoy en el archivo `fechas.py`, y reemplaza las variables `{{FECHA_HOY}}` y `{{FRASE_HOY}}` dentro del HTML.
3. **El Despliegue (Git):** El robot de GitHub hace un *commit* con los nuevos cambios en el archivo `index.html` y los sube al repositorio, actualizando la página automáticamente.

## 🛠️ Tecnologías Utilizadas
* **Backend Automático:** Python 3.10
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **DevOps / CI-CD:** GitHub Actions

## 📂 Estructura del Código
* `actualizar_fecha.py`: Script principal de reemplazo de texto.
* `fechas.py`: Base de datos (Diccionario) con las efemérides.
* `cursorAnimado.js`: Lógica para el efecto de máquina de escribir en el frontend.
* `.github/workflows/actualizar.yml`: Reloj programador de la automatización.
