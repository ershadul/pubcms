# Django settings for alkawsarsite project.
import os

def path(*x):
	"""Get and return the relative path of x."""
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Ershadul Hoque Sarker', 'ershadulhoque@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_HOST = ''

if DEBUG:
    DATABASE_NAME = 'pubcms'
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = ''
else:
    DATABASE_NAME = 'ershadul_qualam'
    DATABASE_USER = 'ershadul_qualam'
    DATABASE_PASSWORD = 'qualam2010'


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6mb49k1w%m&)asfsfsdfsfjkskljfsdfs778^%^&^&ASDF(*(*F&(Ddwdvt5f(tv0g83q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'pubcms.middleware.DomainMiddleware',
    'pubcms.sitesettings.middleware.SiteMiddleware',
    'pubcms.middleware.PubCMSMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'pubcms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS  = (
	"django.core.context_processors.auth",
)

INSTALLED_APPS = (
    'django.contrib.auth',
	'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'pubcms.sections',
    'pubcms.issues',
    'pubcms.articles',
    'pubcms.authors',
    'pubcms.sitesettings',
    'pubcms.feedbacks',
    'pubcms.tags_filters',
)

# Emails
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'admin@alqualam.com'
EMAIL_HOST_PASSWORD = 'alq90alq'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = 'ALQUALAM <noReply@alqualam.com>'
FEEDBACK_EMAIL = 'feedback@alqualam.com'
