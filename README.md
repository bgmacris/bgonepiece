# bgonepiece | Portafolio Bogdan Macris django backend

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Index</summary>
  <ol>
    <li>
      <a href="#url-pagina">URL Pagina</a>
    </li>
    <li>
      <a href="#introduccion">Introduccion</a>
      <ul>
        <li><a href="#tecnologias-utilizadas">Tecnologias utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#proyectos">Proyectos</a>
      <li><a href="#recomendacion">Recomendacion</a></li>
      <ul>
        <ul>
          <li><a href="#snake-game">A* Snake Game</a></li>
          <li><a href="#instalacion">Instalacion</a></li>
        </ul>
        <ul>
          <li><a href="#tictactoc">minimax TicTacToc</a></li>
          <li><a href="#instalacion">Instalacion</a></li>
        </ul>
        <ul>
          <li><a href="#one-piece">One Piece Scraping</a></li>
          <li><a href="#instalacion">Instalacion</a></li>
        </ul>
      </ul>
    </li>
  </ol>
</details>

## URL Pagina
  -> https://bogdanportafolio.onrender.com

<!-- INDTRODUCION -->
## Introduccion

Este repositorio aloja mi portafolio personal, desarrollado utilizando el `framework Django`. El diseño del frontend se basa en una plantilla HTML/CSS gratuita disponible en un repositorio de GitHub, que he adaptado para presentar de manera organizada y profesional información sobre mí, mi currículum vitae, mis habilidades y una selección de proyectos relevantes. Este portafolio tiene como objetivo proporcionar una visión completa de mi perfil y experiencia profesional. Le agradezco su interés y le invito a explorar el contenido aquí presentado.

### Tecnologias utilizadas
* Hosting `Render` Plan Gratuito: Este proyecto utiliza el plan gratuito de Render como servicio de alojamiento para la aplicación web.
* `Django 5.0.3`: La aplicación está desarrollada utilizando la versión 5.0.3 del framework Django, lo que proporciona una base sólida y actualizada para el desarrollo web.
* `Python 3.10.6`: Se emplea Python versión 3.10.6 como lenguaje principal para la lógica de la aplicación y la manipulación de datos.
* `HTML y CSS`: El frontend de la aplicación se construye utilizando HTML y CSS, lo que garantiza una presentación visual y una experiencia de usuario atractivas y consistentes.

<!-- RECOMENDACION -->
## Recomendacion
### Instalación de Entorno Virtual Python

Este repositorio utiliza un entorno virtual de Python para gestionar las dependencias del proyecto de manera aislada. Sigue los pasos a continuación para configurar tu entorno virtual:

#### Paso 1: Instalación de `virtualenv` (si no está instalado)

Si aún no tienes `virtualenv` instalado en tu sistema, puedes hacerlo mediante `pip`, el gestor de paquetes de Python. Ejecuta el siguiente comando:
```
pip install virtualenv
```

#### Paso 2: Creación del Entorno Virtual

Una vez instalado `virtualenv`, puedes crear un nuevo entorno virtual para este proyecto. Navega hasta la carpeta raíz de tu proyecto y ejecuta el siguiente comando:
```
virtualenv venv
```
Esto creará una carpeta llamada `venv` que contendrá el entorno virtual.

#### Paso 3: Activación del Entorno Virtual

Para activar el entorno virtual, debes ejecutar el script correspondiente según tu sistema operativo. A continuación, se muestran los comandos para diferentes sistemas operativos:

##### Windows
```
venv\Scripts\activate
```

##### MacOS y Linux
```
source venv/bin/activate
```


<!-- PROYECTOS -->
## Proyectos

En esta sección, encontrarás una lista de proyectos desarrollados por mí, junto con enlaces a sus respectivos repositorios y una breve descripción de cada uno.

### Snake Game
- **Repositorio:** [Snake Game Repository](https://github.com/bgmacris/a_star__snake)

Este proyecto implementa el algoritmo A* para mejorar el clásico juego de la serpiente. Utiliza la búsqueda informada para guiar el movimiento del jugador. Sin embargo, se reconoce que el algoritmo actual puede beneficiarse de mejoras y actualizaciones para optimizar su rendimiento. Se utiliza el motor gráfico PyGame para la representación visual del juego.

#### Instrucciones de instalación:

1. En tu entorno virtual, instala las dependencias del repositorio `a_star__snake` utilizando el siguiente comando:
   
```
pip install -r requirements.txt
```


2. Una vez instaladas las dependencias, ejecuta el archivo `main.py` para iniciar el juego:

```
python main.py
```


Con estos pasos, podrás instalar las dependencias necesarias y ejecutar el juego Snake Game en tu entorno local.


### Tic Tac Toe
- **Repositorio:** [Tic Tac Toe Repository](https://github.com/bgmacris/3_en_raya)

Este proyecto consiste en el clásico juego de 3 en raya, implementado en Python. Ofrece la modalidad de jugador contra máquina. El algoritmo utilizado para la inteligencia artificial es el algoritmo Minimax.

El algoritmo Minimax es un algoritmo de decisión que se utiliza en la teoría de juegos para minimizar las pérdidas posibles para un jugador, considerando que el oponente también está jugando de forma óptima. Funciona de manera recursiva, explorando todas las posibles jugadas del juego y eligiendo la mejor opción para el jugador y la peor para el oponente en cada paso.

#### Instrucciones de instalación:

1. En tu entorno virtual, instala las dependencias del repositorio `a_star__snake` utilizando el siguiente comando:
   
```
pip install -r requirements.txt
```


2. Una vez instaladas las dependencias, ejecuta el archivo `main.py` para iniciar el juego:

```
python main.py
```

### One Piece
- **Repositorio:** [One Piece Repository](https://github.com/bgmacris/bgonepiece/tree/main/scraping-one-piece)

Este proyecto se compone de dos scripts. El primero realiza scraping web utilizando Selenium y el driver de Chrome. Este script busca el tomo indicado del manga en una página web específica y procede a descargar todas las imágenes de los capítulos, organizándolas en directorios por capítulo (es decir, cada directorio contendrá las imágenes de un capítulo).

El segundo script se encarga de recoger todas las imágenes descargadas y crear un archivo PDF final que las reúna en orden secuencial.

#### Instrucciones de instalación:

1. En tu entorno virtual, instala las dependencias del repositorio `one-piece` utilizando el siguiente comando:

```
pip install -r requirements.txt
```


2. Asegúrate de tener instalado el driver de Chrome para Selenium.

3. Ejecuta el primer script para realizar el scraping y descargar las imágenes:

```
python descargar-tomos.py
```

4. Luego, ejecuta el segundo script para generar el PDF final:

```
python crear_tomos.py
```
