#!/usr/bin/env bash
set -e

rm -f Prajeesh_Ag_CV.yaml
uv run python scripts/create_publication_list.py
uv run rendercv render Prajeesh_Ag_CV.yaml
mv rendercv_output/Prajeesh_Ag_CV.pdf Prajeesh_Ag_CV.pdf
