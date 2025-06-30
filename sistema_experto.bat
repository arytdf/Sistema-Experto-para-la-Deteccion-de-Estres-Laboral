@echo off
setlocal enabledelayedexpansion

set "BASE=%~dp0"
pushd "%BASE%"

python --version >nul 2>&1 || (
    echo Error: Python no estÃ¡ instalado o no estÃ¡ en el PATH.
    echo Instale Python desde https://python.org
    pause
    exit /b 1
)

if not exist "venv\" (
    echo Creando entorno virtual...
    python -m venv venv
)

call "%BASE%venv\Scripts\activate.bat"

echo Actualizando pip...
python -m pip install --quiet --upgrade pip

echo Instalando dependencias...
pip install --quiet -r "%BASE%requerimientos.txt"

echo Iniciando la aplicaciÃ³n...
streamlit run "%BASE%app.py"

popd
endlocal
