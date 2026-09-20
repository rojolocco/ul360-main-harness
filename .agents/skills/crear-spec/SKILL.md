---
name: crear-spec
description: Guía la creación, revisión o actualización de un SPEC funcional-técnico en Markdown a partir de un PRD y del contexto local pertinente. Úsala cuando la persona necesite definir comportamiento verificable, requisitos técnicos, interfaces, datos, errores, seguridad o criterios de aceptación antes de implementar software.
---

# Crear SPEC

## Propósito y límites

Ayuda a transformar un PRD aprobado y el contexto técnico pertinente en un **Software/Technical Specification (SPEC)** funcional-técnico, implementable, verificable y trazable. El resultado se guarda únicamente en `docs/spec/`, nunca en `knowledge/`.

Esta skill complementa a `crear-prd`: el PRD define qué problema se resuelve, para quién, por qué y con qué alcance; el SPEC concreta cómo debe comportarse y construirse la solución dentro de ese alcance. No cambies objetivos, prioridades ni decisiones de producto desde el SPEC. Si hace falta hacerlo, señala la contradicción y recomienda actualizar primero el PRD.

Esta skill no implementa código, no modifica configuración ni el PRD, y no crea tareas de desarrollo. Si la persona solicita también implementación, delimita primero el SPEC y propón la implementación como una acción posterior y separada.

No inventes arquitectura, contratos de API, esquemas, métricas, dependencias, requisitos de seguridad ni otras decisiones. Distingue siempre entre información confirmada, `Supuesto`, `Pendiente` y `Por validar`.

## Reglas documentales

- Lee completamente el PRD de origen antes de proponer una solución técnica.
- Lee antes de modificar cualquier SPEC existente.
- Inspecciona solo el código, documentación, contratos, diagramas, configuración o notas que la persona indique o que sean estrictamente necesarios para interpretar el contexto solicitado.
- `knowledge/` pertenece exclusivamente al trabajo y conocimiento de la persona usuaria. Puedes leer fuentes concretas indicadas, pero no mover, clasificar ni modificar su contenido ni guardar allí artefactos de esta skill.
- Lee los README de la estructura PARA solo cuando hayan sido señalados como contexto o sean necesarios para interpretar una fuente usada de `knowledge/`.
- Los SPEC aprobados viven en `docs/spec/`.
- No crees directorios ni escribas archivos hasta mostrar el borrador, indicar la ruta y los cambios previstos, y obtener confirmación explícita.
- Nunca sobrescribas un SPEC sin releerlo, explicar los cambios y obtener confirmación explícita.
- Usa enlaces Markdown relativos al PRD y a las fuentes locales realmente utilizadas, sin alterar dichas fuentes.
- Usa el idioma de la persona usuaria; usa español por defecto.
- Nombra los archivos con minúsculas, palabras separadas por guiones y el sufijo `-spec.md`: `docs/spec/<nombre-iniciativa>-spec.md`. Si el nombre no es claro, pregunta antes de guardar.
- Los borradores solo se muestran en la conversación; no se guardan hasta ser aprobados.
- No agregues metadatos YAML al SPEC salvo que la persona o una convención existente del repositorio los requiera.

## Calidad y trazabilidad

- Asigna identificadores estables a los requisitos funcionales (`RF-01`, `RF-02`) y criterios de aceptación (`CA-01`, `CA-02`).
- Redacta cada requisito como comportamiento observable y verificable. Evita expresiones ambiguas como «rápido», «intuitivo» o «seguro» sin una condición comprobable.
- Relaciona los requisitos y criterios relevantes con el objetivo, capacidad o restricción correspondiente del PRD. Usa referencias explícitas en el texto o una tabla de trazabilidad cuando haya varias relaciones.
- Separa requisitos funcionales, requisitos no funcionales y decisiones técnicas.
- Describe entradas, salidas, estados, reglas, errores y límites cuando apliquen. No añadas apartados técnicos solo para completar la plantilla.
- Para cada requisito no funcional cuantitativo, registra el umbral y cómo se medirá. Si no se conocen, márcalos como `Pendiente` o `Por validar`.
- Toda propuesta no confirmada debe identificarse como `Supuesto` o `Por validar`, junto con la persona o evidencia necesaria para resolverla cuando se conozca.
- No presentes como implementable un documento con decisiones abiertas que bloqueen contratos, datos, seguridad, aceptación o integración; destaca esos bloqueos en el cierre.

## Flujo

### Fase A: descubrir y validar el contexto

1. Determina si se crea un SPEC nuevo, se revisa uno existente o se deriva/actualiza desde un PRD.
2. Solicita la ruta del PRD si no se indicó. Cuando exista, léelo completo antes de proponer la solución.
3. Si se menciona un SPEC existente, léelo completo e identifica qué se conserva, qué cambia, por qué y qué impacto tendría.
4. Inspecciona únicamente las fuentes locales pertinentes indicadas por la persona o necesarias para comprender las partes afectadas. Informa qué fuentes se usaron.
5. Resume en pocas líneas el objetivo, alcance, exclusiones, capacidades y criterios de éxito extraídos del PRD.
6. Compara la solución solicitada con el PRD. Señala lagunas, ampliaciones de alcance y contradicciones antes de continuar. No las resuelvas unilateralmente.

### Fase B: concretar la especificación

Haz preguntas breves y agrupadas. No repitas lo que ya resuelvan el PRD o las fuentes revisadas. Pregunta solo lo necesario sobre:

- comportamiento esperado y flujos principales;
- entradas, salidas, estados, reglas de negocio, casos límite y errores;
- sistemas, datos, interfaces e integraciones afectadas;
- restricciones conocidas de seguridad, privacidad, rendimiento, disponibilidad, accesibilidad y compatibilidad;
- decisiones técnicas existentes y decisiones que requieren validación responsable;
- evidencia o pruebas que demostrarán el cumplimiento de cada requisito.

Si una respuesta no está disponible, continúa sin bloquear innecesariamente y registra el vacío como `Pendiente`, `Supuesto` o `Por validar`. Si el vacío impide implementar o comprobar la solución, identifícalo explícitamente como bloqueante.

### Fase C: redactar y validar

1. Presenta una síntesis de la solución propuesta, su correspondencia con el PRD y las decisiones abiertas. Pide aclaración cuando exista una contradicción o ambigüedad sustancial.
2. Redacta el borrador con la plantilla siguiente. Omite una sección solo si no aplica y explica brevemente la omisión fuera del documento o dentro de ella cuando sea útil para revisión.
3. Comprueba que cada requisito sea observable o verificable y que no introduzca alcance de producto no aprobado.
4. Comprueba la trazabilidad entre el PRD, los requisitos y los criterios de aceptación.
5. Conserva los vacíos con las etiquetas `Supuesto`, `Pendiente` o `Por validar`; no los ocultes mediante redacción afirmativa.
6. Muestra el SPEC completo o un borrador suficientemente representativo, la ruta propuesta y todos los archivos que se crearían o actualizarían.
7. Solicita autorización explícita antes de escribir. El silencio o una aprobación ambigua no cuentan como autorización.

### Fase D: guardar y cerrar

Solo después de la aprobación explícita:

1. Vuelve a leer la ruta de destino si existe y confirma si se creará o actualizará. Si cambió desde la revisión, detente y explica la diferencia antes de sobrescribir.
2. Crea `docs/spec/` si es necesario y guarda exactamente el Markdown aprobado.
3. Verifica que los enlaces relativos al PRD y a las demás fuentes usadas funcionen desde la ubicación final.
4. Informa la ruta final, las decisiones pendientes, los riesgos, los bloqueos y la siguiente acción recomendada, como revisión técnica, descomposición en tareas o implementación.

## Plantilla del SPEC

Usa esta estructura de forma proporcional al cambio:

```markdown
# SPEC: <nombre de la iniciativa o capacidad>

## Resumen
<Qué se especifica y qué resultado del PRD habilita.>

## Referencia al PRD
- PRD de origen: [<nombre>](../prd/<nombre>-prd.md)
- Objetivo y alcance relevantes:
- Decisiones de producto que condicionan este SPEC:

## Contexto actual
- Estado o comportamiento actual:
- Fuentes revisadas:
- Problema técnico que se resuelve:

## Objetivos y no objetivos técnicos
### Objetivos
- 

### No objetivos
- 

## Requisitos funcionales
- RF-01: <comportamiento observable y verificable>. Trazabilidad: <objetivo, capacidad o sección del PRD>.

## Flujos y reglas de negocio
### Flujo principal
1. 

### Flujos alternativos y casos límite
- 

### Reglas de negocio
- 

## Diseño técnico
### Componentes y responsabilidades
- 

### Interfaces e integraciones
- Entrada:
- Salida:
- Errores:
- Dependencias externas:

### Datos y estados
- Entidades, campos o contratos:
- Validaciones:
- Cambios o migraciones:

## Requisitos no funcionales
- Seguridad y privacidad:
- Rendimiento y capacidad:
- Disponibilidad y resiliencia:
- Compatibilidad y accesibilidad:
- Observabilidad:

## Manejo de errores
- <condición, comportamiento esperado y comunicación a la persona usuaria o sistema consumidor>

## Criterios de aceptación y validación
- [ ] CA-01: <resultado comprobable>. Cubre: <RF-XX y referencia al PRD>.
- Pruebas o evidencias necesarias:

## Riesgos, dependencias y despliegue
- Riesgo:
- Dependencia:
- Migración, compatibilidad o reversión:

## Decisiones pendientes
- [ ] <Pendiente, Supuesto o Por validar; impacto y responsable/evidencia si se conocen>

## Referencias
- [PRD de origen](../prd/<nombre>-prd.md)
- 
```

Los apartados de diseño técnico no fijan una arquitectura predeterminada. Complétalos solo con decisiones confirmadas o con propuestas explícitamente etiquetadas para validación.

## Casos especiales

- **PRD ausente:** no simules que existe. Solicita su ruta y recomienda crear uno mediante `crear-prd`. Solo continúa sin PRD si la persona aprueba explícitamente la excepción; registra la ausencia, su riesgo y la fuente alternativa de alcance en el SPEC.
- **PRD ambiguo o incompleto:** identifica las lagunas que afectan comportamiento, alcance o aceptación. Pide las aclaraciones esenciales y conserva lo demás como pendiente sin inventar respuestas.
- **Contradicción con el PRD:** detén la decisión contradictoria, explica el conflicto y recomienda corregir o aprobar primero el cambio de producto en el PRD.
- **SPEC existente:** léelo completo, presenta el impacto y los cambios propuestos, preserva las decisiones aún vigentes y espera confirmación antes de sobrescribir.
- **Solicitud de implementación:** explica que el resultado de esta skill es el SPEC. Termina y aprueba el documento antes de tratar código, configuración o tareas en una acción separada.
- **Falta de contexto técnico:** no presupongas stack, arquitectura ni integraciones. Produce solo el nivel respaldado por la evidencia y marca como bloqueantes las decisiones imprescindibles.
- **Sección no aplicable:** omítela cuando no aporte valor y explica la razón; no rellenes con decisiones ficticias.
- **Decisión de alto impacto:** registra alternativas y consecuencias conocidas, y déjala `Por validar` para revisión técnica humana.

## Comprobación antes de guardar

Confirma que:

- el PRD se leyó y enlazó, o que la excepción sin PRD fue aprobada y documentada;
- objetivo, alcance y exclusiones no contradicen el PRD;
- los requisitos y criterios tienen identificadores, son verificables y mantienen trazabilidad;
- las decisiones no confirmadas están etiquetadas;
- solo se citan fuentes realmente utilizadas mediante rutas relativas;
- no se modificará código, configuración ni contenido de `knowledge/`;
- la persona vio el borrador, la ruta y los cambios, y autorizó explícitamente la escritura.
