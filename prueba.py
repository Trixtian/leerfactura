import fitz
import json

# Abre el archivo PDF en modo lectura binaria
with fitz.open(r"C:\Users\apsistemas1\Downloads\4105FV222012.pdf") as pdf_file:
    # Crea un diccionario para almacenar la información
    info_dict = {}

    

    # Recorre las páginas del documento para obtener información específica
    for page_num in range(pdf_file.page_count):
        page = pdf_file[page_num]

            # Extrae el texto de la página y agrega al diccionario
        text = page.get_text()
        text_lines = text.splitlines()
        text_dict = {}
        for i, line in enumerate(text_lines):
            text_dict[f'línea {i+1}'] = line
        info_dict[f'página {page_num + 1}'] = text_dict

        # Extrae las anotaciones de la página y agrega al diccionario
        annots = page.annots()
        annot_list = []
        for annot in annots:
            if annot.type[0] != 2:  # Excluye las imágenes
                annot_dict = {}
                annot_dict['texto'] = annot.info
                annot_dict['página'] = page_num + 1
                annot_dict['posición'] = annot.rect
                annot_list.append(annot_dict)
        info_dict[f'página {page_num + 1} anotaciones'] = annot_list

    # Escribe el diccionario en un archivo JSON
    with open('archivo.json', 'w', encoding="utf-8") as json_file:
        json.dump(info_dict, json_file, indent=4, ensure_ascii=False)