class Student:
    def __init__(self, navn, total_poeng, antall_quizer):
        self._navn = navn
        self._total_poeng = total_poeng
        self._antall_quizer = antall_quizer
    def leggTilQuizScore(self, ny_poeng):
        self._total_poeng += ny_poeng
        self._antall_quizer += 1
    def gjennomsnittligScore(self):
        return self._total_poeng/self._antall_quizer
    def skriv_ut(self):
        print("Studenten", self._navn, "har  total poeng", self._total_poeng, "i", self._antall_quizer, "quizer.")
    
