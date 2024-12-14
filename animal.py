class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("nama \t\t: ", self.nama,
        "\nmakanan \t\t :", self.makanan,
        "\nhidup \t\t: ", self.hidup,
        "\nberkembang_biak \t\t: ", self.berkembang_biak)