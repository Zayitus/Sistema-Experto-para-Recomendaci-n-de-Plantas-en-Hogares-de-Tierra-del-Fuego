# PlantAdvisor TDF - Sistema Experto para Plantas en Tierra del Fuego

🌿 **Sistema Experto que recomienda plantas adaptadas a las condiciones específicas de Tierra del Fuego**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![Estado](https://img.shields.io/badge/Estado-Finalizado-success.svg)](https://github.com/Zayitus/Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego)

## 📋 Descripción del Proyecto

PlantAdvisor TDF es un sistema experto desarrollado para ayudar a los residentes de Tierra del Fuego a seleccionar plantas adecuadas para sus hogares, considerando las condiciones climáticas extremas y características específicas de la región patagónica austral.

### Problema Abordado

Los habitantes de Tierra del Fuego enfrentan desafíos únicos para el cultivo de plantas:
- **Inviernos extremos** con temperaturas bajo cero y escasas horas de luz
- **Calefacción constante** durante 7-8 meses, creando ambientes secos
- **Vientos patagónicos** y condiciones climáticas variables
- **Aislamiento geográfico** que limita la disponibilidad de especies

### Solución Propuesta

Un sistema experto que:
- Analiza las condiciones específicas del usuario
- Aplica conocimiento de expertos locales (viveristas, técnicos INTA)
- Recomienda plantas con alta probabilidad de éxito
- Proporciona explicaciones detalladas y consejos de cuidado

## 🚀 Instalación y Configuración

### Requisitos del Sistema

- **Python 3.9 o superior**
- **Pip** (gestor de paquetes de Python)
- **Navegador web moderno** (Chrome, Firefox, Safari, Edge)

### Instalación Paso a Paso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Zayitus/Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego.git
   cd Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Acceder al sistema**
   - Abrir navegador en: `http://localhost:5000`
   - El sistema estará listo para usar

### Instalación Rápida (Una línea)

```bash
git clone https://github.com/Zayitus/Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego.git && cd Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego && pip install -r requirements.txt && python app.py
```

## 📁 Estructura del Proyecto

```
PlantAdvisor-TDF/
├── app.py                          # Aplicación web Flask principal
├── expert_system.py                # Sistema experto principal
├── requirements.txt                # Dependencias Python
├── README.md                       # Esta documentación
├── 
├── src/                           # Código fuente del sistema experto
│   ├── __init__.py               # Inicialización del módulo
│   ├── plants_data.py            # Base de conocimiento de plantas
│   ├── rules.py                  # Motor de reglas de producción
│   └── decision_tree.py          # Implementación del árbol de decisión
├── 
├── templates/                     # Plantillas HTML
│   ├── index.html               # Página principal
│   ├── consulta.html            # Formulario de consulta
│   ├── demo.html                # Página de demostración
│   ├── info.html                # Información del proyecto
│   └── error.html               # Páginas de error
├── 
├── static/                       # Archivos estáticos
│   ├── css/
│   │   └── style.css            # Estilos personalizados
│   ├── js/
│   │   └── main.js              # JavaScript principal
│   └── images/                  # Imágenes del proyecto
└── 
└── docs/                         # Documentación del proyecto
    ├── Entrega1.pdf             # Descripción y formulación
    ├── Entrega2.pdf             # Representación del conocimiento
    └── knowledge_structure.md   # Documentación técnica
```

## 🌱 Funcionalidades del Sistema

### Características Principales

- **Consulta Personalizada**: Formulario intuitivo para capturar condiciones del usuario
- **Motor de Inferencia Híbrido**: Combina reglas de producción y árbol de decisión
- **Recomendaciones Explicables**: Cada sugerencia incluye justificación detallada
- **Base de Conocimiento Especializada**: 12 especies seleccionadas para Tierra del Fuego
- **Interfaz Web Responsiva**: Funciona en computadoras, tablets y móviles

### Variables de Entrada

El sistema evalúa múltiples factores:

| Categoría | Variables |
|-----------|-----------|
| **Ubicación** | Interior, exterior protegido, ambos |
| **Condiciones Ambientales** | Luz disponible, humedad interior, temperatura |
| **Usuario** | Experiencia, tiempo disponible, espacio |
| **Restricciones** | Presencia de mascotas, objetivos específicos |

### Plantas Incluidas

**Interior - Principiantes:**
- Sansevieria (Lengua de Tigre)
- ZZ Plant (Zamioculcas)
- Pothos

**Interior - Intermedios:**
- Ficus Benjamina
- Monstera Deliciosa
- Dracaena Marginata

**Comestibles:**
- Albahaca
- Perejil

**Exterior Protegido:**
- Lavanda
- Romero
- Geranios
- Suculentas variadas

## 🔧 API del Sistema

### Endpoints Disponibles

| Endpoint | Método | Descripción |
|----------|---------|-------------|
| `/` | GET | Página principal |
| `/consulta` | GET | Formulario de consulta |
| `/api/recommend` | POST | Obtener recomendaciones |
| `/api/plant/<id>` | GET | Información de planta específica |
| `/api/plants` | GET | Lista de todas las plantas |
| `/health` | GET | Estado del sistema |

### Ejemplo de Uso de la API

```python
import requests

# Datos de consulta
datos_usuario = {
    "ubicacion": "interior",
    "luz_disponible": "escasa",
    "humedad_interior": "baja",
    "experiencia_usuario": "principiante",
    "mascotas_presentes": False,
    "espacio_disponible": "pequeño"
}

# Solicitar recomendaciones
response = requests.post('http://localhost:5000/api/recommend', json=datos_usuario)
resultado = response.json()

print(f"Recomendaciones: {resultado['recomendaciones']}")
```

## 📊 Arquitectura del Sistema Experto

### Motor de Inferencia

El sistema utiliza una arquitectura híbrida:

1. **Reglas de Producción** (IF-THEN-BECAUSE)
   - Filtros por condiciones ambientales
   - Restricciones de seguridad (mascotas)
   - Adaptaciones estacionales

2. **Árbol de Decisión**
   - Navegación jerárquica por condiciones
   - Cálculo de niveles de confianza
   - Selección de mejores candidatos

3. **Sistema de Explicaciones**
   - Justificación de cada recomendación
   - Consejos específicos para Tierra del Fuego
   - Advertencias y cuidados especiales

### Cálculo de Confianza

```
Confianza = (Σ(Peso_i × Puntuación_i)) / Σ(Peso_i) × 100

Pesos:
- Criterios críticos (luz, toxicidad): 3
- Criterios importantes (humedad, dificultad): 2
- Criterios deseables (estética, utilidad): 1
```

## 🎥 Video Demostrativo

**[Ver Video Explicativo - 7 minutos](LINK_AL_VIDEO)**

El video incluye:
- Presentación del problema y contexto
- Demostración del sistema funcionando
- Explicación de recomendaciones generadas
- Arquitectura técnica del sistema experto

## 🧪 Pruebas y Validación

### Casos de Prueba Incluidos

El sistema incluye casos de demostración predefinidos:

1. **Usuario Principiante**: Poca experiencia, condiciones básicas
2. **Usuario Intermedio**: Algunas restricciones, mascotas presentes  
3. **Usuario Avanzado**: Múltiples ubicaciones, sin restricciones
4. **Exterior Protegido**: Enfoque en plantas resistentes

### Ejecutar Pruebas

```bash
# Verificar que el sistema funciona
curl http://localhost:5000/health

# Probar API de recomendaciones
curl -X POST http://localhost:5000/api/recommend \
     -H "Content-Type: application/json" \
     -d '{"ubicacion":"interior","luz_disponible":"escasa","experiencia_usuario":"principiante"}'
```

## 📈 Métricas del Sistema

- **Plantas en Base de Conocimiento**: 12 especies especializadas
- **Reglas de Producción**: 10+ reglas principales
- **Variables de Entrada**: 8 factores principales
- **Precisión Estimada**: >85% en condiciones validadas
- **Tiempo de Respuesta**: <1 segundo promedio

## 🔄 Desarrollo y Contribuciones

### Estructura de Desarrollo

Este proyecto fue desarrollado siguiendo metodología incremental:

1. **Fase 1**: Análisis del problema y definición de objetivos
2. **Fase 2**: Representación y organización del conocimiento
3. **Fase 3**: Implementación y interfaz web (actual)

### Tecnologías Utilizadas

- **Backend**: Python 3.9+, Flask 2.3+
- **Frontend**: HTML5, CSS3, JavaScript ES6, Bootstrap 5
- **Arquitectura**: Sistemas Expertos (reglas + árbol de decisión)
- **Deployment**: Compatible con Heroku, PythonAnywhere, servidores locales

## 🐛 Solución de Problemas

### Problemas Comunes

**Error: "No module named 'flask'"**
```bash
pip install flask
```

**Error: "Puerto 5000 en uso"**
```bash
# Cambiar puerto en app.py línea final:
app.run(host='0.0.0.0', port=5001, debug=True)
```

**La página no carga**
- Verificar que Python esté en PATH
- Revisar firewall local
- Intentar acceder a `127.0.0.1:5000` en lugar de `localhost:5000`

### Logs y Debugging

El sistema incluye logging detallado:
```bash
# Ejecutar en modo debug
export DEBUG=True
python app.py
```

## 📞 Soporte y Contacto

- **Repositorio**: [GitHub](https://github.com/Zayitus/Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego)
- **Issues**: Reportar problemas en GitHub Issues
- **Documentación**: Ver carpeta `/docs/` para detalles técnicos

## 📄 Licencia y Créditos

**Proyecto Académico** - Universidad Nacional de Tierra del Fuego  
**Materia**: Desarrollo de Sistemas de IA  
**Año**: 2025

### Reconocimientos

- **Expertos Consultados**: Viveristas y técnicos locales de Tierra del Fuego
- **Base Científica**: INTA, CADIC, literatura especializada en botánica austral
- **Contexto Regional**: Condiciones específicas de Río Grande y región

---

## 🚀 ¡Comenzar Ahora!

```bash
# Clonar y ejecutar en 3 comandos
git clone https://github.com/Zayitus/Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego.git
cd Sistema-Experto-para-Recomendaci-n-de-Plantas-en-Hogares-de-Tierra-del-Fuego
pip install -r requirements.txt && python app.py
```

**🌿 ¡Tu planta ideal para Tierra del Fuego te está esperando!**