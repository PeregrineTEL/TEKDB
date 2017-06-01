# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.db.models import Q

class Queryable(models.Model):
    enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True, auto_now_add=True)
    modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True, auto_now=True)


    class Meta:
        abstract = True

    def get_query_json(self):
        return {
            'name': self.name(),
            'image': self.image(),
            'subtitle': self.subtitle(),
            'data': self.data(),
            'enteredbyname': self.enteredbyname,
            'enteredbydate': self.enteredbydate,
            'modifiedbyname': self.modifiedbyname,
            'modifiedbydate': self.modifiedbydate,
        }

    def save(self, *args, **kwargs):

        super(Queryable, self).save(*args, **kwargs)


class Lookupplanningunit(models.Model):
    planningunitid = models.IntegerField(db_column='PlanningUnitID', primary_key=True)  # Field name made lowercase.
    planningunitname = models.CharField(db_column='PlanningUnitName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupPlanningUnit'
        # app_label = 'LookupPlanningUnit'

    def get_name(self):
        return "%s" % (self.planningunitname)

    def __unicode__(self):
        return unicode('%s' % (self.get_name()))

    def __str__(self):
        return self.get_name()


class Lookuptribe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tribeunit = models.CharField(db_column='TribeUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tribe = models.CharField(db_column='Tribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    federaltribe = models.CharField(db_column='FederalTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupTribe'
        # app_label = 'LookupTribe'

    def get_name(self):
        return "%s: %s, %s" % (self.tribe, self.tribeunit, self.federaltribe)

    def __unicode__(self):
        return unicode('%s' % (self.get_name()))

    def __str__(self):
        return self.get_name()


PRIMARY_HABITAT_CHOICES  = [
    ('Coastal Marsh','Coastal Marsh'),
    ('Deep Canyon','Deep Canyon'),
    ('Hard-bottom >100m','Hard-bottom >100m'),
    ('Hard-bottom 0-100m','Hard-bottom 0-100m'),
    ('Offshore Reefs','Offshore Reefs'),
    ('Offshore Rock','Offshore Rock'),
    ('Rocky Intertidal','Rocky Intertidal'),
    ('Sandy Beach','Sandy Beach'),
    ('Soft-bottom >100m','Soft-bottom >100m'),
    ('Soft-bottom 0-100m','Soft-bottom 0-100m'),
    ('Tidal Flats','Tidal Flats'),
    ('Other','Other')
]

class Places(Queryable):
    placeid = models.AutoField(db_column='PlaceID', primary_key=True)  # Field name made lowercase.
    indigenousplacename = models.CharField(db_column='IndigenousPlaceName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    indigenousplacenamemeaning = models.CharField(db_column='IndigenousPlaceNameMeaning', max_length=255, blank=True, null=True, verbose_name='english translation')
    englishplacename = models.CharField(db_column='EnglishPlaceName', max_length=255, blank=True, null=True, verbose_name='english name')
    planningunitid = models.ForeignKey(Lookupplanningunit, db_column='PlanningUnitID', blank=True, null=True, verbose_name='planning unit')
    primaryhabitat = models.CharField(db_column='PrimaryHabitat', max_length=100, blank=True, null=True, choices=PRIMARY_HABITAT_CHOICES, verbose_name='primary habitat')
    tribeid = models.ForeignKey(Lookuptribe, db_column='TribeID', blank=True, null=True, verbose_name='tribe')
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Places'
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
        # app_label = 'Places'

    #TODO: Complex 'Q' query to search all relevant fields
    def keyword_search(keyword):
        return Places.objects.filter(Q(indigenousplacename__icontains=keyword) | Q(indigenousplacenamemeaning__icontains=keyword)| Q(englishplacename__icontains=keyword)| Q(primaryhabitat__icontains=keyword))

    #def keyword_search(keyword):
       #return Resources.objects.filter(commonname__icontains=keyword)  #UPDATE THIS

    def name(self):
        return self.englishplacename                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-map.png'  #UPDATE THIS

    def subtitle(self):
        return self.indigenousplacenamemeaning                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'english place name', 'value': self.englishplacename},
            {'key':'indigenous place name', 'value': self.indigenousplacename},
            {'key':'indigenous place name meaning', 'value': self.indigenousplacenamemeaning},
            {'key':'primary habitat', 'value': self.primaryhabitat}
        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'places'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.indigenousplacenamemeaning,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    def __unicode__(self):
        return unicode('%s' % (self.englishplacename))

    def __str__(self):
        return self.englishplacename


PART_USED_CHOICES = [
    ('Antler','Antler'),
    ('Bone','Bone'),
    ('Egg','Egg'),
    ('Feather','Feather'),
    ('Flower','Flower'),
    ('Meat','Meat'),
    ('Shell','Shell'),
    ('Tooth','Tooth'),
    ('Whisker','Whisker'),
]

SEASON_CHOICES = [
    ('All','All'),
    ('Spring','Spring'),
    ('Spring/Summer','Spring/Summer'),
    ('Summer','Summer'),
    ('Summer/Fall','Summer/Fall'),
    ('Fall','Fall'),
    ('Fall/Winter','Fall/Winter'),
    ('Winter','Winter'),
    ('Winter/Spring','Winter/Spring'),
]


class Resources(Queryable):
    resourceid = models.AutoField(db_column='ResourceID', primary_key=True)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=255, blank=True, null=True, unique=True)  # Field name made lowercase.
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specific = models.BooleanField(db_column='Specific', default=False)  # Field name made lowercase.
    resourceclassificationgroup = models.CharField(db_column='ResourceClassificationGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')  # Field name made lowercase.
    # enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    # enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    # modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    # modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Resources'
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
        # app_label = 'Resources'

    def __unicode__(self):
        return unicode('%s' % (self.commonname))

    def __str__(self):
        return self.commonname

    def keyword_search(keyword):
        return Resources.objects.filter(Q(commonname__icontains=keyword) | Q(genus__icontains=keyword)| Q(species__icontains=keyword))

    #def keyword_search(keyword):
       #return Resources.objects.filter(commonname__icontains=keyword)  #UPDATE THIS

    def name(self):
        return self.commonname                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-resource.png'  #UPDATE THIS

    def subtitle(self):
        return self.species                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'name', 'value': self.commonname},
            {'key':'indigenous name', 'value': self.indigenousname},
            {'key':'species', 'value': self.species},
            {'key':'genus', 'value': self.genus}
        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'resources'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.indigenousname,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }
    ################################


class Placesresourceevents(Queryable):
    placeresourceid = models.AutoField(db_column='PlaceResourceID', primary_key=True)  # Field name made lowercase.
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID')  # Field name made lowercase.
    resourceid = models.ForeignKey(Resources, db_column='ResourceID', verbose_name='resource')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    partused = models.CharField(db_column='PartUsed', max_length=255, blank=True, null=True, verbose_name='part used', choices=PART_USED_CHOICES)
    customaryuse = models.CharField(db_column='CustomaryUse', max_length=255, blank=True, null=True, verbose_name='customary use')
    barterresource = models.BooleanField(db_column='BarterResource', verbose_name='barter resource?', default=False)
    season = models.CharField(db_column='Season', max_length=255, blank=True, null=True, choices=SEASON_CHOICES)
    timing = models.CharField(db_column='Timing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    january = models.BooleanField(db_column='January', default=False)  # Field name made lowercase.
    february = models.BooleanField(db_column='February', default=False)  # Field name made lowercase.
    march = models.BooleanField(db_column='March', default=False)  # Field name made lowercase.
    april = models.BooleanField(db_column='April', default=False)  # Field name made lowercase.
    may = models.BooleanField(db_column='May', default=False)  # Field name made lowercase.
    june = models.BooleanField(db_column='June', default=False)  # Field name made lowercase.
    july = models.BooleanField(db_column='July', default=False)  # Field name made lowercase.
    august = models.BooleanField(db_column='August', default=False)  # Field name made lowercase.
    september = models.BooleanField(db_column='September', default=False)  # Field name made lowercase.
    october = models.BooleanField(db_column='October', default=False)  # Field name made lowercase.
    november = models.BooleanField(db_column='November', default=False)  # Field name made lowercase.
    december = models.BooleanField(db_column='December', default=False)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    islocked = models.BooleanField(db_column='IsLocked', verbose_name='locked?', default=False)
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PlacesResourceEvents'
        verbose_name = 'Place - Resource'
        verbose_name_plural = 'Places - Resources'
        # app_label = 'PlacesResourceEvents'

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs] #[19, 24, 350]

        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs]

        return Placesresourceevents.objects.filter(
            Q(resourceid__in=resource_loi) |
            Q(placeid__in=place_loi) |
            Q(relationshipdescription__icontains=keyword) |
            Q(partused__icontains=keyword) |
            Q(customaryuse__icontains=keyword) |
            Q(season__icontains=keyword) |
            Q(timing__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'part used', 'value': self.partused},
            {'key':'customary use', 'value': self.customaryuse},
            {'key':'season', 'value': self.season},
            {'key':'timing', 'value': self.timing}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Placesresourceevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Resourcesactivityevents(Queryable):
    resourceactivityid = models.AutoField(db_column='ResourceActivityID', primary_key=True)  # Field name made lowercase.
    placeresourceid = models.ForeignKey(Placesresourceevents, models.DO_NOTHING, db_column='PlaceResourceID')  # Field name made lowercase.
    relationshipdescription = models.TextField(db_column='RelationshipDescription', blank=True, null=True)  # Field name made lowercase.
    partused = models.CharField(db_column='PartUsed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activityshortdescription = models.CharField(db_column='ActivityShortDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activitylongdescription = models.TextField(db_column='ActivityLongDescription', blank=True, null=True)  # Field name made lowercase.
    participants = models.CharField(db_column='Participants', max_length=50, blank=True, null=True)  # Field name made lowercase.
    technique = models.CharField(db_column='Technique', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gear = models.CharField(db_column='Gear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customaryuse = models.CharField(db_column='CustomaryUse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timing = models.CharField(db_column='Timing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timingdescription = models.CharField(db_column='TimingDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    islocked = models.BooleanField(db_column='IsLocked', default=False, verbose_name='locked?')  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourcesActivityEvents'
        # app_label = 'ResourcesActivityEvents'

    def keyword_search(keyword):
        placeresource_qs = Placesresourceevents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs]

        return Resourcesactivityevents.objects.filter(Q(placeresourceid__in=placeresource_loi) | Q(relationshipdescription__icontains=keyword) | Q(partused__icontains=keyword) | Q(activityshortdescription__icontains=keyword) | Q(activitylongdescription__icontains=keyword) | Q(participants__icontains=keyword) | Q(technique__icontains=keyword) | Q(gear__icontains=keyword) | Q(customaryuse__icontains=keyword) | Q(timing__icontains=keyword) | Q(timingdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'part used', 'value': self.partused},
            {'key':'activity short description', 'value': self.activityshortdescription},
            {'key':'activity long description', 'value': self.activitylongdescription},
            {'key':'participants', 'value': self.participants},
            {'key':'technique', 'value': self.technique},
            {'key':'gear', 'value': self.gear},
            {'key':'customary use', 'value': self.customaryuse},
            {'key':'timing', 'value': self.timing},
            {'key':'timing description', 'value': self.timingdescription}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Resourcesactivityevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class People(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearborn = models.IntegerField(db_column='YearBorn', blank=True, null=True)  # Field name made lowercase.
    village = models.CharField(db_column='Village', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relationshiptootherpeople = models.TextField(db_column='RelationshipToOtherPeople', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'People'
        # app_label = 'People'

    def get_name(self):
        return "%s %s" % (self.firstname, self.lastname)

    def __unicode__(self):
        return unicode('%s' % (self.get_name()))

    def __str__(self):
        return self.get_name()


REFERENCE_TYPE_CHOICES = (
    ('Book', 'Book'),
    ('Edited Volume', 'Edited Volume'),
    ('Interview', 'Interview'),
    ('Other','Other')
)

class Citations(Queryable):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    referencetype = models.CharField(db_column='ReferenceType', max_length=255, verbose_name='reference type', choices=REFERENCE_TYPE_CHOICES)
    referencetext = models.CharField(db_column='ReferenceText', max_length=50, blank=True, null=True, verbose_name='description')
    authortype = models.CharField(db_column='AuthorType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authorprimary = models.CharField(db_column='AuthorPrimary', max_length=255, blank=True, null=True, verbose_name='primary author')
    authorsecondary = models.CharField(db_column='AuthorSecondary', max_length=255, blank=True, null=True, verbose_name='secondary author')
    intervieweeid = models.ForeignKey(People, db_column='IntervieweeID', related_name='interviewee', blank=True, null=True)  # Field name made lowercase.
    interviewerid = models.ForeignKey(People, db_column='InterviewerID', related_name='interviewer', blank=True, null=True)  # Field name made lowercase.
    placeofinterview = models.CharField(db_column='PlaceofInterview', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    seriestitle = models.CharField(db_column='SeriesTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seriesvolume = models.CharField(db_column='SeriesVolume', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serieseditor = models.CharField(db_column='SeriesEditor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=100, blank=True, null=True)  # Field name made lowercase.
    publishercity = models.CharField(db_column='PublisherCity', max_length=255, blank=True, null=True, verbose_name='city')
    preparedfor = models.CharField(db_column='PreparedFor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    # enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    # enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    # modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    # modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Citations'
        verbose_name = 'Citation'
        verbose_name_plural = 'Citations'
        # app_label = 'Citations'

    #TODO: Complex 'Q' query to search all relevant fields

    def keyword_search(keyword):
        return Citations.objects.filter(Q(referencetype__icontains=keyword) | Q(referencetext__icontains=keyword) | Q(title__icontains=keyword) | Q(authorprimary__icontains=keyword) | Q(seriestitle__icontains=keyword) | Q(publisher__icontains=keyword) | Q(placeofinterview__icontains=keyword) | Q(publishercity__icontains=keyword))

    #def keyword_search(keyword):
       #return Resources.objects.filter(commonname__icontains=keyword)  #UPDATE THIS

    def name(self):
        return self.referencetype                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-citation.png'  #UPDATE THIS

    def subtitle(self):
        return self.referencetext                             #UPDATE THIS


    def data(self):                                     #UPDATE THIS
        return [
            {'key':'reference type', 'value': self.referencetype},
            {'key':'reference text', 'value': self.referencetext},
            {'key':'title', 'value': self.title},
            {'key':'author type', 'value': self.authortype},
            {'key':'secondary author', 'value': self.authorsecondary},
            {'key':'year', 'value': self.year},
            {'key':'series volume', 'value': self.seriesvolume},
            {'key':'series title', 'value': self.seriestitle},
            {'key':'series editor', 'value': self.serieseditor},
            {'key':'place of interview', 'value': self.placeofinterview},
            {'key':'prepared for', 'value': self.preparedfor},
            {'key':'publisher', 'value': self.publisher},
            {'key':'publisher city', 'value': self.publishercity},
            {'key':'comments', 'value': self.comments},
            {'key':'primary author', 'value': self.authorprimary}
        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'citations'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.referencetext,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


    def get_name(self):
        if self.referencetype == 'Interview':
            try:
                interviewee = People.objects.get(pk=self.intervieweeid)
            except Exception as e:
                interviewee = 'Unknown Interviewee'
            return '[%s] %s (%d) - %d' % (self.referencetype, interviewee, self.year, self.pk)
        else:
            return '[%s] %s (%d) - %d' % (self.referencetype, self.title, self.year, self.pk)

    def __unicode__(self):
        return unicode('%s' % (self.get_name()))

    def __str__(self):
        return self.get_name()

    def save(self, *args, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        super(Citations, self).save(*args, **kwargs)


class Placescitationevents(Queryable):
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', primary_key=True, verbose_name='place')
    citationid = models.ForeignKey(Citations, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PlacesCitationEvents'
        verbose_name = 'Place - Citation'
        verbose_name_plural = 'Places - Citations'
        # app_label = 'PlacesCitationEvents'
        unique_together = (('placeid', 'citationid'),)

    def keyword_search(keyword):
        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs] #[19, 24, 350]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return Placescitationevents.objects.filter(Q(citationid__in=citation_loi) | Q(placeid__in=place_loi) | Q(relationshipdescription__icontains=keyword)| Q(pages__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.pages                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Placescitationevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Currentversion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    backendversion = models.IntegerField(db_column='BackendVersion', blank=True, null=True)  # Field name made lowercase.
    frontendversion = models.IntegerField(db_column='FrontendVersion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CurrentVersion'
        app_label = 'CurrentVersion'


LOCALITY_TYPE_CHOICES = [
    ('bay','bay'),
    ('beach','beach'),
    ('creek','creek'),
    ('estuary','estuary'),
    ('intertidal','intertidal'),
    ('lagoon','lagoon'),
    ('mainstem river','mainstem river'),
    ('offshore rocks','offshore rocks'),
    ('open ocean','open ocean'),
    ('river eddy','river eddy'),
    ('river mouth','river mouth'),
    ('side channel river','side channel river'),
    ('subtidal','subtidal')
]

class Locality(models.Model):
    localityid = models.AutoField(db_column='LocalityID', primary_key=True)  # Field name made lowercase.
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=255, blank=True, null=True, verbose_name='english name')
    indigenousname = models.CharField(db_column='IndigenousName', max_length=255, blank=True, null=True, verbose_name='indigenous name')
    localitytype = models.CharField(db_column='LocalityType', max_length=255, blank=True, null=True, choices=LOCALITY_TYPE_CHOICES, verbose_name='type')
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Locality'
        verbose_name = 'Locality'
        verbose_name_plural = 'Localities'
        # app_label = 'Locality'

    #TODO: Complex 'Q' query to search all relevant fields
    def keyword_search(keyword):
        return Locality.objects.filter(Q(englishname__icontains=keyword) | Q(indigenousname__icontains=keyword))

    #def keyword_search(keyword):
       #return Resources.objects.filter(commonname__icontains=keyword)  #UPDATE THIS

    def name(self):
        return self.englishname                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-map.png'  #UPDATE THIS

    def subtitle(self):
        return self.indigenousname                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'english name', 'value': self.englishname},
            {'key':'indigenous name', 'value': self.indigenousname},
            #{'key':'indigenous place name meaning', 'value': self.indigenousplacenamemeaning},
            {'key':'locality type', 'value': self.localitytype}
        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'locality'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.indigenousname,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Localitygisselections(models.Model):
    localityid = models.IntegerField(db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    localitylabel = models.CharField(db_column='LocalityLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefc = models.CharField(db_column='SourceFC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LocalityGISSelections'
        app_label = 'LocalityGISSelections'


class Localityplaceresourceevent(Queryable):
    placeresourceid = models.ForeignKey(Placesresourceevents, models.DO_NOTHING, db_column='PlaceResourceID', primary_key=True)  # Field name made lowercase.
    localityid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='LocalityID')  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LocalityPlaceResourceEvent'
        # app_label = 'LocalityPlaceResourceEvent'
        unique_together = (('placeresourceid', 'localityid'),)

    def keyword_search(keyword):
        locality_qs = Locality.keyword_search(keyword)
        locality_loi = [locality.pk for locality in locality_qs] #[19, 24, 350]

        placeresource_qs = Placesresourceevents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs]

        return Localityplaceresourceevent.objects.filter(Q(placeresourceid__in=placeresource_loi) | Q(localityid__in=locality_loi))


class Lookupactivity(models.Model):
    activity = models.CharField(db_column='Activity', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupActivity'
        app_label = 'LookupActivity'


class Lookupauthortype(models.Model):
    authortype = models.CharField(db_column='AuthorType', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupAuthorType'
        app_label = 'LookupAuthorType'


class Lookupcustomaryuse(models.Model):
    usedfor = models.CharField(db_column='UsedFor', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupCustomaryUse'
        app_label = 'LookupCustomaryUse'


class Lookuphabitat(models.Model):
    habitat = models.CharField(db_column='Habitat', primary_key=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupHabitat'
        app_label = 'LookupHabitat'


class Lookuplocalitytype(models.Model):
    localitytype = models.CharField(db_column='LocalityType', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupLocalityType'
        app_label = 'LookupLocalityType'


class Lookupmediatype(models.Model):
    mediatype = models.CharField(db_column='MediaType', primary_key=True, max_length=255)  # Field name made lowercase.
    mediacategory = models.CharField(db_column='MediaCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupMediaType'
        app_label = 'LookupMediaType'


class Lookuppartused(models.Model):
    partused = models.CharField(db_column='PartUsed', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupPartUsed'
        app_label = 'LookupPartUsed'


class Lookupparticipants(models.Model):
    participants = models.CharField(db_column='Participants', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupParticipants'
        app_label = 'LookupParticipants'


class Lookupreferencetype(models.Model):
    documenttype = models.CharField(db_column='DocumentType', primary_key=True, max_length=25)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupReferenceType'
        app_label = 'LookupReferenceType'


class Lookupresourcegroup(models.Model):
    resourceclassificationgroup = models.CharField(db_column='ResourceClassificationGroup', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupResourceGroup'
        app_label = 'LookupResourceGroup'


class Lookupseason(models.Model):
    season = models.CharField(db_column='Season', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupSeason'
        app_label = 'LookupSeason'


class Lookuptechniques(models.Model):
    techniques = models.CharField(db_column='Techniques', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupTechniques'
        app_label = 'LookupTechniques'


class Lookuptiming(models.Model):
    timing = models.CharField(db_column='Timing', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupTiming'
        app_label = 'LookupTiming'


class Lookupuserinfo(models.Model):
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usingcustomusername = models.BooleanField(db_column='UsingCustomUsername', default=False)  # Field name made lowercase.
    usertitle = models.CharField(db_column='UserTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    useraffiliation = models.CharField(db_column='UserAffiliation', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LookupUserInfo'
        app_label = 'LookupUserInfo'

MEDIA_TYPE_CHOICES =    [
    ('audio','audio'),
    ('image','image'),
    ('PDF','PDF'),
    ('video','video'),
    ('other','other')
]

class Media(Queryable):
    mediaid = models.AutoField(db_column='MediaID', primary_key=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=255, blank=True, null=True, verbose_name='type', choices=MEDIA_TYPE_CHOICES)
    medianame = models.CharField(db_column='MediaName', max_length=255, blank=True, null=True, verbose_name='name')
    mediadescription = models.TextField(db_column='MediaDescription', blank=True, null=True, verbose_name='description')
    medialink = models.CharField(db_column='MediaLink', max_length=255, blank=True, null=True, verbose_name='link')
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Media'
        verbose_name = 'Medium'
        verbose_name_plural = 'Media'
        # app_label = 'Media'

    def keyword_search(keyword):
        return Media.objects.filter(Q(mediatype__icontains=keyword) | Q(medianame__icontains=keyword)| Q(mediadescription__icontains=keyword) | Q(medialink__icontains=keyword))

    #def keyword_search(keyword):
       #return Resources.objects.filter(commonname__icontains=keyword)  #UPDATE THIS

    def name(self):
        return self.medianame                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-media.png'  #UPDATE THIS

    def subtitle(self):
        return self.mediatype                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'name', 'value': self.medianame},
            {'key':'media type', 'value': self.mediatype},
            {'key':'media description', 'value': self.mediadescription},
            {'key':'link', 'value': self.medialink}
        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'media'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.mediadescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }

    def __unicode__(self):
        return unicode('%s' % (self.medianame))

    def __str__(self):
        return self.medianame

class Mediacitationevents(Queryable):
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID', primary_key=True, verbose_name='media')
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MediaCitationEvents'
        verbose_name = 'Medium - Citation'
        verbose_name_plural = 'Media - Citations'
        # app_label = 'MediaCitationEvents'
        unique_together = (('mediaid', 'citationid'),)

    #def keyword_search(keyword):
        #return MediaCitationEvents.objects.filter(Q(relationshipdescription__icontains=keyword) | Q(pages__icontains=keyword))

    def keyword_search(keyword):
        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs] #[19, 24, 350]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return Mediacitationevents.objects.filter(Q(citationid__in=citation_loi) | Q(mediaid__in=media_loi) | Q(relationshipdescription__icontains=keyword))

    #def keyword_search(keyword):
       #return Resources.objects.filter(commonname__icontains=keyword)  #UPDATE THIS

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Mediacitationevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Placealtindigenousname(models.Model):
    altindigenousnameid = models.AutoField(db_column='AltIndigenousNameID', primary_key=True)  # Field name made lowercase.
    placeid = models.ForeignKey(Places, db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    altindigenousname = models.CharField(db_column='AltIndigenousName', max_length=255, blank=True, null=True, verbose_name='alternate indigenous name')

    class Meta:
        managed = True
        db_table = 'PlaceAltIndigenousName'
        verbose_name = 'Place - Indigenous Name'
        verbose_name_plural = 'Places - Indigenous Names'
        app_label = 'PlaceAltIndigenousName'


class Placegisselections(models.Model):
    placeid = models.IntegerField(db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    placelabel = models.CharField(db_column='PlaceLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcefc = models.CharField(db_column='SourceFC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PlaceGISSelections'
        app_label = 'PlaceGISSelections'


class Placesmediaevents(Queryable):
    placeid = models.ForeignKey(Places, models.DO_NOTHING, db_column='PlaceID', primary_key=True, verbose_name='place')
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID', verbose_name='media')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PlacesMediaEvents'
        verbose_name = 'Place - Medium'
        verbose_name_plural = 'Places - Media'
        # app_label = 'PlacesMediaEvents'
        unique_together = (('placeid', 'mediaid'),)

    def keyword_search(keyword):
        place_qs = Places.keyword_search(keyword)
        place_loi = [place.pk for place in place_qs] #[19, 24, 350]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return Placesmediaevents.objects.filter(Q(placeid__in=place_loi) | Q(mediaid__in=media_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Placesmediaevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }



class Placesresourcecitationevents(Queryable):
    placeresourceid = models.ForeignKey(Placesresourceevents, models.DO_NOTHING, db_column='PlaceResourceID', primary_key=True)  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PlacesResourceCitationEvents'
        # app_label = 'PlacesResourceCitationEvents'
        unique_together = (('placeresourceid', 'citationid'),)

    def keyword_search(keyword):
        placeresource_qs = Placesresourceevents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs] #[19, 24, 350]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return Placesresourcecitationevents.objects.filter(Q(citationid__in=citation_loi) | Q(placeresourceid__in=placeresource_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Placesresourcecitationevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Placesresourcemediaevents(Queryable):
    placeresourceid = models.ForeignKey(Placesresourceevents, models.DO_NOTHING, db_column='PlaceResourceID', primary_key=True)  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PlacesResourceMediaEvents'
        # app_label = 'PlacesResourceMediaEvents'
        unique_together = (('placeresourceid', 'mediaid'),)

    def keyword_search(keyword):
        placeresource_qs = Placesresourceevents.keyword_search(keyword)
        placeresource_loi = [placeresource.pk for placeresource in placeresource_qs] #[19, 24, 350]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return Placesresourcemediaevents.objects.filter(Q(placeresourceid__in=placeresource_loi) | Q(mediaid__in=media_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Placesresourcemediaevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Resourceactivitycitationevents(Queryable):
    resourceactivityid = models.ForeignKey(Resourcesactivityevents, models.DO_NOTHING, db_column='ResourceActivityID', primary_key=True)  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourceActivityCitationEvents'
        # app_label = 'ResourceActivityCitationEvents'
        unique_together = (('resourceactivityid', 'citationid'),)

    def keyword_search(keyword):
        resourceactivity_qs = Resourcesactivityevents.keyword_search(keyword)
        resourceactivity_loi = [resourceactivity.pk for resourceactivity in resourceactivity_qs] #[19, 24, 350]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return Resourceactivitycitationevents.objects.filter(Q(citationid__in=citation_loi) | Q(resourceactivityid__in=resourceactivity_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Resourceactivitycitationevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Resourceactivitymediaevents(Queryable):
    resourceactivityid = models.ForeignKey(Resourcesactivityevents, models.DO_NOTHING, db_column='ResourceActivityID', primary_key=True)  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourceActivityMediaEvents'
        # app_label = 'ResourceActivityMediaEvents'
        unique_together = (('resourceactivityid', 'mediaid'),)

    def keyword_search(keyword):
        resourceactivity_qs = Resourcesactivityevents.keyword_search(keyword)
        resourceactivity_loi = [resourceactivity.pk for resourceactivity in resourceactivity_qs] #[19, 24, 350]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return Resourceactivitymediaevents.objects.filter(Q(resourceactivityid__in=resourceactivity_loi) | Q(mediaid__in=media_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Resourceactivitymediaevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Resourcealtindigenousname(models.Model):
    altindigenousnameid = models.AutoField(db_column='AltIndigenousNameID', primary_key=True)  # Field name made lowercase.
    resourceid = models.IntegerField(db_column='ResourceID', blank=True, null=True)  # Field name made lowercase.
    altindigenousname = models.CharField(db_column='AltIndigenousName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourceAltIndigenousName'
        app_label = 'ResourceAltIndigenousName'


class Resourceresourceevents(Queryable):
    resourceid = models.IntegerField(db_column='ResourceID', primary_key=True)  # Field name made lowercase.
    altresourceid = models.IntegerField(db_column='AltResourceID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourceResourceEvents'
        # app_label = 'ResourceResourceEvents'
        unique_together = (('resourceid', 'altresourceid'),)

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs] #[19, 24, 350]

        return Resourceresourceevents.objects.filter(Q(resourceid__in=resource_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Resourceresourceevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Resourcescitationevents(Queryable):
    resourceid = models.ForeignKey(Resources, models.DO_NOTHING, db_column='ResourceID', primary_key=True, verbose_name='resource')
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', verbose_name='citation')
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourcesCitationEvents'
        verbose_name = 'Resource - Citation'
        verbose_name_plural = 'Resources - Citations'
        # app_label = 'ResourcesCitationEvents'
        unique_together = (('resourceid', 'citationid'),)

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs] #[19, 24, 350]

        citation_qs = Citations.keyword_search(keyword)
        citation_loi = [citation.pk for citation in citation_qs]

        return Resourcescitationevents.objects.filter(Q(citationid__in=citation_loi) | Q(resourceid__in=resource_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Resourcescitationevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Resourcesmediaevents(Queryable):
    resourceid = models.ForeignKey(Resources, models.DO_NOTHING, db_column='ResourceID', primary_key=True, verbose_name='resource')
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID')  # Field name made lowercase.
    relationshipdescription = models.CharField(db_column='RelationshipDescription', max_length=255, blank=True, null=True, verbose_name='relationship description')
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    #enteredbyname = models.CharField(db_column='EnteredByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #enteredbytribe = models.CharField(db_column='EnteredByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbytitle = models.CharField(db_column='EnteredByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #enteredbydate = models.DateTimeField(db_column='EnteredByDate', blank=True, null=True)  # Field name made lowercase.
    #modifiedbyname = models.CharField(db_column='ModifiedByName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytitle = models.CharField(db_column='ModifiedByTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbytribe = models.CharField(db_column='ModifiedByTribe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #modifiedbydate = models.DateTimeField(db_column='ModifiedByDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResourcesMediaEvents'
        verbose_name = 'Resource - Medium'
        verbose_name_plural = 'Resources - Media'
        # app_label = 'ResourcesMediaEvents'
        unique_together = (('resourceid', 'mediaid'),)

    def keyword_search(keyword):
        resource_qs = Resources.keyword_search(keyword)
        resource_loi = [resource.pk for resource in resource_qs] #[19, 24, 350]

        media_qs = Media.keyword_search(keyword)
        media_loi = [media.pk for media in media_qs]

        return Resourcesmediaevents.objects.filter(Q(mediaid__in=media_loi) | Q(resourceid__in=resource_loi) | Q(relationshipdescription__icontains=keyword))

    def name(self):
        return self.relationshipdescription                          #UPDATE THIS

    def image(self):
        return '/static/explore/img/demo-activity.png'  #UPDATE THIS

    def subtitle(self):
        return self.relationshipdescription                             #UPDATE THIS

    def data(self):                                     #UPDATE THIS
        return [
            {'key':'relationship description', 'value': self.relationshipdescription},
            {'key':'pages', 'value': self.pages}

        ]

    #TODO: look at explore/views.py (get_model_by_type)
    def get_response_format(self):
        type = 'Resourcesmediaevents'                              #UPDATE THIS
        return {
            'id': self.pk,
            # pk is django keyword for any model's Primary Key
            'type': type,
            'name': self.name(),
            'image': self.image(),
            'description': self.relationshipdescription,         #UPDATE THIS
            'link': '/explore/%s/%d' % (type, self.pk)
        }


class Useraccess(models.Model):
    accessid = models.AutoField(db_column='AccessID', primary_key=True)  # Field name made lowercase.
    accesslevel = models.CharField(db_column='AccessLevel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserAccess'
        app_label = 'UserAccess'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    affiliation = models.CharField(db_column='Affiliation', max_length=255)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    accesslevel = models.IntegerField(db_column='AccessLevel')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # app_label = 'Users'