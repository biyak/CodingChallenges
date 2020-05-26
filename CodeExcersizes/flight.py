#movie on the flight problem

def whichMovie(movie_times, duration):
    time = duration - 30

    movie1 = None
    movie2 = None

    max_time = 0

    for i in range(0, len(movie_times)-1):
        if movie_times[i] < time:
                   for j in range(i, len(movie_times)):
                                  time_spent = movie_times[i] + movie_times[j]
                                  if time_spent <= time and time_spent > max_time:
                                       max_time = time_spent
                                       movie1 = movie_times[i]
                                       movie2 = movie_times[j]


    print( [movie1, movie2])

whichMovie([90, 85, 75, 60, 120, 150, 125], 250)
                   

def WhichMovieOptimal(movie_times, duration):
    answer_arr = [0] * len(movie_times)+1

    
