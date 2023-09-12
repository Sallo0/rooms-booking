import slugify


def get_slug(value: str):
    return slugify.slugify(value, separator="-")
