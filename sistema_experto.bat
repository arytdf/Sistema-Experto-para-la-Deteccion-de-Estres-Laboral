@echo off
setlocal enabledelayedexpansion

:: ───────── Directorio base (donde vive este .bat) ─────────
set "BASE=%~dp0"
pushd "%BASE%"

:: ───────── Verificar Python ─────────
python --version >nul 2>&1 || (
    echo Error: Python no esta en el PATH. Instálalo desde https://python.org
    pause
    goto :EOF
)

:: ───────── Crear venv si falta ──────
if not exist "venv\" (
    echo Creando entorno virtual...
    python -m venv venv
)

:: ───────── Activar venv y actualizar pip ──────
call "%BASE%venv\Scripts\activate.bat"
python -m pip install --quiet --upgrade pip

echo.
echo ─── Verificando dependencias ───

:: Streamlit
pip show streamlit >nul 2>&1 || (
    echo Instalando Streamlit...
    pip install --quiet streamlit
)

:: PyYAML
pip show pyyaml >nul 2>&1 || (
    echo Instalando PyYAML...
    pip install --quiet pyyaml
)

:: ReportLab (PDF)
pip show reportlab >nul 2>&1 || (
    echo Instalando ReportLab...
    pip install --quiet reportlab
)

echo Dependencias OK.
echo.

:: ───────── Regenerar reglas.json si corresponde ─────────
if not exist "data\reglas.json" (
    echo Creando data\reglas.json desde data\reglas.yml...
    python "%BASE%data\generate_json.py"
) else (
    for %%F in ("data\reglas.yml") do (
        if %%~tF GTR %%~t"data\reglas.json" (
            echo reglas.yml mas nuevo. Regenerando reglas.json...
            python "%BASE%data\generate_json.py"
        )
    )
)

:: ───────── Lanzar la app ─────────
echo Iniciando la aplicacion...
streamlit run "%BASE%app.py"

pause
popd
endlocal


