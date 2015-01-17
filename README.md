[![Build Status](https://travis-ci.org/ikks/flisol-connect.svg?branch=master)](https://travis-ci.org/ikks/flisol-connect)

flisol-connect
==============

Presencia web en el Flisol como se describe en http://flisol.info/CT/PresenciaWeb

Sitio de prueba en http://test.installfest.info

Mapa de ruta
============

- [X] Hacer la estructura de backend para soportar los modelos de datos
persistentes necesarios
- [ ] Usar autenticación con persona, github, bitbucket, openstreetmap,
facebook y googleplus.
  - [ ] Hacer página de administración de redes sociales para agregar y
  eliminar
- [X] Implementar las historias de usuario para solicitar y registrar una
instancia y un equipo
- [ ] las notificaciones en tiempo real junto con la opción de autenticarse en
el sitio para poder crear una sede.
- [ ] Hacer la página de Mi flisol en la cual puedo revisar a qué instancias
me he inscrito y el equipo que he registrado.
- [ ] Hacer la página de enlace con el wiki del 2.015 para ofrecer snippet de
openstreetmap y garantizar el flujo.
- [ ] Mejorar el admin para permitir que un administrador de sede pueda cambiar
el estado de la instancia.
- [ ] Crear los roles necesarios para ayudar en la administración de las
instancias.


Contribuir
==========

Siéntase libre de hacer fork de este proyecto para hacer fixes o solicitar PR
para añadir características.

Este sitio está hecho en Django Y Foundation.

Traducciones
------------

Hemos configurado Transifex para facilitar el proceso de
traducción, nos interesa que esté tanto en español como
portugués, estamos usando como idioma base el inglés.

Para contribuir vía Transifex, por favor visite
https://www.transifex.com/projects/p/flisol-connect/

Información de distribuciones
-----------------------------

Puede ayudarnos colocando distribuciones(de Linux o sistemas operativos libres),
por favor suscríbase a la lista de desarrollo, no hay que ser desarrollador :)

Colaborar en administración
---------------------------

Hay un rol muy importante, el cual consiste en ayudar en la operación del
portal autorizando o desautorizando para evitar spam y falsos positivos, no
se requiere conocimientos técnicos para efectuarlo y con un equipo de 5
personas será posible llevar toda la carga del portal.

Su entorno local
----------------

Para correrlo en su entorno debe crear un archivo `local_settings`, cree su
virtualenv y actualice las dependencias con pip.


Licencia
========

Este software es software libre y se apoya en herramientas y datos libres con
el mismo ánimo del Flisol.

Autores
=======

 * Igor Támara <igor@tamarapatino.org>
 * Añada su nombre y correo...
