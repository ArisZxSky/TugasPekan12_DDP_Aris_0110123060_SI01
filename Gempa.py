class Gempa:
    lokasi = ""
    skala = 0
    def _init_(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala <= 2:
            return "Dampak gempa tidak berasa"
        elif self.skala <=4:
           return "Dampak gempa bangunan retak-retak"
        elif self.skala <=6:
            return "Dampak gempa bangunan roboh"
        elif self.skala <= 10:
            return"Dampak gempa bangunan roboh dan berpotensi tsunami"

    def cetak(self):
        print("Lokasi\t: ", self.lokasi,
        "\nSkala\t: ", self.skala,
        "\nDampak\t: ", self.dampak(),
        "\n---------------------------------------------------------------")