# Vengelico Jewellery

Vengelico Jewellery is a small Django website for a jewellery store. It includes static informational pages, a shop page backed by product data, a contact form, and a cart page styled with the shared static CSS.

## Pages

- Home: `/`
- About: `/about/`
- Shop: `/shop/`
- Contact: `/contact/`
- Cart: `/cart/`

## Project Structure

```text
first/
+-- first/              # Django project settings and root URLs
+-- pages/              # Django app with views, URLs, models, and migrations
+-- static/
|   +-- css/style.css   # Main site styling
|   +-- js/script.js    # Mobile menu, reveal animation, button behavior
+-- templates/          # HTML templates
+-- media/              # Uploaded product images
+-- db.sqlite3          # Local development database
+-- manage.py
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install Django:

```powershell
pip install django pillow
```

Run migrations:

```powershell
python manage.py migrate
```

Start the development server:

```powershell
python manage.py runserver
```

Open the site at:

```text
http://127.0.0.1:8000/
```

## Admin

Create an admin user if you want to manage data through Django admin:

```powershell
python manage.py createsuperuser
```

Then visit:

```text
http://127.0.0.1:8000/admin/
```

## Notes

- Product images are stored in `media/products/`.
- Static assets are linked from `static/css/style.css` and `static/js/script.js`.
- The cart page is currently a static visual page. It does not yet include backend cart logic.
