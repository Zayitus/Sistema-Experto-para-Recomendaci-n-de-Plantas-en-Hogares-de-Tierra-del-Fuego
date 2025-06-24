#!/usr/bin/env python3
"""
Script de migración para reorganizar PlantAdvisor TDF a estructura profesional
Migra archivos existentes sin romper funcionalidad
"""

import os
import shutil
import sys
from pathlib import Path


class ProjectMigrator:
    """Migra proyecto a estructura profesional"""
    
    def __init__(self, project_root: str = "."):
        self.root = Path(project_root).resolve()
        self.backup_dir = self.root / "backup_old_structure"
        
    def create_directories(self):
        """Crear nueva estructura de directorios"""
        directories = [
            # Código fuente
            "src/plant_advisor",
            "src/plant_advisor/knowledge",
            "src/plant_advisor/models", 
            "src/plant_advisor/services",
            "src/plant_advisor/utils",
            "src/web",
            "src/web/routes",
            "src/web/middleware",
            
            # Tests
            "tests/unit",
            "tests/integration", 
            "tests/fixtures",
            
            # Documentación
            "docs/academic",
            
            # Configuración
            "config/environments",
            
            # Scripts
            "scripts",
            
            # Requirements organizados
            "requirements",
            
            # Deployment
            "deployment/systemd",
            
            # GitHub workflows
            ".github/workflows",
        ]
        
        print("🗂️  Creando estructura de directorios...")
        for directory in directories:
            dir_path = self.root / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"   ✓ {directory}")
    
    def create_init_files(self):
        """Crear archivos __init__.py necesarios"""
        init_dirs = [
            "src",
            "src/plant_advisor",
            "src/plant_advisor/knowledge",
            "src/plant_advisor/models",
            "src/plant_advisor/services", 
            "src/plant_advisor/utils",
            "src/web",
            "src/web/routes",
            "src/web/middleware",
            "tests",
            "tests/unit",
            "tests/integration",
            "tests/fixtures",
            "config",
        ]
        
        print("📝 Creando archivos __init__.py...")
        for directory in init_dirs:
            init_file = self.root / directory / "__init__.py"
            if not init_file.exists():
                with open(init_file, 'w') as f:
                    f.write(f'"""Módulo {directory.replace("/", ".")}"""\n')
                print(f"   ✓ {directory}/__init__.py")
    
    def backup_current_structure(self):
        """Crear backup de estructura actual"""
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        
        print("💾 Creando backup de estructura actual...")
        self.backup_dir.mkdir()
        
        # Archivos Python principales
        python_files = [
            "app.py",
            "expert_system.py", 
            "plants_data.py",
            "rules.py",
            "decision_tree.py",
            "__init__.py"
        ]
        
        for file in python_files:
            src_file = self.root / file
            if src_file.exists():
                shutil.copy2(src_file, self.backup_dir / file)
                print(f"   ✓ Respaldado {file}")
    
    def migrate_python_files(self):
        """Migrar archivos Python a nueva estructura"""
        migrations = {
            # Archivo origen: destino
            "app.py": "src/app.py",
            "expert_system.py": "src/plant_advisor/expert_system.py",
            "plants_data.py": "src/plant_advisor/knowledge/plants_data.py", 
            "rules.py": "src/plant_advisor/knowledge/rules.py",
            "decision_tree.py": "src/plant_advisor/knowledge/decision_tree.py",
        }
        
        print("📦 Migrando archivos Python...")
        for src_file, dest_file in migrations.items():
            src_path = self.root / src_file
            dest_path = self.root / dest_file
            
            if src_path.exists():
                # Crear directorio destino si no existe
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Copiar archivo (mantener original como backup)
                shutil.copy2(src_path, dest_path)
                print(f"   ✓ {src_file} → {dest_file}")
            else:
                print(f"   ⚠️  {src_file} no encontrado")
    
    def update_imports_in_files(self):
        """Actualizar imports en archivos migrados"""
        print("🔧 Actualizando imports...")
        
        # Actualizar imports en app.py
        app_file = self.root / "src" / "app.py"
        if app_file.exists():
            content = app_file.read_text()
            
            # Actualizar imports
            content = content.replace(
                "from expert_system import",
                "from plant_advisor.expert_system import"
            )
            content = content.replace(
                "from plants_data import", 
                "from plant_advisor.knowledge.plants_data import"
            )
            
            app_file.write_text(content)
            print("   ✓ Imports actualizados en app.py")
        
        # Actualizar imports en expert_system.py
        expert_file = self.root / "src" / "plant_advisor" / "expert_system.py"
        if expert_file.exists():
            content = expert_file.read_text()
            
            content = content.replace(
                "from plants_data import PLANTAS",
                "from .knowledge.plants_data import PLANTAS"
            )
            content = content.replace(
                "from rules import RuleEngine", 
                "from .knowledge.rules import RuleEngine"
            )
            content = content.replace(
                "from decision_tree import DecisionTree",
                "from .knowledge.decision_tree import DecisionTree"
            )
            
            expert_file.write_text(content)
            print("   ✓ Imports actualizados en expert_system.py")
        
        # Actualizar imports en decision_tree.py
        tree_file = self.root / "src" / "plant_advisor" / "knowledge" / "decision_tree.py"
        if tree_file.exists():
            content = tree_file.read_text()
            content = content.replace(
                "from plants_data import PLANTAS",
                "from .plants_data import PLANTAS"
            )
            tree_file.write_text(content)
            print("   ✓ Imports actualizados en decision_tree.py")
    
    def create_requirements_files(self):
        """Crear archivos de requirements organizados"""
        print("📋 Creando archivos de requirements...")
        
        # Base requirements
        base_reqs = """# Dependencias base para PlantAdvisor TDF
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
"""
        
        # Development requirements
        dev_reqs = """-r base.txt

# Herramientas de desarrollo
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-flask>=1.2.0
black>=23.7.0
flake8>=6.0.0
mypy>=1.5.0
isort>=5.12.0
pre-commit>=3.3.0

# Seguridad
safety>=2.3.0
bandit>=1.7.0

# Documentación
sphinx>=7.1.0
sphinx-rtd-theme>=1.3.0
"""
        
        # Testing requirements
        test_reqs = """-r base.txt

# Testing específico
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-flask>=1.2.0
coverage>=7.3.0
requests>=2.31.0
"""
        
        # Production requirements
        prod_reqs = """-r base.txt

# Producción
gunicorn>=21.2.0
psycopg2-binary>=2.9.0
redis>=4.6.0
"""
        
        requirements_files = {
            "requirements/base.txt": base_reqs,
            "requirements/development.txt": dev_reqs,
            "requirements/testing.txt": test_reqs,
            "requirements/production.txt": prod_reqs,
        }
        
        for file_path, content in requirements_files.items():
            full_path = self.root / file_path
            full_path.write_text(content)
            print(f"   ✓ {file_path}")
    
    def create_config_files(self):
        """Crear archivos de configuración"""
        print("⚙️  Creando archivos de configuración...")
        
        # settings.py
        settings_content = '''"""
Configuración principal del sistema PlantAdvisor TDF
"""
import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Configuración base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'plantas_fueguinas_2025_dev'
    DEBUG = False
    TESTING = False
    
    # Flask configuración
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')
    
    # PlantAdvisor configuración
    MAX_RECOMMENDATIONS = 3
    CONFIDENCE_THRESHOLD = 10
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = os.environ.get('LOG_FILE', 'logs/plantadvisor.log')

class DevelopmentConfig(Config):
    """Configuración de desarrollo"""
    DEBUG = True
    FLASK_ENV = 'development'
    LOG_LEVEL = 'DEBUG'

class TestingConfig(Config):
    """Configuración de testing"""
    TESTING = True
    SECRET_KEY = 'testing_key'
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Configuración de producción"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY debe estar definida en producción")

# Configuración por ambiente
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
'''
        
        settings_file = self.root / "config" / "settings.py"
        settings_file.write_text(settings_content)
        print("   ✓ config/settings.py")
        
        # .env.example
        env_example = """# Variables de entorno para PlantAdvisor TDF
# Copiar a .env y configurar valores

# Flask
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
DEBUG=True

# Aplicación
MAX_RECOMMENDATIONS=3
CONFIDENCE_THRESHOLD=10

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/plantadvisor.log

# Base de datos (futuro)
# DATABASE_URL=sqlite:///plantadvisor.db

# Redis (futuro)  
# REDIS_URL=redis://localhost:6379

# Email (futuro)
# MAIL_SERVER=smtp.gmail.com
# MAIL_PORT=587
"""
        
        env_file = self.root / ".env.example"
        env_file.write_text(env_example)
        print("   ✓ .env.example")
    
    def create_basic_tests(self):
        """Crear tests básicos"""
        print("🧪 Creando tests básicos...")
        
        # conftest.py
        conftest_content = '''"""
Configuración de pytest para PlantAdvisor TDF
"""
import pytest
import sys
from pathlib import Path

# Agregar src al path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

@pytest.fixture
def app():
    """Fixture de la aplicación Flask"""
    from app import app
    app.config['TESTING'] = True
    return app

@pytest.fixture  
def client(app):
    """Cliente de testing"""
    return app.test_client()

@pytest.fixture
def expert_system():
    """Fixture del sistema experto"""
    from plant_advisor.expert_system import PlantExpertSystem
    return PlantExpertSystem()

@pytest.fixture
def sample_conditions():
    """Condiciones de ejemplo para testing"""
    return {
        "ubicacion": "interior",
        "luz_disponible": "escasa",
        "humedad_interior": "baja",
        "experiencia_usuario": "principiante",
        "mascotas_presentes": False,
        "espacio_disponible": "pequeño"
    }
'''
        
        conftest_file = self.root / "tests" / "conftest.py"
        conftest_file.write_text(conftest_content)
        print("   ✓ tests/conftest.py")
        
        # Test básico del sistema experto
        test_expert_content = '''"""
Tests unitarios para el sistema experto
"""
import pytest

class TestExpertSystem:
    """Tests del sistema experto principal"""
    
    def test_system_initialization(self, expert_system):
        """Test inicialización del sistema"""
        assert expert_system is not None
        assert len(expert_system.plantas) > 0
        
    def test_get_recommendation_basic(self, expert_system, sample_conditions):
        """Test recomendación básica"""
        result = expert_system.get_plant_recommendation(sample_conditions)
        
        assert result['success'] is True
        assert 'recomendaciones' in result
        assert len(result['recomendaciones']) <= 3
        
    def test_validate_conditions(self, expert_system):
        """Test validación de condiciones"""
        valid_conditions = {
            "ubicacion": "interior",
            "luz_disponible": "escasa", 
            "experiencia_usuario": "principiante"
        }
        
        validation = expert_system.validate_conditions(valid_conditions)
        assert validation['valid'] is True
        
    def test_invalid_conditions(self, expert_system):
        """Test condiciones inválidas"""
        invalid_conditions = {
            "ubicacion": "invalid_location"
        }
        
        validation = expert_system.validate_conditions(invalid_conditions)
        assert validation['valid'] is False
        assert len(validation['errors']) > 0
'''
        
        test_expert_file = self.root / "tests" / "unit" / "test_expert_system.py"
        test_expert_file.write_text(test_expert_content)
        print("   ✓ tests/unit/test_expert_system.py")
        
        # Test de API
        test_api_content = '''"""
Tests de integración para la API
"""
import json
import pytest

class TestAPI:
    """Tests de la API REST"""
    
    def test_health_endpoint(self, client):
        """Test endpoint de health"""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        
    def test_recommend_endpoint(self, client, sample_conditions):
        """Test endpoint de recomendaciones"""
        response = client.post('/api/recommend',
                              data=json.dumps(sample_conditions),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        
    def test_plants_list_endpoint(self, client):
        """Test endpoint lista de plantas"""
        response = client.get('/api/plants')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert 'plants' in data
        assert len(data['plants']) > 0
'''
        
        test_api_file = self.root / "tests" / "integration" / "test_api.py"
        test_api_file.write_text(test_api_content)
        print("   ✓ tests/integration/test_api.py")
    
    def create_additional_files(self):
        """Crear archivos adicionales profesionales"""
        print("📄 Creando archivos adicionales...")
        
        # .gitignore mejorado
        gitignore_content = """# PlantAdvisor TDF - Git ignore

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Database
*.db
*.sqlite
*.sqlite3

# Backup
backup_*/

# Temporary files
*.tmp
*.temp

# Flask
instance/
.webassets-cache

# Documentation builds
docs/_build/

# MyPy
.mypy_cache/
.dmypy.json
dmypy.json
"""
        
        gitignore_file = self.root / ".gitignore"
        gitignore_file.write_text(gitignore_content)
        print("   ✓ .gitignore")
        
        # CHANGELOG.md
        changelog_content = """# Changelog - PlantAdvisor TDF

Todas las mejoras notables de este proyecto serán documentadas aquí.

## [1.0.0] - 2025-06-23

### Agregado
- Sistema experto completo con 25 especies de plantas
- 5 especies nativas de Tierra del Fuego incluidas
- Interfaz web responsive con Bootstrap 5
- API REST completa con 6 endpoints
- Motor de inferencia híbrido (reglas + árbol de decisión)
- Galería de imágenes para todas las especies
- Sistema de demostración interactivo
- Documentación técnica completa
- Estructura de proyecto profesional
- Tests unitarios y de integración
- Configuración CI/CD

### Técnico
- Flask 2.3+ como framework web
- Python 3.9+ como versión mínima
- Arquitectura modular y escalable
- Configuración moderna con pyproject.toml
- Makefile con comandos automatizados
- Docker support incluido

### Especies Incluidas
- **Nativas TDF**: Lenga, Ñire, Calafate, Mata Negra, Coirón
- **Interior**: Sansevieria, ZZ Plant, Pothos, Ficus, Monstera, etc.
- **Comestibles**: Albahaca, Perejil, Orégano, Ciboulette
- **Exterior Adaptado**: Lavanda, Romero, Geranios, etc.
"""
        
        changelog_file = self.root / "CHANGELOG.md"
        changelog_file.write_text(changelog_content)
        print("   ✓ CHANGELOG.md")
    
    def create_start_script(self):
        """Crear script de inicio para desarrollo"""
        start_script_content = '''#!/usr/bin/env python3
"""
Script para iniciar PlantAdvisor TDF en modo desarrollo
"""
import os
import sys
from pathlib import Path

# Agregar src al path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

def main():
    """Función principal"""
    print("🌿 Iniciando PlantAdvisor TDF (Desarrollo)")
    print("📍 Sistema Experto para Plantas de Tierra del Fuego")
    print("🔧 Modo: Desarrollo con hot-reload")
    print("🌐 URL: http://localhost:5000")
    print("-" * 50)
    
    # Configurar variables de entorno
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'
    
    # Importar y ejecutar app
    try:
        from app import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except ImportError as e:
        print(f"❌ Error importando aplicación: {e}")
        print("💡 Verificar que la estructura esté migrada correctamente")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error ejecutando aplicación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''
        
        start_script_file = self.root / "scripts" / "start_dev.py"
        start_script_file.write_text(start_script_content)
        print("   ✓ scripts/start_dev.py")
    
    def run_migration(self):
        """Ejecutar migración completa"""
        print("🚀 Iniciando migración a estructura profesional...")
        print("=" * 60)
        
        try:
            self.backup_current_structure()
            self.create_directories()
            self.create_init_files()
            self.migrate_python_files()
            self.update_imports_in_files()
            self.create_requirements_files()
            self.create_config_files()
            self.create_basic_tests()
            self.create_additional_files()
            self.create_start_script()
            
            print("=" * 60)
            print("✅ Migración completada exitosamente!")
            print("🌿 PlantAdvisor TDF - Estructura Profesional")
            print()
            print("📋 Próximos pasos:")
            print("   1. Verificar funcionamiento: make run")
            print("   2. Ejecutar tests: make test")
            print("   3. Ver comandos: make help")
            print("   4. Desarrollo: make dev")
            print()
            print("💾 Backup disponible en: backup_old_structure/")
            
        except Exception as e:
            print(f"❌ Error durante migración: {e}")
            print("💾 Estructura original respaldada en: backup_old_structure/")
            sys.exit(1)


def main():
    """Función principal del script"""
    migrator = ProjectMigrator()
    migrator.run_migration()


if __name__ == "__main__":
    main()