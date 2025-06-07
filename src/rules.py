# Reglas del sistema experto

def regla_luz_escasa(condiciones):
    """Regla R1: Plantas para luz escasa"""
    if condiciones.get('luz_disponible') == 'escasa':
        return ['sansevieria', 'zz_plant', 'pothos']
    return []

def regla_humedad_baja(condiciones):
    """Regla R2: Plantas para ambientes secos"""
    if condiciones.get('humedad_interior') == 'baja':
        return ['sansevieria', 'zz_plant', 'suculentas']
    return []

# ... más reglas según la documentación
