#!/usr/bin/env bash

# remove_polyfill.sh
# Remove recursivamente a tag:
#   <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
# de todos os arquivos encontrados a partir do diretório de execução.

set -euo pipefail

TARGET='<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>'

# Contadores
found=0
modified=0
skipped=0

echo "Iniciando varredura em: $(pwd)"
echo "-------------------------------------------"

# Itera sobre todos os arquivos (exclui o próprio script para segurança)
SCRIPT_NAME="$(basename "$0")"

while IFS= read -r -d '' file; do
    # Pula o próprio script
    [[ "$(basename "$file")" == "$SCRIPT_NAME" ]] && continue

    # Verifica se o arquivo é de texto (evita binários)
    if ! file --mime-type "$file" 2>/dev/null | grep -qE 'text/|xml|html|javascript|json'; then
        ((skipped++)) || true
        continue
    fi

    ((found++)) || true

    # Verifica se contém a string alvo antes de tentar modificar
    if grep -qF "$TARGET" "$file" 2>/dev/null; then
        # Faz a substituição in-place usando um arquivo temporário (compatível com macOS e Linux)
        tmp=$(mktemp)
        if grep -vF "$TARGET" "$file" > "$tmp" && mv "$tmp" "$file"; then
            echo "[MODIFICADO] $file"
            ((modified++)) || true
        else
            rm -f "$tmp"
            echo "[ERRO]       $file — não foi possível modificar"
        fi
    fi

done < <(find . -type f -print0)

echo "-------------------------------------------"
echo "Arquivos de texto verificados : $found"
echo "Arquivos modificados          : $modified"
echo "Arquivos binários ignorados   : $skipped"
echo "Concluído."
