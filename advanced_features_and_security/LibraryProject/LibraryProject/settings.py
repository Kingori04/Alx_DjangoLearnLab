from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name):
    
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable")


DEBUG = False  

# Ensure allowed hosts are set correctly
ALLOWED_HOSTS = ["yourdomain.com"]  # Change to your domain







# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# settings.py

# Enforce HTTPS connections  
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS  
SECURE_HSTS_SECONDS = 31536000  # Enable HTTP Strict Transport Security (HSTS) for 1 year  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains  
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS policy 
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Enforce secure cookies  
SESSION_COOKIE_SECURE = True  # Ensure session cookies are sent over HTTPS  
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are sent over HTTPS  

# Additional security headers  
X_FRAME_OPTIONS = "DENY"  # Prevent clickjacking  
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-type sniffing  
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS protection  



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
]
AUTH_USER_MODEL = "bookshelf.CustomUser" 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#  Secure Session & CSRF Cookies
CSRF_COOKIE_SECURE = True  
SESSION_COOKIE_SECURE = True  
CSRF_COOKIE_HTTPONLY = True  
SESSION_COOKIE_HTTPONLY = True 
CSRF_USE_SESSIONS = True  

# Enable Content Security Policy (CSP)
INSTALLED_APPS += ["csp"]  
MIDDLEWARE.insert(0, "csp.middleware.CSPMiddleware")

CSP_DEFAULT_SRC = ("'self'",)  
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")  
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[BASE_DIR / "relationship_app/templates", BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#SECURITY: Secure Browsing Headers
SECURE_BROWSER_XSS_FILTER = True  # Protects against XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing
X_FRAME_OPTIONS = "DENY"  # Prevents clickjacking

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# Redirect URLs for Authentication
LOGIN_REDIRECT_URL = "home"  # Redirect after successful login
LOGOUT_REDIRECT_URL = "login"  # Redirect to login page after logout

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")




# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
