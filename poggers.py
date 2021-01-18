movies = ["John Wick Chapter 1", "John Wick Chapter 2", "John Wick Chapter 3", "Matrix"]  
movie = raw_input("Πρόσθεσε μια ταινία: ")
while movie in movies:
    print "Υπάρχει ήδη στη λίστα"
    movie = raw_input("Πρόσθεσε μια άλλη ταινία: ")
else:
    movies.append(movie)
    moviessorted = sorted(movies)
    print "Ταινίες: " "(" + str(len(movies)) + ")", moviessorted
