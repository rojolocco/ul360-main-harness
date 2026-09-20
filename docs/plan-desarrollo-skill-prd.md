# Plan de desarrollo: skill para crear PRD

## 1. Propósito

Crear una skill reutilizable para este repositorio que guíe la elaboración, revisión y transformación de un **Product Requirements Document (PRD)** a partir de una conversación y del contexto local pertinente.

La skill deberá ayudar a definir, antes de diseñar o implementar software, **qué se quiere crear o cambiar, por qué, para quién, qué problema resuelve, cuál es su alcance y cómo se reconocerá el éxito**.

El resultado aprobado se guardará en `docs/prd/`. La carpeta `knowledge/` seguirá reservada exclusivamente para el trabajo y conocimiento de la persona usuaria.

## 2. Relación con la skill `crear-spec`

La skill debe establecer el alcance de producto que posteriormente podrá concretar `.agents/skills/crear-spec/SKILL.md`:

| `crear-prd` | `crear-spec` |
| --- | --- |
| Define qué crear o cambiar, por qué y para quién. | Define el comportamiento y las condiciones técnicas necesarias para construirlo. |
| Delimita problema, valor, alcance y éxito. | Detalla flujos, reglas, interfaces, datos, errores y validación. |
| Expresa capacidades y resultados observables. | Convierte esas capacidades en requisitos verificables. |
| Evita imponer arquitectura o implementación. | Registra decisiones técnicas confirmadas y propuestas por validar. |
| Produce `docs/prd/<iniciativa>-prd.md`. | Produce `docs/spec/<iniciativa>-spec.md`. |

El PRD será la fuente principal de alcance para el SPEC. Por ello, la skill no deberá mezclar decisiones técnicas con decisiones de producto. Si durante la conversación aparecen detalles de arquitectura, APIs, datos o implementación, deberá separarlos y recomendar tratarlos posteriormente mediante `crear-spec`.

## 3. Contexto del repositorio

| Aspecto | Decisión |
| --- | --- |
| Propósito del repositorio | Desarrollar y conservar conocimiento de la persona usuaria en `knowledge/`. |
| Producción principal | Documentos Markdown; no código de producto. |
| Organización del conocimiento | Método PARA mediante `0_ENTRADA`, `1_PROJECTOS`, `2_AREAS`, `3_RECURSOS`, `4_ARCHIVO` y `5_PAPELERA`. |
| Reserva de `knowledge/` | La skill puede consultar contexto pertinente, pero no guardar allí PRD ni modificar, mover o clasificar su contenido. |
| Destino de los PRD | `docs/prd/`, fuera de `knowledge/`. |
| Estado inicial previsto | La skill debe funcionar aunque `knowledge/` solo contenga los README que describen las carpetas PARA. |
| Código Python en `src/` | Solo se añadirá para utilidades deterministas de soporte si una necesidad repetitiva lo justifica. |
| Ubicación de la skill | `.agents/skills/crear-prd/SKILL.md` como fuente compartida para los harnesses compatibles con Agent Skills. |

La convención PARA puede variar entre proyectos. La skill deberá leer sus README y respetar el significado documentado por la persona usuaria, sin imponer una taxonomía universal.

## 4. Principios y restricciones

- Leer antes de modificar cualquier archivo.
- No inventar investigación, evidencia, usuarios, métricas, requisitos ni decisiones.
- Diferenciar siempre información confirmada, `Supuesto`, `Pendiente` y `Por validar`.
- Mantener el PRD centrado en problema, valor, alcance y resultados observables.
- No incluir arquitectura, contratos de API, modelos de datos, tareas de programación ni código.
- Leer primero los README de la estructura PARA para comprender el contexto del repositorio.
- Inspeccionar después únicamente las fuentes adicionales pertinentes que indique la persona usuaria.
- No modificar, mover ni clasificar contenido de `knowledge/`.
- Mostrar el borrador, la ruta y los cambios previstos antes de escribir.
- No sobrescribir un PRD existente sin releerlo, explicar los cambios y obtener aprobación explícita.
- Utilizar enlaces Markdown relativos únicamente a fuentes locales realmente consultadas.
- Usar el idioma de la persona usuaria, con español como valor por defecto.
- No guardar borradores: se mostrarán en la conversación hasta recibir aprobación.
- Nombrar los archivos en minúsculas, con palabras separadas por guiones y el sufijo `-prd.md`.

## 5. Resultado esperado de la primera versión

Al invocar la skill, el agente deberá:

1. Determinar si se creará un PRD, se revisará uno existente o se transformarán notas indicadas por la persona usuaria.
2. Leer los README de las carpetas PARA y comprender la convención local.
3. Revisar únicamente el contexto adicional pertinente.
4. Formular preguntas breves sobre iniciativa, motivación, problema, personas beneficiarias y resultado esperado.
5. Completar, cuando sea necesario, alcance, exclusiones, riesgos, dependencias y señales de éxito.
6. Detectar contradicciones, información ausente y decisiones todavía no validadas.
7. Redactar capacidades como resultados observables, sin imponer soluciones técnicas.
8. Presentar un borrador completo o suficientemente representativo para revisión.
9. Solicitar aprobación explícita antes de crear o actualizar archivos.
10. Guardar el PRD aprobado en `docs/prd/` y comunicar pendientes y siguiente acción recomendada.

## 6. Alcance funcional

### Incluido

- Creación, revisión y transformación de PRD.
- Entrevista guiada para descubrir la iniciativa y el problema.
- Uso de los README de PARA para interpretar el contexto del repositorio.
- Consulta de notas y documentos locales señalados como fuentes pertinentes.
- Definición de personas involucradas, objetivo, valor, propuesta y alcance.
- Redacción de capacidades y requisitos de producto observables.
- Identificación de criterios de éxito verificables o pendientes de definición.
- Registro explícito de supuestos, riesgos, dependencias y preguntas abiertas.
- Trazabilidad mediante enlaces relativos a las fuentes locales utilizadas.
- Revisión de documentos existentes sin pérdida de decisiones todavía vigentes.

### Excluido en la v1

- Diseño de arquitectura o selección de tecnologías.
- Definición de APIs, esquemas, componentes o integraciones técnicas.
- Implementación de código o configuración.
- Generación automática de tareas de desarrollo.
- Gestión automática del ciclo de vida de proyectos o del método PARA.
- Movimiento, clasificación o modificación de contenido en `knowledge/`.
- Invención de investigación, métricas, requisitos o decisiones.
- Escritura o sobrescritura de documentos sin aprobación explícita.

## 7. Flujo conversacional propuesto

### Fase A: descubrir y validar el contexto

1. Confirmar el tipo de trabajo: PRD nuevo, revisión o transformación de notas.
2. Leer los README existentes de:
   - `knowledge/0_ENTRADA/`;
   - `knowledge/1_PROJECTOS/`;
   - `knowledge/2_AREAS/`;
   - `knowledge/3_RECURSOS/`;
   - `knowledge/4_ARCHIVO/`;
   - `knowledge/5_PAPELERA/`.
3. Identificar el significado que la persona usuaria da a cada carpeta. Si no está documentado y resulta relevante, preguntar en lugar de asumir.
4. Revisar únicamente las notas, proyectos o documentos adicionales que indique la persona usuaria.
5. Si existe un PRD previo, leerlo completamente y distinguir qué se conserva, qué cambia y por qué.
6. Informar brevemente qué fuentes se utilizaron y señalar lagunas o contradicciones relevantes.

Como referencia, no como imposición, las carpetas suelen representar:

- `0_ENTRADA`: capturas o material pendiente de procesar;
- `1_PROJECTOS`: trabajo asociado a resultados concretos y temporales;
- `2_AREAS`: responsabilidades continuas;
- `3_RECURSOS`: referencias y material de consulta;
- `4_ARCHIVO`: contenido inactivo que se conserva;
- `5_PAPELERA`: contenido descartado o pendiente de eliminación.

### Fase B: definir el producto

Preguntar primero, en lenguaje no técnico y sin repetir información ya disponible:

- ¿Qué queremos crear o cambiar?
- ¿Por qué es importante ahora?
- ¿Qué problema, necesidad u oportunidad aborda?
- ¿Para quién se crea y qué situación vive esa persona?
- ¿Qué resultado o cambio de comportamiento esperamos?

Cuando esas respuestas estén claras, preguntar solo lo necesario para cerrar el PRD:

- qué incluye y qué queda fuera de la primera versión;
- restricciones, alternativas, riesgos y dependencias conocidas;
- señales observables o métricas que indicarían éxito;
- otras personas interesadas que deban considerarse.

Los vacíos no bloqueantes se conservarán como pendientes. Si una ambigüedad impide definir la iniciativa, el problema, la persona beneficiaria o el alcance, deberá resolverse antes de presentar el documento como listo.

### Fase C: redactar y validar

1. Presentar una síntesis de una o dos frases sobre la iniciativa.
2. Pedir aclaración cuando exista ambigüedad sustancial sobre el qué, el porqué, la persona o el problema.
3. Redactar el borrador usando la plantilla base.
4. Expresar las capacidades como resultados observables, no como soluciones técnicas.
5. Comprobar la consistencia entre objetivo, propuesta, alcance, capacidades y criterios de éxito.
6. Etiquetar toda información no confirmada como `Supuesto`, `Pendiente` o `Por validar`.
7. Mostrar el borrador, la ruta propuesta y todos los archivos que se crearían o actualizarían.
8. Solicitar aprobación explícita antes de escribir; el silencio o una respuesta ambigua no serán suficientes.

### Fase D: guardar y cerrar

1. Releer el destino si ya existe y comprobar que no cambió desde la revisión.
2. Crear `docs/prd/` solo después de la aprobación, si aún no existe.
3. Guardar el Markdown aprobado como `docs/prd/<nombre-iniciativa>-prd.md`.
4. Validar los enlaces relativos a las fuentes utilizadas.
5. Informar la ruta final, decisiones pendientes y siguiente acción recomendada, como revisión de producto o creación de un SPEC.

## 8. Estructura base del PRD

La skill incorporará una plantilla proporcional a la iniciativa. Las secciones que no aporten valor podrán omitirse con una explicación breve.

```markdown
# PRD: <nombre de la iniciativa>

## Resumen
<Qué se propone crear o cambiar y por qué, en pocas líneas.>

## Contexto y problema
- Situación actual:
- Problema u oportunidad:
- Evidencia disponible:

## Personas involucradas
- Usuario o beneficiario principal:
- Necesidades y contexto de uso:
- Otros interesados:

## Objetivo y valor esperado
- Objetivo:
- Resultado esperado para la persona usuaria:
- Valor para la iniciativa/área:

## Propuesta
<Descripción de alto nivel de lo que se creará, sin detallar la implementación técnica.>

## Alcance
### Incluye
- 

### No incluye
- 

## Requisitos o capacidades
- [ ] <capacidad observable o necesidad que debe cubrirse>

## Criterios de éxito
- <resultado verificable, métrica o señal cualitativa>

## Supuestos, riesgos y dependencias
- Supuesto:
- Riesgo:
- Dependencia:

## Preguntas y decisiones pendientes
- [ ] 

## Referencias
- 
```

Las capacidades deberán expresar resultados observables. Por ejemplo, se preferirá «La persona puede encontrar…» frente a «Crear una API…». Los detalles técnicos se derivarán posteriormente en un SPEC enlazado al PRD.

## 9. Diseño de archivos

La primera entrega tendrá una única fuente de instrucciones compatible con los harnesses que soporten Agent Skills:

```text
.agents/
└── skills/
    └── crear-prd/
        └── SKILL.md
```

`SKILL.md` deberá contener:

- frontmatter válido con `name: crear-prd` y una descripción de activación precisa;
- propósito, límites y relación con `crear-spec`;
- reglas documentales y de seguridad;
- interpretación de la estructura PARA del repositorio;
- flujo de cuatro fases;
- preguntas esenciales y complementarias;
- plantilla del PRD;
- tratamiento de casos especiales;
- comprobaciones previas al guardado.

No se añadirá Python en la primera versión. Solo se evaluará una utilidad en `src/` si las pruebas revelan tareas deterministas repetitivas, como validar nombres o enlaces.

## 10. Plan de implementación

| Etapa | Actividades | Entregable | Criterio de salida |
| --- | --- | --- | --- |
| 1. Alinear | Confirmar relación PRD–SPEC, idioma, ubicación, nomenclatura y política de aprobación. | Decisiones documentadas. | No quedan dudas que alteren el flujo o los destinos. |
| 2. Especificar | Definir instrucciones, preguntas mínimas, lectura de PARA, plantilla y casos especiales. | Borrador de `SKILL.md`. | Funciona con un `knowledge/` que solo contiene README. |
| 3. Implementar | Crear o ajustar `.agents/skills/crear-prd/SKILL.md`. | Fuente única de la skill. | Frontmatter válido e instrucciones coherentes con `crear-spec`. |
| 4. Probar | Ejecutar escenarios de aceptación en los harnesses objetivo. | Registro de resultados y defectos. | No se inventa información ni se escribe sin aprobación. |
| 5. Ajustar | Eliminar preguntas redundantes, aclarar límites y refinar la plantilla. | v1 estable. | Produce PRD claros con poca orientación y sin contenido técnico impropio. |
| 6. Documentar | Registrar uso, límites y transición hacia la creación de SPEC. | Documentación final. | Una persona puede usar ambas skills de forma secuencial. |

## 11. Casos de prueba de aceptación

1. **Repositorio recién creado:** con `knowledge/` limitado a sus README, la skill interpreta la estructura, pregunta por la iniciativa y propone un PRD en `docs/prd/`.
2. **Nota en entrada:** dada una nota de `0_ENTRADA`, la utiliza como evidencia sin moverla, clasificarla ni modificarla.
3. **Convención PARA particular:** si un README define un uso distinto para una carpeta, ese significado prevalece.
4. **Contexto no documentado:** si un README no explica una convención necesaria, pregunta en lugar de imponer una clasificación.
5. **Información incompleta:** conserva métricas, evidencia o alcance desconocidos como pendientes en vez de inventarlos.
6. **Solicitud técnica:** separa arquitectura, APIs o código del PRD y recomienda crear posteriormente un SPEC.
7. **PRD existente:** relee el documento, explica qué cambia y conserva las decisiones vigentes antes de pedir aprobación.
8. **Consistencia:** objetivo, propuesta, alcance, capacidades y criterios de éxito no se contradicen.
9. **Trazabilidad:** el PRD final enlaza solo las notas y documentos que realmente sirvieron como contexto.
10. **Seguridad documental:** no modifica `knowledge/` ni sobrescribe archivos sin autorización explícita.
11. **Nombre ambiguo:** pregunta antes de decidir el nombre del archivo cuando la iniciativa no tenga una denominación clara.
12. **Sección no aplicable:** omite apartados irrelevantes en vez de rellenarlos con contenido ficticio.
13. **Compatibilidad de harnesses:** los harnesses objetivo cargan la misma fuente de instrucciones o referencian esa fuente sin duplicarla.

## 12. Decisiones que deben confirmarse durante el desarrollo

- Harnesses objetivo y mecanismo de descubrimiento de `.agents/skills/` en cada uno.
- Si el repositorio requerirá una revisión de producto adicional antes de considerar aprobado un PRD.
- Si se adoptarán estados documentales o metadatos comunes para PRD y SPEC.
- Si será necesario automatizar la validación de nombres y enlaces.
- Qué evidencia mínima, si alguna, se exigirá para presentar una iniciativa como lista para pasar a SPEC.

Estas decisiones no bloquean el borrador inicial de la skill; deberán permanecer explícitas hasta ser confirmadas y no podrán resolverse inventando convenciones.

## 13. Definición de terminado de la v1

La v1 estará terminada cuando la skill pueda funcionar con un `knowledge/` recién inicializado, interpretar la convención PARA documentada, consultar solo el contexto pertinente y producir un PRD Markdown claro, no técnico y trazable en `docs/prd/`.

El proceso deberá definir qué se crea o cambia, por qué, para quién, qué problema resuelve, qué incluye y cómo se reconocerá el éxito; además, deberá conservar las incertidumbres de forma explícita, no modificar `knowledge/` y exigir aprobación antes de crear o actualizar el documento final. El PRD resultante deberá servir como entrada coherente para la skill `crear-spec`.
