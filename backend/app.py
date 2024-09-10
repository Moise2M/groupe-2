from fastapi import FastAPI

app = FastAPI()


print("API Loaded")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


#mon code 

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()




UPLOAD_FOLDER = "path/to/the/upload/directory"

@app.get("/download/{filename}")
# permet de definir le endpoint pour accedder a cette resource (en bas)
async def download_file(filename: str):
    #cette fonction est une fonction asynchrone qui permet de servir un fichier via un endpoint GET (donc GET /download/filename)
    #donc le parametre filename est le nom du fichier definit dans la requete ({filename}()
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    # c'est le chemin absolute pour acceder au fichier en combinant le répertoire de téléchargement (UPLOAD_FOLDER)
    # avec le nom du fichier (filename)

    # Vérifiez si le fichier existe
    if os.path.exists(file_path):
        #si le fichier os.path..join(UPLOAD_FOLDER, filename) existe: execute l'instruction en bas 
        return FileResponse(file_path, media_type='application/octet-stream', filename=filename)
        #FileResponse est une classe de réponse fournie par FastAPI pour envoyer des fichiers
        #Parametre file_path: obligatiore permet de sepcifier le chemin ver l'image
        #Parametre media_type: facultatif Définit le type MIME du fichier. Le type MIME informe le client (navigateur ou autre client HTTP) du type de contenu qu'il doit s'attendre à recevoir.
        #Valeur application/octet-stream : Ce type MIME générique est utilisé pour indiquer que le fichier est un flux binaire (généralement utilisé pour les fichiers téléchargés où le type spécifique n'est pas connu). Cela permet de forcer le téléchargement du fichier dans certains cas, plutôt que de l'afficher dans le navigateur.
        #filename (facultatif) : Spécifie le nom de fichier suggéré pour le téléchargement. Ce nom est celui que le client verra lorsqu'il téléchargera le fichier.
    else:
        return {"error": "File not found"}
    #Si le fichier n'existe pas, une réponse JSON est renvoyée avec un message d'erreur.

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)