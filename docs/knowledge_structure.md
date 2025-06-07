# Estructura del Conocimiento - Sistema Experto Plantas Fueguinas

## Resumen Ejecutivo

Este documento describe la arquitectura del conocimiento implementada en el Sistema Experto para recomendación de plantas adaptadas a las condiciones de Tierra del Fuego. La estructura está diseñada para capturar y formalizar el conocimiento de expertos locales en un sistema computacional eficiente.

## 1. Arquitectura General

### Componentes Principales
- **Base de Conocimiento**: 12 especies de plantas seleccionadas
- **Motor de Reglas**: 10+ reglas de producción
- **Árbol de Decisión**: Estructura jerárquica de evaluación
- **Sistema de Inferencia**: Encadenamiento hacia adelante

### Flujo de Procesamiento
```
Usuario → Interfaz → Recolección de Condiciones → Evaluación de Reglas → 
Árbol de Decisión → Cálculo de Confianza → Recomendaciones + Explicaciones
```

## 2. Base de Conocimiento de Plantas

### Plantas de Interior - Nivel Principiante
| Planta | Luz Mínima | Humedad | Toxicidad | Confianza Base |
|--------|------------|---------|-----------|----------------|
| Sansevieria | Escasa | Baja | No tóxica | 95% |
| ZZ Plant | Escasa | Baja | Tóxica | 90% |
| Pothos | Moderada | Media | Tóxica | 85% |

### Plantas de Interior - Nivel Intermedio
| Planta | Luz Mínima | Humedad | Características | Confianza Base |
|--------|------------|---------|-----------------|----------------|
| Ficus Benjamina | Moderada | Media | Sensible a cambios | 75% |
| Monstera | Abundante | Alta | Requiere espacio | 85% |
| Dracaena | Moderada | Baja | Crecimiento vertical | 80% |

### Plantas Comestibles
| Planta | Ubicación | Requerimientos | Utilidad | Confianza Base |
|--------|-----------|----------------|----------|----------------|
| Albahaca | Interior soleado | Luz abundante | Culinaria | 70% |
| Perejil | Interior/Exterior | Luz moderada | Culinaria | 75% |

### Plantas de Exterior Protegido
| Planta | Resistencia Frío | Protección Viento | Utilidad | Confianza Base |
|--------|------------------|-------------------|----------|----------------|
| Lavanda | Alta | Necesaria | Aromática | 85% |
| Romero | Muy Alta | Moderada | Culinaria/Aromática | 90% |
| Geranios | Media | Necesaria | Ornamental | 75% |

## 3. Variables de Entrada del Sistema

### Variables Ambientales
- **luz_disponible**: `['escasa', 'moderada', 'abundante']`
- **humedad_interior**: `['baja', 'media', 'alta']`
- **temperatura_ambiente**: `['fria', 'templada', 'calida']`
- **exposicion_viento**: `['protegida', 'semi_protegida', 'expuesta']`

### Variables del Usuario
- **experiencia_usuario**: `['principiante', 'intermedio', 'avanzado']`
- **tiempo_disponible**: `['bajo', 'medio', 'alto']`
- **mascotas_presentes**: `[True, False]`
- **espacio_disponible**: `['pequeño', 'mediano', 'grande']`

### Variables Contextuales
- **ubicacion**: `['interior', 'exterior_protegido', 'ambos']`
- **epoca_año**: `['invierno', 'verano', 'transicion']`
- **tipo_vivienda**: `['apartamento', 'casa', 'casa_con_jardin']`

## 4. Sistema de Reglas de Producción

### Reglas de Filtrado Ambiental

#### R1: Plantas para Luz Escasa
```
SI luz_disponible = "escasa" Y ubicacion = "interior"
ENTONCES recomendar = ["Sansevieria", "ZZ Plant", "Pothos"]
PORQUE estas plantas han evolucionado para tolerar condiciones de baja luminosidad
CONFIANZA = 90%
```

#### R2: Filtro por Humedad Baja
```
SI humedad_interior = "baja" Y calefaccion_constante = True
ENTONCES priorizar = plantas WHERE tolerancia_sequedad = "alta"
PORQUE la calefacción fueguina reduce drásticamente la humedad ambiental
CONFIANZA = 95%
```

#### R3: Exclusión por Cambios Térmicos
```
SI temperatura_variable = True Y ubicacion_ventana = True
ENTONCES excluir = ["Ficus", "Monstera"]
PORQUE son sensibles a fluctuaciones térmicas bruscas
CONFIANZA = 85%
```

### Reglas de Filtrado por Usuario

#### R4: Nivel Principiante
```
SI experiencia_usuario = "principiante" Y tiempo_disponible = "bajo"
ENTONCES recomendar = plantas WHERE dificultad = "baja"
PORQUE minimizan riesgo de fracaso y frustración
CONFIANZA = 88%
```

#### R5: Seguridad con Mascotas
```
SI mascotas_presentes = True
ENTONCES excluir = plantas WHERE toxicidad = True
Y priorizar = ["Sansevieria", "Plantas_comestibles", "Suculentas"]
PORQUE garantiza seguridad de animales domésticos
CONFIANZA = 100%
```

### Reglas de Optimización Estacional

#### R6: Adaptación Invierno Fueguino
```
SI epoca_año = "invierno" Y fotoperíodo = "corto"
ENTONCES modificar_cuidados = "reducir_riego_50%" 
Y priorizar = plantas WHERE tolerancia_baja_luz = "alta"
PORQUE el metabolismo vegetal disminuye significativamente
CONFIANZA = 92%
```

## 5. Árbol de Decisión - Estructura Jerárquica

### Nivel 1: Ubicación Principal
```
UBICACIÓN
├── Interior (80% casos)
│   ├── Luz Disponible
│   └── Humedad Interior
├── Exterior Protegido (15% casos)
│   └── Resistencia Heladas
└── Ambos (5% casos)
    └── Facilidad Traslado
```

### Nivel 2: Condiciones Específicas
```
INTERIOR → LUZ DISPONIBLE
├── Escasa (≤4h luz directa)
│   └── → [Sansevieria, ZZ Plant, Pothos]
├── Moderada (4-8h luz indirecta)
│   └── → [Dracaena, Ficus, Plantas_comestibles]
└── Abundante (>8h luz directa)
    └── → [Monstera, Albahaca, Geranios_interior]
```

### Nivel 3: Filtros Adicionales
```
EXPERIENCIA_USUARIO
├── Principiante → Filtrar por dificultad = "baja"
├── Intermedio → Permitir dificultad ≤ "media"
└── Avanzado → Sin restricciones
```

## 6. Sistema de Cálculo de Confianza

### Fórmula de Confianza
```
Confianza_Final = (Σ(Peso_i × Puntuación_i)) / Σ(Peso_i) × 100

Donde:
- Criterios Críticos (luz, toxicidad): Peso = 3
- Criterios Importantes (humedad, dificultad): Peso = 2
- Criterios Deseables (estética, utilidad): Peso = 1
```

### Matriz de Puntuación
| Criterio | Puntuación Máxima | Condición |
|----------|-------------------|-----------|
| Compatibilidad Luz | 100 | Requisitos cumplidos completamente |
| Tolerancia Humedad | 100 | Adaptada a condiciones del hogar |
| Nivel Dificultad | 100 | Coincide con experiencia usuario |
| Seguridad Mascotas | 100/0 | Tóxica = 0, No tóxica = 100 |
| Utilidad Práctica | 80 | Comestible/aromática = bonus |
| Valor Ornamental | 60 | Apariencia atractiva |

### Ejemplos de Cálculo

#### Sansevieria para Usuario Principiante con Mascotas
```
Luz escasa: 3 × 100 = 300
Humedad baja: 2 × 100 = 200  
Dificultad baja: 2 × 100 = 200
No tóxica: 3 × 100 = 300
Ornamental: 1 × 60 = 60

Total: 1060 / 11 = 96.4% confianza
```

## 7. Motor de Inferencia

### Algoritmo de Encadenamiento Hacia Adelante

```python
def inferir_recomendaciones(condiciones_usuario):
    1. plantas_candidatas = TODAS_LAS_PLANTAS
    2. aplicar_reglas_filtrado(condiciones_usuario, plantas_candidatas)
    3. evaluar_arbol_decision(condiciones_usuario, plantas_candidatas)
    4. calcular_confianza_para_cada_planta(plantas_candidatas)
    5. ordenar_por_confianza_descendente(plantas_candidatas)
    6. seleccionar_top_3(plantas_candidatas)
    7. generar_explicaciones_contextuales(plantas_seleccionadas)
    8. return recomendaciones_con_explicaciones
```

### Manejo de Incertidumbre
- **Información Incompleta**: Usar valores por defecto basados en patrones comunes
- **Conflictos entre Reglas**: Priorizar reglas de seguridad sobre conveniencia
- **Múltiples Recomendaciones**: Mostrar top 3 con diferentes niveles de confianza

## 8. Generación de Explicaciones

### Plantilla de Explicación
```
"Recomiendo [PLANTA] para tu situación porque:

✓ COMPATIBILIDAD: [razón específica basada en condiciones]
✓ ADAPTACIÓN FUEGUINA: [ventaja para condiciones locales]
✓ NIVEL USUARIO: [apropiada para tu experiencia]
⚠️ CONSIDERACIÓN: [cuidado especial si aplica]

Confianza: [X]% basada en [criterios evaluados]"
```

### Ejemplo de Explicación Generada
```
"Recomiendo Sansevieria para tu situación porque:

✓ COMPATIBILIDAD: Prospera en condiciones de poca luz y tolera ambientes secos
✓ ADAPTACIÓN FUEGUINA: Perfecta para hogares con calefacción constante durante el invierno
✓ NIVEL USUARIO: Ideal para principiantes, perdona errores de riego
⚠️ CONSIDERACIÓN: Regar solo cuando la tierra esté completamente seca

Confianza: 96% basada en luz escasa, humedad baja, seguridad mascotas y facilidad cuidado"
```

## 9. Validación y Mantenimiento

### Métricas de Evaluación
- **Precisión**: 85%+ de recomendaciones exitosas implementadas
- **Cobertura**: 95%+ de consultas reciben recomendación válida
- **Consistencia**: 0% de recomendaciones contradictorias
- **Satisfacción Usuario**: Objetivo >80% en encuestas de seguimiento

### Proceso de Actualización
1. **Feedback de Usuarios**: Recolección continua de resultados
2. **Consulta Expertos**: Revisión trimestral con especialistas locales
3. **Ajuste de Reglas**: Modificación basada en evidencia empírica
4. **Nuevas Especies**: Incorporación gradual de plantas adicionales

## 10. Limitaciones y Alcance

### Limitaciones Actuales
- **Especies Limitadas**: 12 plantas, enfocado en más comunes
- **Variables Simplificadas**: Condiciones discretas vs. continuas
- **Contexto Geográfico**: Específico para Tierra del Fuego
- **Estacionalidad**: Consideraciones básicas, no modelo climático completo

### Alcance Futuro
- **Expansión Catálogo**: 30+ especies nativas e introducidas
- **Variables Continuas**: Mediciones precisas de luz, humedad, temperatura
- **Integración Sensores**: Conexión con dispositivos de monitoreo ambiental
- **Machine Learning**: Aprendizaje basado en resultados de usuarios

---

**Última Actualización**: Junio 2025  
**Versión**: 2.0 - Representación del Conocimiento  
**Estado**: Documentación completada, lista para implementación
```

