#!/usr/bin/python3
"""Ce module définit une classe pour gérer le stockage de fichiers pour le clone hbnb."""
import json


class FileStorage:
    """Cette classe gère le stockage des modèles hbnb au format JSON."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Retourne un dictionnaire des modèles actuellement en stockage."""
        return FileStorage.__objects

    def new(self, obj):
        """Ajoute un nouvel objet au dictionnaire de stockage."""
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        self.all().update({key: obj})

    def save(self):
        """Enregistre le dictionnaire de stockage dans un fichier."""
        with open(FileStorage.__file_path, 'w') as file:
            temp = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(temp, file)

    def reload(self):
        """Charge le dictionnaire de stockage à partir du fichier."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as file:
                temp = json.load(file)
                FileStorage.__objects = {
                    key: classes[val['__class__']](**val) for key, val in temp.items()
                }
        except FileNotFoundError:
            pass
