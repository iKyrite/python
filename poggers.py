movies = ["John Wick Chapter 1", "John Wick Chapter 2", "John Wick Chapter 3", "Matrix"]  
movie = raw_input("�������� ��� ������: ")
while movie in movies:
    print "������� ��� ��� �����"
    movie = raw_input("�������� ��� ���� ������: ")
else:
    movies.append(movie)
    moviessorted = sorted(movies)
    print "�������: " "(" + str(len(movies)) + ")", moviessorted
