from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def info(self):
        pass

class Mahasiswa(User):
    def __init__(self, nama, nim):
        super().__init__(nama)
        self.nim = nim

    def info(self):
        return f"{self.nama} (NIM: {self.nim})"
