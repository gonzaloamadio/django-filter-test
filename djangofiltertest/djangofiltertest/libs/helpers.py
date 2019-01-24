"""
Library with some generic functions specific for this project
"""
# -*- coding: utf-8 -*-
import string
from slugify import slugify

from datetime import datetime
from random import choice, randint

from .shortuuid import encode as _suencode

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)-8s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='log_back_emedido.log',
#                     filemode='a')
# log = logging.getLogger('back_emedido')

# ----------------------------------------------------------------------------
#                    STRING FUNCTIONS
# ----------------------------------------------------------------------------

def gen_secret_key(numero):
    """
        Gen secret key of length 'numero'. A mix of ascii and numbers
    """
    return ''.join(
        choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        for _ in range(numero)
    )

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
        print(random_string_generator())
        print(random_string_generator(size=50))
    """
    return ''.join(choice(chars) for _ in range(size))

def before(value, a, last_appearance=False):
    # Find first part and return slice before it.
    # If last_appearance=True, look a from right of string, i.e. last appearance
    if last_appearance:
        pos_a = value.rfind(a)
    else:
        pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def after(value, a, last_appearance=False):
    # Find and validate first part.
    # If last_appearance=True, look a from right of string, i.e. last appearance
    if last_appearance:
        pos_a = value.rfind(a)
    else:
        pos_a = value.find(a)

    if pos_a == -1: return ""
    # Returns chars after the found string.
    # Adjusted position, because find gives the first position of chain founded.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]


# ----------------------------------------------------------------------------
#                           SLUG
# ----------------------------------------------------------------------------

def slug_string_generator(instance, new_slug=None):
    """
    It assumes your instance has a model with a slug field
      and a title character (char) field.

    It also assume that intance is looked up by slug
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def slug_generator(instance):
    """
        Generation of slug. Return, slugged title and UUID of instance hashed
    """
    return "{title_slug}-{hashid}".format(
            hashid=_suencode(instance.id),
            title_slug=slugify(instance.title[:128])
        )

def slug_deconstructor(slug):
    """
        Inverse operation of slug_generator. Split it in slugtitle and hashid

        Input: slug (should be of shape : "{slug}-{hashid}"
        Output: ({slug}-{hashid})
    """
    return before(slug,"-",last_appearance=True),after(slug,"-",last_appearance=True)
