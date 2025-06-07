"""
Estructura del Árbol de Decisión
Sistema Experto para Recomendación de Plantas en Tierra del Fuego
"""

class DecisionTree:
    """
    Implementa el árbol de decisión para la recomendación de plantas
    basado en la arquitectura definida en la Entrega 2
    """
    
    def __init__(self):
        self.tree_structure = self._build_tree()
    
    def _build_tree(self):
        """
        Construye la estructura del árbol de decisión según la documentación
        """
        return {
            'ubicacion': {
                'interior': {
                    'luz_disponible': {
                        'escasa': {
                            'plantas': ['sansevieria', 'zz_plant', 'pothos'],
                            'confianza': [95, 90, 85]
                        },
                        'moderada': {
                            'plantas': ['dracaena', 'ficus', 'plantas_comestibles'],
                            'confianza': [80, 75, 70]
                        },
                        'abundante': {
                            'plantas': ['monstera', 'ficus', 'albahaca'],
                            'confianza': [85, 80, 75]
                        }
                    },
                    'humedad_interior': {
                        'baja': {
                            'plantas': ['sansevieria', 'zz_plant', 'suculentas'],
                            'confianza': [95, 90, 88]
                        },
                        'media': {
                            'plantas': ['pothos', 'dracaena', 'ficus'],
                            'confianza': [85, 80, 75]
                        },
                        'alta': {
                            'plantas': ['monstera', 'ficus', 'plantas_comestibles'],
                            'confianza': [90, 85, 80]
                        }
                    }
                },
                'exterior_protegido': {
                    'resistencia_heladas': {
                        'alta': {
                            'plantas': ['lavanda', 'romero'],
                            'confianza': [85, 90]
                        },
                        'media': {
                            'plantas': ['geranios', 'suculentas'],
                            'confianza': [75, 70]
                        }
                    }
                },
                'ambos': {
                    'facilidad_traslado': {
                        'alta': {
                            'plantas': ['geranios', 'suculentas', 'plantas_comestibles'],
                            'confianza': [80, 85, 75]
                        }
                    }
                }
            }
        }
    
    def evaluate_conditions(self, condiciones_usuario):
        """
        Evalúa las condiciones del usuario contra el árbol de decisión
        
        Args:
            condiciones_usuario (dict): Condiciones proporcionadas por el usuario
            
        Returns:
            list: Lista de plantas recomendadas con sus niveles de confianza
        """
        recomendaciones = []
        
        # Navegación por el árbol según ubicación
        ubicacion = condiciones_usuario.get('ubicacion', 'interior')
        
        if ubicacion in self.tree_structure['ubicacion']:
            nodo_actual = self.tree_structure['ubicacion'][ubicacion]
            
            # Evaluación según luz disponible (para interior)
            if ubicacion == 'interior':
                luz = condiciones_usuario.get('luz_disponible', 'moderada')
                if luz in nodo_actual['luz_disponible']:
                    plantas_luz = nodo_actual['luz_disponible'][luz]
                    recomendaciones.extend(self._format_recommendations(plantas_luz))
                
                # Evaluación según humedad interior
                humedad = condiciones_usuario.get('humedad_interior', 'media')
                if humedad in nodo_actual['humedad_interior']:
                    plantas_humedad = nodo_actual['humedad_interior'][humedad]
                    recomendaciones.extend(self._format_recommendations(plantas_humedad))
            
            # Evaluación para exterior protegido
            elif ubicacion == 'exterior_protegido':
                resistencia = condiciones_usuario.get('resistencia_heladas', 'media')
                if resistencia in nodo_actual['resistencia_heladas']:
                    plantas_exterior = nodo_actual['resistencia_heladas'][resistencia]
                    recomendaciones.extend(self._format_recommendations(plantas_exterior))
        
        # Filtros adicionales por experiencia del usuario
        experiencia = condiciones_usuario.get('experiencia_usuario', 'principiante')
        recomendaciones = self._filter_by_experience(recomendaciones, experiencia)
        
        # Filtros por restricciones especiales
        if condiciones_usuario.get('mascotas_presentes', False):
            recomendaciones = self._filter_pet_safe(recomendaciones)
        
        return self._remove_duplicates(recomendaciones)
    
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
    
    def _filter_by_experience(self, recomendaciones, experiencia):
        """
        Filtra recomendaciones según la experiencia del usuario
        """
        # Plantas fáciles para principiantes
        plantas_principiante = ['sansevieria', 'zz_plant', 'pothos', 'suculentas']
        plantas_intermedio = ['dracaena', 'ficus', 'geranios', 'plantas_comestibles']
        plantas_avanzado = ['monstera', 'lavanda', 'romero']
        
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
        plantas_seguras = ['sansevieria', 'suculentas', 'plantas_comestibles', 'lavanda', 'romero']
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
        """
        explanations = {
            'sansevieria': "Perfecta para condiciones de poca luz y baja humedad típicas de hogares fueguinos con calefacción constante.",
            'zz_plant': "Extremadamente resistente a ambientes secos y descuidos de riego, ideal para el clima interior fueguino.",
            'pothos': "Se adapta bien a diferentes condiciones de luz y ayuda a purificar el aire en espacios cerrados.",
            'dracaena': "Tolera el aire seco de la calefacción y crece verticalmente, aprovechando espacios pequeños.",
            'ficus': "Excelente para humidificar ambientes secos, pero requiere ubicación estable sin corrientes.",
            'monstera': "Planta espectacular que requiere espacio amplio y cuidados intermedios.",
            'suculentas': "Perfectas para condiciones extremadamente secas y bajo mantenimiento.",
            'geranios': "Pueden pasar el invierno en interior y florecer abundantemente en verano fueguino.",
            'plantas_comestibles': "Proporcionan hierbas frescas durante todo el año, valiosas en el contexto fueguino.",
            'lavanda': "Aromática y resistente una vez establecida, necesita protección de vientos fuertes.",
            'romero': "Muy resistente a heladas y útil para cocina, adaptado al clima fueguino."
        }
        
        return explanations.get(planta, f"Recomendada según las condiciones específicas de Tierra del Fuego.")


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
        'mascotas_presentes': False
    }
    
    recomendaciones = recommend_plants(condiciones_ejemplo)
    
    print("Recomendaciones para las condiciones dadas:")
    for i, rec in enumerate(recomendaciones, 1):
        print(f"{i}. {rec['planta']} (Confianza: {rec['confianza']}%)")
        print(f"   Explicación: {rec['explicacion']}\n")
