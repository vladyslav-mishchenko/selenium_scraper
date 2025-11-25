from load_django import *
from parser_app.models import Smartphone


def print_from_db():

    # print data from db
    print("")
    print("----------------------------smartphone")
    for i in Smartphone.objects.all():
        print(
            f"Smartphone: {i.name} | "
            f"Price: {i.price} | "
            f"Discounted Price: {i.discounted_price} | "
            f"Reviews: {i.reviews} | "
            f"Images: {i.image_paths} | "
            f"Product Code: {i.product_code} | "
            f"Characteristics: {i.characteristics} | "
            f"Color: {i.color} | "
            f"Internal memory: {i.internal_memory} | "
            f"Screen diagonal: {i.screen_diagonal} | "
            f"Display resolution: {i.display_resolution} "
            f"Manufacturer: {i.manufacturer} "
            f"Series: {i.series} | "
        )
    print("------------------------------------end")
