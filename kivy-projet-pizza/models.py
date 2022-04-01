class Pizza:
    nom=""
    ingredients=""
    prix=0
    vagetarienne=False

    def __init__(self,nom,ingredients,prix,vagetarienne):
        self.nom=nom
        self.ingredients=ingredients
        self.prix=prix
        self.vagetarienne=vagetarienne

    def get_dictionary(self):
        data={"nom":self.nom,
            "ingredients":self.ingredients,
            "prix":self.prix,
            "vegetarien":self.vagetarienne}
        return data
