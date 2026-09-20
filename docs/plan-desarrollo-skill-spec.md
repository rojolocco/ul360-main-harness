# Plan de desarrollo: skill para crear SPEC

## 1. Propósito

Crear una skill reutilizable para este repositorio que guíe la elaboración, revisión y actualización de un **SPEC funcional-técnico** a partir de un PRD aprobado y del contexto técnico pertinente.

La skill deberá convertir el alcance de producto definido mediante `crear-prd` en comportamientos verificables, requisitos técnicos, interfaces, datos, manejo de errores y criterios de aceptación, sin implementar código ni ampliar unilateralmente el alcance del PRD.

El resultado aprobado se guardará en `docs/spec/`. La carpeta `knowledge/` seguirá reservada exclusivamente para el trabajo y conocimiento de la persona usuaria.

## 2. Relación con la skill `crear-prd`

La nueva skill debe complementar, no duplicar, a `.agents/skills/crear-prd/SKILL.md`:

| `crear-prd` | `crear-spec` |
| --- | --- |
| Define qué crear o cambiar, por qué y para quién. | Define el comportamiento y las condiciones técnicas necesarias para construirlo. |
| Delimita problema, valor, alcance y éxito. | Detalla flujos, reglas, interfaces, datos, errores y validación. |
| Evita decisiones de implementación. | Registra decisiones técnicas confirmadas y propuestas por validar. |
| Produce `docs/prd/<iniciativa>-prd.md`. | Produce `docs/spec/<iniciativa>-spec.md`. |

El PRD será la fuente principal de alcance y trazabilidad. Si el SPEC requiere cambiar objetivos, prioridades, capacidades o exclusiones, la skill deberá detener esa decisión y recomendar primero la actualización del PRD.

## 3. Principios y restricciones

- Leer completamente el PRD de origen antes de proponer el SPEC.
- No inventar arquitectura, contratos, datos, métricas, dependencias ni requisitos de seguridad.
- Diferenciar siempre información confirmada, `Supuesto`, `Pendiente` y `Por validar`.
- Inspeccionar solo código, documentación, configuración, diagramas o notas relevantes para el cambio.
- No modificar código, configuración ni archivos de `knowledge/` como parte de esta skill.
- Mostrar el borrador, la ruta y los cambios previstos antes de escribir.
- No sobrescribir un SPEC existente sin releerlo, explicar el impacto y obtener aprobación explícita.
- Utilizar enlaces Markdown relativos al PRD y a las fuentes locales realmente consultadas.
- Usar el idioma de la persona usuaria, con español como valor por defecto.
- No agregar metadatos YAML salvo que una convención del repositorio o la persona usuaria lo requiera.

## 4. Resultado esperado de la primera versión

Al invocar la skill, el agente deberá:

1. Determinar si se creará, revisará o actualizará un SPEC.
2. Solicitar y leer el PRD de origen.
3. Resumir el objetivo, alcance, exclusiones y capacidades relevantes del PRD.
4. Detectar contradicciones, ampliaciones de alcance y vacíos bloqueantes.
5. Revisar el contexto técnico estrictamente necesario.
6. Formular preguntas breves sobre comportamiento, datos, interfaces, errores, restricciones y validación.
7. Redactar requisitos funcionales y criterios de aceptación identificados y trazables.
8. Presentar un borrador completo o suficientemente representativo para aprobación.
9. Guardar el documento aprobado en `docs/spec/`.
10. Informar decisiones pendientes, riesgos, bloqueos y siguiente acción recomendada.

## 5. Alcance funcional

### Incluido

- Creación, revisión y actualización de SPEC funcional-técnicos.
- Trazabilidad entre PRD, requisitos y criterios de aceptación.
- Requisitos funcionales con identificadores estables (`RF-01`, `RF-02`, etc.).
- Criterios de aceptación con identificadores estables (`CA-01`, `CA-02`, etc.).
- Descripción de flujos, reglas de negocio, casos límite y estados.
- Definición de entradas, salidas, errores, datos e integraciones cuando apliquen.
- Requisitos no funcionales medibles o marcados como pendientes.
- Registro explícito de riesgos, dependencias, decisiones y bloqueos.
- Revisión de SPEC existentes sin pérdida de decisiones todavía vigentes.

### Excluido en la v1

- Implementación de código o configuración.
- Generación automática de tareas de desarrollo.
- Modificación del PRD desde el SPEC.
- Selección unilateral de arquitectura o tecnología.
- Invención de contratos de API, esquemas o umbrales de calidad.
- Gestión automática del ciclo de despliegue.
- Escritura de artefactos en `knowledge/`.

## 6. Flujo conversacional propuesto

### Fase A: descubrir y validar el contexto

1. Confirmar el tipo de trabajo: SPEC nuevo, revisión o actualización.
2. Solicitar la ruta del PRD si no fue indicada y leerlo por completo.
3. Si existe un SPEC previo, leerlo y distinguir qué se conserva, qué cambia y por qué.
4. Inspeccionar únicamente las fuentes técnicas necesarias para comprender las partes afectadas.
5. Resumir el objetivo, alcance, exclusiones, capacidades y criterios de éxito del PRD.
6. Señalar antes de continuar cualquier contradicción, ampliación de alcance o ausencia de información esencial.

### Fase B: concretar la solución

Preguntar solo por información que no esté resuelta en el PRD o en las fuentes consultadas:

- comportamiento y flujo principal;
- flujos alternativos, estados y casos límite;
- entradas, salidas y reglas de negocio;
- datos, interfaces, sistemas e integraciones afectados;
- errores esperados y forma de comunicarlos;
- restricciones de seguridad, privacidad, rendimiento, disponibilidad, accesibilidad y compatibilidad;
- decisiones técnicas ya confirmadas y decisiones que requieren validación;
- pruebas o evidencias que demostrarán el cumplimiento.

Los vacíos no bloqueantes se conservarán como pendientes. Los vacíos que impidan implementar, integrar o verificar la solución se destacarán como bloqueantes.

### Fase C: redactar y validar

1. Presentar una síntesis de la solución y su correspondencia con el PRD.
2. Redactar el borrador usando la plantilla base.
3. Verificar que cada requisito sea observable y comprobable.
4. Comprobar la trazabilidad entre PRD, requisitos y criterios de aceptación.
5. Etiquetar decisiones no confirmadas y evitar presentarlas como hechos.
6. Mostrar el borrador, la ruta propuesta y todos los archivos que se crearían o actualizarían.
7. Solicitar aprobación explícita para escribir.

### Fase D: guardar y cerrar

1. Releer el destino si ya existe y comprobar que no cambió desde la revisión.
2. Crear `docs/spec/` solo después de la aprobación, si aún no existe.
3. Guardar el Markdown aprobado como `docs/spec/<nombre-iniciativa>-spec.md`.
4. Validar los enlaces relativos al PRD y a las fuentes utilizadas.
5. Informar la ruta final, pendientes, riesgos, bloqueos y siguiente acción recomendada.

## 7. Estructura base del SPEC

La skill incorporará una plantilla proporcional al cambio. Las secciones no aplicables podrán omitirse con una explicación breve.

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
- RF-01: <comportamiento observable>. Trazabilidad: <referencia al PRD>.

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
- <condición y comportamiento esperado>

## Criterios de aceptación y validación
- [ ] CA-01: <resultado comprobable>. Cubre: <RF-XX y referencia al PRD>.
- Pruebas o evidencias necesarias:

## Riesgos, dependencias y despliegue
- Riesgo:
- Dependencia:
- Migración, compatibilidad o reversión:

## Decisiones pendientes
- [ ] <etiqueta, decisión, impacto y responsable o evidencia requerida>

## Referencias
- [PRD de origen](../prd/<nombre>-prd.md)
- 
```

## 8. Diseño de archivos

La primera entrega tendrá una única fuente de instrucciones compatible con los harnesses que soporten Agent Skills:

```text
.agents/
└── skills/
    └── crear-spec/
        └── SKILL.md
```

`SKILL.md` deberá contener:

- frontmatter válido con `name: crear-spec` y una descripción de activación precisa;
- propósito, límites y relación con `crear-prd`;
- reglas documentales y de seguridad;
- flujo de cuatro fases;
- reglas de calidad y trazabilidad;
- plantilla del SPEC;
- tratamiento de casos especiales;
- lista de comprobación previa al guardado.

No se añadirá Python en la primera versión. Solo se evaluará una utilidad en `src/` si las pruebas revelan tareas deterministas repetitivas, como validar identificadores, trazabilidad o enlaces.

## 9. Plan de implementación

| Etapa | Actividades | Entregable | Criterio de salida |
| --- | --- | --- | --- |
| 1. Alinear | Confirmar relación PRD–SPEC, idioma, ubicación, nomenclatura y política de aprobación. | Decisiones documentadas. | No quedan dudas que alteren el flujo o los destinos. |
| 2. Especificar | Definir instrucciones, preguntas mínimas, plantilla, trazabilidad y casos especiales. | Borrador de `SKILL.md`. | Cubre creación, revisión y actualización sin implementar código. |
| 3. Implementar | Crear o ajustar `.agents/skills/crear-spec/SKILL.md`. | Fuente única de la skill. | Frontmatter válido e instrucciones coherentes con `crear-prd`. |
| 4. Probar | Ejecutar escenarios de aceptación en los harnesses objetivo. | Registro de resultados y defectos. | No se inventa información ni se escribe sin aprobación. |
| 5. Ajustar | Eliminar redundancias, aclarar bloqueos y refinar la plantilla. | v1 estable. | Produce SPEC verificables y trazables con pocas preguntas innecesarias. |
| 6. Documentar | Registrar uso, límites y relación con la skill de PRD. | Documentación final. | Una persona puede usar ambas skills de forma secuencial. |

## 10. Casos de prueba de aceptación

1. **Flujo nominal:** dado un PRD aprobado, la skill genera un SPEC trazable y propone guardarlo en `docs/spec/`.
2. **PRD ausente:** solicita la ruta y recomienda usar `crear-prd`; solo continúa por excepción explícita y documentada.
3. **PRD ambiguo:** detecta vacíos de alcance o aceptación y no inventa respuestas.
4. **Contradicción con el PRD:** señala el conflicto y recomienda actualizar primero el documento de producto.
5. **Contexto técnico insuficiente:** no presupone stack ni arquitectura y marca las decisiones imprescindibles como bloqueantes.
6. **SPEC existente:** relee el documento, explica qué cambia y conserva las decisiones vigentes antes de pedir aprobación.
7. **Trazabilidad:** cada requisito y criterio relevante referencia la capacidad, objetivo o restricción correspondiente del PRD.
8. **Requisitos no funcionales:** todo umbral cuantitativo incluye método de medición o queda marcado como pendiente.
9. **Solicitud de implementación:** separa la creación del SPEC de cualquier cambio de código o configuración.
10. **Seguridad documental:** no modifica `knowledge/` ni sobrescribe archivos sin autorización explícita.
11. **Enlaces relativos:** el SPEC final enlaza correctamente el PRD y solo las fuentes realmente utilizadas.
12. **Sección no aplicable:** omite apartados irrelevantes en vez de rellenarlos con contenido ficticio.

## 11. Decisiones que deben confirmarse durante el desarrollo

- Harnesses objetivo y mecanismo de descubrimiento de `.agents/skills/` en cada uno.
- Si el repositorio exigirá revisión humana técnica adicional antes de considerar aprobado un SPEC.
- Si se adoptará una tabla de trazabilidad obligatoria o referencias junto a cada requisito.
- Si habrá estados documentales o metadatos comunes para PRD y SPEC.
- Convención para versionar cambios incompatibles en interfaces o datos.
- Herramientas disponibles para validar enlaces e identificadores de forma automática.

Estas decisiones no bloquean el borrador inicial de la skill; deberán permanecer explícitas hasta ser confirmadas.

## 12. Definición de terminado de la v1

La v1 estará terminada cuando la skill pueda partir de un PRD aprobado, detectar conflictos y vacíos, consultar únicamente el contexto técnico pertinente y producir un SPEC Markdown implementable, verificable y trazable en `docs/spec/`. El proceso deberá preservar la separación entre producto y solución técnica, no inventar decisiones, no modificar código ni `knowledge/`, y exigir aprobación explícita antes de crear o actualizar el documento final.
