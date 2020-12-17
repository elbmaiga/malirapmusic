from django.db import models

# Create your models here.

class Category(models.Model):
    ALBUMS = "ALBUMS"
    SINGLES = "SINGLES"
    VIDEOS = "VIDEOS"
    ACTU_BUZZ = "ACTU BUZZ"
    OTHERS = "OTHERS"
    CATEGORY = [
        ("Actu Buzz", ACTU_BUZZ),
        ("Albums", ALBUMS),
        ("Singles", SINGLES),
        ("Videos", VIDEOS),
        ("Others", OTHERS)
    ]

    fields = models.CharField("Category fields", max_length=100, choices=CATEGORY, unique=True)

    def __str__(self):
        return self.fields

class File_Uploaded(models.Model):
    MP3 = "MP3"
    MP4 = "MP4"
    WAV = "WAV"
    AAC = "AAC"
    PDF = "PDF"
    OTHERS = "OTHERS"
    FILE_TYPE = [
        ("mp3", MP3),
        ("mp4", MP4),
        ("wav", WAV),
        ("aac", AAC),
        ("pdf", PDF),
        ("others", OTHERS)
    ]
    url = models.FileField(upload_to="libraries/")
    type_file = models.CharField("Type File", choices=FILE_TYPE, max_length=10)
    created_at = models.DateTimeField("Created At", auto_now=True)

    def __str__(self):
        return self.url.path

class Articles(models.Model):
    title = models.CharField("Title", max_length=255)
    category = models.ManyToManyField(Category)
    slug = models.SlugField("Slug", max_length=255, unique=True)
    content = models.TextField("Content", default="N/A", blank=True)
    cover = models.ImageField(upload_to="libraries/")
    media = models.ManyToManyField(File_Uploaded, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    views = models.IntegerField("Views number", default=0)
    download = models.IntegerField("Download number", default=0)
    is_in_pub = models.BooleanField("Is in pub", default=False)

    def __str__(self):
        return self.title

class Galleries(models.Model):
    title = models.CharField("Title", max_length=255, blank=True)
    file = models.ImageField(upload_to="gallery/")
    views = models.IntegerField("Views number", default=0)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    def __str__(self):
        if self.title:
            return self.title
        else: return self.file.url