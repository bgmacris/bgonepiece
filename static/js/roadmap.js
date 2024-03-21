// Función para ajustar la altura de las columnas del kamban
window.onload = function () {
    function ajustarAlturaColumnas() {
        var columnas = document.querySelectorAll('.column');
        columnas.forEach(function (columna) {
            let alturaTotal = columna.querySelector('h2').offsetHeight + 11;
            var tareas = columna.querySelectorAll('.task');
            if (tareas.length === 0) {
                alturaTotal += 60;
            }
            tareas.forEach(function (tarea) {
                alturaTotal += tarea.offsetHeight + 10;
            });
            alturaTotal += 15
            columna.style.height = alturaTotal + 'px';
        });
    }

    // Llamar a la función de ajuste de altura cuando se carga la página
    ajustarAlturaColumnas();

    // Llamar a la función de ajuste de altura cuando se redimensiona la ventana
    window.addEventListener('resize', function () {
        ajustarAlturaColumnas();
    });
};


// FUNCIONES para mover las tareas de columnas
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.dataset.id);
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drop(ev, columna_destino) {
    var data = ev.dataTransfer.getData("text");
    var tarea = document.getElementById(data);

    actualizarEstadoTarea(data, columna_destino);
}

function actualizarEstadoTarea(id_tarea, columna_destino) {
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var url = '/actualizar_tarea_estado/'; // URL de la vista que manejará la actualización de estado
    var formData = new FormData();
    formData.append('id', id_tarea);
    formData.append('id_status', columna_destino);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log('Estado de tarea actualizado correctamente');
        } else {
            console.error('Error al actualizar estado de tarea');
        }
    };
    xhr.send(formData);
    location.reload();
}


// FUNCIONES para manejar popups tareas
function showTaskDetails(task) {
    document.getElementById('popup-title').innerText = task.dataset.title;
    document.getElementById('popup-comment').innerText = "Comentario: " + task.dataset.comment;
    document.getElementById('popup-assigned-user').innerText = "Usuario asignado: " + task.dataset.assignedUser;
    document.getElementById('popup-start-date').innerText = "Fecha de inicio: " + task.dataset.startDate;
    document.getElementById('popup-end-date').innerText = "Fecha de finalización: " + task.dataset.endDate;
    document.getElementById('popup-priority').innerText = "Prioridad: " + task.dataset.priority;
    document.getElementById('popup-tag').innerText = "Etiqueta: " + task.dataset.tag;
    document.getElementById('popup-status').innerText = "Estado: " + task.dataset.status;
    document.getElementById('popup').style.display = 'block';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}


// FUNCIONES para manejar creacion de tareas
// Función para abrir el modal y establecer el estado de la tarea
function abrirModal(estado) {
    // Agregar evento de clic al botón de cerrar modal
    document.getElementById("close-modal-btn").addEventListener("click", cerrarModal);
    // Establecer el estado de la tarea en el formulario
    console.log("AA", estado)
    document.getElementById("id_status").value = estado;

    // Ocultar campo timetile en el formulario
    var timeline = document.getElementById("id_timeline_date");
    var timeline_label = document.querySelector("label[for='id_timeline_date']");
    // Ocultar el elemento cambiando su estilo CSS
    //timeline.style.display = "none";
    //timeline_label.style.display = "none";

    // Mostrar el modal
    var modal = document.getElementById("modal");
    modal.style.display = "block";
}

// Función para cerrar el modal
function cerrarModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none"; // Ocultar el modal
}

// Cerrar el modal si se hace clic fuera del modal
window.addEventListener("click", function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});

// Manejar el envío del formulario mediante AJAX
$("#task-form").submit(function (event) {
    event.preventDefault();
    var form = $(this);
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (response) {
            // Aquí puedes manejar la respuesta del servidor
            console.log(response);
            // Cerrar el modal después de enviar el formulario
            modal.style.display = "none";
            location.reload();
        },
        error: function (xhr, status, error) {
            // Manejar errores aquí
            console.error(xhr.responseText);
        }
    });
});