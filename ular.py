from animal import animal

class Ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun 
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t: ", self.design, 
              "\nRacun  \t\t: ", self.racun)
    
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()

piton = Ular("Piton", "Buaya", "Hutan", "Bertelur", "Garis Bercorak", "Tidak Berbisa")
piton.cetak_ular()