# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 19:09
from __future__ import unicode_literals

import gnupg
import hashlib
import os

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
from django.template.defaultfilters import slugify
from django.utils.termcolors import colorize as colourise  # Spelling hurts me


class GnuPG(object):
    """
    A handy singleton to use when handling encrypted files.
    """

    gpg = gnupg.GPG(gnupghome=settings.GNUPG_HOME)

    @classmethod
    def decrypted(cls, file_handle):
        return cls.gpg.decrypt_file(
            file_handle, passphrase=settings.PASSPHRASE).data

    @classmethod
    def encrypted(cls, file_handle):
        return cls.gpg.encrypt_file(
            file_handle,
            recipients=None,
            passphrase=settings.PASSPHRASE,
            symmetric=True
        ).data


class Document(object):
    """
    Django's migrations restrict access to model methods, so this is a snapshot
    of the methods that existed at the time this migration was written, since
    we need to make use of a lot of these shortcuts here.
    """

    def __init__(self, doc):
        self.pk = doc.pk
        self.correspondent = doc.correspondent
        self.title = doc.title
        self.file_type = doc.file_type
        self.tags = doc.tags
        self.created = doc.created

    def __str__(self):
        created = self.created.strftime("%Y%m%d%H%M%S")
        if self.correspondent and self.title:
            return "{}: {} - {}".format(
                created, self.correspondent, self.title)
        if self.correspondent or self.title:
            return "{}: {}".format(created, self.correspondent or self.title)
        return str(created)

    @property
    def source_path(self):
        return os.path.join(
            settings.MEDIA_ROOT,
            "documents",
            "originals",
            "{:07}.{}.gpg".format(self.pk, self.file_type)
        )

    @property
    def source_file(self):
        return open(self.source_path, "rb")

    @property
    def file_name(self):
        return slugify(str(self)) + "." + self.file_type


def set_checksums(apps, schema_editor):

    document_model = apps.get_model("documents", "Document")

    if not document_model.objects.all().exists():
        return

    print(colourise(
        "\n\n"
        "  This is a one-time only migration to generate checksums for all\n"
        "  of your existing documents.  If you have a lot of documents\n"
        "  though, this may take a while, so a coffee break may be in\n"
        "  order."
        "\n", opts=("bold",)
    ))

    sums = {}
    for d in document_model.objects.all():

        document = Document(d)

        print("    {} {} {}".format(
            colourise("*", fg="green"),
            colourise("Generating a checksum for", fg="white"),
            colourise(document.file_name, fg="cyan")
        ))

        with document.source_file as encrypted:
            checksum = hashlib.md5(GnuPG.decrypted(encrypted)).hexdigest()

        if checksum in sums:
            error = "\n{line}{p1}\n\n{doc1}\n{doc2}\n\n{p2}\n\n{code}\n\n{p3}{line}".format(
                p1=colourise("It appears that you have two identical documents in your collection and \nPaperless no longer supports this (see issue #97).  The documents in question\nare:", fg="yellow"),
                p2=colourise("To fix this problem, you'll have to remove one of them from the database, a task\nmost easily done by running the following command in the same\ndirectory as manage.py:", fg="yellow"),
                p3=colourise("When that's finished, re-run the migrate, and provided that there aren't any\nother duplicates, you should be good to go.", fg="yellow"),
                doc1=colourise("  * {} (id: {})".format(sums[checksum][1], sums[checksum][0]), fg="red"),
                doc2=colourise("  * {} (id: {})".format(document.file_name, document.pk), fg="red"),
                code=colourise("  $ echo 'DELETE FROM documents_document WHERE id = {pk};' | ./manage.py dbshell".format(pk=document.pk), fg="green"),
                line=colourise("\n{}\n".format("=" * 80), fg="white", opts=("bold",))
            )
            raise RuntimeError(error)
        sums[checksum] = (document.pk, document.file_name)

        document_model.objects.filter(pk=document.pk).update(checksum=checksum)


def do_nothing(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('documents', '0013_auto_20160325_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='checksum',
            field=models.CharField(
                default='-',
                db_index=True,
                editable=False,
                max_length=32,
                help_text='The checksum of the original document (before it '
                          'was encrypted).  We use this to prevent duplicate '
                          'document imports.',
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_checksums, do_nothing),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='document',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
