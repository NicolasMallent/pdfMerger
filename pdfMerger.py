#!/usr/bin/env python

import sys
import argparse

# Vérifier la version de Python
python_version = sys.version_info[:2]

if python_version <= (3, 6):
    from PyPDF2 import PdfFileMerger
    def concatener_pdfs(fichiers_pdf, sortie_pdf):
        merger = PdfFileMerger()
        for fichier in fichiers_pdf:
            merger.append(fichier)
        merger.write(sortie_pdf)
        merger.close()
        print(f"Fichier {sortie_pdf} généré avec succès.")

else:  # Python 3.7 ou plus → Utilisation de pypdf avec PdfWriter
    from pypdf import PdfWriter

    def concatener_pdfs(fichiers_pdf, sortie_pdf):
        writer = PdfWriter()
        for fichier in fichiers_pdf:
            writer.append(fichier) 
        writer.write(sortie_pdf)
        writer.close()
        print(f"Fichier {sortie_pdf} généré avec succès.")

def main():
    parser = argparse.ArgumentParser(description="Concaténer plusieurs fichiers PDF en un seul.")
    parser.add_argument("fichiers", nargs="+", help="Liste des fichiers PDF à concaténer (au moins 2)")
    parser.add_argument("-o", "--output", default="merged.pdf", help="Nom du fichier PDF de sortie")

    args = parser.parse_args()

    if len(args.fichiers) < 2:
        print("Erreur : Il faut au moins deux fichiers PDF en entrée.", file=sys.stderr)
        sys.exit(1)
    concatener_pdfs(args.fichiers, args.output)

if __name__ == '__main__':
    main()