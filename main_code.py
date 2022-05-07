from flask import Flask, jsonify, request
import csv

all_movies= []
with open('movies.csv') as f:
    reader= csv.reader(f)
    data= list(reader)
    all_movies= data[1:]

movies_liked=[]
movies_not_liked=[]
movies_not_watched=[]

app= Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success",
    })


@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie= all_movies[0],
    all_movies=all_movies[1:]
    movies_liked.append(movie)
    return jsonify({
        "status": "success",
    }),201


@app.route("/not-liked-movie", methods=["POST"])
def unliked_movie():
    movie= all_movies[0],
    all_movies=all_movies[1:]
    movies_not_liked.append(movie)
    return jsonify({
        "status": "success",
    }),201


@app.route("/not-watched-movie", methods=["POST"])
def not_watched_movie():
    movie= all_movies[0],
    all_movies=all_movies[1:]
    movies_not_watched.append(movie)
    return jsonify({
        "status": "success",
    }),201

if __name__ == "__main__":
    app.run()