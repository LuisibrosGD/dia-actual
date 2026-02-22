
const contenedor = document.getElementById("frase");
const texto = contenedor.dataset.texto;
let i = 0;

// crea el cursor
const cursor = document.createElement("span");
cursor.classList.add("cursor");
contenedor.appendChild(cursor);

/**
 * Crea un efecto visual de "máquina de escribir" insertando caracteres 
 * uno por uno en el DOM justo antes del elemento del cursor animado.
 * * La función se llama a sí misma de forma recursiva cada 50ms hasta 
 * completar la longitud total del texto extraído del dataset.
 */
function escribir() {
    if (i < texto.length){
        cursor.insertAdjacentText("beforebegin", texto[i]);
        i++;
        setTimeout(escribir, 50); // 50 ms por letra
    } else{
        cursor.remove();
    }
}
setTimeout(escribir, 500);