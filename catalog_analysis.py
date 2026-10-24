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

   # этап 3
    # Цикл for и continue
    print_not_comedies(movies)   
    # Цикл while и break
    find_first_masterpiece(movies)

    # этап 8
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
        
    sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


def correct_year_word(years:int):
    
    if years % 100 in (11,12,13,14):
        return "лет"
    
    last_number = years % 10
    if last_number == 1:
        return "год"
    elif last_number in (2,3,4):
        return "года"
    else:
        return "лет"    
   

def build_report(movies:list[dict]):
   
    sep = '\n'
    
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    avg_years = catalog_age_stats(movies)[2]
    print(f"Средний возраст фильмов: {avg_years} {correct_year_word(avg_years)}")
    print(sep)

    print("Топ-3 фильма:")
    for movie in sort_movies_by_rating(movies)[:3]:
        print(format_report_line(movie))
    print(sep)

    print("Фильмов по жанрам:")
    for genre, count in count_by_genre(movies).items():
        print(f"{genre} — {count}")
    print(sep)

    print(f"Все жанры каталога: {", ".join(sorted(all_genres(movies)))}")



def genres_only_in_one(movie1:dict, movie2:dict):
    return movie1["genres"] - movie2["genres"]


def all_genres(movies:list[dict]):
    result = set()
    for movie in movies:
        result.update(movie["genres"])
        
    return result


def iter_high_rated(movies:list[dict], min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
          yield movie  

def common_actors(movie1:dict, movie2:dict):
    return set(movie1["actors"]) & set(movie2["actors"])

def movies_above_average(movies:list[dict]):
    avg = average_rating(movies)
    return {movie["title"]:movie["rating"] for movie in movies if movie["rating"]>avg} 
  


def count_by_genre(movies:list[dict]):
    result = {}
    for movie in movies:
        for genre in movie["genres"]:
           result[genre] = result.get(genre, 0) + 1

    return result

def actor_filmography(movies:list[dict]):
    result = {}
    for movie in movies:
        for actor in movie["actors"]:
           filmography = result.get(actor, [])
           filmography.append(movie["title"])
           result[actor] = filmography

    return result


def top_n_by_rating(movies:list[dict], n = 3):
    sorted_movies = sort_movies_by_rating(movies)
    result =[(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

    return result


def titles_sorted_by_rating(movies:list[dict]):
    return [movie["title"] for movie in sort_movies_by_rating(movies)]


def sort_movies_by_rating(movies:list[dict], descending = True):
    return sorted(movies, key=lambda movie: movie["rating"], reverse=descending)


def print_not_comedies(movies:list[dict]):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies:list[dict]):
    i = 0
    while i < len(movies):
        movie = movies[i]
        if movie["rating"] > 9.0:
            print(movie)
            break
        i += 1
    else:
        print("Шедевров не найдено")


def format_report_line(movie:dict):
    return (f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
            f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, '
            f'жанры: {", ".join(sorted(movie["genres"]))}')


def make_slug(title:str):
    return title.lower().replace(" ", "-")


def normalize_title(title:str):
    normalized_title = ""
    for word in title.split():
       normalized_title +=  word[0].upper() + word[1:] + " "
    
    return normalized_title.rstrip()


def count_long_movies(movies:list[dict], theshhold = 120):
    long_movie_counter = 0
    for movie in movies:
        if movie["duration_min"] > theshhold:
            long_movie_counter += 1
    
    return long_movie_counter    


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
    build_report(movies)
