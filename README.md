# 🎬 Movie Backend API

A production-ready Django REST API for a Movie Recommendation App.

## 🚀 Features
- JWT Authentication
- Movie CRUD APIs
- Redis Caching
- Swagger Docs
- PostgreSQL Ready
- Render Deployment Ready

## 🔧 Build Command (Render)
pip install -r requirements.txt && python manage.py migrate

## ▶ Start Command (Render)
gunicorn movie_backend.wsgi:application

## 🔐 Environment Variables
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:5432/dbname
TMDB_API_KEY=your_tmdb_key
