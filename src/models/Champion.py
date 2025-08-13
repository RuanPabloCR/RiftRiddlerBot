class Champion():
    def __init__(self, name, gender, specie, mana, reach, region, release_year):
        self.name = name
        self.gender = gender
        self.species = specie
        self.mana = mana
        self.reach = reach
        self.region = region
        self.release_year = release_year
    def compare_Choose(self, other):
        if not isinstance(other, Champion):
            return None
    def __eq__(self, other):
        if not isinstance(other, Champion):
            return False
        return (
            self.name == other.name and
            self.gender == other.gender and
            self.species == other.species and
            self.mana == other.mana and
            self.reach == other.reach and
            self.region == other.region and
            self.release_year == other.release_year
        )

champions = {
    1: Champion("Aatrox", "Homem", "Humano", "Sem Mana", "Corpo a corpo", "Runeterra/Shurima", 2013),
    2: Champion("Ahri", "Feminino", "Raposa", "Mana", "Longo alcance", "Ionia", 2011),
    3: Champion("Akali", "Feminino", "Humano", "Energia", "Corpo a corpo/Longo alcance", "Ionia", 2010),
    4: Champion("Alistar", "Masculino", "Minotauro", "Mana", "Corpo a corpo", "Runeterra", 2009),
    5: Champion("Amumu", "Masculino", "Múmia", "Mana", "Corpo a corpo", "Shurima", 2009),
}