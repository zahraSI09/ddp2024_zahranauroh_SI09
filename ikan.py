from animal import animal

class Ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna 
    def cetak_ikan(self):
        super().cetak()
        print("jenis \t\t: ", self.jenis, 
              "\nwarna  \t\t: ", self.warna)
        
lele = Ikan("Lele", "Cacing", "Air Tawar", "Bertelur", "Lele Mandalika", "Abu-Abu Kehitaman")
lele.cetak_ikan()

kakap = Ikan("Kakap", "Ikan kecil, udang, dll,", "Air Laut", "Bertelur", "Kakap Merah", "Merah")
kakap.cetak_ikan()