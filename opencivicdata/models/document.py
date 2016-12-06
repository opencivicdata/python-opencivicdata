from .base import OCDIDField, RelatedEntityBase, RelatedBase

class Document(OCDBase):
    identifier = models.CharField(max_length=100)
    title = models.TextField()
    classification = ArrayField(base_field=models.TextField(), blank=True, default=list)       subject = ArrayField(base_field=models.TextField(), blank=True, default=list)
 
    class Meta:
        abstract = True
   
class DocumentAbstract(RelatedBase):
    abstract = models.TextField()
    note = models.TextField(blank=True)
    date = models.TextField(max_length=10, blank=True)  # YYYY[-MM[-DD]]

    class Meta:
        abstract = True


class DocumentTitle(RelatedBase):
    title = models.TextField()
    note = models.TextField(blank=True)

    class Meta:
        abstract = True
    
class DocumentIdentifier(IdentifierBase):
    note = models.TextField(blank=True)

    class Meta:
        abstract = True

class DocumentAction(RelatedBase):
    description = models.TextField()
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    classification = ArrayField(base_field=models.TextField(), blank=True, default=list)     # enum
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        abstract = True

class RelatedDocument(RelatedBase):
    identifier = models.CharField(max_length=100)

    class Meta:
        abstract = True

class DocumentVersion(RelatedBase):
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]

    class Meta:
        abstract = True
