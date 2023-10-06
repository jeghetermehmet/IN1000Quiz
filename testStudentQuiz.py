from student import Student
student1 = Student("Johakim", 400, 8)
student2 = Student("Kristin", 230, 3)
student3 = Student("Dag", 230, 4)
student1.leggTilQuizScore(45)
student1.leggTilQuizScore(65)
student2.leggTilQuizScore(80)
student2.leggTilQuizScore(55)
student3.leggTilQuizScore(70)
student3.leggTilQuizScore(78)

student1.skriv_ut()
print("Gjennomsnitlig poeng:", student1.gjennomsnittligScore())
student2.skriv_ut()
print("Gjennomsnitlig poeng:", student2.gjennomsnittligScore())
student3.skriv_ut()
print("Gjennomsnitlig poeng:", student3.gjennomsnittligScore())

