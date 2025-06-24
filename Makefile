# PlantAdvisor TDF - Makefile para automatización de tareas
# Sistema Experto para Recomendación de Plantas en Tierra del Fuego

.PHONY: help install install-dev test test-unit test-integration test-coverage
.PHONY: lint format check-format check-lint security run dev clean build
.PHONY: docs serve-docs deploy docker-build docker-run health-check

# Variables
PYTHON := python3
PIP := pip3
VENV := venv
SRC_DIR := src
TEST_DIR := tests
COVERAGE_MIN := 80

# Colores para output
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Mostrar este mensaje de ayuda
	@echo "$(GREEN)PlantAdvisor TDF - Sistema Experto para Plantas$(NC)"
	@echo "$(YELLOW)Comandos disponibles:$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# === INSTALACIÓN ===
install: ## Instalar dependencias base
	@echo "$(YELLOW)Instalando dependencias base...$(NC)"
	$(PIP) install -r requirements/base.txt
	@echo "$(GREEN)✓ Dependencias base instaladas$(NC)"

install-dev: ## Instalar dependencias de desarrollo
	@echo "$(YELLOW)Instalando dependencias de desarrollo...$(NC)"
	$(PIP) install -r requirements/development.txt
	$(PIP) install -e .
	pre-commit install
	@echo "$(GREEN)✓ Entorno de desarrollo configurado$(NC)"

install-test: ## Instalar dependencias de testing
	@echo "$(YELLOW)Instalando dependencias de testing...$(NC)"
	$(PIP) install -r requirements/testing.txt
	@echo "$(GREEN)✓ Dependencias de testing instaladas$(NC)"

venv: ## Crear entorno virtual
	@echo "$(YELLOW)Creando entorno virtual...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✓ Entorno virtual creado en ./$(VENV)$(NC)"
	@echo "$(YELLOW)Activar con: source $(VENV)/bin/activate$(NC)"

# === TESTING ===
test: ## Ejecutar todos los tests
	@echo "$(YELLOW)Ejecutando todos los tests...$(NC)"
	pytest $(TEST_DIR) -v
	@echo "$(GREEN)✓ Tests completados$(NC)"

test-unit: ## Ejecutar solo tests unitarios
	@echo "$(YELLOW)Ejecutando tests unitarios...$(NC)"
	pytest $(TEST_DIR)/unit -v -m "unit"
	@echo "$(GREEN)✓ Tests unitarios completados$(NC)"

test-integration: ## Ejecutar tests de integración
	@echo "$(YELLOW)Ejecutando tests de integración...$(NC)"
	pytest $(TEST_DIR)/integration -v -m "integration"
	@echo "$(GREEN)✓ Tests de integración completados$(NC)"

test-coverage: ## Ejecutar tests con coverage
	@echo "$(YELLOW)Ejecutando tests con coverage...$(NC)"
	pytest --cov=$(SRC_DIR) --cov-report=html --cov-report=term-missing --cov-fail-under=$(COVERAGE_MIN)
	@echo "$(GREEN)✓ Coverage report generado en htmlcov/$(NC)"

test-api: ## Ejecutar tests de API específicamente
	@echo "$(YELLOW)Ejecutando tests de API...$(NC)"
	pytest $(TEST_DIR) -v -m "api"
	@echo "$(GREEN)✓ Tests de API completados$(NC)"

# === CALIDAD DE CÓDIGO ===
lint: ## Ejecutar linting (flake8, mypy)
	@echo "$(YELLOW)Ejecutando linting...$(NC)"
	flake8 $(SRC_DIR) $(TEST_DIR)
	mypy $(SRC_DIR)
	@echo "$(GREEN)✓ Linting completado$(NC)"

format: ## Formatear código (black, isort)
	@echo "$(YELLOW)Formateando código...$(NC)"
	black $(SRC_DIR) $(TEST_DIR)
	isort $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)✓ Código formateado$(NC)"

check-format: ## Verificar formato sin cambiar archivos
	@echo "$(YELLOW)Verificando formato...$(NC)"
	black --check $(SRC_DIR) $(TEST_DIR)
	isort --check-only $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)✓ Formato verificado$(NC)"

check-lint: ## Verificar calidad sin fix automático
	@echo "$(YELLOW)Verificando calidad de código...$(NC)"
	flake8 $(SRC_DIR) $(TEST_DIR) --statistics
	mypy $(SRC_DIR) --strict
	@echo "$(GREEN)✓ Calidad verificada$(NC)"

security: ## Ejecutar análisis de seguridad
	@echo "$(YELLOW)Ejecutando análisis de seguridad...$(NC)"
	safety check
	bandit -r $(SRC_DIR)
	@echo "$(GREEN)✓ Análisis de seguridad completado$(NC)"

# === EJECUCIÓN ===
run: ## Ejecutar aplicación en modo producción
	@echo "$(YELLOW)Iniciando PlantAdvisor TDF...$(NC)"
	@echo "$(GREEN)🌿 Sistema Experto para Plantas de Tierra del Fuego$(NC)"
	@echo "$(YELLOW)Acceder en: http://localhost:5000$(NC)"
	$(PYTHON) $(SRC_DIR)/app.py

dev: ## Ejecutar aplicación en modo desarrollo
	@echo "$(YELLOW)Iniciando PlantAdvisor TDF (modo desarrollo)...$(NC)"
	@echo "$(GREEN)🌿 Sistema Experto - Modo Desarrollo$(NC)"
	@echo "$(YELLOW)Acceder en: http://localhost:5000$(NC)"
	@echo "$(YELLOW)Hot-reload activado$(NC)"
	$(PYTHON) scripts/start_dev.py

serve: ## Servidor con auto-reload para desarrollo
	@echo "$(YELLOW)Iniciando servidor de desarrollo...$(NC)"
	FLASK_ENV=development FLASK_DEBUG=1 $(PYTHON) -m flask --app $(SRC_DIR)/app.py run --host=0.0.0.0 --port=5000

# === UTILIDADES ===
clean: ## Limpiar archivos temporales y cache
	@echo "$(YELLOW)Limpiando archivos temporales...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	@echo "$(GREEN)✓ Archivos temporales eliminados$(NC)"

build: ## Construir paquete para distribución
	@echo "$(YELLOW)Construyendo paquete...$(NC)"
	$(PYTHON) -m build
	@echo "$(GREEN)✓ Paquete construido en dist/$(NC)"

install-package: build ## Instalar paquete localmente
	@echo "$(YELLOW)Instalando paquete localmente...$(NC)"
	$(PIP) install dist/*.whl
	@echo "$(GREEN)✓ Paquete instalado$(NC)"

# === DOCUMENTACIÓN ===
docs: ## Generar documentación
	@echo "$(YELLOW)Generando documentación...$(NC)"
	sphinx-build -b html docs/ docs/_build/html
	@echo "$(GREEN)✓ Documentación generada en docs/_build/html$(NC)"

serve-docs: docs ## Servir documentación localmente
	@echo "$(YELLOW)Sirviendo documentación en http://localhost:8000$(NC)"
	cd docs/_build/html && $(PYTHON) -m http.server 8000

# === DOCKER ===
docker-build: ## Construir imagen Docker
	@echo "$(YELLOW)Construyendo imagen Docker...$(NC)"
	docker build -t plantadvisor-tdf:latest .
	@echo "$(GREEN)✓ Imagen Docker construida$(NC)"

docker-run: ## Ejecutar contenedor Docker
	@echo "$(YELLOW)Ejecutando contenedor Docker...$(NC)"
	docker run -p 5000:5000 --name plantadvisor-tdf plantadvisor-tdf:latest

docker-compose-up: ## Levantar stack completo con docker-compose
	@echo "$(YELLOW)Levantando stack con docker-compose...$(NC)"
	docker-compose -f deployment/docker-compose.yml up -d
	@echo "$(GREEN)✓ Stack levantado$(NC)"

# === HEALTH CHECKS ===
health-check: ## Verificar estado del sistema
	@echo "$(YELLOW)Verificando estado del sistema...$(NC)"
	curl -f http://localhost:5000/health || echo "$(RED)Sistema no responde$(NC)"
	@echo "$(GREEN)✓ Health check completado$(NC)"

status: ## Mostrar estado actual del proyecto
	@echo "$(GREEN)=== PlantAdvisor TDF - Estado del Proyecto ===$(NC)"
	@echo "$(YELLOW)Python version:$(NC) $(shell $(PYTHON) --version)"
	@echo "$(YELLOW)Pip version:$(NC) $(shell $(PIP) --version)"
	@echo "$(YELLOW)Virtual env:$(NC) $(VIRTUAL_ENV)"
	@echo "$(YELLOW)Git branch:$(NC) $(shell git branch --show-current 2>/dev/null || echo 'No git')"
	@echo "$(YELLOW)Git status:$(NC)"
	@git status --porcelain 2>/dev/null || echo "No git repository"
	@echo "$(YELLOW)Tests status:$(NC)"
	@pytest --collect-only -q $(TEST_DIR) 2>/dev/null | tail -1 || echo "Tests no configurados"

# === MIGRACIÓN ===
migrate-structure: ## Migrar proyecto a nueva estructura
	@echo "$(YELLOW)Migrando a estructura profesional...$(NC)"
	$(PYTHON) scripts/migrate_structure.py
	@echo "$(GREEN)✓ Estructura migrada$(NC)"

# === CI/CD ===
ci: install-dev check-format check-lint test-coverage ## Pipeline completo CI/CD
	@echo "$(GREEN)✓ Pipeline CI/CD completado exitosamente$(NC)"

pre-commit: format lint test-unit ## Verificaciones pre-commit
	@echo "$(GREEN)✓ Pre-commit checks completados$(NC)"

# === QUICK SETUP ===
quick-setup: venv install-dev ## Setup rápido completo
	@echo "$(GREEN)🌿 PlantAdvisor TDF configurado exitosamente!$(NC)"
	@echo "$(YELLOW)Próximos pasos:$(NC)"
	@echo "  1. Activar entorno: source $(VENV)/bin/activate"
	@echo "  2. Ejecutar: make dev"
	@echo "  3. Abrir: http://localhost:5000"

# === INFORMACIÓN ===
info: ## Mostrar información del proyecto
	@echo "$(GREEN)🌿 PlantAdvisor TDF - Sistema Experto$(NC)"
	@echo "$(YELLOW)Descripción:$(NC) Sistema de recomendación de plantas para Tierra del Fuego"
	@echo "$(YELLOW)Versión:$(NC) 1.0.0"
	@echo "$(YELLOW)Autor:$(NC) Gaston Schvartz"
	@echo "$(YELLOW)Plantas incluidas:$(NC) 25 especies (5 nativas de TDF)"
	@echo "$(YELLOW)Tecnologías:$(NC) Python, Flask, Sistema Experto híbrido"
	@echo "$(YELLOW)Ejecutar 'make help' para ver todos los comandos$(NC)"