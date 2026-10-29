# Verificación

## Pruebas automatizadas del motor
7 pruebas aprobadas: las 16 misiones; todos los dígitos correctos e incorrectos de 0 a 9; entradas inválidas; bloqueo de saltos y de cambios a resultados completados; los cuatro códigos finales; puntuación antes/después de la caja; autorización docente; pausa, reanudación, expiración y serialización del cronómetro; independencia de niveles y persistencia de textos.

El repositorio fuente incluye `tests/engine.test.js`; ejecución: `npm test` desde el proyecto fuente. La carpeta publicable no requiere Node ni instalación.

## Verificaciones de interfaz
Navegador de escritorio: inicio, selección, representación de tarjetas, campos escritos, respuesta incorrecta sin desbloqueo, validación correcta y siguiente misión; recorrido completo del Nivel 1, persistencia tras recarga, caja fuerte con 8646, victoria con 100/100 y revisión del reporte. El generador PDF se verificó con un reporte de prueba de dos páginas y renderizado visual.

Las rutas son relativas y todos los recursos residen en el paquete. No se ha publicado en una cuenta de GitHub del usuario; el paquete está preparado para GitHub Pages.

Las pruebas automatizadas verifican las reglas, no la seguridad frente a manipulación del código público. No se han probado físicamente iPads o teléfonos.
