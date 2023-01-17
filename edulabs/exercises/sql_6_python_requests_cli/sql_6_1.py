import configparser
import argparse
import psycopg2


class Imdb:

    def __init__(self, filename: str, section: str):
        self.__filename = filename
        self.__section = section
        self.__db_config: dict = dict()

        parser = configparser.ConfigParser()
        parser.read(self.__filename)
        if parser.has_section(section):
            parameters = parser.items(section)
            for param in parameters:
                self.__db_config[param[0]] = param[1]
        else:
            raise Exception()

        # connection
        self.__conn = psycopg2.connect(**self.__db_config)


    @property
    def conn(self):
        return self.__conn

    @staticmethod
    def close_connection(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            finally:
                args[0].conn.close()
        return wrapper


    @close_connection
    def search_movie(self, movie_name: str) -> tuple | None:
        if isinstance(movie_name, str):
            with self.conn.cursor() as cur:
                query1 = 'SELECT rating FROM movies WHERE movie_name = %s'
                cur.execute(query1, (movie_name,))
                movie_query = cur.fetchone()
                if movie_query:
                    query2 = f"SELECT release_date, rating FROM movies WHERE movie_name = %s"
                    cur.execute(query2, (movie_name,))
                    info = cur.fetchone()
                    return info
                else:
                    return None


    @close_connection
    def display_movies_by_rating(self, movie_name: str):
        if isinstance(movie_name, str):
            with self.conn.cursor() as cur:
                query1 = 'SELECT rating FROM movies WHERE movie_name = %s'
                cur.execute(query1, (movie_name,))
                movie_query: int = cur.fetchone()[0]
                query2 = 'SELECT movie_name FROM movies WHERE rating < %s'
                cur.execute(query2, (movie_query,))
                info = cur.fetchall()
                return info


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('section')
    parser.add_argument('type')
    parser.add_argument('movie')
    args = parser.parse_args()
    if args.type == "search_movie":
        return Imdb(filename=args.filename, section=args.section).search_movie(movie_name=args.movie)
    elif args.type == "display_movies_by_rating":
        return Imdb(filename=args.filename, section=args.section).display_movies_by_rating(movie_name=args.movie)


if __name__ == '__main__':
    print(main())
