from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_github',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='social_linkedin',
            new_name='linkedin',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='social_twitter',
            new_name='twitter',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='social_website',
            new_name='website',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='youtube',
        ),
    ]