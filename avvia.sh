#!/bin/bash

echo "=========================================="
echo "  PRONOSTICI CALCIO - AVVIO AUTOMATICO"
echo "=========================================="
echo ""

# Vai nella directory corretta
cd "$(dirname "$0")"

# Controlla se esiste virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creazione ambiente virtuale..."
    python3 -m venv venv
    echo "✅ Ambiente creato!"
    echo ""
fi

# Attiva ambiente virtuale
echo "🔧 Attivazione ambiente..."
source venv/bin/activate

# Installa dipendenze se non presenti
if ! python -c "import flask" 2>/dev/null; then
    echo "📥 Installazione dipendenze (solo la prima volta)..."
    pip install --quiet Flask requests beautifulsoup4 flask-cors
    echo "✅ Dipendenze installate!"
    echo ""
fi

# Avvia backend
echo "🚀 Avvio backend con partite VERE da diretta.it..."
echo ""
python backend_scraper.py
