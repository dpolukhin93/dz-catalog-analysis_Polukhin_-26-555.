import math as math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
      "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
] 

def main():
    print(average_rating(movies))
    print(catalog_age_stats(movies, 2026))
    for i in range(0, len(movies), 2):
        dur = movies[i]["duration_min"]
        print(f"{dur} : {duration_in_hours(dur)}")

def average_rating(movies:list[dict]):
   
    total_movies = len(movies)
    rate_sum = 0
   
    for movie in movies:
       rate_sum += movie["rating"]

    return round(rate_sum / total_movies, 1)

def catalog_age_stats(movies:list[dict], current_year = 2026):
   
    #newest - минимум в годах, oldest - максимум в годах
    newest = current_year
    oldest = 0 
   
    total_movies = len(movies)
    if total_movies == 0:
        return (0, 0, 0)

    age_sum = 0
    for movie in movies:
        movie_age = current_year - movie["year"]
        newest = movie_age if movie_age <= newest else newest
        oldest = movie_age if movie_age >= oldest else oldest
        age_sum += movie_age

    average = math.ceil(age_sum/total_movies)

    return (newest, oldest, average)

def duration_in_hours(minutes:int):
    return f"{minutes // 60} ч {minutes % 60} м"

def rating_tier(rating:float):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year:int):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year < 2015:
            return "старые"
        case _:
            return "недавние"

if __name__ == "__main__":
    main()
