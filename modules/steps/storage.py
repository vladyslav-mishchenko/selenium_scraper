from load_django import *
from parser_app.models import Smartphone


def save_to_db(data):

    # save to db without defaults and unique
    smartphone, created = Smartphone.objects.get_or_create(
        name=data["name"],
        price=data["price"],
        discounted_price=data["discounted_price"],
        reviews=data["reviews"],
        image_paths=data["image_paths"],
        product_code=data["product_code"],
        characteristics=data["characteristics"],
        color=data["color"],
        internal_memory=data["internal_memory"],
        screen_diagonal=data["screen_diagonal"],
        display_resolution=data["display_resolution"],
        manufacturer=data["manufacturer"],
        series=data["series"],
    )

    # print created or exists
    if created:
        print(f"Created: {smartphone}")
    else:
        print(f"Exists: {smartphone}")
