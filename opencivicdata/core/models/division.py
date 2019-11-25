from django.db import models


class DivisionManager(models.Manager):
    def children_of(self, division_id, subtype=None, depth=1):
        query, n = Division.subtypes_from_id(division_id)
        q_objects = []

        # only get children
        if subtype:
            query["subtype{0}".format(n)] = subtype
        else:
            q_objects.append(~models.Q(**{"subtype{0}".format(n): ""}))
        q_objects.append(~models.Q(**{"subid{0}".format(n): ""}))

        # allow for depth wildcards
        n += depth

        # ensure final field is null
        q_objects.append(models.Q(**{"subtype{0}".format(n): ""}))
        q_objects.append(models.Q(**{"subid{0}".format(n): ""}))

        return self.filter(*q_objects, **query)

    def create(self, id, name, redirect=None):
        return super(DivisionManager, self).create(
            id=id, name=name, redirect=redirect, **Division.subtypes_from_id(id)[0]
        )


class Division(models.Model):
    """
    A political geography, which may have multiple boundaries over its lifetime.

    Types of divisions include, among others:
    * Governmental jurisdiction - A division that a government has jurisdiction over.
    (e.g. North Carolina)
    * Political district - A division that elects a representative to a legislature.
    (e.g. North Carolina Congressional District 4)
    * Service zone - An area to which a government provides a service.
    (e.g. Washington DC Police District 105)
    """

    objects = DivisionManager()

    id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300, help_text="The name of the division.")
    # cascade is SET_NULL, will un-redirect if deletion happens
    redirect = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    country = models.CharField(
        max_length=2,
        help_text="An ISO-3166-1 alpha-2 code identifying the county where this division is found.",
    )

    # up to 7 pieces of the id that are searchable
    subtype1 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The first subtype in the unique identifier.",
    )
    subid1 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The first subidentifier in the unique identifer.",
    )
    subtype2 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The second subtype in the unique identifier.",
    )
    subid2 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The second subidentifier in the unique identifer.",
    )
    subtype3 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The third subtype in the unique identifier.",
    )
    subid3 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The third subidentifier in the unique identifer.",
    )
    subtype4 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The fourth subtype in the unique identifier.",
    )
    subid4 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The fourth subidentifier in the unique identifer.",
    )
    subtype5 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The fifth subtype in the unique identifier.",
    )
    subid5 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The fifth subidentifier in the unique identifer.",
    )
    subtype6 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The sixth subtype in the unique identifier.",
    )
    subid6 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The sixth subidentifier in the unique identifer.",
    )
    subtype7 = models.CharField(
        max_length=50,
        blank=True,
        help_text="The seventh subtype in the unique identifier.",
    )
    subid7 = models.CharField(
        max_length=100,
        blank=True,
        help_text="The seventh subidentifier in the unique identifer.",
    )

    class Meta:
        db_table = "opencivicdata_division"

    def __str__(self):
        return "{0} ({1})".format(self.name, self.id)

    @staticmethod
    def subtypes_from_id(division_id):
        pieces = [piece.split(":", 1) for piece in division_id.split("/")]
        fields = {}

        # if it included the ocd-division bit, pop it off
        if pieces[0] == ["ocd-division"]:
            pieces.pop(0)

        if pieces[0][0] != "country":
            raise ValueError("OCD id must start with country")

        fields["country"] = pieces[0][1]

        # add the remaining pieces
        n = 1
        for stype, subid in pieces[1:]:
            fields["subtype{0}".format(n)] = stype
            fields["subid{0}".format(n)] = subid
            n += 1

        return fields, n
