import os
from pathlib import Path

# Configuración de las rutas
# Cambia esta ruta si tu carpeta de imágenes se llama de otra forma
CARPERTA_IMAGENES = "assets/images/Cubos"
RUTA_WEB_IMAGENES = "/assets/images/Cubos"

def generar_yaml_cubos():
    if not os.path.exists(CARPERTA_IMAGENES):
        print(f"Error: No se encontró la carpeta '{CARPERTA_IMAGENES}'")
        print("Asegúrate de que la ruta sea correcta o edita el script.")
        return

    # Extensiones de imagen válidas
    extensiones_validas = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    
    lineas_yaml = []
    
    # Listar y ordenar los archivos para que salgan en orden alfábetico
    archivos = sorted(os.listdir(CARPERTA_IMAGENES))
    
    for archivo in archivos:
        path_archivo = Path(archivo)
        if path_archivo.suffix.lower() in extensiones_validas:
            # 1. Obtener el nombre sin la extensión (.jpg, .png, etc.)
            nombre_limpio = path_archivo.stem
            
            # 2. Hacer el nombre más legible (reemplazar guiones/guiones bajos por espacios)
            # Ejemplo: "megaminx_shengshou" -> "Megaminx Shengshou"
            nombre_legible = nombre_limpio.replace('_', ' ').replace('-', ' ').title()
            
            # 3. Construir la ruta que usará la web
            ruta_imagen_web = f"{RUTA_WEB_IMAGENES}/{archivo}"
            
            # 4. Generar la estructura YAML vacía
            bloque_cubo = (
                f"- name_es: \"{nombre_legible}\"\n"
                f"  name_en: \"{nombre_legible}\"\n"
                f"  desc_es: \"\"\n"
                f"  desc_en: \"\"\n"
                f"  image: \"{ruta_imagen_web}\"\n"
            )
            lineas_yaml.append(bloque_cubo)
            
    # Guardar el resultado o mostrarlo por pantalla
    if lineas_yaml:
        # Crea la carpeta _data si no existe
        os.makedirs("_data", exist_ok=True)
        
        with open("_data/cubos.yml", "w", encoding="utf-8") as f:
            f.write("\n".join(lineas_yaml))
            
        print(f"¡Hecho! Se han procesado {len(lineas_yaml)} cubos.")
        print("El archivo se ha guardado automáticamente en '_data/cubos.yml'")
    else:
        print(f"No se encontraron imágenes válidas en '{CARPERTA_IMAGENES}'")

if __name__ == "__main__":
    generar_yaml_cubos()