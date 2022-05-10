from django.contrib.auth.models import User


from django.db import models

############################################################


class Daraja(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Daraja"

    def __str__(self):
        return self.title


class Unvon(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Unvon"

    def __str__(self):
        return self.title


class Fakultet(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Fakultet"

    def __str__(self):
        return self.title


class Kafedra(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Kafedra"

    def __str__(self):
        return self.title


############################################################


class FileType(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)

    class Meta:
        db_table = "File Type"

    def __str__(self):
        return self.title


class TeacherFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=f"file/")
    type = models.ForeignKey(FileType, on_delete=models.CASCADE, related_name="type")
    teacher_id = models.ForeignKey(
        "TeacherData", on_delete=models.CASCADE, related_name="teacher"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Teacher File"

    def __str__(self):
        return self.title


############################################################


class TeacherData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    informaton = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=f"images/user",
        max_length=255,
        default="Profile.png",
        blank=True,
        null=True,
    )

    daraja = models.ForeignKey(
        Daraja, on_delete=models.CASCADE, related_name="daraja", blank=True, null=True
    )
    unvon = models.ForeignKey(
        Unvon, on_delete=models.CASCADE, related_name="unvon", blank=True, null=True
    )
    fakultet = models.ForeignKey(
        Fakultet,
        on_delete=models.CASCADE,
        related_name="fakultet",
        blank=True,
        null=True,
    )
    kafedra = models.ForeignKey(
        Kafedra, on_delete=models.CASCADE, related_name="kafedra", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Teacher Data"

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.middle_name
