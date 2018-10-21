from django.contrib import admin

from .models import Admission
from .models import Cycle
from .models import Dossier
from .models import Enseignant
# Register your models here.
from .models import Etudiant
from .models import Matiere
from .models import Niveau
from .models import Note
from .models import Parcours
from .models import Responsable

admin.site.register(Etudiant)
admin.site.register(Admission)
admin.site.register(Dossier)
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Niveau)
admin.site.register(Parcours)
admin.site.register(Cycle)
admin.site.register(Responsable)
admin.site.register(Note)
