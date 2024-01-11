from pyrogram import Client, filters
from pyrogram.types import Message
import os

# Créez une instance de client avec votre propre token de bot et votre nom d'utilisateur
app = Client("my_account", bot_token="6863934525:AAHIQuoW7MbumOZzLz8MkK109DW2SLRdZAs", api_id="29022005", api_hash="bfd616932410d155a39403b4fac5884b")

# Filtre pour les messages contenant des documents
@app.on_message(filters.document)
async def rename_doc(client: Client, message: Message):
    # Vérifiez si la taille du fichier est inférieure à 2 Go (2 * 1024 * 1024 * 1024 octets)
    if message.document.file_size <= 2 * 1024 * 1024 * 1024:
        # Téléchargez le fichier
        file_path = await message.download()
        
        # Renommez le fichier (ajoutez votre propre logique de renommage ici)
        new_file_path = os.path.join(os.path.dirname(file_path), "new_name" + os.path.splitext(file_path)[1])
        os.rename(file_path, new_file_path)
        
        # Envoyez le fichier renommé
        await message.reply_document(new_file_path)
        
        # Supprimez le fichier renommé du serveur local
        os.remove(new_file_path)

# Exécutez le client
app.run()
