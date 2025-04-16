# Preguntas

## Criterio 6a) Objetivos estratégicos

### ¿Qué objetivos estratégicos específicos de la empresa aborda tu software?
- **Centralización y automatización de la gestión operativa:**  
  El software CLI permite a la empresa gestionar tareas y calendarios de manera centralizada, automatizando procesos como el registro, seguimiento y actualización del estado de las tareas, lo que elimina la dependencia de registros manuales en hojas de cálculo o documentos en papel.
- **Optimización de recursos y eficiencia operativa:**  
  La automatización de recordatorios y la asignación de tareas reduce el tiempo perdido en la organización manual, permitiendo que los equipos se concentren en tareas de mayor valor.
- **Mejora en la comunicación interna:**  
  Al disponer de una plataforma centralizada que mantiene actualizada la información sobre tareas y eventos, se promueve una mayor transparencia y coordinación entre los diferentes departamentos de la empresa.

### ¿Cómo se alinea el software con la estrategia general de digitalización?
- **Digitalización de procesos manuales:**  
  Transformando la gestión de tareas y eventos – que anteriormente se realizaban de forma manual – en procesos automatizados, la aplicación potencia la transformación digital de la organización.
- **Integración con sistemas de registro persistente:**  
  A través del uso de archivos JSON para la persistencia de datos, el sistema establece un primer paso para migrar hacia soluciones de almacenamiento y análisis de información más avanzadas.
- **Soporte para la toma de decisiones:**  
  La generación de reportes y la consulta en tiempo real de las tareas registradas ofrecen datos concretos que respaldan decisiones estratégicas y operativas.

---

## Criterio 6b) Áreas de negocio y comunicaciones

### ¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?
- **Producción y operaciones:**  
  Permite una mejor planificación y asignación de recursos al gestionar de forma centralizada la creación, seguimiento y actualización de tareas.
- **Negocio y gestión de proyectos:**  
  Facilita el seguimiento de las actividades operativas y los objetivos comerciales mediante un registro claro y estructurado de tareas y fechas límite.
- **Comunicaciones internas:**  
  La disponibilidad de información actualizada y centralizada mejora la coordinación entre los equipos y departamentos, evitando duplicidades y errores en la comunicación.

### ¿Qué impacto operativo esperas en las operaciones diarias?
- **Reducción de errores y tiempos de espera:**  
  La automatización en el registro y actualización de tareas reduce errores humanos y acelera los procesos administrativos.
- **Mejora en la coordinación y colaboración:**  
  Al contar con una herramienta centralizada, la información se comparte de manera inmediata, favoreciendo la colaboración y la coordinación interdepartamental.
- **Optimización en la toma de decisiones:**  
  Los datos consolidados permiten detectar cuellos de botella y oportunidades de mejora, ayudando a los responsables a tomar decisiones basadas en información actualizada.

---

## Criterio 6c) Áreas susceptibles de digitalización

### ¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?
- **Gestión de proyectos y tareas:**  
  Especialmente en aquellas áreas donde actualmente se utiliza gestión manual, la digitalización permitirá una organización más eficaz.
- **Programación y coordinación de reuniones/eventos:**  
  La automatización en el registro y seguimiento de fechas y citas evita solapamientos y mejora la planificación.
- **Control y seguimiento administrativo:**  
  Procesos rutinarios de seguimiento y actualización de actividades se benefician enormemente de la automatización y centralización de la información.

### ¿Cómo mejorará la digitalización las operaciones en esas áreas?
- **Automatización de procesos:**  
  La capacidad de registrar, actualizar y consultar tareas automáticamente elimina la dependencia de procesos manuales y reduce el tiempo invertido en administración.
- **Visibilidad y transparencia:**  
  La centralización en un único sistema proporciona una visión clara del progreso de proyectos y tareas, permitiendo un seguimiento detallado.
- **Mejora en la toma de decisiones:**  
  Al disponer de datos consolidados y en tiempo real, la empresa puede ajustar sus procesos operativos de manera ágil y basada en evidencia.

---

## Criterio 6d) Encaje de áreas digitalizadas (AD)

### ¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?
- **Interacción mixta:**  
  La aplicación CLI funciona en entornos donde algunas áreas ya se han digitalizado, mientras que otras continúan utilizando métodos tradicionales (como registros en papel o hojas de cálculo). Esto crea un escenario híbrido en el que la nueva herramienta debe integrarse y complementar los sistemas existentes.
- **Actuación como puente:**  
  El software facilita la exportación de datos a formatos legibles por otros sistemas (por ejemplo, JSON), permitiendo que la información se comparta entre las plataformas digitales y no digitales.

### ¿Qué soluciones o mejoras propondrías para integrar estas áreas?
- **Capacitación y soporte:**  
  Desarrollar programas de formación para que los usuarios de áreas tradicionales se adapten rápidamente a la herramienta digital.
- **Desarrollo de conectores:**  
  Crear APIs o scripts de integración que permitan la interoperabilidad con otros sistemas legacy (por ejemplo, sistemas ERP o CRM utilizados en la empresa).
- **Transición progresiva:**  
  Adoptar una estrategia de digitalización gradual que permita la incorporación paulatina de módulos digitales sin interrumpir la operativa existente.

---

## Criterio 6e) Necesidades presentes y futuras

### ¿Qué necesidades actuales de la empresa resuelve tu software?
- **Centralización de información:**  
  Unifica datos dispersos de tareas y eventos en una sola plataforma, facilitando el acceso y la consulta.
- **Mejor organización y planificación:**  
  Permite una asignación estructurada de tareas y el seguimiento de fechas importantes, evitando solapamientos y retrasos.
- **Reducción de tiempos administrativos:**  
  La automatización de procesos (como recordatorios y actualizaciones) libera tiempo para que el personal se enfoque en actividades estratégicas.

---

## Criterio 6f) Relación con tecnologías

### ¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?
- **Lenguaje Python para CLI:**  
  Un lenguaje de programación ampliamente utilizado y fácil de mantener, que garantiza la portabilidad y flexibilidad del software en entornos diversos.
- **Persistencia con archivos JSON:**  
  Permite el almacenamiento sencillo y rápido de datos sin la necesidad de configurar una base de datos compleja en la fase inicial, facilitando un primer paso hacia soluciones más avanzadas.
- **Ejecución en plataforma CLI:**  
  Al no depender de interfaces web específicas, la aplicación puede ejecutarse en cualquier sistema operativo (Windows, macOS, Linux) con Python instalado, asegurando una alta compatibilidad.

### ¿Qué beneficios específicos aporta la implantación de estas tecnologías?
- **Escalabilidad y rendimiento:**  
  La aplicación puede crecer en funcionalidad y ser adaptada a mayores volúmenes de datos conforme la empresa lo necesite.
- **Facilidad de integración y mantenimiento:**  
  La arquitectura modular y basada en tecnologías estándar facilita la incorporación de nuevas funcionalidades y la integración con otros sistemas.
- **Portabilidad:**  
  Al ser una aplicación CLI, se garantiza la operatividad en múltiples plataformas sin depender de un navegador o entorno web específico.

---

## Criterio 6g) Brechas de seguridad

### ¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?
- **Acceso no autorizado:**  
  Usuarios sin permisos adecuados podrían intentar acceder a información sensible almacenada en el archivo de tareas.
- **Intercepción de datos:**  
  Aunque el sistema utiliza archivos locales, la transferencia de datos entre sistemas (por ejemplo, al exportar información) podría estar expuesta.
- **Errores en la validación de datos:**  
  Sin un control riguroso, entradas maliciosas o erróneas podrían comprometer la integridad de la información.

### ¿Qué medidas concretas propondrías para mitigarlas?
- **Control de acceso y autenticación:**  
  Implementar mecanismos básicos de autenticación (por ejemplo, contraseñas o uso de claves de API para accesos a funciones críticas) para proteger el acceso al sistema.
- **Cifrado y almacenamiento seguro:**  
  Adoptar técnicas de cifrado para los datos almacenados y durante cualquier transferencia de información sensible.
- **Validación y sanitización exhaustiva:**  
  Establecer controles rigurosos en todas las entradas de datos para prevenir inyecciones y asegurar que los datos sean consistentes antes de su procesamiento.

---

## Criterio 6h) Tratamiento de datos y análisis

### ¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?
- **Gestión centralizada con archivos JSON:**  
  Los datos se gestionan a través de un archivo JSON que almacena de forma estructurada la información sobre las tareas, facilitando su lectura y actualización.
- **Validación y sanitización de entradas:**  
  Se aplican procedimientos de validación en el momento de registrar cada tarea para asegurar que los datos cumplen con los formatos requeridos (por ejemplo, el formato YYYY-MM-DD para fechas).
- **Pruebas y monitoreo:**  
  Se diseñan pruebas unitarias que permiten verificar la integridad y consistencia de los datos en las operaciones de agregar, actualizar y consultar tareas.

### ¿Qué haces para garantizar la calidad y consistencia de los datos?
- **Automatización de pruebas:**  
  Se han implementado tests automatizados que verifican la funcionalidad del registro y actualización de datos para detectar errores en etapas tempranas.
- **Revisión y auditoría continua:**  
  Se realizan revisiones de código y auditorías periódicas en el manejo de datos para asegurar que se sigan las mejores prácticas.
- **Documentación detallada:**  
  Toda la metodología de tratamiento y flujo de datos se encuentra documentada en la Wiki del proyecto, facilitando la identificación de problemas y la adopción de mejoras continuas.
