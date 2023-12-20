#!/usr/bin/python3
"""Ce module définit une classe pour gérer le stockage de fichiers pour le clone hbnb."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State



class FileStorage:
    """Cette classe gère le stockage des modèles hbnb au format JSON."""

    __objects = {}
    __file_path = 'file.json'

    def all(self, cls=None):
        """Retourne un dictionnaire des modèles actuellement en stockage.

        Args:
            cls (classe, optionnel): Si spécifié, filtre le résultat pour inclure
                uniquement les objets de la classe spécifiée.

        Returns:
            dict: Un dictionnaire contenant les objets en stockage.
        """

        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls and issubclass(cls, BaseModel):
                cls_dict = {k: v for k,
                            v in self.__objects.items() if isinstance(v, cls)}
                return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Ajoute un nouvel objet au dictionnaire de stockage."""

        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        self.all().update({key: obj})

    def save(self):
        """Enregistre le dictionnaire de stockage dans un fichier."""

        with open(FileStorage.__file_path, 'w') as f:
            instantane = {}
            instantane.update(FileStorage.__objects)
            for keyword, value in instantane.items():
                instantane[keyword] = value.to_dict()
            json.dump(instantane, f)

    def reload(self):
        """Charge le dictionnaire de stockage à partir du fichier."""

        avilables = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

        try:
            instantane = {}
            with open(FileStorage.__file_path, 'r') as f:
                instantane = json.load(f)
                for keyword, value in instantane.items():
                        self.all()[keyword] = avilables[value['__class__']](**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """
        Supprime obj de __objects s'il est présent - si obj est égal à None,
        la méthode ne doit rien faire.
        """

        if obj is None:
            return
        obj_to_del = f"{obj.__class__.__name__}.{obj.id}"

        try:
            del FileStorage.__objects[obj_to_del]
        except KeyboardInterrupt:
            pass
        except AttributeError:
            pass
        
