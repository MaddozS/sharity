# Charity Control
Repositorio de documentos Equipo 2 de la asignatura "Programación Orientada a Objetos".

## Integrantes del equipo.
* Anaya Axel
* Cruz Pedro
* Hernández Rodrigo
* Mendez José

## Introducción

### Resumen:
Sharity es un servicio web para controlar y administrar eventos de giro caritativo, permitiendole tener un control homogéneo de las cantidades requeridas, además de permitir una transparencia al saber cuales son los productos que se manejan y ya se han recaudado.

### Relevancia:
Un problema común dentro de las plataformas de organización de eventos caritativos es la contribución de artículos, al final de cada evento suele haber un artículo que fue recaudado un factor común entre los colaboradores, mientras otros de igual importancia no recibieron la cantidad esperada, incluso podrían haber productos y materiales que no se logren recolectar.
Actualmente no existe una plataforma con dicho enfoque donde se pueda controlar la organización de colectas. Mediante Sharity es posible observar que tipo de artículos se necesitan y cuánta gente se encuentra  contribuyendo con determinado producto, para lograr balancear la cantidad de cada artículos en la recaudación de forma sencilla y eficaz.

### Público Objetivo:
Cualquier persona que esté interesada en apoyar y generar eventos de caridad y altruistas.

## Definición del Proyecto

### Objetivos:
El objetivo principal de Sharity es proporcionar una plataforma útil y eficaz para llevar un control sobre los materiales y productos necesarios para un evento caritativo.
Los objetivos generales son:
1. Dar transparencia a los eventos caritativos.
2. Proporcionar un control sencillo de los productos y materiales para un evento.
3. Dar difusión de eventos caritativos.
4. Proporcionar a quien lo use en total conocimiento de lo recaudado.

### Innovación:
Un problema común dentro de las plataformas de organización de eventos caritativos es la contribución de artículos, al final de cada evento suele haber un artículo que fue recaudado de más mientras otros de igual importancia no recibieron el mismo impacto. Actualmente no existe una plataforma donde se pueda controlar ese problema. Mediante Sharity es posible observar que tipo de artículos se necesitan y cuánta gente se encuentra  contribuyendo con tal producto, para lograr balancear el impacto de cada artículo en la recaudación de forma sencilla y eficaz.

## Plan de Proyecto

### Investigación:
Se realizó una búsqueda con el objetivo de fundamentar el impacto que lograría recibir sharity. La información recaudada se basa en: aplicaciones similares a sharity, eventos caritativos en mérida e impacto entre gente interesada a eventos caritativos.

Al momento de investigar aplicaciones relacionadas a la sharity se encontraron aplicaciones como: Dashport, SmartSara,  Eventbrite e incluso el apartado de eventos de facebook, sin embargo estas aplicaciones, logran variar mucho sus enfoques, y estos no logran contribuir con eventos que tratan de beneficiar a una causa.

Se pudo observar que entre los eventos existentes dentro de las aplicaciones se puede observar que proveen de la información necesaria para llamar la atención de un público interesado en este tipo de eventos, sin embargo sufren faltas de organización con los tipos de donaciones que requieren ya que de estos alguno suelen recibir un impacto mayor a otros logrando un desequilibrio entre productos.

Dentro de los eventos que son creados por facebook, aquellos que tienen un enfoque caritativos se pudieron observar que tuvieron un impacto mínimo entre los usuarios de facebook, debido a que estos tenían una escasez de personas interesadas en estos. Se llevó a cabo una encuesta donde se preguntaba qué tan común es escuchar acerca de un evento caritativo y que tan fácil es acceder a ellos, se encontró de 45 persona que el 88.9% se encuentran interesados en asistir a este tipo de eventos, 61.1% considera que es difícil enterarse de estos eventos y el 83.3% le gustaría involucrarse más a estos. Más de la mitad de los encuestados no conoce alguna plataforma donde se crean eventos de este estilo de forma organizada y el impacto que provoca los eventos de facebook no logra el objetivo deseado. Como se puede apreciar se logra encontrar una gran cantidad de gente que se encuentra interesada en este tipo de eventos sin embargo el difícil acceso a estos obstaculiza su participación a estos.

La organización y las funcionalidades con las que cuenta Sharity puede facilitar el acceso a este tipo de eventos que una gran cantidad de personas se encuentra interesada, logra una mejora en la organización de productos que requiere cada evento y logra realizar un enfoque específico para las organizaciones.

## Definición de Requerimientos

### Actores del Sistema:
*Usuario. Persona que utiliza el sistema.*
* Podrá inscribirse dentro de algún evento de su agrado que esté disponible a su alcance.
* Puede observar la cantidad de gente que asistirá a un evento.
* Puede observar los artículos que un evento necesita.
* Puede calificar a los eventos asistidos.
* Puede suscribirse a una Empresa u Organizador

*Organizador/Empresa. Persona/Empresa que crea y organiza un evento.*
* Puede crear eventos.
* Puede proveer control de administrador a otros usuarios.
* Puede publicar los materiales requeridos por parte del usuario

### Requerimientos de Usuario:
1. Los usuarios podrán inscribirse dentro de algún evento de su agrado creado por un organizador o empresa.
2. Los usuarios pueden observar la cantidad de gente que ha confirmado su asistencia a cierto evento.
3. Cada usuario podrá observar una lista de artículos que se necesite para un evento, y contribuir a este.
4. Los usuarios pueden calificar los eventos a los que ha asistido, para mostrar el éxito de cada evento.
5. Los usuarios podrán suscribirse a ciertos organizadores o empresas para estar al pendiente de futuros eventos
6. Los organizadores o empresas podrán crear múltiples eventos

### Requerimientos del Sistema:

*_Alta._  Requerimiento cuya funcionalidad será esencial al sistema.*
*_Media._  Requerimiento cuya funcionalidad es necesaria para el sistema sin embargo, con menor relevancia para el usuario.*
*_Baja._  Requerimiento que puede ser omitido del sistema.*

**Funcionales.**

| RF001   |      Dashboard.      |  
|----------|:-------------:|
| Prioridad:| Alta |
| Descripción |- Al iniciar el sistema, se deberá mostrar la pagina principal, que es el dashboard<br> - Desde el dashboard el usuario podrá buscar algún evento de su interés, o podrá visualizar algunos eventos populares. <br> - El usuario podrá ir al apartado de Organizador, donde se le permitirá crear y configurar eventos. |

***

| RF002   |      CRUD de Eventos.     |  
|----------|:-------------:|
| Prioridad:| Alta |
| Descripción |  - Se podrán administrar los eventos si se es un organizador del evento.<br> - Se podrán administrar los eventos si se es un organizador del evento. |

***

| RF003   |     Búsqueda de eventos.      |  
|----------|:-------------:|
| Prioridad:| Alta |
| Descripción | - El sistema aprueba al usuario el realizar búsquedas sobre eventos o categorías |

***

| RF004   |     Difusión de Eventos.      |  
|----------|:-------------:|
| Prioridad:| Media |
| Descripción | - El sistema aprueba  al usuario compartir sus eventos en algunas redes sociales. |

***

| RF005   |     Menú.      |  
|----------|:-------------:|
| Prioridad:| Alta |
| Descripción |  - El sistema tendrá un menú que te permitirá visualizar los eventos a los que te has registrado, te permitirá ir al dashboard y buscar eventos. |


**No Funcionales.**

| RNF001   |      Recomendación Dinámica de Eventos.      |  
|----------|:-------------:|
| Prioridad:| Baja |
| Descripción | - El sistema aprueba  recomendar eventos cercanos a la ubicación del usuario. |

***

| RNF002   |      Difusión de Eventos     |  
|----------|:-------------:|
| Prioridad:| Media |
| Descripción | - Los eventos solamente podrán ser difundidos en facebook. |

***

### Casos de Uso

**CU01.** Búsqueda por buscador.

**Descripción.** El usuario busca un evento de su agrado dentro del buscador de la página, con el motivo de facilitar la interacción con eventos.

**Secuencia:**
1. El usuario entra a la página.
2. El usuario selecciona el buscador dentro del menú.
3. El usuario introduce el evento que desea encontrar.
4. La página muestra el evento ingresado dentro del buscador.

**Salidas Alternativas:**
3.1  Si el el evento ingresado no es encontrado se le informa al usuario que el evento no existe.


**CU02.** Creación de evento.

**Descripción.** El usuario crea un evento el cual se encontrará accesible para los demás usuarios.

**Secuencia:**
1. El usuario entra a la página.
2. El usuario selecciona la opción de crear un nuevo evento dentro del dashboard.
3. El usuario ingresa los datos del evento.
4. El usuario finaliza la creación dando click al botón de crear evento.

**Salidas Alternativas:**
4.1 El usuario cancela la creación del evento.


**CU03.** Inscripción a evento.

**Descripción.** El usuario se inscribe a un evento de su agrado.

**Secuencia:**
1. El usuario entra a la página.
2. El usuario realiza la búsqueda del evento dentro del buscador(observar CU01).
3. El usuario selecciona la opción de inscribirse al evento.
4. El usuario ingresa los datos que se solicitan para la inscripción.
5. El usuario selecciona la opción de finalizar inscripción.

**Salidas Alternativas:**
4.1 El usuario cancela la inscripción del evento y regresa a la página previa.
5.1 El cupo del evento se ha llenado y la inscripción no se finaliza.

### Diagrama de Casos de Uso.

![Diagrama](https://lh3.googleusercontent.com/4Uyto3RYELpwsCj4zi13b_bqaqsjtmaGe4zKnmTJ7mOyR1QzmpvMRwo5zb6j8DAi3yDU8-BLEVsjg173y_DBAO7IJQKEkn1mWOSpzu17)

## Proceso de Trabajo

### Herramientas:

**Control de actividades:**
1. Microsoft Planner
2. Google Drive
3. Google Docs
4. Google Spreadsheets

**Herramientas de desarrollo:**
1. Visual Studio Code
2. NodeJS
3. Vue
4. Firebase

**Herramientas de diseño:**
1. Lucidchart
2. Figma
3. Bootstrap

**Herramientas de comunicación:**
1. WhatsApp
2. Discord

### Metodología:

**Control de Actividades:**
El enfoque de estas herramientas será la organización y gestión de las actividades que se llevarán a cabo como equipo. Será el medio por donde se realizarán las asignaciones de las tareas responsables por cada miembro.
* Microsoft Planner.  Por medio de esta herramienta se llevará a cabo la división y calendarización de tareas con las cuales cada integrante debe cumplir.
* Google Drive. Administrador de documentos donde se almacenarán todo documento realizado durante el desarrollo del proyecto para llevar a cabo una mejor organización de estos.
* Google Docs. Esta herramienta será utilizada para llevar a cabo la documentación del proyecto presente.
* Google Spreadsheets. Herramienta que será utilizada con el motivo de organización de calendario de actividades.

**Herramientas de Desarrollo:**
* Visual Studio  Code. Esta herramienta será utilizada como el editor de texto principal para desarrollar el proyecto.
* NodeJS. Herramienta utilizada para usar js como ambiente para interactuar con un servidor web.
* Vue. Es el framework que será utilizado por parte del front-end para desarrollar la página web.
* Firebase. Herramienta utilizada por parte del back-end para llevar a cabo métodos de autenticación para la página web.

**Herramientas de Diseño:**
* Lucidchart. Aplicación principal por donde se realizarán diagramas para llevar a cabo el diseño del proyecto ya sean las clases, casos de uso, entre otros.
* Figma. Aplicación para crear animaciones dentro de la página web.
* Bootstrap. Framework css base para crear el diseño de la página web.

**Herramientas de Comunicación.**
* Whatsapp. Cumple ser la plataforma de comunicación principal entre los integrantes del equipo.
* Discord. Plataforma de comunicación vía llamadas donde los integrantes realizarán juntas para discutir el proceso de trabajo del proyecto y futuras tareas.

### Proceso:

Para el proceso del desarrollo de la aplicación, usaremos la metodología SCRUM, pues esta nos permite tener una organización óptima de las tareas que queremos realizar además de poder tener un control de lo que realiza cada quién.
También, con el poco tiempo que tenemos para el proyecto, con SCRUM podemos optimizar mejor el alcance de finalización del proyecto.

### Historias de Usuario:

1. El sistema contará con un CRUD de eventos
2. Como usuario puedo realizar búsquedas sobre algún evento
3. Como usuario puedo difundir mis eventos por medio de redes sociales 

### Métricas:

**Métricas de equipo:**

Mediante Planner, la cantidad de tareas que se tiene en equipo se puede visualizar mediante gráficas, además de estar organizadas por el tipo de tarea que sea, permitiendo saber el avance del proyecto.

![Metrica1](https://lh4.googleusercontent.com/6MV3knF3uOLlVLLJMZnSZEHQguT7vBnQtkxGT2XRuMGvzGgLbex4pjivdkfnJL9zAah9P2kAmRP6-YatGfsw6QF9EeB68FGDRJNZaEXY85X6rViEBMyB5RS0tuTR_GIwBsCbJ37G)

Además podemos visualizar la cantidad de tareas de ha realizado cada quién, con la misma organización de las gráficas.
De igual manera, en un hoja de cálculo grupal tendremos organizadas de la misma manera, pero con la diferencia que las organizaremos por Sprint para saber qué tareas se relegaron al siguiente sprint, ya sea porque no se completaron o porque no estaban completas.

Las aportaciones serán medidas por una tabla como la siguiente:

![Metrica2](https://lh6.googleusercontent.com/GELbY7T45oUScTWBOHzF3M1RMUfhMSovMMyfUWXOKQ9Db-_wn5jkPnlYf0o9YXfM6Gp3GJ24HloNn7CDw2yWMxCKcdOFRat9QDKd3ej_neDL8SbhLdIJGSXQCW9B7Uje-i6mliFu)

Esta tabla nos permite visualizar el estado de las tareas para una fácil visualización del avance del equipo. Del mismo modo, nos permite determinar cuales eran nuestros planes para las tareas al inicio, y cómo estas se fueron modificando a lo largo del desarrollo. 

**Metricas individuales**

El avance individual será medido conforme el cumplimiento de las tareas designadas, con la opción de reasignar tareas. 
Para equilibrar de una mejor manera el porcentaje que tendrá cada tarea, se usarán dos métricas diferentes: complejidad y horas requeridas. Las horas serán asignadas de manera individual según crean conveniente cada integrante, pero la complejidad será asignada entre todos los integrantes, con una numeración del 1 al 10.
Al final, cada tarea tendrá una suma del puntaje de complejidad y las horas requeridas (1 punto por hora), los puntos de todas las tareas serán sumadas, lo que ese sería el 100% de las tareas,  y las tareas que tenga cada quién se hará la relación con los puntos que tenga. 

Ejemplo:

| **Tarea** |      **Puntos**      |  
|----------|:-------------:|
| tarea 1 | 4 |
| tarea 2 | 2 |
| tarea 3 | 10 |
| tarea 4 | 3 |

***

*Total = 21 puntos*
*Integrante 1 hará tarea 3 = 10 puntos = 47%*
*Integrante 2 hará tarea 1, 2, 4, 5 = 11 puntos = 53%*
Si una tarea es reasignada, la persona que recibe la tarea puede aumentar su porcentaje de participación del proyecto, puesto a que tendrá más puntaje a realizar en el proyecto.
Al final de cada sprint se colocarán las tareas realizadas, las tareas sin terminar serán relegadas al siguiente sprint, por que la cantidad de puntos aumentará en ese sprint, haciendo que los porcentajes puedan variar más a favor de una persona.
Cabe aclarar que la creación de tareas y sus puntajes tratará de ser lo más equitativo posible para que todos los integrantes tengan un porcentaje parecido.

## Roles del Equipo

| **Miembro** |      **Rol(es)**      |  
|----------|:-------------:|
| Anaya Axel | SCRUM MASTER, diseño de la base de datos, desarrollo back-end. |
| Cruz Pedro | Desarrollo front-end, diseño. |
| Méndez José | Back-end, diseñp de la base de datos. |
| Hernández Rpdrigo | Front-end, QA |
