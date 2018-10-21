import datetime

from django.db import models


class Promotion(models.Model):
    annee = models.CharField(default="2018-2019", max_length=255)
    numero = models.CharField(default=22, max_length=255)

    def __str__(self):
        return "Promotion " + self.numero + '(' + self.annee + ')'


class Etudiant(models.Model):
    nom = models.CharField(max_length=255, default="")
    promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=255, default="")
    avatar = models.FileField(default=None)
    email = models.CharField(max_length=255, default="")
    M = 'MASCULIN'
    F = 'FEMMININ'

    SEXE_CHOICES = (
        (M, 'Masculin'),
        (F, 'Femminin'),
    )
    sexe = models.CharField(
        max_length=8,
        choices=SEXE_CHOICES,
        default=M,
    )
    date_inscription = models.DateField(default=datetime.date.today)
    username = models.CharField(default="", max_length=255)
    password = models.CharField(max_length=255, default="")
    date_naissance = models.DateField(default=datetime.date.today)
    lieu_naissance = models.CharField(max_length=255, default="")
    pays = models.CharField(max_length=255, default="Vietnam")

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Enseignant(models.Model):
    nom = models.CharField(max_length=255, default="")
    prenom = models.CharField(max_length=255, default="")
    avatar = models.FileField(default=None)
    email = models.CharField(max_length=255, default="")
    M = 'MASCULIN'
    F = 'FEMMININ'

    SEXE_CHOICES = (
        (M, 'Femminin'),
        (F, 'Masculin'),
    )
    sexe = models.CharField(
        max_length=8,
        choices=SEXE_CHOICES,
        default=M,
    )
    date_inscription = models.DateField(default=datetime.date.today)
    username = models.CharField(default="", max_length=255)
    password = models.CharField(max_length=255, default="")
    code_enseignant = models.CharField(default=0, max_length=255)

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Responsable(models.Model):
    nom = models.CharField(max_length=255, default="")
    prenom = models.CharField(max_length=255, default="")
    avatar = models.FileField(default=None)
    email = models.CharField(max_length=255, default="")

    M = 'MASCULIN'
    F = 'FEMMININ'

    SEXE_CHOICES = (
        (M, 'Femminin'),
        (F, 'Masculin'),
    )
    sexe = models.CharField(
        max_length=8,
        choices=SEXE_CHOICES,
        default=M,
    )
    date_inscription = models.DateField(default=datetime.date.today)
    username = models.CharField(default="", max_length=255)
    password = models.CharField(max_length=255, default="")
    code_responsable = models.CharField(default=0, max_length=255)

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Niveau(models.Model):
    intitule = models.CharField(max_length=1, default="1")

    def __str__(self):
        return ' Niveau ' + self.intitule


class Cycle(models.Model):
    intitule = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.intitule)


class Parcours(models.Model):
    responsable_id = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    niveau_id = models.ForeignKey(Niveau, on_delete=models.CASCADE)

    def __str__(self):
        return str(Cycle.objects.filter(id=self.cycle_id.pk).first()) + ' ' + str(
            Niveau.objects.filter(id=self.niveau_id.pk).first())


class Semestre(models.Model):
    numero = models.CharField(max_length=255, default=1)

    def __str__(self):
        return 'Semestre ' + self.numero


class Matiere(models.Model):
    semestre_id = models.ForeignKey(Semestre, on_delete=models.CASCADE, default=1)
    parcours_id = models.ForeignKey(Parcours, on_delete=models.CASCADE)
    enseignant_id = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    intitule = models.CharField(max_length=255, default="")
    credit = models.CharField(max_length=2, default="4")

    def __str__(self):
        return self.intitule + ' ' + Parcours.objects.filter(id=self.parcours_id.pk).first()


class Note(models.Model):
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere_id = models.ForeignKey(Matiere, on_delete=models.CASCADE)


class Relevee(models.Model):
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    parcours_id = models.ForeignKey(Parcours, on_delete=models.CASCADE)


class Admission(models.Model):
    parcours_id = models.ForeignKey(Parcours, on_delete=models.CASCADE)
    date_limite = models.DateField(default=datetime.date.today)
    annee = models.CharField(default="", max_length=4)

    def __str__(self):
        return 'Admission ' + Parcours.objects.filter(id=self.parcours_id.pk).first() + ' ' + self.annee


class Dossier(models.Model):
    admission_id = models.ForeignKey(Admission, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, default="")
    prenom = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    pays = models.CharField(max_length=255, default="")
    passport = models.FileField(default=None)
    photo = models.FileField(default=None)
    transcripts = models.FileField(default=None)
    diplomes = models.FileField(default=None)
    recommandations = models.FileField(default=None)
    password = models.CharField(default="", max_length=255)

    def __str__(self):
        return 'Dossier ' + self.nom + ' ' + Admission.objects.filter(id=self.admission_id.pk).first()
