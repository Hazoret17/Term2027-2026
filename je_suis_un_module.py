""" auteur: monsieur nicolas
date : aujourd'hui
version: 1
"""


def premiermodule():
    print("voici mon 1er module")


if __name__ == "__main__":
    premiermodule()


print("contenu de la variable __doc__\n", __doc__)
print("contenu de la variable __name__\n", __name__)