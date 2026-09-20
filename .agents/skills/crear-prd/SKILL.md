---
name: crear-prd
description: Guía la creación, revisión o transformación de un PRD en Markdown desde una conversación y contexto local. Úsala para definir qué producto crear o cambiar, por qué, para quién, qué problema resuelve, su alcance y éxito, antes de diseñar o implementar software.
---

# Crear PRD

## Propósito, límites y relación con el SPEC

Convierte una idea, necesidad o notas locales en un **Product Requirements Document (PRD)** claro, trazable y centrado en producto. Un PRD define qué se quiere crear o cambiar, por qué, para quién, qué problema resuelve, qué incluye y cómo se reconocerá el éxito. El resultado aprobado se guarda únicamente en `docs/prd/<iniciativa>-prd.md`.

Esta skill precede a `crear-spec`:

- `crear-prd` define problema, valor, personas, alcance, exclusiones, capacidades y resultados observables.
- `crear-spec` concreta posteriormente flujos, reglas, interfaces, datos, errores, validación y decisiones técnicas dentro del alcance aprobado.

No incluyas arquitectura, selección de tecnologías, APIs, modelos de datos, componentes, tareas de programación, configuración ni código. Si aparecen, sepáralos de las decisiones de producto, regístralos solo como contexto si es necesario y recomienda tratarlos después con `crear-spec`. No cambies el PRD para acomodar una solución técnica no aprobada.

No inventes investigación, evidencia, usuarios, métricas, requisitos ni decisiones. Distingue explícitamente la información confirmada de `Supuesto`, `Pendiente` y `Por validar`.

## Reglas documentales y seguridad

- Lee antes de modificar cualquier archivo.
- `knowledge/` está reservado exclusivamente para el trabajo y conocimiento de la persona usuaria. Puedes leer fuentes pertinentes, pero nunca guardes PRD allí ni muevas, clasifiques o modifiques su contenido.
- Lee primero los README de la estructura PARA; después, consulta únicamente las fuentes adicionales pertinentes que señale la persona usuaria. No supongas que existe otro contexto.
- Los PRD aprobados viven en `docs/prd/`. Los borradores se muestran solo en la conversación; no los guardes.
- No crees directorios ni escribas o actualices archivos hasta mostrar el borrador, la ruta propuesta y todos los cambios previstos, y recibir aprobación explícita. El silencio o una respuesta ambigua no autorizan la escritura.
- Si el PRD ya existe, léelo completo antes de proponer cambios. Explica qué se conserva, qué cambia y por qué; pide aprobación explícita antes de sobrescribirlo.
- Antes de guardar un PRD existente, vuelve a leer el destino. Si cambió desde la revisión, detente y explica la diferencia antes de sobrescribir.
- Usa enlaces Markdown relativos solo a fuentes locales realmente consultadas. No enlaces archivos no revisados ni alteres las fuentes para añadir enlaces.
- Usa el idioma de la persona usuaria; usa español por defecto.
- Nombra el archivo en minúsculas, con palabras separadas por guiones y el sufijo `-prd.md`: `docs/prd/<nombre-iniciativa>-prd.md`. Si el nombre es ambiguo, pregunta antes de decidirlo.
- No añadas metadatos YAML al PRD salvo que la persona o una convención existente lo requiera.

## Flujo

### Fase A: descubrir y validar el contexto

1. Determina si es un PRD nuevo, la revisión de uno existente o la transformación de notas indicadas.
2. Lee todos los `README.md` existentes en `knowledge/0_ENTRADA/`, `knowledge/1_PROJECTOS/`, `knowledge/2_AREAS/`, `knowledge/3_RECURSOS/`, `knowledge/4_ARCHIVO/` y `knowledge/5_PAPELERA/`.
3. Interpreta la estructura PARA según esos README. Como referencia, y nunca como imposición: `0_ENTRADA` suele contener capturas pendientes; `1_PROJECTOS`, resultados temporales; `2_AREAS`, responsabilidades continuas; `3_RECURSOS`, material de consulta; `4_ARCHIVO`, contenido inactivo conservado; y `5_PAPELERA`, contenido descartado. Si un README o la persona define otro significado, este prevalece. Si falta una convención necesaria, pregunta en vez de asumirla.
4. Revisa únicamente las notas, proyectos o documentos adicionales que la persona señale como pertinentes. Una nota de entrada puede ser evidencia, pero no debe moverse ni clasificarse.
5. Si hay un PRD previo, léelo completamente y distingue decisiones vigentes, cambios propuestos y su motivo.
6. Informa brevemente las fuentes utilizadas y las lagunas o contradicciones relevantes.

### Fase B: definir el producto

Pregunta primero, de forma breve, agrupada y no técnica, solo lo que no esté ya resuelto:

- ¿Qué queremos crear o cambiar?
- ¿Por qué es importante ahora?
- ¿Qué problema, necesidad u oportunidad aborda?
- ¿Para quién se crea y en qué situación se encuentra esa persona?
- ¿Qué resultado o cambio de comportamiento esperamos?

Cuando lo esencial esté claro, pregunta solo lo necesario para completar el alcance:

- ¿Qué incluye y qué queda fuera de la primera versión?
- ¿Qué restricciones, alternativas, riesgos o dependencias se conocen?
- ¿Qué señales observables, métricas o resultados indicarían éxito?
- ¿Qué otras personas interesadas deben considerarse?

Conserva los vacíos no bloqueantes como `Pendiente` o `Por validar`. Si la ambigüedad impide entender la iniciativa, el problema, la persona beneficiaria o el alcance, pide aclaración antes de presentar el PRD como listo. No conviertas preferencias técnicas en requisitos de producto.

### Fase C: redactar y validar

1. Presenta una síntesis de una o dos frases de la iniciativa. Pide aclaración si hay ambigüedad sustancial sobre qué, por qué, para quién o el problema.
2. Redacta un borrador proporcional con la plantilla siguiente. Omite apartados que no aporten valor e indica brevemente la razón; no los rellenes con contenido ficticio.
3. Formula cada capacidad como resultado observable o necesidad que se cubre, por ejemplo: «La persona puede encontrar…». No redactes soluciones como «Crear una API…».
4. Comprueba la coherencia entre objetivo, propuesta, alcance, exclusiones, capacidades y criterios de éxito. Señala contradicciones en lugar de resolverlas unilateralmente.
5. Etiqueta toda información no confirmada como `Supuesto`, `Pendiente` o `Por validar`.
6. Muestra el borrador completo o uno suficientemente representativo, la ruta propuesta y todos los archivos que se crearían o actualizarían. Solicita autorización explícita para escribir.

### Fase D: guardar y cerrar

Solo después de la aprobación explícita:

1. Relee el destino si existe y verifica que no cambió desde la última revisión.
2. Crea `docs/prd/` solo si es necesario y guarda exactamente el Markdown aprobado.
3. Verifica que las referencias relativas funcionen desde la ruta final y que apunten únicamente a fuentes usadas.
4. Comunica la ruta final, supuestos, pendientes, riesgos y dependencias. Recomienda como siguiente paso una revisión de producto o, cuando el alcance esté aprobado y se necesiten detalles técnicos, `crear-spec`.

## Plantilla del PRD

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
<Descripción de alto nivel de lo que se creará, sin detallar implementación técnica.>

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

## Casos especiales

- **Repositorio o conocimiento recién inicializado:** si solo hay README de PARA, interpreta esos README, informa que no hay antecedentes adicionales y continúa con la entrevista.
- **Nota en `0_ENTRADA`:** úsala como evidencia y enlázala únicamente si fue consultada; no la muevas, clasifiques ni modifiques.
- **Convención PARA particular o incompleta:** el significado documentado localmente prevalece. Si falta una definición relevante, pregunta; no impongas taxonomías.
- **Información incompleta:** no inventes evidencia, métricas, alcance ni decisiones. Registra el vacío con la etiqueta apropiada.
- **Solicitud técnica:** separa arquitectura, APIs, datos o código del PRD y recomienda crear o actualizar un SPEC posteriormente.
- **PRD existente:** conserva las decisiones vigentes, describe el impacto de los cambios propuestos y espera aprobación antes de sobrescribir.
- **Nombre de iniciativa ambiguo:** pide un nombre antes de fijar la ruta del archivo.
- **Sección no aplicable:** omítela y explica brevemente por qué, en vez de completar marcadores ficticios.

## Comprobación antes de guardar

Confirma que:

- se leyeron los README de PARA existentes y solo el contexto adicional pertinente;
- se entiende o se marcaron como bloqueantes la iniciativa, el problema, la persona beneficiaria y el alcance;
- el documento no contiene arquitectura, APIs, modelos de datos, tareas ni código;
- objetivo, propuesta, alcance, capacidades y criterios de éxito son coherentes;
- toda incertidumbre está etiquetada como `Supuesto`, `Pendiente` o `Por validar`;
- las referencias son relativas y corresponden solo a archivos realmente consultados;
- no se modificará contenido de `knowledge/`;
- la persona vio el borrador, la ruta y los cambios previstos, y autorizó explícitamente la escritura.
