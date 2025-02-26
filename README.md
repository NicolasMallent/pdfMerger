# pdfMerger
Outil pour concatener/merger des fichiers PDF

## Linux
### Setup
```
# Check python version
python3 --version

# Si python <= 3.6
pip install "PyPDF2<2.0"

# Si python >= 3.7
pip install pypdf
```

### How to use it
```
python3 ./pdfMerger.py fichier1 fichier2 ... [-o nom_du_fichier] 
```

Vous pouvez renseigner le fichier de sorti avec l'option `-o nom_du_fichier` 

## Windows