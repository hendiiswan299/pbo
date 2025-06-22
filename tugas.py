import json
import os

class Tugas:
    def __init__(self, judul, deadline, deskripsi):
        self.judul = judul
        self.deadline = deadline
        self.deskripsi = deskripsi

    def to_dict(self):
        return {
            "judul": self.judul,
            "deadline": self.deadline,
            "deskripsi": self.deskripsi
        }

    @staticmethod
    def from_dict(data):
        return Tugas(data["judul"], data["deadline"], data["deskripsi"])

class TugasManager:
    def __init__(self, filepath="data/tugas.json"):
        self.filepath = filepath
        self.tugas_list = self.load()

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r") as file:
            data = json.load(file)
            return [Tugas.from_dict(item) for item in data]

    def simpan(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
    
        with open(self.filepath, "w") as file:
            json.dump([t.to_dict() for t in self.tugas_list], file, indent=4)


    def tambah_tugas(self, tugas):
        self.tugas_list.append(tugas)
        self.simpan()

    def tampilkan_semua(self):
        return self.tugas_list

    def hapus_tugas(self, judul):
        self.tugas_list = [t for t in self.tugas_list if t.judul != judul]
        self.simpan()
