# FCams: Flock Camera Locator for Dallas, Texas

This Django website displays and marks the locations of flock cameras in the streets of Dallas, Texas. The project is designed to be easily extended to other states in the future.

## Features
- Django-based web application
- Map interface to visualize camera locations
- Modular design for future expansion

## Getting Started

1. **Create and activate the virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install django
   ```
3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
5. **Access the site:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Next Steps
- Add a Django app for camera locations
- Integrate a map (e.g., Leaflet or Google Maps)
- Add camera data for Dallas

---

*This project is in its initial setup phase. More features and instructions will be added as development progresses.*
