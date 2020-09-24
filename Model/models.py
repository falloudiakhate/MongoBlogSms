from djongo import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    telephone = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    promo = models.CharField(max_length=50)
    genie = models.CharField(max_length=50)
    entreprise_actuelle = models.CharField(max_length=50, blank=True, null=True, default="Aucun")
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    

class MetaDataPublication(models.Model):
    titre = models.CharField(max_length=50)
    date_pub = models.DateTimeField(default=timezone.now)
    pub_url = models.URLField(max_length=200)
    image_pub = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    contenu_pub = models.TextField()
    
    class Meta:
        abstract = True
        
    def __str__(self):
            return self.titre
        
class Commentaire(models.Model):
    contenu_com = models.TextField()
    date_com = models.DateTimeField(default=timezone.now)
    author_com_username = models.CharField(max_length=50 , blank=True, null=True)
    photo_com = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    

    

    
    class Meta:
        abstract = True
        
    def __str__(self):
            return self.contenu
        
class Tag(models.Model):
    nombre_j_aime = models.IntegerField()
    nombre_j_aime_pas = models.IntegerField()
    
    class Meta:
        abstract = True
        
    def __str__(self):
            return self.nombre_j_aime
        
        

class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    class Meta:
        abstract = True
        
    def __str__(self):
            return self.nom




class Publication(models.Model):
    
    meta_data_publication= models.EmbeddedField(
        model_container=MetaDataPublication,
    )
    
    author_pub_username = models.CharField(max_length=50 , blank=True, null=True)
    photo_pub = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    

    
    commentaire = models.EmbeddedField(
        model_container=Commentaire,
    )
    
    tag = models.EmbeddedField(
        model_container=Tag,
    )
    
    categorie = models.EmbeddedField(
        model_container=Categorie,
    )


class MetaDataMessage(models.Model):
    date_sms = models.DateTimeField(default=timezone.now, blank=True, null=True)
    image_sms = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None, null=True,
                                  blank=True)

    contenu_sms = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True


class Message(models.Model):
    date_sms = models.DateTimeField(default=timezone.now)
    image_sms = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None, null=True,
                                  blank=True)
    contenu_sms = models.CharField(max_length=500)
    author_sms_username = models.CharField(max_length=50)
    recepteur_sms_username = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.contenu_sms


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['date_sms', 'image_sms', "contenu_sms", "author_sms_username", 'recepteur_sms_username']

class Statut(models.Model):
    date_statut = models.DateTimeField(default=timezone.now)
    image_statut = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    contenu_statut = models.CharField(max_length=100)
    author_statut_username = models.CharField(max_length=50)

class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = "__all__"
        
        
        

class Post(models.Model):
    catgs = (
        ("Réalisations","réalisations"),
        ("Carrière","carrière"),
        ("Activités","activités")
    )
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    photo = models.ImageField(upload_to="posts/")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Author,related_name="like")
    categorie = models.CharField(max_length=15,choices=catgs,null=True)

    def __str__(self):
        return self.author.user.username

    def total_likes(self):
        return self.likes.count()
    
class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_content = models.TextField()
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
