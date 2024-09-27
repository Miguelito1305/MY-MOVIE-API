from fastapi import FastAPI, Body #importar libreria
from fastapi.responses import HTMLResponse
from movies_list import movies_list

app = FastAPI() #crear instancia de la clase fastapi
app.title = "Mi API con FastAPI"
app.version = "0.0.1"


@app.get('/', tags =["Home"]) #definimos una ruta
def message():
    return HTMLResponse('<h1>Hola mundo</h1>')

@app.get('/movies', tags = ["Movies"])
def movies():
    return movies_list

@app.get('/movies/{movie_id}', tags = ["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []

@app.get('/movies', tags = ["Movies"])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies_list if item["year"] == year]

@app.post('/movies', tags = ["Movies"])
def create_movie(id: int= Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list

@app.put('/movies/{movie_id}', tags = ["Movies"])
def update_movie(movie_id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies_list:
        if item["id"] == movie_id:
            item["title"] = title
            item["overview"] = overview
            item["year"] = year
            item["rating"] = rating
            item["category"] = category
            return item
    return []

@app.delete('/movies/{movie_id}', tags = ["Movies"])
def delete_movie(movie_id: int):
    for item in movies_list:
        if item["id"] == movie_id:
            movies_list.remove(item)
            return movies_list
    return []