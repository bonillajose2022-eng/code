# THE SECRET CODE – ENGLISH ESCAPE ROOM
Aspaen Neiva · Aplicación estática completa · HTML, CSS y JavaScript ES Modules.

## Inicio rápido
1. Publique esta carpeta en GitHub Pages siguiendo los pasos siguientes.
2. Abra TEACHER DASHBOARD antes de entregar el dispositivo a los estudiantes. Configure un PIN propio (4–12 cifras), duración, pistas y modalidad.
3. START MISSION → seleccionar nivel → escribir el nombre del equipo → BEGIN OPERATION → ACCEPT MISSION.
4. Inicie START TIMER cuando el grupo esté listo. El tiempo inicial es 17 minutos.
5. Las respuestas escritas quedan guardadas; VERIFY CODE solo comprueba el dígito. En Teacher Verified Mode el docente revisa el trabajo y autoriza con su PIN.
6. Después de las cuatro misiones, introduzca la combinación en orden. Descargue el reporte PDF.

## Publicar gratuitamente en GitHub Pages
1. Inicie sesión en GitHub y cree un repositorio nuevo, por ejemplo `the-secret-code`.
2. Seleccione **Add file → Upload files**. Suba el CONTENIDO de esta carpeta, con `index.html` en la raíz. Mantenga las carpetas `assets`, `data`, `utils` intactas. Confirme con **Commit changes**.
3. Abra **Settings → Pages → Build and deployment → Deploy from a branch**.
4. Seleccione la rama `main` y la carpeta `/ (root)`; pulse **Save**.
5. Espere a que GitHub muestre la dirección publicada y abra esa dirección. No requiere servidor propio, pagos, claves API ni compilación.
6. Para actualizar contenido, edite `data/missions.js`, confirme los cambios y espere la nueva publicación.

Para probar ANTES de publicar, sirva la carpeta mediante un servidor HTTP local, por ejemplo `python3 -m http.server 8000` desde esta carpeta y abra `http://localhost:8000`. No abra `index.html` con doble clic: los navegadores restringen ES Modules bajo `file://`.

## Archivos
- `index.html`: estructura y metadatos.
- `styles.css`: diseño, colores, tarjetas, caja fuerte, animaciones y adaptación móvil.
- `script.js`: navegación, panel docente, sonidos Web Audio, revisión y reportes.
- `data/missions.js`: las 16 misiones, campos de respuesta, dos pistas y solucionario.
- `utils/engine.js`: verificación, bloqueos, puntaje y cronómetro.
- `utils/storage.js`: guardado local por navegador.
- `utils/reports.js`: PDF descargable sin dependencias.
- `assets/images/`: emblema y 16 ilustraciones SVG originales, locales y editables.
- `QA.md`: alcance de las verificaciones realizadas.

Todas las rutas son relativas. No hay fuentes, sonidos, imágenes ni librerías descargadas de servidores externos. La lectura en voz alta usa la voz en inglés disponible en el dispositivo; su disponibilidad sin red depende del navegador.

## Docente, PIN y privacidad
El PIN se configura en el dispositivo; no existe PIN fijo en el código. Se guarda un resumen SHA-256 local. La configuración del PIN requiere HTTPS (GitHub Pages lo proporciona) o localhost.

Este es un control de aula, NO autenticación segura. Un usuario con herramientas de desarrollo puede leer respuestas o alterar el progreso. El solucionario se oculta en la interfaz estudiantil, pero forma parte de los archivos públicos. Para cuentas seguras o resultados centralizados hace falta un servidor externo.

Configure el PIN antes del alumnado. Si se olvida, borrar los datos del sitio en el navegador restablece todo y elimina progreso. Exporte primero los reportes necesarios.

Cada nivel tiene una agencia y un progreso independiente en el navegador actual. No hay sincronización entre dispositivos ni registro central. PLAY AGAIN / RESET GAME reemplaza únicamente el equipo del nivel seleccionado, previa confirmación. Exporte el PDF antes de iniciar otro equipo en el mismo nivel. Reiniciar todos los equipos desde el panel conserva la configuración y el PIN.

## Cronómetro y puntuación
El cronómetro no empieza solo. Puede pausarse y reanudarse; conserva la fecha límite al recargar o cambiar de pantalla. A cero bloquea las verificaciones y la caja fuerte. El docente puede añadir cinco minutos. Solo el equipo seleccionado se muestra; un cronómetro iniciado de otro nivel sigue descontando tiempo real.

RESET TIMER y las extensiones requieren PIN. La duración seleccionada se aplica a nuevas partidas; el panel ofrece aplicarla al equipo actual explícitamente. El tiempo utilizado del reporte suma los segundos de cronómetro activo; pausas no cuentan. Reiniciar el tiempo no elimina lo ya utilizado.

Puntajes: participación/una misión 25; dos 50; tres 75; cuatro pendientes del código final 75; cuatro y caja abierta 100. No se penalizan errores, pistas ni tiempo. No se incluye modalidad competitiva adicional.

## Ajustes pedagógicos transparentes
Se conserva el contenido del documento maestro, con dos aclaraciones necesarias:
- Nivel 2, Misión 1: se cuentan seis adverbios terminados en `-ly`. `Suddenly` expresa un suceso inesperado; no es estrictamente un adverbio de modo. Por ello se eliminó la restricción «describe how an action happens».
- Nivel 2, Misión 2: la llegada correcta es 9:30 a.m. Su hora NO da 0. Para conservar el código acordado 6046, la instrucción pide la última cifra de los minutos.
Se permite `ran into` en Nivel 3 Misión 1 y se explicita la concordancia formal en Nivel 4 Misión 3.

No se muestra una imagen de banana en el acertijo del Nivel 1. Los textos originales se reconstruyen como texto seleccionable, con ilustraciones locales que apoyan la investigación.

## Editar preguntas
En `data/missions.js`, cada nivel contiene `missions`. Cada misión tiene `title`, `text`, `fields`, `digit` (entero de 0 a 9), `answer` (solo panel docente) y dos `hints`. El código final se deriva de los cuatro `digit`; no se repite en el motor. Cambiar los dígitos durante una partida guardada exige reiniciarla. No incluya respuestas en `text` o en las pistas.

Los campos escritos no son calificados automáticamente. Los contadores de palabras son informativos y las variantes de redacción las revisa el docente. El PDF muestra el trabajo guardado, no las respuestas modelo. Para caracteres no latinos el PDF básico utiliza `?`; acentos latinos se transliteran para compatibilidad. El reporte imprimible desde el navegador conserva Unicode completo.

## Accesibilidad y compatibilidad
Botones táctiles, etiquetas asociadas, foco visible, teclado numérico, contraste, estados anunciados y reducción de movimiento. Compatible con navegadores modernos con ES Modules, localStorage y Web Audio. La voz requiere speechSynthesis. Se recomienda revisar en el dispositivo del aula antes del evento.
