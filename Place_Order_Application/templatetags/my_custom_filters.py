from django import template

register = template.Library()

def removeLetters(value,arguments):
    """
    This function removes arguments from given value.
    :param value: A string
    :param arguments: An argument to be removed
    :return: Value without arguemnt
    """

    return value.replace(arguments,"")


