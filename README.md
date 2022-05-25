# EnglishProject

Hola Rodrigo!!

Subo el proyecto por aquí porque esta muy pesado hacerlo por el nodo. No voy a subir el sprint todavía, para ver que puedo mejorar hasta el martes. El index esta listo, con los enlaces redirigiendo a las otras paginas. Me falta hacer mas bonito la autenticación y el comentario, pero estan funcionado ambos.

Saludos


24/05/2022

Capa front

Mi aplicación learnEnglish será utilizada para personas que quieran mejorar el nivel de ingles, especialmente pensado en 3 tipos de pruebas, IELTS, Cambridge y TOELF. En el index cree una página con un estilo de olas en movimiento, para que al usuario no le moleste en utilizarla, ademas de del navbar, footer. Tambien tiene distintos botones que te llevan a otros templates como el login, el registro, el formulario o los comentarios, donde puedes dejar tu comentario para que el superusuario lo vea en Django.


Back-end

Esta creado en un entorno virtual, dentro de settings agregue 2 installed apps para que funcionara la aplicación, así como el template, le cambie la base de datos a postgresql y le agregue static y media url.

Dentro del urlpattern (de la aplicación) le agregue el admin (para ver los archivos en django), el login y logout. Tambien he realizado una serie de migrations cuando he cambiado los models y forms de python.

Agregue un archivo static, en donde tengo tanto las imagenes como el archivo css, el cual cambia el front end del proyecto. Luego tengo todos los templates de html, dentro de estos templates ocupo el static load, extends base layout, block content para no escribir tanto codigo. Tambien utilizo el crsf token para darle seguridad a las contraseñas que crean los usuarios. 

Tambien dentro del html, esta indexado todos los link que ocupo para diseñar las paginas (css, bulma, bootstrap), así como tambien el javascript que he necesitado para desarrollar ciertas animaciones. 

La pagína aun le falta por desarrollarse, me gustaría agregar mas funcionalidades y obviamente colocar todo el contendio que deseo, sin embargo, por una cosa de tiempo, tengo contenido del ambito lorem ipsum.

Dentro de los archivos python tengo el admin, en donde agregue las funcionalidades de profesor, curso y comentario. Dentro del archivo forms tengo el resultado de las clases con las cuales funciona django en el front end, especificando el form, label, atribute, max_lenght entre otros.

En models tengo las clases que utilizo en la aplicación en conjunto con el def str para mostras y que el usario pueda agregar la información requerida. 

Dentro de la urls tengo todo los patrones que el usario puede colocar en el buscador, para abrir nuevas paginas de la aplicación. Y por ultimo en views se renderiza la aplicación y se muestra al usuario. 



Django

En django administration tengo unido el grupo de profesores con curso, con la relacion many to many para que cada profesor pueda tomar cuantos cursos quiera,  si se va, esto no borre el curso. 

Tambien en la seccion comentarios deje para que cada persona (sin estar ingresada en la app) pueda dejar su comentario.

La información recogida en los formularios es de vital importancia para conocer quien fue la persona que creo su cuenta, pidiendole sus nombres, apellidos, fecha de nacimiento entre otros. Esto es para poder llevar una contabilidad de la cantidad de personas que crean cuentas en nuestro servidor. Esta información se puede ver solamente atraves de django, no quise hacerlo que se mostrara en la pagina, ya que la pagina no busca eso, sino que busca que el usuario pueda utilizarla para aprender ingles.


