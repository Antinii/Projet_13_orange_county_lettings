from django.db import migrations


def migrate_profiles_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old_profile in OldProfile.objects.all():
        new_profile = NewProfile(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )
        new_profile.save()

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profiles_data),
    ]
