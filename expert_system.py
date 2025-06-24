"""
Sistema Experto para Recomendación de Plantas en Tierra del Fuego
Clase principal que integra todas las funcionalidades
CON VALIDACIÓN ESTRICTA DE UBICACIÓN Y OBJETIVO
"""

import sys
import os
from plants_data import PLANTAS
from rules import RuleEngine
from decision_tree import DecisionTree
import random

class PlantExpertSystem:
    """
    Sistema Experto principal para recomendación de plantas fueguinas
    CON FILTROS CRÍTICOS DE UBICACIÓN Y OBJETIVO ESPECÍFICO
    """
    
    def __init__(self):
        self.plantas = PLANTAS
        self.rule_engine = RuleEngine()
        self.decision_tree = DecisionTree()
        self.session_history = []
    
    def get_plant_recommendation(self, user_conditions):
        """
        Función principal que genera recomendaciones basadas en condiciones del usuario
        CON VALIDACIÓN ESTRICTA DE UBICACIÓN Y OBJETIVO EN CADA PASO
        
        Args:
            user_conditions (dict): Condiciones proporcionadas por el usuario
            
        Returns:
            dict: Recomendaciones con explicaciones y nivel de confianza
        """
        try:
            ubicacion_solicitada = user_conditions.get('ubicacion', 'interior')
            objetivo_solicitado = user_conditions.get('objetivo_principal', 'ninguno')
            print(f"🔍 SISTEMA EXPERTO INICIADO:")
            print(f"   📍 Ubicación: '{ubicacion_solicitada}'")
            print(f"   🎯 Objetivo: '{objetivo_solicitado}'")
            
            # 1. Aplicar reglas de filtrado (incluye filtros críticos de ubicación y objetivo)
            print(f"\n📋 PASO 1: Aplicando reglas de producción...")
            filtered_plants = self.rule_engine.apply_rules(user_conditions, self.plantas)
            print(f"📋 RESULTADO REGLAS: {len(filtered_plants)} plantas aprobadas")
            
            # 2. Evaluar con árbol de decisión (incluye filtros de ubicación y objetivo)
            print(f"\n🌳 PASO 2: Evaluando con árbol de decisión...")
            tree_recommendations = self.decision_tree.evaluate_conditions(user_conditions)
            print(f"🌳 RESULTADO ÁRBOL: {len(tree_recommendations)} plantas recomendadas")
            
            # 3. Combinar resultados CON VALIDACIÓN FINAL DE UBICACIÓN Y OBJETIVO
            print(f"\n🔗 PASO 3: Combinando resultados...")
            final_recommendations = self._combine_recommendations_with_strict_validation(
                filtered_plants, tree_recommendations, user_conditions
            )
            
            # 4. Generar explicaciones detalladas
            print(f"\n📝 PASO 4: Generando explicaciones...")
            for rec in final_recommendations:
                rec['explicacion_detallada'] = self._generate_detailed_explanation(
                    rec, user_conditions
                )
            
            # 5. Guardar en historial
            self.session_history.append({
                'condiciones': user_conditions,
                'recomendaciones': final_recommendations
            })
            
            print(f"\n✅ PROCESO COMPLETADO: {len(final_recommendations)} recomendaciones finales")
            for rec in final_recommendations:
                categoria = rec['datos_planta'].get('categoria', 'N/A')
                print(f"   ✅ {rec['nombre']} ({categoria}): {rec['confianza']:.1f}% confianza")
            
            return {
                'success': True,
                'recomendaciones': final_recommendations,
                'total_plantas_evaluadas': len(self.plantas),
                'metodo_inferencia': 'reglas + arbol_decision + filtro_ubicacion_objetivo'
            }
            
        except Exception as e:
            print(f"❌ ERROR EN SISTEMA EXPERTO: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'recomendaciones': []
            }
    
    def _combine_recommendations_with_strict_validation(self, rule_results, tree_results, conditions):
        """
        Combina resultados de reglas y árbol de decisión CON VALIDACIÓN FINAL ESTRICTA
        """
        combined = {}
        ubicacion_usuario = conditions.get('ubicacion', 'interior')
        objetivo_usuario = conditions.get('objetivo_principal')
        
        print(f"🔗 COMBINANDO con validación estricta:")
        print(f"   📍 Ubicación: '{ubicacion_usuario}'")
        print(f"   🎯 Objetivo: '{objetivo_usuario}'")
        print(f"   📋 Reglas: {len(rule_results)} plantas")
        print(f"   🌳 Árbol: {len(tree_results)} plantas")
        
        # Agregar resultados de reglas (YA están filtradas por las reglas críticas)
        for plant_id, confidence in rule_results.items():
            if plant_id in self.plantas and confidence > 0:
                
                # VALIDACIÓN FINAL ESTRICTA
                if not self._is_strictly_compatible(plant_id, conditions):
                    print(f"   ❌ REGLAS - {plant_id}: ELIMINADA en validación final estricta")
                    continue
                
                combined[plant_id] = {
                    'planta_id': plant_id,
                    'nombre': self.plantas[plant_id]['nombre_comun'],
                    'confianza': confidence,
                    'fuente': 'reglas',
                    'datos_planta': self.plantas[plant_id]
                }
                categoria = self.plantas[plant_id].get('categoria', 'N/A')
                print(f"   ✅ REGLAS - {plant_id} ({categoria}): {confidence:.1f}% confianza")
        
        # Agregar/actualizar con resultados del árbol (CON VALIDACIÓN FINAL)
        for result in tree_results:
            plant_id = result['planta']
            
            # VALIDACIÓN FINAL ESTRICTA
            if not self._is_strictly_compatible(plant_id, conditions):
                print(f"   ❌ ÁRBOL - {plant_id}: ELIMINADA en validación final estricta")
                continue
            
            if plant_id in combined:
                # Promedio ponderado de confianzas
                old_confidence = combined[plant_id]['confianza']
                combined[plant_id]['confianza'] = (old_confidence * 0.6 + result['confianza'] * 0.4)
                combined[plant_id]['fuente'] = 'reglas + arbol'
                categoria = self.plantas[plant_id].get('categoria', 'N/A')
                print(f"   🔄 COMBINADO - {plant_id} ({categoria}): {combined[plant_id]['confianza']:.1f}% confianza")
            else:
                if plant_id in self.plantas:
                    combined[plant_id] = {
                        'planta_id': plant_id,
                        'nombre': self.plantas[plant_id]['nombre_comun'],
                        'confianza': result['confianza'],
                        'fuente': 'arbol',
                        'datos_planta': self.plantas[plant_id]
                    }
                    categoria = self.plantas[plant_id].get('categoria', 'N/A')
                    print(f"   ✅ ÁRBOL - {plant_id} ({categoria}): {result['confianza']}% confianza")
        
        # Convertir a lista y ordenar por confianza
        recommendations = list(combined.values())
        recommendations.sort(key=lambda x: x['confianza'], reverse=True)
        
        print(f"🔗 COMBINACIÓN FINAL: {len(recommendations)} plantas válidas")
        
        # Retornar top 3
        return recommendations[:3]
    
    def _is_strictly_compatible(self, plant_id, conditions):
        """
        VALIDACIÓN FINAL ESTRICTA: Verifica compatibilidad total con ubicación Y objetivo
        """
        if plant_id not in self.plantas:
            return False
        
        plant_data = self.plantas[plant_id]
        categoria_planta = plant_data.get('categoria', 'interior')
        ubicacion_usuario = conditions.get('ubicacion', 'interior')
        objetivo_usuario = conditions.get('objetivo_principal')
        
        # VALIDACIÓN 1: Compatibilidad de ubicación
        ubicacion_compatible = False
        if ubicacion_usuario == 'interior':
            ubicacion_compatible = categoria_planta in ['interior', 'comestible', 'ambos']
        elif ubicacion_usuario == 'exterior_protegido':
            ubicacion_compatible = categoria_planta in ['exterior_protegido', 'comestible', 'ambos']
        elif ubicacion_usuario == 'ambos':
            ubicacion_compatible = True
        
        # VALIDACIÓN 2: Compatibilidad de objetivo (CRÍTICA)
        objetivo_compatible = True  # Por defecto compatible si no hay objetivo específico
        
        if objetivo_usuario == 'comestible':
            # ESTRICTO: Solo plantas comestibles o calafate
            objetivo_compatible = (categoria_planta == 'comestible' or plant_id == 'calafate')
            
        elif objetivo_usuario == 'nativas':
            # ESTRICTO: Solo plantas nativas
            objetivo_compatible = plant_data.get('planta_nativa', False)
            
        elif objetivo_usuario == 'purificar_aire':
            # ESTRICTO: Solo plantas que purifican aire
            objetivo_compatible = plant_data.get('purifica_aire', False)
            
        elif objetivo_usuario == 'decorativo':
            # Para decorativo: priorizar ornamentales, evitar comestibles
            objetivo_compatible = categoria_planta in ['interior', 'exterior_protegido', 'ambos']
            
        elif objetivo_usuario == 'facil_cuidado':
            # Para fácil cuidado: principiantes o nativas fáciles
            dificultad = plant_data.get('dificultad', 'intermedio')
            es_nativa = plant_data.get('planta_nativa', False)
            objetivo_compatible = (dificultad == 'principiante' or (es_nativa and dificultad != 'avanzado'))
        
        # VALIDACIÓN 3: Mascotas (si están presentes)
        mascotas_compatible = True
        if conditions.get('mascotas_presentes', False):
            mascotas_compatible = not plant_data.get('toxica_mascotas', False)
        
        compatible = ubicacion_compatible and objetivo_compatible and mascotas_compatible
        
        # Debug para casos específicos
        if plant_id == 'pothos' and not compatible:
            print(f"   🔍 POTHOS VALIDACIÓN FINAL:")
            print(f"      - Categoría: {categoria_planta}")
            print(f"      - Ubicación OK: {ubicacion_compatible}")
            print(f"      - Objetivo OK: {objetivo_compatible} (objetivo: {objetivo_usuario})")
            print(f"      - Mascotas OK: {mascotas_compatible}")
            print(f"      - RESULTADO: {compatible}")
        
        return compatible
    
    def _generate_detailed_explanation(self, recommendation, conditions):
        """
        Genera explicación detallada para una recomendación
        INCLUYE VALIDACIÓN DE UBICACIÓN Y OBJETIVO EN LA EXPLICACIÓN
        """
        plant_data = recommendation['datos_planta']
        explanations = []
        
        # Explicación por compatibilidad de ubicación (NUEVA)
        ubicacion_usuario = conditions.get('ubicacion')
        categoria_planta = plant_data.get('categoria')
        
        if ubicacion_usuario == 'interior' and categoria_planta == 'interior':
            explanations.append("🏠 UBICACIÓN PERFECTA: Diseñada específicamente para cultivo en interior")
        elif ubicacion_usuario == 'exterior_protegido' and categoria_planta == 'exterior_protegido':
            explanations.append("🌳 UBICACIÓN IDEAL: Perfecta para jardines exteriores protegidos del clima fueguino")
        elif categoria_planta == 'ambos':
            explanations.append("🔄 VERSÁTIL: Puede cultivarse tanto en interior como exterior según la temporada")
        elif categoria_planta == 'comestible':
            explanations.append("🌿 COMESTIBLE: Planta de hierbas que se adapta a diferentes ubicaciones")
        
        # Explicación por objetivo específico (NUEVA)
        objetivo_usuario = conditions.get('objetivo_principal')
        if objetivo_usuario == 'comestible' and categoria_planta == 'comestible':
            explanations.append("🍃 OBJETIVO CUMPLIDO: Proporciona hierbas frescas para uso culinario")
        elif objetivo_usuario == 'nativas' and plant_data.get('planta_nativa', False):
            explanations.append("🌳 PATRIMONIO NATURAL: Especie nativa que preserva la flora autóctona fueguina")
        elif objetivo_usuario == 'purificar_aire' and plant_data.get('purifica_aire', False):
            explanations.append("💨 AIRE PURO: Filtra contaminantes y mejora la calidad del aire interior")
        elif objetivo_usuario == 'decorativo':
            explanations.append("🎨 VALOR DECORATIVO: Añade belleza y vida a tu espacio")
        elif objetivo_usuario == 'facil_cuidado':
            explanations.append("🌱 FÁCIL CUIDADO: Requiere mínimo mantenimiento, ideal para principiantes")
        
        # Explicación por luz
        luz_usuario = conditions.get('luz_disponible', 'moderada')
        luz_planta = plant_data.get('luz_minima', 'moderada')
        if self._is_light_compatible(luz_usuario, luz_planta):
            explanations.append(f"☀️ COMPATIBILIDAD DE LUZ: Perfecta para condiciones de luz {luz_usuario}")
        
        # Explicación por humedad
        humedad_usuario = conditions.get('humedad_interior', 'media')
        humedad_planta = plant_data.get('humedad_requerida', 'media')
        if humedad_usuario == humedad_planta or humedad_planta == 'baja':
            explanations.append(f"💧 HUMEDAD IDEAL: Se adapta perfectamente a la humedad {humedad_usuario} típica de hogares fueguinos con calefacción")
        
        # Explicación por experiencia
        experiencia = conditions.get('experiencia_usuario', 'principiante')
        dificultad = plant_data.get('dificultad', 'intermedio')
        if (experiencia == 'principiante' and dificultad == 'principiante') or \
           (experiencia == 'intermedio' and dificultad in ['principiante', 'intermedio']):
            explanations.append(f"👤 NIVEL ADECUADO: Perfecta para tu nivel de experiencia ({experiencia})")
        
        # Explicación por mascotas
        if conditions.get('mascotas_presentes', False):
            if not plant_data.get('toxica_mascotas', False):
                explanations.append("🐾 SEGURIDAD: Completamente segura para mascotas")
        
        # Explicaciones especiales para plantas nativas
        if plant_data.get('planta_nativa', False):
            explanations.append("🌳 NATIVA TDF: Especie nativa de Tierra del Fuego, perfectamente adaptada al clima austral y parte del patrimonio natural")
        
        # Ventajas específicas para Tierra del Fuego
        ventajas_fueguinas = {
            'sansevieria': "❄️ VENTAJA FUEGUINA: Extremadamente resistente a la calefacción constante del invierno fueguino",
            'zz_plant': "🔥 VENTAJA FUEGUINA: Tolera perfectamente el aire seco de los sistemas de calefacción locales",
            'pothos': "🏠 VENTAJA FUEGUINA: Purifica el aire en espacios cerrados durante los largos inviernos",
            'albahaca': "🌿 VALOR CULINARIO: Hierbas frescas durante inviernos cuando productos frescos son costosos en TDF",
            'perejil': "🌿 VITAMINAS FRESCAS: Proporciona nutrientes frescos durante todo el año fueguino",
            'oregano': "🌿 CONDIMENTO LOCAL: Resistente al aire seco y proporciona sabor fresco todo el año",
            'ciboulette': "🌿 RESISTENCIA AL FRÍO: Una de las pocas hierbas que tolera el clima fueguino",
            'lavanda': "🌬️ VENTAJA FUEGUINA: Una vez establecida, resiste los vientos patagónicos y heladas ocasionales",
            'romero': "❄️ VENTAJA FUEGUINA: Resistente al clima fueguino y proporciona hierbas frescas todo el año",
            'lenga': "🍂 SÍMBOLO FUEGUINO: Árbol emblemático con espectacular coloración otoñal dorada, patrimonio de la región",
            'nire': "🌳 ADAPTACIÓN PERFECTA: Nativo que resiste perfectamente los vientos patagónicos",
            'calafate': "🫐 TRADICIÓN FUEGUINA: Frutos comestibles azules, parte del folklore patagónico ('quien come calafate, vuelve')",
            'mata_negra': "💪 RESISTENCIA EXTREMA: Prácticamente no requiere cuidados, adaptada a condiciones adversas",
            'coiron': "🌾 PAISAJE AUTÉNTICO: Pasto nativo que forma parte del paisaje estepario fueguino"
        }
        
        plant_id = recommendation['planta_id']
        if plant_id in ventajas_fueguinas:
            explanations.append(ventajas_fueguinas[plant_id])
        
        # Cuidados especiales
        cuidados_especiales = {
            'ficus': "⚠️ CUIDADO: Mantener alejada de corrientes de aire frío cerca de ventanas",
            'monstera': "⚠️ ESPACIO: Necesita ubicación con espacio amplio para crecer",
            'lenga': "⚠️ PACIENCIA: Requiere años para establecerse, pero vale la pena la espera",
            'pothos': "⚠️ MASCOTAS: Mantener alejada de mascotas por toxicidad"
        }
        
        if plant_id in cuidados_especiales:
            explanations.append(cuidados_especiales[plant_id])
        elif plant_data.get('categoria') == 'comestible':
            explanations.append("💡 CONSEJO: Ubicar en ventana sur para maximizar horas de luz")
        
        return "\n".join(explanations)
    
    def _is_light_compatible(self, user_light, plant_light):
        """
        Evalúa compatibilidad de requerimientos de luz
        """
        light_levels = {'escasa': 1, 'moderada': 2, 'abundante': 3}
        return light_levels.get(user_light, 2) >= light_levels.get(plant_light, 2)
    
    def get_plant_info(self, plant_id):
        """
        Obtiene información detallada de una planta específica
        """
        if plant_id in self.plantas:
            return self.plantas[plant_id]
        return None
    
    def get_available_plants(self):
        """
        Retorna lista de todas las plantas disponibles
        """
        return [
            {
                'id': plant_id,
                'nombre': data['nombre_comun'],
                'categoria': data['categoria'],
                'dificultad': data['dificultad']
            }
            for plant_id, data in self.plantas.items()
        ]
    
    def get_plants_by_location_and_objective(self, location, objective=None):
        """
        Retorna plantas filtradas por ubicación y objetivo específico
        """
        compatible_plants = []
        for plant_id, data in self.plantas.items():
            categoria = data.get('categoria', 'interior')
            
            # Filtro por ubicación
            location_ok = False
            if location == 'interior' and categoria in ['interior', 'comestible', 'ambos']:
                location_ok = True
            elif location == 'exterior_protegido' and categoria in ['exterior_protegido', 'comestible', 'ambos']:
                location_ok = True
            elif location == 'ambos':
                location_ok = True
            
            # Filtro por objetivo
            objective_ok = True  # Por defecto compatible
            if objective == 'comestible':
                objective_ok = (categoria == 'comestible' or plant_id == 'calafate')
            elif objective == 'nativas':
                objective_ok = data.get('planta_nativa', False)
            elif objective == 'purificar_aire':
                objective_ok = data.get('purifica_aire', False)
            
            if location_ok and objective_ok:
                compatible_plants.append({'id': plant_id, 'data': data})
        
        return compatible_plants
    
    def get_session_history(self):
        """
        Retorna el historial de la sesión actual
        """
        return self.session_history
    
    def reset_session(self):
        """
        Reinicia el historial de la sesión
        """
        self.session_history = []
    
    def validate_conditions(self, conditions):
        """
        Valida que las condiciones del usuario sean válidas
        """
        required_fields = ['ubicacion', 'luz_disponible', 'experiencia_usuario']
        valid_values = {
            'ubicacion': ['interior', 'exterior_protegido', 'ambos'],
            'luz_disponible': ['escasa', 'moderada', 'abundante'],
            'humedad_interior': ['baja', 'media', 'alta'],
            'experiencia_usuario': ['principiante', 'intermedio', 'avanzado'],
            'tiempo_disponible': ['bajo', 'medio', 'alto'],
            'espacio_disponible': ['pequeño', 'mediano', 'grande'],
            'objetivo_principal': ['decorativo', 'purificar_aire', 'comestible', 'nativas', 'facil_cuidado']
        }
        
        errors = []
        
        # Verificar campos requeridos
        for field in required_fields:
            if field not in conditions:
                errors.append(f"Campo requerido faltante: {field}")
        
        # Verificar valores válidos
        for field, value in conditions.items():
            if field in valid_values and value not in valid_values[field]:
                errors.append(f"Valor inválido para {field}: {value}")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors
        }

# Función de conveniencia para uso directo
def get_plant_recommendations(user_conditions):
    """
    Función simple para obtener recomendaciones
    """
    system = PlantExpertSystem()
    return system.get_plant_recommendation(user_conditions)