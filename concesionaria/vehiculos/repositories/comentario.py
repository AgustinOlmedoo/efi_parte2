from typing import List, Optional
from vehiculos.models import Comentario,Vehiculo

class ComentarioRepository:

    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()
    
        
    def get_by_id(self, id: int) -> Optional[Comentario]:
        try:
            return Comentario.objects.get(id=id)
        except Comentario.DoesNotExist:
            return None

    def filter(
        self,
        vehiculo: Optional[Vehiculo] = None,
        autor: Optional[str] = None,

    ) -> List[Comentario]:
        queryset = Comentario.objects.all()

        if vehiculo is not None:
            queryset = queryset.filter(vehiculo=vehiculo)  
        
        if autor is not None:
            queryset = queryset.filter(author=autor)  
        
        
        return list(queryset)


    def create(
        self,
        autor: str,
        vehiculo: Optional[Vehiculo],
        contenido: str,

    ) -> Comentario:
        return Comentario.objects.create(
            author=autor,
            vehiculo=vehiculo,
            contenido=contenido,
        )

    def delete(self, comentario: Comentario):
        return comentario.delete()

    def update(
        self,
        comentario: Comentario,
        autor: str,
        vehiculo: Optional[Vehiculo],
        contenido: str,


        ) -> Comentario:
                comentario.author = autor
                comentario.vehiculo = vehiculo
                comentario.contenido = contenido
                comentario.save()
                return comentario