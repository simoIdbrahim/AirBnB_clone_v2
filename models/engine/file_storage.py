#!/usr/bin/python3
"""Ce module définit une classe pour gérer le stockage de fichiers pour le clone hbnb"""
import json


class FileStorage:
    """Cette classe gère le stockage des modèles hbnb au format JSON"""

    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """Retourne un dictionnaire des modèles actuellement en stockage"""

        return FileStorage.__objects

    def new(self, obj):
        """Ajoute un nouvel objet au dictionnaire de stockage"""

        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Enregistre le dictionnaire de stockage dans un fichier"""

        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)

            for keyword, value in temp.items():
                temp[keyword] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Charge le dictionnaire de stockage à partir du fichier"""
        from models.base_model import BaseModel
        from models.review import Review
        from models.place import Place
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        
        avilable = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for keyword, value in temp.items():
                        self.all()[keyword] = avilable[value['__class__']](**value)
        except FileNotFoundError:
            pass
