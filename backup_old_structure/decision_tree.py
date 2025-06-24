"""
Estructura del Árbol de Decisión
Sistema Experto para Recomendación de Plantas en Tierra del Fuego
Incluye soporte para especies nativas CON FILTRO DE UBICACIÓN Y OBJETIVO
"""

class DecisionTree:
    """
    Implementa el árbol de decisión para la recomendación de plantas
    basado en la arquitectura definida en la Entrega 2
    CON VALIDACIÓN ESTRICTA DE UBICACIÓN Y OBJETIVO
    """
    
    def __init__(self):
        self.tree_structure = self._build_tree()
    
    def _build_tree(self):
        """
        Construye la estructura del árbol de decisión según la documentación
        Incluye soporte para especies nativas de Tierra del Fuego
        ORGANIZADO POR UBICACIÓN PRIMERO
        """
        return {
            'ubicacion': {
                'interior': {
                    'luz_disponible': {
                        'escasa': {
                            'plantas': ['sansevieria', 'zz_plant', 'pothos', 'espatifilo'],
                            'confianza': [95, 90, 85, 80]
                        },
                        'moderada': {
                            'plantas': ['dracaena', 'ficus', 'perejil', 'filodendro'],
                            'confianza': [80, 75, 70, 75]
                        },
                        'abundante': {
                            'plantas': ['monstera', 'albahaca', 'oregano', 'cactus_opuntia'],
                            'confianza': [85, 80, 75, 85]
                        }
                    },
                    'humedad_interior': {
                        'baja': {
                            'plantas': ['sansevieria', 'zz_plant', 'suculentas_echeveria', 'cactus_opuntia'],
                            'confianza': [95, 90, 88, 90]
                        },
                        'media': {
                            'plantas': ['pothos', 'dracaena', 'ficus', 'perejil'],
                            'confianza': [85, 80, 75, 75]
                        },
                        'alta': {
                            'plantas': ['monstera', 'ficus', 'espatifilo', 'filodendro'],
                            'confianza': [90, 85, 85, 80]
                        }
                    }
                },
                'exterior_protegido': {
                    'resistencia_heladas': {
                        'alta': {
                            'plantas': ['lenga', 'nire', 'romero', 'calafate', 'mata_negra'],
                            'confianza': [95, 90, 85, 90, 85]
                        },
                        'media': {
                            'plantas': ['lavanda', 'geranios', 'pensamiento', 'coiron'],
                            'confianza': [75, 70, 75, 85]
                        }
                    },
                    'plantas_nativas': {
                        'prioritarias': {
                            'plantas': ['lenga', 'nire', 'calafate', 'mata_negra', 'coiron'],
                            'confianza': [95, 90, 90, 85, 85]
                        }
                    }
                },
                'ambos': {
                    'facilidad_traslado': {
                        'alta': {
                            'plantas': ['geranios', 'suculentas_echeveria', 'oregano', 'manzanilla'],
                            'confianza': [80, 85, 75, 70]
                        }
                    }
                }
            },
            'objetivo_principal': {
                'nativas': {
                    'plantas': ['lenga', 'nire', 'calafate', 'mata_negra', 'coiron'],
                    'confianza': [95, 90, 90, 85, 85]
                },
                'comestible': {
                    'plantas': ['albahaca', 'perejil', 'oregano', 'ciboulette', 'calafate'],
                    'confianza': [85, 80, 85, 75, 85]
                },
                'decorativo': {
                    'plantas': ['monstera', 'ficus', 'lenga', 'lavanda', 'geranios'],
                    'confianza': [90, 85, 95, 85, 80]
                },
                'purificar_aire': {
                    'plantas': ['sansevieria', 'pothos', 'ficus', 'espatifilo', 'dracaena'],
                    'confianza': [90, 85, 85, 90, 80]
                },
                'facil_cuidado': {
                    'plantas': ['sansevieria', 'zz_plant', 'suculentas_echeveria', 'cactus_opuntia', 'mata_negra'],
                    'confianza': [95, 90, 85, 90, 85]
                }
            }
        }
    
    def evaluate_conditions(self, condiciones_usuario):
        """
        Evalúa las condiciones del usuario contra el árbol de decisión
        *** FILTRO DE UBICACIÓN Y OBJETIVO DESDE EL INICIO ***
        
        Args:
            condiciones_usuario (dict): Condiciones proporcionadas por el usuario
            
        Returns:
            list: Lista de plantas recomendadas con sus niveles de confianza FILTRADAS POR UBICACIÓN Y OBJETIVO
        """
        recomendaciones = []
        ubicacion_usuario = condiciones_usuario.get('ubicacion', 'interior')
        objetivo_usuario = condiciones_usuario.get('objetivo_principal')
        
        print(f"🔍 ÁRBOL DE DECISIÓN: Evaluando para ubicación '{ubicacion_usuario}' + objetivo '{objetivo_usuario}'")
        
        # *** VALIDACIÓN CRÍTICA POR UBICACIÓN Y OBJETIVO PRIMERO ***
        recomendaciones_sin_filtrar = []
        
        # Evaluación por objetivo principal (nueva funcionalidad)
        if objetivo_usuario and objetivo_usuario in self.tree_structure['objetivo_principal']:
            objetivo_nodo = self.tree_structure['objetivo_principal'][objetivo_usuario]
            recomendaciones_objetivo = self._format_recommendations(objetivo_nodo)
            recomendaciones_sin_filtrar.extend(recomendaciones_objetivo)
            print(f"   📋 Objetivo '{objetivo_usuario}': {len(recomendaciones_objetivo)} plantas encontradas")
        
        # Navegación por el árbol según ubicación
        if ubicacion_usuario in self.tree_structure['ubicacion']:
            nodo_actual = self.tree_structure['ubicacion'][ubicacion_usuario]
            
            # Evaluación según luz disponible (para interior)
            if ubicacion_usuario == 'interior':
                luz = condiciones_usuario.get('luz_disponible', 'moderada')
                if luz in nodo_actual['luz_disponible']:
                    plantas_luz = nodo_actual['luz_disponible'][luz]
                    recomendaciones_luz = self._format_recommendations(plantas_luz)
                    recomendaciones_sin_filtrar.extend(recomendaciones_luz)
                    print(f"   💡 Interior + Luz '{luz}': {len(recomendaciones_luz)} plantas")
                
                # Evaluación según humedad interior
                humedad = condiciones_usuario.get('humedad_interior', 'media')
                if humedad in nodo_actual['humedad_interior']:
                    plantas_humedad = nodo_actual['humedad_interior'][humedad]
                    recomendaciones_humedad = self._format_recommendations(plantas_humedad)
                    recomendaciones_sin_filtrar.extend(recomendaciones_humedad)
                    print(f"   💧 Interior + Humedad '{humedad}': {len(recomendaciones_humedad)} plantas")
            
            # Evaluación para exterior protegido (incluye nativas)
            elif ubicacion_usuario == 'exterior_protegido':
                resistencia = condiciones_usuario.get('resistencia_heladas', 'media')
                if resistencia in nodo_actual['resistencia_heladas']:
                    plantas_exterior = nodo_actual['resistencia_heladas'][resistencia]
                    recomendaciones_exterior = self._format_recommendations(plantas_exterior)
                    recomendaciones_sin_filtrar.extend(recomendaciones_exterior)
                    print(f"   🌨️ Exterior + Resistencia '{resistencia}': {len(recomendaciones_exterior)} plantas")
                
                # Siempre considerar plantas nativas para exterior
                if 'plantas_nativas' in nodo_actual:
                    plantas_nativas = nodo_actual['plantas_nativas']['prioritarias']
                    recomendaciones_nativas = self._format_recommendations(plantas_nativas)
                    recomendaciones_sin_filtrar.extend(recomendaciones_nativas)
                    print(f"   🌳 Nativas prioritarias: {len(recomendaciones_nativas)} plantas")
            
            # Evaluación para ambos (plantas versátiles)
            elif ubicacion_usuario == 'ambos':
                if 'facilidad_traslado' in nodo_actual:
                    plantas_ambos = nodo_actual['facilidad_traslado']['alta']
                    recomendaciones_ambos = self._format_recommendations(plantas_ambos)
                    recomendaciones_sin_filtrar.extend(recomendaciones_ambos)
                    print(f"   🔄 Plantas versátiles: {len(recomendaciones_ambos)} plantas")
        
        # *** APLICAR FILTRO CRÍTICO DE UBICACIÓN Y OBJETIVO ***
        print(f"🔍 ANTES DEL FILTRO: {len(recomendaciones_sin_filtrar)} recomendaciones sin filtrar")
        recomendaciones = self._filter_by_location_and_objective_compatibility(recomendaciones_sin_filtrar, condiciones_usuario)
        print(f"🔍 DESPUÉS DEL FILTRO: {len(recomendaciones)} recomendaciones compatibles")
        
        # Filtros adicionales por experiencia del usuario
        experiencia = condiciones_usuario.get('experiencia_usuario', 'principiante')
        recomendaciones = self._filter_by_experience(recomendaciones, experiencia)
        
        # Filtros por restricciones especiales
        if condiciones_usuario.get('mascotas_presentes', False):
            recomendaciones = self._filter_pet_safe(recomendaciones)
        
        resultado_final = self._remove_duplicates(recomendaciones)
        print(f"🔍 RESULTADO FINAL ÁRBOL: {len(resultado_final)} plantas recomendadas")
        
        return resultado_final
    
    def _format_recommendations(self, plantas_nodo):
        """
        Formatea las recomendaciones del nodo del árbol
        """
        recommendations = []
        plantas = plantas_nodo['plantas']
        confianzas = plantas_nodo['confianza']
        
        for i, planta in enumerate(plantas):
            recommendations.append({
                'planta': planta,
                'confianza': confianzas[i] if i < len(confianzas) else 70,
                'fuente': 'arbol_decision'
            })
        
        return recommendations
    
    def _filter_by_location_and_objective_compatibility(self, recomendaciones, condiciones_usuario):
        """
        FILTRO CRÍTICO: Elimina plantas incompatibles con la ubicación Y objetivo específico
        """
        from plants_data import PLANTAS
        
        ubicacion_usuario = condiciones_usuario.get('ubicacion', 'interior')
        objetivo_usuario = condiciones_usuario.get('objetivo_principal')
        filtered_recommendations = []
        
        print(f"🔍 FILTRO ÁRBOL: Usuario quiere '{ubicacion_usuario}' + objetivo '{objetivo_usuario}'")
        
        for rec in recomendaciones:
            plant_id = rec['planta']
            
            if plant_id not in PLANTAS:
                print(f"   ⚠️ {plant_id}: NO ENCONTRADA en base de datos")
                continue
            
            plant_data = PLANTAS[plant_id]
            categoria_planta = plant_data.get('categoria', 'interior')
            
            # FILTRO 1: Compatibilidad de ubicación
            ubicacion_compatible = False
            if ubicacion_usuario == 'interior':
                ubicacion_compatible = categoria_planta in ['interior', 'comestible', 'ambos']
            elif ubicacion_usuario == 'exterior_protegido':
                ubicacion_compatible = categoria_planta in ['exterior_protegido', 'comestible', 'ambos']
            elif ubicacion_usuario == 'ambos':
                ubicacion_compatible = True
            
            # FILTRO 2: Compatibilidad de objetivo (CRÍTICO)
            objetivo_compatible = True  # Por defecto compatible
            
            if objetivo_usuario == 'comestible':
                # Si busca comestibles, SOLO plantas comestibles o calafate
                objetivo_compatible = (categoria_planta == 'comestible' or plant_id == 'calafate')
                
            elif objetivo_usuario == 'nativas':
                # Si busca nativas, SOLO plantas nativas
                objetivo_compatible = plant_data.get('planta_nativa', False)
                
            elif objetivo_usuario == 'purificar_aire':
                # Si busca purificadoras, SOLO las que purifican aire
                objetivo_compatible = plant_data.get('purifica_aire', False)
                
            elif objetivo_usuario == 'decorativo':
                # Si busca decorativas, priorizar ornamentales (no comestibles)
                objetivo_compatible = categoria_planta in ['interior', 'exterior_protegido', 'ambos']
                
            elif objetivo_usuario == 'facil_cuidado':
                # Si busca fácil cuidado, plantas principiantes o nativas establecidas
                dificultad = plant_data.get('dificultad', 'intermedio')
                es_nativa = plant_data.get('planta_nativa', False)
                objetivo_compatible = (dificultad == 'principiante' or (es_nativa and dificultad != 'avanzado'))
            
            # DECISIÓN FINAL
            compatible = ubicacion_compatible and objetivo_compatible
            
            # Debug detallado
            ubicacion_status = "✅" if ubicacion_compatible else "❌"
            objetivo_status = "✅" if objetivo_compatible else "❌"
            final_status = "✅ ACEPTADA" if compatible else "❌ RECHAZADA"
            
            # Debug especial para Pothos
            if plant_id == 'pothos':
                print(f"   🔍 POTHOS DETALLADO:")
                print(f"      - Categoría: {categoria_planta}")
                print(f"      - Ubicación compatible: {ubicacion_compatible} (user: {ubicacion_usuario})")
                print(f"      - Objetivo compatible: {objetivo_compatible} (user: {objetivo_usuario})")
                print(f"      - Resultado: {final_status}")
            else:
                print(f"   {plant_id} ({categoria_planta}): Ubicación {ubicacion_status} + Objetivo {objetivo_status} → {final_status}")
            
            if compatible:
                filtered_recommendations.append(rec)
        
        print(f"🔍 FILTRO ÁRBOL RESULTADO: {len(filtered_recommendations)} plantas compatibles de {len(recomendaciones)} originales")
        return filtered_recommendations
    
    def _filter_by_experience(self, recomendaciones, experiencia):
        """
        Filtra recomendaciones según la experiencia del usuario
        """
        from plants_data import PLANTAS
        
        # Plantas fáciles para principiantes
        plantas_principiante = ['sansevieria', 'zz_plant', 'pothos', 'suculentas_echeveria', 'cactus_opuntia', 
                               'perejil', 'oregano', 'romero', 'mata_negra', 'coiron']
        plantas_intermedio = ['dracaena', 'ficus', 'geranios', 'albahaca', 'lavanda', 'nire', 'calafate', 'manzanilla']
        plantas_avanzado = ['monstera', 'lenga', 'espatifilo', 'filodendro']
        
        if experiencia == 'principiante':
            return [r for r in recomendaciones if r['planta'] in plantas_principiante]
        elif experiencia == 'intermedio':
            return [r for r in recomendaciones if r['planta'] in plantas_principiante + plantas_intermedio]
        else:  # avanzado
            return recomendaciones  # Sin filtro
    
    def _filter_pet_safe(self, recomendaciones):
        """
        Filtra plantas tóxicas para mascotas
        """
        plantas_seguras = ['sansevieria', 'suculentas_echeveria', 'cactus_opuntia', 'perejil', 'oregano', 'ciboulette', 
                          'lavanda', 'romero', 'geranios', 'pensamiento', 'manzanilla',
                          'lenga', 'nire', 'calafate', 'mata_negra', 'coiron']  # Todas las nativas son seguras
        return [r for r in recomendaciones if r['planta'] in plantas_seguras]
    
    def _remove_duplicates(self, recomendaciones):
        """
        Elimina recomendaciones duplicadas y ordena por confianza
        """
        plantas_unicas = {}
        for rec in recomendaciones:
            planta = rec['planta']
            if planta not in plantas_unicas or rec['confianza'] > plantas_unicas[planta]['confianza']:
                plantas_unicas[planta] = rec
        
        # Ordenar por confianza descendente
        resultado = list(plantas_unicas.values())
        resultado.sort(key=lambda x: x['confianza'], reverse=True)
        
        return resultado[:3]  # Top 3 recomendaciones
    
    def get_explanation(self, planta, condiciones_usuario):
        """
        Genera explicación para una recomendación específica
        Incluye explicaciones especiales para plantas nativas
        """
        explanations = {
            # Plantas de interior
            'sansevieria': "Perfecta para condiciones de poca luz y baja humedad típicas de hogares fueguinos con calefacción constante.",
            'zz_plant': "Extremadamente resistente a ambientes secos y descuidos de riego, ideal para el clima interior fueguino.",
            'pothos': "Se adapta bien a diferentes condiciones de luz y ayuda a purificar el aire en espacios cerrados.",
            'dracaena': "Tolera el aire seco de la calefacción y crece verticalmente, aprovechando espacios pequeños.",
            'ficus': "Excelente para humidificar ambientes secos, pero requiere ubicación estable sin corrientes.",
            'monstera': "Planta espectacular que requiere espacio amplio y cuidados intermedios.",
            'suculentas_echeveria': "Perfecta para las condiciones extremadamente secas de interiores calefaccionados.",
            'cactus_opuntia': "Extremadamente resistente al aire seco y calefacción constante.",
            'espatifilo': "Florece en condiciones de poca luz, ideal para inviernos fueguinos.",
            'filodendro': "Se adapta bien a la luz artificial y contribuye a humidificar el ambiente.",
            
            # Plantas comestibles
            'albahaca': "Valiosa fuente de hierbas frescas durante inviernos cuando productos frescos son costosos.",
            'perejil': "Resistente a temperaturas frescas y proporciona vitaminas frescas durante todo el año.",
            'oregano': "Extremadamente resistente al aire seco interior y proporciona condimento fresco.",
            'ciboulette': "Resistente al frío y proporciona condimento fresco durante todo el año.",
            
            # Plantas de exterior
            'lavanda': "Una vez establecida, resiste heladas ocasionales y proporciona aroma relajante.",
            'romero': "Muy resistente a heladas y útil para cocina, adaptado al clima fueguino.",
            'geranios': "Flexibilidad de ubicación permite aprovechar el corto pero intenso verano fueguino.",
            'pensamiento': "Una de las pocas flores que tolera heladas y proporciona color temprano en primavera.",
            'manzanilla': "Resistente al clima y proporciona té relajante, valioso durante largos inviernos.",
            
            # PLANTAS NATIVAS DE TIERRA DEL FUEGO
            'lenga': "🌳 NATIVA TDF: Árbol emblemático de Tierra del Fuego con espectacular coloración otoñal dorada. Completamente adaptado al clima austral y símbolo de la región.",
            'nire': "🌳 NATIVA TDF: Árbol nativo de menor porte que la lenga, crece más rápido y resiste perfectamente los vientos patagónicos. Ideal para jardines medianos.",
            'calafate': "🫐 NATIVA TDF: Arbusto con frutos comestibles azules, parte del folklore patagónico. Completamente adaptado al clima y produce alimento natural.",
            'mata_negra': "🌿 NATIVA TDF: Arbusto extremadamente resistente a condiciones adversas. Prácticamente no requiere cuidados una vez establecido.",
            'coiron': "🌾 NATIVA TDF: Pasto nativo del paisaje estepario fueguino. Cero mantenimiento y resistencia extrema a vientos y sequías."
        }
        
        base_explanation = explanations.get(planta, f"Recomendada según las condiciones específicas de Tierra del Fuego.")
        
        # Agregar información adicional según el contexto
        objetivo = condiciones_usuario.get('objetivo_principal', '')
        if objetivo == 'nativas' and planta in ['lenga', 'nire', 'calafate', 'mata_negra', 'coiron']:
            base_explanation += " Esta especie forma parte del patrimonio natural fueguino y contribuye a la conservación de la flora nativa."
        
        return base_explanation


# Función principal para usar el árbol de decisión
def recommend_plants(condiciones_usuario):
    """
    Función principal que utiliza el árbol de decisión para recomendar plantas
    
    Args:
        condiciones_usuario (dict): Diccionario con las condiciones del usuario
        
    Returns:
        list: Lista de recomendaciones con explicaciones
    """
    tree = DecisionTree()
    recomendaciones = tree.evaluate_conditions(condiciones_usuario)
    
    # Agregar explicaciones
    for rec in recomendaciones:
        rec['explicacion'] = tree.get_explanation(rec['planta'], condiciones_usuario)
    
    return recomendaciones


# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de condiciones de usuario
    condiciones_ejemplo = {
        'ubicacion': 'interior',
        'luz_disponible': 'escasa',
        'humedad_interior': 'baja',
        'experiencia_usuario': 'principiante',
        'mascotas_presentes': False,
        'objetivo_principal': 'comestible'
    }
    
    recomendaciones = recommend_plants(condiciones_ejemplo)
    
    print("Recomendaciones para las condiciones dadas:")
    for i, rec in enumerate(recomendaciones, 1):
        print(f"{i}. {rec['planta']} (Confianza: {rec['confianza']}%)")
        print(f"   Explicación: {rec['explicacion']}\n")