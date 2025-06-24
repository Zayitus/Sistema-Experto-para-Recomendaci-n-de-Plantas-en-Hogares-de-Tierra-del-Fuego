"""
Motor de reglas de producción para el Sistema Experto
Implementa reglas IF-THEN-BECAUSE específicas para condiciones fueguinas
Incluye soporte para especies nativas de Tierra del Fuego
CON REGLAS ESTRICTAS PARA OBJETIVOS ESPECÍFICOS
"""

class RuleEngine:
    """
    Motor de reglas que aplica conocimiento experto para filtrar plantas
    """
    
    def __init__(self):
        self.rules = [
            self.regla_compatibilidad_ubicacion,  # *** PRIMERA REGLA - MÁS IMPORTANTE ***
            self.regla_objetivo_comestible,       # *** SEGUNDA REGLA - FILTRO ESTRICTO ***
            self.regla_mascotas_seguras,
            self.regla_luz_escasa,
            self.regla_humedad_baja,
            self.regla_temperatura_variable,
            self.regla_principiante,
            self.regla_adaptacion_invierno,
            self.regla_espacio_pequeño,
            self.regla_tiempo_limitado,
            self.regla_purificacion_aire,
            self.regla_especies_nativas,
            self.regla_objetivo_decorativo,
            self.regla_facilidad_cuidado
        ]
    
    def apply_rules(self, conditions, plantas_db):
        """
        Aplica todas las reglas con lógica ESTRICTA para objetivos específicos
        
        Args:
            conditions (dict): Condiciones del usuario
            plantas_db (dict): Base de datos de plantas
            
        Returns:
            dict: Plantas con puntuaciones calculadas
        """
        plant_scores = {}
        
        # Inicializar puntuaciones
        for plant_id in plantas_db:
            plant_scores[plant_id] = 0
        
        print(f"🔍 APLICANDO REGLAS para ubicación: {conditions.get('ubicacion')} + objetivo: {conditions.get('objetivo_principal')}")
        
        # Aplicar cada regla
        for rule in self.rules:
            rule_result = rule(conditions, plantas_db)
            rule_name = rule.__name__
            
            # Sumar puntuaciones de la regla
            for plant_id, score in rule_result.items():
                if plant_id in plant_scores:
                    old_score = plant_scores[plant_id]
                    plant_scores[plant_id] += score
                    
                    # Debug para reglas críticas
                    if rule_name in ['regla_compatibilidad_ubicacion', 'regla_objetivo_comestible', 'regla_mascotas_seguras'] and score == 0:
                        print(f"   ❌ {plant_id}: ELIMINADA por {rule_name}")
                    elif score > 0 and plant_id == 'pothos':  # Debug específico para Pothos
                        print(f"   {plant_id}: {old_score} + {score} = {plant_scores[plant_id]} ({rule_name})")
        
        # Normalizar puntuaciones a porcentajes
        max_possible_score = len(self.rules) * 100
        for plant_id in plant_scores:
            plant_scores[plant_id] = min(100, (plant_scores[plant_id] / max_possible_score) * 100)
        
        # Filtrar plantas con puntuación > 5 (muy restrictivo para objetivos específicos)
        filtered_scores = {k: v for k, v in plant_scores.items() if v > 5}
        
        print(f"🔍 RESULTADO REGLAS: {len(filtered_scores)} plantas aprobadas de {len(plant_scores)} evaluadas")
        for plant_id, score in filtered_scores.items():
            categoria = plantas_db[plant_id].get('categoria', 'N/A')
            print(f"   ✅ {plant_id} ({categoria}): {score:.1f}%")
        
        return filtered_scores
    
    def regla_compatibilidad_ubicacion(self, conditions, plantas_db):
        """
        Regla R1: FILTRO CRÍTICO de compatibilidad por ubicación (PRIMERA REGLA)
        SI ubicacion = "interior" ENTONCES eliminar plantas de exterior_protegido
        SI ubicacion = "exterior_protegido" ENTONCES eliminar plantas solo de interior
        PORQUE las plantas deben ser apropiadas para la ubicación elegida
        """
        scores = {}
        ubicacion_usuario = conditions.get('ubicacion', 'interior')
        
        for plant_id, plant_data in plantas_db.items():
            categoria_planta = plant_data.get('categoria', 'interior')
            
            # Compatibilidad de ubicaciones
            compatible = False
            
            if ubicacion_usuario == 'interior':
                # Usuario quiere solo interior
                compatible = categoria_planta in ['interior', 'comestible', 'ambos']
                
            elif ubicacion_usuario == 'exterior_protegido':
                # Usuario quiere solo exterior
                compatible = categoria_planta in ['exterior_protegido', 'comestible', 'ambos']
                
            elif ubicacion_usuario == 'ambos':
                # Usuario acepta cualquier ubicación
                compatible = True
            
            # Asignar puntuaciones
            if compatible:
                scores[plant_id] = 100  # Compatible
            else:
                scores[plant_id] = 0    # NO compatible - eliminar completamente
                
        return scores
    
    def regla_objetivo_comestible(self, conditions, plantas_db):
        """
        Regla R2: Plantas comestibles - VERSIÓN ESTRICTA
        SI objetivo_principal = "comestible"
        ENTONCES SOLO recomendar plantas comestibles (eliminar ornamentales)
        """
        scores = {}
        
        if conditions.get('objetivo_principal') == 'comestible':
            print(f"🌿 REGLA COMESTIBLE APLICADA (modo estricto)")
            
            for plant_id, plant_data in plantas_db.items():
                categoria = plant_data.get('categoria')
                
                if categoria == 'comestible':
                    scores[plant_id] = 100  # SOLO plantas comestibles
                    
                elif plant_id == 'calafate':
                    scores[plant_id] = 95  # Calafate (nativa con frutos comestibles)
                    
                else:
                    scores[plant_id] = 0   # *** CRÍTICO: Eliminar plantas NO comestibles ***
                    if plant_id == 'pothos':
                        print(f"   ❌ POTHOS: categoría '{categoria}' (NO comestible), ELIMINADA")
        
        return scores
    
    def regla_mascotas_seguras(self, conditions, plantas_db):
        """
        Regla R3: Seguridad con mascotas
        SI mascotas_presentes = True
        ENTONCES excluir plantas tóxicas
        """
        scores = {}
        
        if conditions.get('mascotas_presentes', False):
            for plant_id, plant_data in plantas_db.items():
                if not plant_data.get('toxica_mascotas', False):
                    scores[plant_id] = 100  # Bonus por seguridad
                else:
                    scores[plant_id] = 0   # Eliminación por toxicidad
        
        return scores
    
    def regla_luz_escasa(self, conditions, plantas_db):
        """
        Regla R4: Plantas para luz escasa
        SI luz_disponible = "escasa" Y ubicacion = "interior"
        ENTONCES recomendar plantas tolerantes a poca luz
        """
        scores = {}
        
        if conditions.get('luz_disponible') == 'escasa' and conditions.get('ubicacion') in ['interior', 'ambos']:
            plantas_aptas = ['sansevieria', 'zz_plant', 'pothos', 'espatifilo']
            
            for plant_id, plant_data in plantas_db.items():
                if plant_id in plantas_aptas or plant_data.get('luz_minima') == 'escasa':
                    scores[plant_id] = 95
                elif plant_data.get('luz_minima') == 'moderada':
                    scores[plant_id] = 60
                else:
                    scores[plant_id] = 20
        
        return scores
    
    def regla_humedad_baja(self, conditions, plantas_db):
        """
        Regla R5: Plantas para ambientes secos
        SI humedad_interior = "baja" Y calefaccion_constante implícita
        ENTONCES priorizar plantas resistentes a sequedad
        """
        scores = {}
        
        if conditions.get('humedad_interior') == 'baja':
            for plant_id, plant_data in plantas_db.items():
                tolerancia = plant_data.get('tolerancia_sequedad', 'media')
                resistencia_calef = plant_data.get('resistencia_calefaccion', 'media')
                
                if tolerancia in ['alta', 'muy_alta', 'extrema'] and resistencia_calef in ['buena', 'excelente']:
                    scores[plant_id] = 90
                elif plant_data.get('humedad_requerida') == 'baja':
                    scores[plant_id] = 85
                elif plant_data.get('humedad_requerida') == 'media':
                    scores[plant_id] = 60
                else:
                    scores[plant_id] = 25
        
        return scores
    
    def regla_temperatura_variable(self, conditions, plantas_db):
        """
        Regla R6: Exclusión por cambios térmicos
        SI ubicacion cerca de ventanas O temperatura variable
        ENTONCES evitar plantas sensibles
        """
        scores = {}
        
        # Asumir temperatura variable si hay luz abundante (cerca de ventanas)
        temp_variable = (conditions.get('luz_disponible') == 'abundante' and 
                        conditions.get('ubicacion') == 'interior')
        
        if temp_variable:
            plantas_sensibles = ['ficus', 'monstera']
            
            for plant_id, plant_data in plantas_db.items():
                if plant_id in plantas_sensibles:
                    scores[plant_id] = 30  # Penalizar pero no eliminar
                else:
                    scores[plant_id] = 80
        
        return scores
    
    def regla_principiante(self, conditions, plantas_db):
        """
        Regla R7: Recomendaciones para principiantes
        SI experiencia_usuario = "principiante"
        ENTONCES priorizar plantas de bajo mantenimiento
        """
        scores = {}
        
        if conditions.get('experiencia_usuario') == 'principiante':
            for plant_id, plant_data in plantas_db.items():
                if plant_data.get('dificultad') == 'principiante':
                    scores[plant_id] = 95
                elif plant_data.get('dificultad') == 'intermedio':
                    scores[plant_id] = 50
                else:
                    scores[plant_id] = 20
        
        return scores
    
    def regla_adaptacion_invierno(self, conditions, plantas_db):
        """
        Regla R8: Adaptación al invierno fueguino
        Prioriza plantas que manejan bien condiciones invernales
        """
        scores = {}
        
        # Esta regla siempre aplica en Tierra del Fuego
        for plant_id, plant_data in plantas_db.items():
            resistencia_calef = plant_data.get('resistencia_calefaccion', 'media')
            tolerancia_seq = plant_data.get('tolerancia_sequedad', 'media')
            
            if resistencia_calef == 'excelente':
                scores[plant_id] = 90
            elif resistencia_calef == 'buena':
                scores[plant_id] = 75
            elif resistencia_calef == 'media':
                scores[plant_id] = 60
            else:
                scores[plant_id] = 30
            
            # Bonus por tolerancia a sequedad
            if tolerancia_seq in ['alta', 'muy_alta', 'extrema']:
                scores[plant_id] += 10
            
            # Bonus especial para plantas nativas (siempre adaptadas)
            if plant_data.get('planta_nativa', False):
                scores[plant_id] += 15
        
        return scores
    
    def regla_espacio_pequeño(self, conditions, plantas_db):
        """
        Regla R9: Plantas para espacios pequeños
        SI espacio_disponible = "pequeño"
        ENTONCES evitar plantas grandes
        """
        scores = {}
        
        if conditions.get('espacio_disponible') == 'pequeño':
            for plant_id, plant_data in plantas_db.items():
                tamaño = plant_data.get('tamaño_maximo', 'mediano')
                
                if tamaño == 'pequeño':
                    scores[plant_id] = 95
                elif tamaño == 'mediano':
                    scores[plant_id] = 75
                elif tamaño == 'grande':
                    scores[plant_id] = 40
                else:  # muy_grande
                    scores[plant_id] = 15
        
        return scores
    
    def regla_tiempo_limitado(self, conditions, plantas_db):
        """
        Regla R10: Plantas para poco tiempo de cuidado
        SI tiempo_disponible = "bajo"
        ENTONCES priorizar plantas de bajo mantenimiento
        """
        scores = {}
        
        if conditions.get('tiempo_disponible') == 'bajo':
            plantas_bajo_mantenimiento = ['sansevieria', 'zz_plant', 'suculentas_echeveria', 'cactus_opuntia']
            
            for plant_id, plant_data in plantas_db.items():
                if plant_id in plantas_bajo_mantenimiento:
                    scores[plant_id] = 90
                elif plant_data.get('dificultad') == 'principiante':
                    scores[plant_id] = 75
                # Plantas nativas también son de bajo mantenimiento una vez establecidas
                elif plant_data.get('planta_nativa', False):
                    scores[plant_id] = 85
                else:
                    scores[plant_id] = 40
        
        return scores
    
    def regla_purificacion_aire(self, conditions, plantas_db):
        """
        Regla R11: Plantas purificadoras de aire
        SI objetivo_principal = "purificar_aire"
        ENTONCES priorizar plantas purificadoras
        """
        scores = {}
        
        if conditions.get('objetivo_principal') == 'purificar_aire':
            for plant_id, plant_data in plantas_db.items():
                if plant_data.get('purifica_aire', False):
                    scores[plant_id] = 95
                else:
                    scores[plant_id] = 40
        
        return scores
    
    def regla_especies_nativas(self, conditions, plantas_db):
        """
        Regla R12: Especies nativas de Tierra del Fuego
        SI objetivo_principal = "nativas" O ubicacion = "exterior_protegido"
        ENTONCES priorizar especies nativas
        """
        scores = {}
        
        # Priorizar nativas si se solicitan específicamente
        if conditions.get('objetivo_principal') == 'nativas':
            for plant_id, plant_data in plantas_db.items():
                if plant_data.get('planta_nativa', False):
                    scores[plant_id] = 100  # Máxima prioridad para nativas
                else:
                    scores[plant_id] = 20   # Baja prioridad para no nativas
        
        # También priorizar nativas para exterior (están naturalmente adaptadas)
        elif conditions.get('ubicacion') == 'exterior_protegido':
            for plant_id, plant_data in plantas_db.items():
                if plant_data.get('planta_nativa', False):
                    scores[plant_id] = 90   # Alta prioridad para nativas en exterior
                elif plant_data.get('categoria') == 'exterior_protegido':
                    scores[plant_id] = 75   # Prioridad media para otras de exterior
                else:
                    scores[plant_id] = 40
        
        return scores
    
    def regla_objetivo_decorativo(self, conditions, plantas_db):
        """
        Regla R13: Plantas decorativas
        SI objetivo_principal = "decorativo"
        ENTONCES priorizar plantas con alto valor ornamental
        """
        scores = {}
        
        if conditions.get('objetivo_principal') == 'decorativo':
            for plant_id, plant_data in plantas_db.items():
                valor_ornamental = plant_data.get('valor_ornamental', 'medio')
                
                if valor_ornamental in ['muy_alto', 'espectacular']:
                    scores[plant_id] = 95
                elif valor_ornamental == 'alto':
                    scores[plant_id] = 85
                else:
                    scores[plant_id] = 60
        
        return scores
    
    def regla_facilidad_cuidado(self, conditions, plantas_db):
        """
        Regla R14: Plantas de fácil cuidado
        SI objetivo_principal = "facil_cuidado"
        ENTONCES priorizar plantas resistentes y de bajo mantenimiento
        """
        scores = {}
        
        if conditions.get('objetivo_principal') == 'facil_cuidado':
            plantas_faciles = ['sansevieria', 'zz_plant', 'suculentas_echeveria', 'cactus_opuntia', 'pothos']
            
            for plant_id, plant_data in plantas_db.items():
                if plant_id in plantas_faciles:
                    scores[plant_id] = 95
                elif plant_data.get('dificultad') == 'principiante':
                    scores[plant_id] = 90
                # Plantas nativas también son fáciles una vez establecidas
                elif plant_data.get('planta_nativa', False) and plant_data.get('dificultad') != 'avanzado':
                    scores[plant_id] = 85
                else:
                    scores[plant_id] = 50
        
        return scores
    
    def get_rule_explanations(self, plant_id, conditions, plant_data):
        """
        Genera explicaciones de por qué se aplicaron ciertas reglas
        """
        explanations = []
        
        # Explicaciones por luz
        if conditions.get('luz_disponible') == 'escasa':
            if plant_data.get('luz_minima') == 'escasa':
                explanations.append("✓ Perfecta para condiciones de poca luz")
        
        # Explicaciones por humedad
        if conditions.get('humedad_interior') == 'baja':
            if plant_data.get('tolerancia_sequedad') in ['alta', 'muy_alta', 'extrema']:
                explanations.append("✓ Excelente tolerancia al aire seco de la calefacción")
        
        # Explicaciones por experiencia
        if conditions.get('experiencia_usuario') == 'principiante':
            if plant_data.get('dificultad') == 'principiante':
                explanations.append("✓ Ideal para tu nivel de experiencia")
        
        # Explicaciones por mascotas
        if conditions.get('mascotas_presentes', False):
            if not plant_data.get('toxica_mascotas', False):
                explanations.append("✓ Completamente segura para mascotas")
        
        # Explicaciones por especies nativas
        if plant_data.get('planta_nativa', False):
            explanations.append("🌿 Especie nativa de Tierra del Fuego - perfectamente adaptada al clima austral")
        
        # Explicaciones por objetivo
        objetivo = conditions.get('objetivo_principal')
        if objetivo == 'nativas' and plant_data.get('planta_nativa', False):
            explanations.append("✓ Especie nativa solicitada - patrimonio natural fueguino")
        elif objetivo == 'comestible' and plant_data.get('categoria') == 'comestible':
            explanations.append("✓ Planta comestible que proporciona hierbas frescas")
        elif objetivo == 'purificar_aire' and plant_data.get('purifica_aire', False):
            explanations.append("✓ Excelente purificadora de aire para espacios cerrados")
        
        # Explicación por ubicación
        ubicacion_usuario = conditions.get('ubicacion')
        categoria_planta = plant_data.get('categoria')
        if ubicacion_usuario == 'interior' and categoria_planta == 'interior':
            explanations.append("✓ Perfecta para cultivo en interior")
        elif ubicacion_usuario == 'exterior_protegido' and categoria_planta == 'exterior_protegido':
            explanations.append("✓ Ideal para jardines exteriores protegidos")
        elif categoria_planta == 'ambos':
            explanations.append("✓ Versátil - puede cultivarse tanto en interior como exterior")
        
        return explanations