
const contenedor = document.getElementById("frase");
const texto = contenedor.dataset.texto;
let i = 0;

// crea el cursor
const cursor = document.createElement("span");
cursor.classList.add("cursor");
contenedor.appendChild(cursor);

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