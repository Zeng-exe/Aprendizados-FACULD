
function ligarSistema() {

    const lamp = document.getElementById("lampContainer");
    const status = document.getElementById("connection-status");
    const login = document.getElementById("loginContainer");

    if (lamp.classList.contains("ligado")) {

        // Desliga o abajur
        lamp.classList.remove("ligado");

        // Fecha o login
        login.classList.remove("mostrar");

        status.innerText = "● Sistema desligado";

    } else {

        // Liga o abajur
        lamp.classList.add("ligado");

        status.innerText = "Conectando...";

        // Abre o login
        setTimeout(function() {

            if (lamp.classList.contains("ligado")) {
                login.classList.add("mostrar");
            }

        }, 1000);

        // Atualiza o status
        setTimeout(function() {

            if (lamp.classList.contains("ligado")) {
                status.innerText = "● Sistema conectado";
            }

        }, 1800);
    }
}
