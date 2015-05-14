from django.db import models
#from property_inventory.models import Property

class ConditionReport(models.Model):
	GOOD_STATUS = 3
	FAIR_STATUS = 2
	POOR_STATUS = 1
	NA_STATUS = None

	STATUS_CHOICES = ( (GOOD_STATUS, 'Good / Satisfactory'), (FAIR_STATUS, 'Fair / Repair'), (POOR_STATUS, 'Poor / Replace'), (NA_STATUS, 'N/A') )

	Property = models.ForeignKey('property_inventory.Property')

	roof_shingles = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Shingles')
	roof_shingles_notes = models.CharField(max_length=512, blank=True)
	roof_framing = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Framing')
	roof_framing_notes = models.CharField(max_length=512, blank=True)
	roof_gutters = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Gutters')
	roof_gutters_notes = models.CharField(max_length=512, blank=True)

	foundation_slab = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Slab')
	foundation_slab_notes = models.CharField(max_length=512, blank=True)
	foundation_crawl = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Crawlspace')
	foundation_crawl_notes = models.CharField(max_length=512, blank=True)

	exterior_siding_brick = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Brick')
	exterior_siding_brick_notes = models.CharField(max_length=512, blank=True)
	exterior_siding_vinyl = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Vinyl')
	exterior_siding_vinyl_notes = models.CharField(max_length=512, blank=True)
	exterior_siding_wood = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Wood')
	exterior_siding_wood_notes = models.CharField(max_length=512, blank=True)
	exterior_siding_other = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Other')
	exterior_siding_other_notes = models.CharField(max_length=512, blank=True)

	windows = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Windows')
	windows_notes = models.CharField(max_length=512, blank=True)
	garage = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Garage')
	garage_notes = models.CharField(max_length=512, blank=True)
	fencing = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Fencing')
	fencing_notes = models.CharField(max_length=512, blank=True)
	landscaping = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Landscaping')
	landscaping_notes = models.CharField(max_length=512, blank=True)
	doors = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Doors')
	doors_notes = models.CharField(max_length=512, blank=True)
	kitchen_cabinets = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Kitchen Cabinets')
	kitchen_cabinets_notes = models.CharField(max_length=512, blank=True)

	flooring_subflooring = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Subflooring')
	flooring_subflooring_notes = models.CharField(max_length=512, blank=True)
	flooring_covering = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Covering')
	flooring_covering_notes = models.CharField(max_length=512, blank=True)

	electrical_knob_tube_cloth = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Knob, tube and cloth')
	electrical_knob_tube_cloth_notes = models.CharField(max_length=512, blank=True)
	electrical_standard = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Standard')
	electrical_standard_notes = models.CharField(max_length=512, blank=True)

	plumbing_metal = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Copper / metal')
	plumbing_metal_notes = models.CharField(max_length=512, blank=True)
	plumbing_plastic = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='PVC / PEX')
	plumbing_plastic_notes = models.CharField(max_length=512, blank=True)

	walls_drywall = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Drywall')
	walls_drywall_notes = models.CharField(max_length=512, blank=True)
	walls_lathe_plaster = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Plaster and lathe')
	walls_lathe_plaster_notes = models.CharField(max_length=512, blank=True)

	hvac_furance = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Furnace')
	hvac_furance_notes = models.CharField(max_length=512, blank=True)
	hvac_duct_work = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Duct work')
	hvac_duct_work_notes = models.CharField(max_length=512, blank=True)
	hvac_air_conditioner = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, verbose_name='AC')
	hvac_air_conditioner_notes = models.CharField(max_length=512, blank=True)

