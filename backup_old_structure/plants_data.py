"""
Base de conocimiento expandida con 25 plantas para Tierra del Fuego
Incluye especies nativas e introducidas adaptadas a la región
"""

PLANTAS = {
    # ============ PLANTAS DE INTERIOR - PRINCIPIANTES ============
    'sansevieria': {
        'nombre_comun': 'Sansevieria (Lengua de Tigre)',
        'nombre_cientifico': 'Sansevieria trifasciata',
        'categoria': 'interior',
        'dificultad': 'principiante',
        'luz_minima': 'escasa',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'extrema',
        'resistencia_calefaccion': 'excelente',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'sansevieria.jpg',
        'descripcion': 'Extremadamente resistente a condiciones secas y poca luz. Perfecta para hogares fueguinos con calefacción constante.',
        'cuidados_especiales': 'Regar solo cuando la tierra esté completamente seca. En invierno fueguino, reducir riego a mínimo.',
        'ventajas_fueguinas': 'Tolera perfectamente el aire seco de la calefacción y las pocas horas de luz invernal.'
    },
    
    'zz_plant': {
        'nombre_comun': 'ZZ Plant (Zamioculcas)',
        'nombre_cientifico': 'Zamioculcas zamiifolia',
        'categoria': 'interior',
        'dificultad': 'principiante',
        'luz_minima': 'escasa',
        'humedad_requerida': 'baja',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'extrema',
        'resistencia_calefaccion': 'excelente',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'zz_plant.jpg',
        'descripcion': 'Adaptación excepcional a baja humedad. Perfecta para principiantes en condiciones fueguinas.',
        'cuidados_especiales': 'Mantener alejada de mascotas. Regar muy esporádicamente en invierno.',
        'ventajas_fueguinas': 'Crece lentamente pero de forma estable, resistiendo descuidos típicos durante inviernos largos.'
    },

    'pothos': {
        'nombre_comun': 'Pothos',
        'nombre_cientifico': 'Epipremnum aureum',
        'categoria': 'interior',
        'dificultad': 'principiante',
        'luz_minima': 'moderada',
        'humedad_requerida': 'media',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'alta',
        'resistencia_calefaccion': 'buena',
        'tamaño_maximo': 'variable',
        'valor_ornamental': 'muy_alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'pothos.jpg',
        'descripcion': 'Adaptable a diferentes condiciones de luz. Excelente purificador de aire para espacios cerrados.',
        'cuidados_especiales': 'Mantener alejado de mascotas. Puede crecer como colgante o trepadora.',
        'ventajas_fueguinas': 'Ayuda a humidificar ambientes secos y prospera en luz artificial durante inviernos largos.'
    },

    'suculentas_echeveria': {
        'nombre_comun': 'Echeveria (Suculenta Rosa)',
        'nombre_cientifico': 'Echeveria elegans',
        'categoria': 'interior',
        'dificultad': 'principiante',
        'luz_minima': 'moderada',
        'humedad_requerida': 'muy_baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'extrema',
        'resistencia_calefaccion': 'excelente',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'alto',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'echeveria.jpg',
        'descripcion': 'Suculenta compacta ideal para espacios pequeños. Requiere mínimo mantenimiento.',
        'cuidados_especiales': 'Riego muy esporádico. Ubicar cerca de ventana pero protegida de corrientes.',
        'ventajas_fueguinas': 'Perfecta para las condiciones extremadamente secas de interiores calefaccionados.'
    },

    'cactus_opuntia': {
        'nombre_comun': 'Tuna (Cactus de Paletas)',
        'nombre_cientifico': 'Opuntia microdasys',
        'categoria': 'interior',
        'dificultad': 'principiante',
        'luz_minima': 'abundante',
        'humedad_requerida': 'muy_baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'extrema',
        'resistencia_calefaccion': 'excelente',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'alto',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'opuntia.jpg',
        'descripcion': 'Cactus resistente que añade carácter único a espacios bien iluminados.',
        'cuidados_especiales': 'Riego mínimo en invierno. Cuidado con las espinas pequeñas.',
        'ventajas_fueguinas': 'Extremadamente resistente al aire seco y calefacción constante.'
    },

    # ============ PLANTAS DE INTERIOR - INTERMEDIAS ============
    'ficus': {
        'nombre_comun': 'Ficus Benjamina (Gomero)',
        'nombre_cientifico': 'Ficus benjamina',
        'categoria': 'interior',
        'dificultad': 'intermedio',
        'luz_minima': 'moderada',
        'humedad_requerida': 'media',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'media',
        'resistencia_calefaccion': 'media',
        'tamaño_maximo': 'grande',
        'valor_ornamental': 'muy_alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'ficus.jpg',
        'descripcion': 'Excelente para humidificar ambientes, pero sensible a cambios bruscos de temperatura.',
        'cuidados_especiales': 'Ubicar lejos de corrientes de aire frío. No mover frecuentemente.',
        'ventajas_fueguinas': 'Ayuda significativamente con la humedad en ambientes con calefacción.'
    },

    'monstera': {
        'nombre_comun': 'Monstera Deliciosa',
        'nombre_cientifico': 'Monstera deliciosa',
        'categoria': 'interior',
        'dificultad': 'intermedio',
        'luz_minima': 'moderada',
        'humedad_requerida': 'alta',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'baja',
        'resistencia_calefaccion': 'media',
        'tamaño_maximo': 'muy_grande',
        'valor_ornamental': 'espectacular',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'monstera.jpg',
        'descripcion': 'Planta espectacular que requiere espacio amplio y cuidados intermedios.',
        'cuidados_especiales': 'Necesita humedad controlada y espacio para crecer. Limpiar hojas regularmente.',
        'ventajas_fueguinas': 'Crea un punto focal dramático durante largos inviernos, pero requiere atención a la humedad.'
    },

    'dracaena': {
        'nombre_comun': 'Dracaena Marginata',
        'nombre_cientifico': 'Dracaena marginata',
        'categoria': 'interior',
        'dificultad': 'intermedio',
        'luz_minima': 'moderada',
        'humedad_requerida': 'baja',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'alta',
        'resistencia_calefaccion': 'buena',
        'tamaño_maximo': 'grande',
        'valor_ornamental': 'alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'dracaena.jpg',
        'descripcion': 'Tolerante a aire seco. Crecimiento vertical ideal para espacios pequeños.',
        'cuidados_especiales': 'Mantener alejada de mascotas. Limpiar hojas para optimizar fotosíntesis.',
        'ventajas_fueguinas': 'Su crecimiento vertical aprovecha bien espacios limitados en viviendas fueguinas.'
    },

    'filodendro': {
        'nombre_comun': 'Filodendro',
        'nombre_cientifico': 'Philodendron hederaceum',
        'categoria': 'interior',
        'dificultad': 'intermedio',
        'luz_minima': 'moderada',
        'humedad_requerida': 'media',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'media',
        'resistencia_calefaccion': 'buena',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'filodendro.jpg',
        'descripcion': 'Planta trepadora versátil con hojas en forma de corazón.',
        'cuidados_especiales': 'Mantener alejado de mascotas. Puede crecer como colgante.',
        'ventajas_fueguinas': 'Se adapta bien a la luz artificial y contribuye a humidificar el ambiente.'
    },

    'espatifilo': {
        'nombre_comun': 'Espatifilo (Cuna de Moisés)',
        'nombre_cientifico': 'Spathiphyllum wallisii',
        'categoria': 'interior',
        'dificultad': 'intermedio',
        'luz_minima': 'escasa',
        'humedad_requerida': 'alta',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'baja',
        'resistencia_calefaccion': 'media',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'muy_alto',
        'purifica_aire': True,
        'planta_nativa': False,
        'imagen': 'espatifilo.jpg',
        'descripcion': 'Produce elegantes flores blancas y es excelente purificador de aire.',
        'cuidados_especiales': 'Requiere humedad constante. Mantener alejado de mascotas.',
        'ventajas_fueguinas': 'Florece en condiciones de poca luz, ideal para inviernos fueguinos.'
    },

    # ============ PLANTAS COMESTIBLES ============
    'albahaca': {
        'nombre_comun': 'Albahaca',
        'nombre_cientifico': 'Ocimum basilicum',
        'categoria': 'comestible',
        'dificultad': 'intermedio',
        'luz_minima': 'abundante',
        'humedad_requerida': 'media',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'baja',
        'resistencia_calefaccion': 'media',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'albahaca.jpg',
        'descripcion': 'Requiere ventana soleada. Proporciona hierbas frescas con ciclo de cultivo corto.',
        'cuidados_especiales': 'Ubicar en ventana sur. Pellizcar flores para promover crecimiento de hojas.',
        'ventajas_fueguinas': 'Valiosa fuente de hierbas frescas durante inviernos cuando productos frescos son costosos.'
    },

    'perejil': {
        'nombre_comun': 'Perejil',
        'nombre_cientifico': 'Petroselinum crispum',
        'categoria': 'comestible',
        'dificultad': 'principiante',
        'luz_minima': 'moderada',
        'humedad_requerida': 'media',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'media',
        'resistencia_calefaccion': 'buena',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'perejil.jpg',
        'descripcion': 'Adaptable a condiciones de luz variables. Permite cultivo continuo.',
        'cuidados_especiales': 'Cortar desde afuera hacia adentro. Mantener tierra húmeda pero no encharcada.',
        'ventajas_fueguinas': 'Resistente a temperaturas frescas y proporciona vitaminas frescas durante todo el año.'
    },

    'oregano': {
        'nombre_comun': 'Orégano',
        'nombre_cientifico': 'Origanum vulgare',
        'categoria': 'comestible',
        'dificultad': 'principiante',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'alta',
        'resistencia_calefaccion': 'excelente',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'oregano.jpg',
        'descripcion': 'Hierba aromática resistente que tolera sequía y proporciona sabor intenso.',
        'cuidados_especiales': 'Pellizcar flores para mantener sabor de hojas. Riego moderado.',
        'ventajas_fueguinas': 'Extremadamente resistente al aire seco interior y proporciona condimento fresco.'
    },

    'ciboulette': {
        'nombre_comun': 'Ciboulette (Cebollín)',
        'nombre_cientifico': 'Allium schoenoprasum',
        'categoria': 'comestible',
        'dificultad': 'principiante',
        'luz_minima': 'moderada',
        'humedad_requerida': 'media',
        'toxica_mascotas': True,
        'tolerancia_sequedad': 'media',
        'resistencia_calefaccion': 'buena',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'ciboulette.jpg',
        'descripcion': 'Hierba perenne fácil de cultivar que proporciona sabor suave a cebolla.',
        'cuidados_especiales': 'Cortar regularmente para promover crecimiento. Mantener alejado de mascotas.',
        'ventajas_fueguinas': 'Resistente al frío y proporciona condimento fresco durante todo el año.'
    },

    # ============ ESPECIES NATIVAS DE TIERRA DEL FUEGO ============
    'lenga': {
        'nombre_comun': 'Lenga',
        'nombre_cientifico': 'Nothofagus pumilio',
        'categoria': 'exterior_protegido',
        'dificultad': 'avanzado',
        'luz_minima': 'abundante',
        'humedad_requerida': 'media',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'media',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'muy_grande',
        'valor_ornamental': 'espectacular',
        'purifica_aire': False,
        'planta_nativa': True,
        'imagen': 'lenga.jpg',
        'descripcion': 'Árbol nativo emblemático de Tierra del Fuego. Espectacular coloración otoñal dorada.',
        'cuidados_especiales': 'Requiere espacio amplio y años para establecerse. Plantar en primavera.',
        'ventajas_fueguinas': 'Completamente adaptado al clima austral. Símbolo de la región y patrimonio natural.'
    },

    'nire': {
        'nombre_comun': 'Ñire',
        'nombre_cientifico': 'Nothofagus antarctica',
        'categoria': 'exterior_protegido',
        'dificultad': 'intermedio',
        'luz_minima': 'abundante',
        'humedad_requerida': 'media',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'alta',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'grande',
        'valor_ornamental': 'muy_alto',
        'purifica_aire': False,
        'planta_nativa': True,
        'imagen': 'nire.jpg',
        'descripcion': 'Árbol nativo de menor porte que la lenga. Excelente para jardines medianos.',
        'cuidados_especiales': 'Más tolerante que la lenga. Proteger de vientos extremos cuando joven.',
        'ventajas_fueguinas': 'Nativo adaptado, crece más rápido que la lenga y resiste vientos patagónicos.'
    },

    'calafate': {
        'nombre_comun': 'Calafate',
        'nombre_cientifico': 'Berberis microphylla',
        'categoria': 'exterior_protegido',
        'dificultad': 'intermedio',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'muy_alta',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'alto',
        'purifica_aire': False,
        'planta_nativa': True,
        'imagen': 'calafate.jpg',
        'descripcion': 'Arbusto nativo con frutos comestibles azules. Parte del folklore patagónico.',
        'cuidados_especiales': 'Muy resistente una vez establecido. Cuidado con espinas al podar.',
        'ventajas_fueguinas': 'Completamente adaptado al clima. Produce frutos comestibles y tiene valor cultural.'
    },

    'mata_negra': {
        'nombre_comun': 'Mata Negra',
        'nombre_cientifico': 'Junellia tridens',
        'categoria': 'exterior_protegido',
        'dificultad': 'intermedio',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'extrema',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': True,
        'imagen': 'mata_negra.jpg',
        'descripcion': 'Arbusto bajo nativo, extremadamente resistente a condiciones adversas.',
        'cuidados_especiales': 'Prácticamente no requiere cuidados una vez establecido.',
        'ventajas_fueguinas': 'Perfectamente adaptado a vientos y sequías. Ideal para jardines de bajo mantenimiento.'
    },

    'coiron': {
        'nombre_comun': 'Coirón',
        'nombre_cientifico': 'Festuca gracillima',
        'categoria': 'exterior_protegido',
        'dificultad': 'principiante',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'extrema',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': True,
        'imagen': 'coiron.jpg',
        'descripcion': 'Pasto nativo en matas que forma parte del paisaje estepario fueguino.',
        'cuidados_especiales': 'No requiere cuidados. Cortar una vez al año si se desea.',
        'ventajas_fueguinas': 'Parte del ecosistema natural. Cero mantenimiento y resistencia extrema.'
    },

    # ============ PLANTAS DE EXTERIOR NO NATIVAS ADAPTADAS ============
    'lavanda': {
        'nombre_comun': 'Lavanda',
        'nombre_cientifico': 'Lavandula angustifolia',
        'categoria': 'exterior_protegido',
        'dificultad': 'intermedio',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'muy_alta',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'muy_alto',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'lavanda.jpg',
        'descripcion': 'Aromática y ornamental. Requiere protección de vientos fuertes.',
        'cuidados_especiales': 'Proteger de vientos patagónicos. Podar después de floración.',
        'ventajas_fueguinas': 'Una vez establecida, resiste heladas ocasionales y proporciona aroma relajante.'
    },

    'romero': {
        'nombre_comun': 'Romero',
        'nombre_cientifico': 'Rosmarinus officinalis',
        'categoria': 'exterior_protegido',
        'dificultad': 'principiante',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'muy_alta',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'grande',
        'valor_ornamental': 'alto',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'romero.jpg',
        'descripcion': 'Muy resistente una vez establecido. Soporta heladas leves y tiene uso culinario.',
        'cuidados_especiales': 'Plantar en suelo con buen drenaje. Protección inicial del viento.',
        'ventajas_fueguinas': 'Extremadamente resistente al clima fueguino y proporciona hierbas aromáticas todo el año.'
    },

    'geranios': {
        'nombre_comun': 'Geranios',
        'nombre_cientifico': 'Pelargonium spp.',
        'categoria': 'ambos',
        'dificultad': 'intermedio',
        'luz_minima': 'abundante',
        'humedad_requerida': 'media',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'alta',
        'resistencia_calefaccion': 'buena',
        'tamaño_maximo': 'mediano',
        'valor_ornamental': 'muy_alto',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'geranios.jpg',
        'descripcion': 'Pueden invernar en interior y florecer abundantemente en verano fueguino.',
        'cuidados_especiales': 'Trasladar al interior antes de heladas. Reducir riego en invierno.',
        'ventajas_fueguinas': 'Flexibilidad de ubicación permite aprovechar el corto pero intenso verano fueguino.'
    },

    'pensamiento': {
        'nombre_comun': 'Pensamiento',
        'nombre_cientifico': 'Viola tricolor',
        'categoria': 'exterior_protegido',
        'dificultad': 'principiante',
        'luz_minima': 'moderada',
        'humedad_requerida': 'media',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'media',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'alto',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'pensamiento.jpg',
        'descripcion': 'Flor colorida que tolera frío y florece en primavera fueguina.',
        'cuidados_especiales': 'Plantar en otoño para floración primaveral. Proteger de vientos fuertes.',
        'ventajas_fueguinas': 'Una de las pocas flores que tolera heladas y proporciona color temprano en primavera.'
    },

    'manzanilla': {
        'nombre_comun': 'Manzanilla',
        'nombre_cientifico': 'Matricaria chamomilla',
        'categoria': 'exterior_protegido',
        'dificultad': 'principiante',
        'luz_minima': 'abundante',
        'humedad_requerida': 'baja',
        'toxica_mascotas': False,
        'tolerancia_sequedad': 'alta',
        'resistencia_calefaccion': 'no_aplica',
        'tamaño_maximo': 'pequeño',
        'valor_ornamental': 'medio',
        'purifica_aire': False,
        'planta_nativa': False,
        'imagen': 'manzanilla.jpg',
        'descripcion': 'Hierba medicinal y aromática de fácil cultivo. Florece en verano.',
        'cuidados_especiales': 'Sembrar en primavera. Cosechar flores para té medicinal.',
        'ventajas_fueguinas': 'Resistente al clima y proporciona té relajante, valioso durante largos inviernos.'
    }
}

# Metadatos actualizados
METADATA = {
    'total_plantas': len(PLANTAS),
    'plantas_nativas': len([p for p in PLANTAS.values() if p.get('planta_nativa', False)]),
    'plantas_introducidas': len([p for p in PLANTAS.values() if not p.get('planta_nativa', False)]),
    'categorias': ['interior', 'exterior_protegido', 'ambos', 'comestible'],
    'niveles_dificultad': ['principiante', 'intermedio', 'avanzado'],
    'fuentes_conocimiento': [
        'Vivero Flora Austral (Río Grande)',
        'INTA Tierra del Fuego',
        'Herbario del Museo del Fin del Mundo',
        'Experiencia local de cultivadores',
        'Guías de flora patagónica'
    ],
    'ultima_actualizacion': '2025-06-08',
    'region_especializada': 'Tierra del Fuego, Argentina',
    'incluye_especies_nativas': True
}

def get_plantas_nativas():
    """Retorna solo las plantas nativas de Tierra del Fuego"""
    return {k: v for k, v in PLANTAS.items() if v.get('planta_nativa', False)}

def get_plantas_by_categoria(categoria):
    """Retorna plantas filtradas por categoría"""
    return {k: v for k, v in PLANTAS.items() if v['categoria'] == categoria}

def get_plantas_by_dificultad(dificultad):
    """Retorna plantas filtradas por nivel de dificultad"""
    return {k: v for k, v in PLANTAS.items() if v['dificultad'] == dificultad}

def get_plantas_seguras_mascotas():
    """Retorna plantas no tóxicas para mascotas"""
    return {k: v for k, v in PLANTAS.items() if not v['toxica_mascotas']}

def get_plant_info(plant_id):
    """Obtiene información de una planta específica"""
    return PLANTAS.get(plant_id, None)

def get_plantas_comestibles():
    """Retorna plantas comestibles y hierbas"""
    return {k: v for k, v in PLANTAS.items() if v['categoria'] == 'comestible'}

def get_estadisticas_sistema():
    """Retorna estadísticas del sistema expandido"""
    stats = {
        'total_plantas': METADATA['total_plantas'],
        'nativas': METADATA['plantas_nativas'],
        'introducidas': METADATA['plantas_introducidas'],
        'por_categoria': {},
        'por_dificultad': {},
        'toxicas_mascotas': len([p for p in PLANTAS.values() if p['toxica_mascotas']]),
        'seguras_mascotas': len([p for p in PLANTAS.values() if not p['toxica_mascotas']]),
        'purificadoras_aire': len([p for p in PLANTAS.values() if p.get('purifica_aire', False)])
    }
    
    # Estadísticas por categoría
    for categoria in METADATA['categorias']:
        stats['por_categoria'][categoria] = len(get_plantas_by_categoria(categoria))
    
    # Estadísticas por dificultad
    for dificultad in METADATA['niveles_dificultad']:
        stats['por_dificultad'][dificultad] = len(get_plantas_by_dificultad(dificultad))
    
    return stats