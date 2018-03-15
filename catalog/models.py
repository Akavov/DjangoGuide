from django.db import models

# Create your models here.
class MyModelName(models.Model):
    """
    A typical class defining a model, deriver from the Model class
    """

    #Fields
    my_field_name=models.CharField(max_length=20,help_text="Enter field documentation")

    #Metadata
    class Meta:
        ordering=["-my_field_name"]

    #Methods
    def get_absolute_url(self):
        """
        Return the url to access a particular instance of MyModelName
        """

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc)
        """
        return self.field_name
