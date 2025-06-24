"""
Aplicación Web Flask para el Sistema Experto de Plantas Fueguinas
"""

from flask import Flask, render_template, request, jsonify, session
from expert_system import PlantExpertSystem
import os
from datetime import datetime

# Configuración de la aplicación
app = Flask(__name__)
app.secret_key = 'plantas_fueguinas_2025'  # En producción usar variable de entorno

# Instancia global del sistema experto
expert_system = PlantExpertSystem()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/consulta')
def consulta():
    """Página del formulario de consulta"""
    return render_template('consulta.html')

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    """
    API endpoint para obtener recomendaciones
    """
    try:
        # Obtener datos del formulario
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No se recibieron datos'
            }), 400
        
        # Validar condiciones
        validation = expert_system.validate_conditions(data)
        if not validation['valid']:
            return jsonify({
                'success': False,
                'error': 'Datos inválidos',
                'details': validation['errors']
            }), 400
        
        # Obtener recomendaciones
        result = expert_system.get_plant_recommendation(data)
        
        # Agregar timestamp
        result['timestamp'] = datetime.now().isoformat()
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error interno: {str(e)}'
        }), 500

@app.route('/api/plant/<plant_id>')
def api_plant_info(plant_id):
    """
    API endpoint para obtener información de una planta específica
    """
    try:
        plant_info = expert_system.get_plant_info(plant_id)
        
        if plant_info:
            return jsonify({
                'success': True,
                'plant': plant_info
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Planta no encontrada'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/plants')
def api_plants_list():
    """
    API endpoint para obtener lista de todas las plantas
    """
    try:
        plants = expert_system.get_available_plants()
        return jsonify({
            'success': True,
            'plants': plants,
            'total': len(plants)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/resultados')
def resultados():
    """Página para mostrar resultados"""
    return render_template('resultados.html')

@app.route('/info')
def info():
    """Página de información del proyecto"""
    return render_template('info.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    """
    Página de demostración con ejemplos predefinidos
    """
    if request.method == 'POST':
        # Procesar formulario de demo
        demo_case = request.form.get('demo_case', 'principiante')
        
        # Casos de demostración predefinidos
        demo_cases = {
            'principiante': {
                'ubicacion': 'interior',
                'luz_disponible': 'escasa',
                'humedad_interior': 'baja',
                'experiencia_usuario': 'principiante',
                'tiempo_disponible': 'bajo',
                'mascotas_presentes': False,
                'espacio_disponible': 'pequeño'
            },
            'intermedio': {
                'ubicacion': 'interior',
                'luz_disponible': 'moderada',
                'humedad_interior': 'media',
                'experiencia_usuario': 'intermedio',
                'tiempo_disponible': 'medio',
                'mascotas_presentes': True,
                'espacio_disponible': 'mediano'
            },
            'avanzado': {
                'ubicacion': 'ambos',
                'luz_disponible': 'abundante',
                'humedad_interior': 'alta',
                'experiencia_usuario': 'avanzado',
                'tiempo_disponible': 'alto',
                'mascotas_presentes': False,
                'espacio_disponible': 'grande'
            },
            'exterior': {
                'ubicacion': 'exterior_protegido',
                'luz_disponible': 'abundante',
                'humedad_interior': 'baja',
                'experiencia_usuario': 'intermedio',
                'tiempo_disponible': 'medio',
                'mascotas_presentes': False,
                'espacio_disponible': 'grande'
            }
        }
        
        conditions = demo_cases.get(demo_case, demo_cases['principiante'])
        result = expert_system.get_plant_recommendation(conditions)
        
        return render_template('demo.html', 
                             demo_result=result, 
                             demo_conditions=conditions,
                             demo_case=demo_case)
    
    return render_template('demo.html')

@app.route('/health')
def health_check():
    """
    Health check endpoint para verificar que la aplicación está funcionando
    """
    try:
        # Verificar que el sistema experto funciona
        test_conditions = {
            'ubicacion': 'interior',
            'luz_disponible': 'escasa',
            'experiencia_usuario': 'principiante'
        }
        
        test_result = expert_system.get_plant_recommendation(test_conditions)
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'system_working': test_result['success'],
            'total_plants': len(expert_system.plantas)
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

# Manejador de errores
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', 
                         error_code=404, 
                         error_message="Página no encontrada"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', 
                         error_code=500, 
                         error_message="Error interno del servidor"), 500

# Filtros personalizados para templates
@app.template_filter('capitalize_first')
def capitalize_first(text):
    """Capitaliza solo la primera letra"""
    if not text:
        return text
    return text[0].upper() + text[1:] if len(text) > 1 else text.upper()

@app.template_filter('format_confidence')
def format_confidence(confidence):
    """Formatea el nivel de confianza"""
    return f"{confidence:.0f}%"

# Funciones auxiliares para templates
@app.context_processor
def utility_processor():
    return dict(
        app_name="PlantAdvisor Tierra del Fuego",
        app_version="1.0",
        current_year=datetime.now().year
    )

if __name__ == '__main__':
    # Configuración para desarrollo
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    print(f"🌿 Iniciando PlantAdvisor Tierra del Fuego")
    print(f"📱 Acceso: http://localhost:{port}")
    print(f"🔧 Modo debug: {debug_mode}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode
    )