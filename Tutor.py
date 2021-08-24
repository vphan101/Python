passwd="root",
database="testdatabase"
)

user=[("tim","techwithtim","12345","tim@gmail.com"),
     ("joe","joey123","password123", "joe@hotmail.com"),
     ("sarah","sarah1234","pass234","sarah@gmail.com")]

user_scores = [(45,100),
              (30,200),
              (46,124)]

mycursor = db.cursor()

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCAHR(50), passwd VARCHAR(50))"

Q2 = "CREATE TABLE Scores ()"