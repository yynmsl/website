"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import datetime
import os
from configparser import ConfigParser
from celery.schedules import crontab
from celery.schedules import timedelta
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iejntz(i+3am$yj@c+fp76raf84u^tvpua299wm-0$ulj9b%#^'
conf = ConfigParser()
conf.read('config.ini')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'apps.user.apps.UserConfig',
    'apps.article.apps.ArticleConfig',
    'apps.course.apps.CourseConfig',
    'apps.support.apps.SupportConfig',
    'apps.forum.apps.ForumConfig',
    'rest_framework',
    'pure_pagination',
    'django_filters',
    'captcha',
    'djcelery',
]

#邮箱登录配置
AUTHENTICATION_BACKENDS=(
    'apps.user.views.CustomBackend',
)

#分页配置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'apps.forum.middle.ZxMiddleware'
]

ROOT_URLCONF = 'website.urls'
AUTH_USER_MODEL = 'user.User'
# django_simple_captcha 验证码配置
# 格式
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(hidden_field)s %(image)s'
# 噪点样式
CAPTCHA_NOISE_FUNCTIONS = (
    #'captcha.helpers.noise_null',  # 没有样式
                           'captcha.helpers.noise_arcs', # 线
                           'captcha.helpers.noise_dots', # 点
                           )
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 25)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 图片中的文字为随机英文字母，如 mdsh
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'    # 图片中的文字为数字表达式，如1+2=</span>

CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
        # 'default': {
        #         'ENGINE': 'django.db.backends.sqlite3',
        #         'NAME':os.path.join(BASE_DIR,'db.sqlite3')
        # }
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':conf.get('Mysql','NAME'),
        "HOST":conf.get('Mysql','HOST'),
        "POST":conf.get('Mysql','POST'),
        "USER":conf.get('Mysql','USER'),
        "PASSWORD":conf.get('Mysql','PASSWORD'),
         'OPTIONS': {
                    'init_command': 'SET default_storage_engine=INNODB',
                },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}
#drf
REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 4,
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     #'rest_framework.authentication.TokenAuthentication',#全局配置token
    # )
}


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATIC_ROOT 配置部署的时候才用

MEDIA_URL = "/upload/"   # 媒体文件别名(相对路径) 和 绝对路径
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'upload')
)


DOMAIN = 'https://www.fengjinqi.com'#用户验证邮箱访问地址
EMAIL_HOST = "smtp.exmail.qq.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = 'fengjinqi@fengjinqi.com'
EMAIL_WEBITE_NAME = '晓晓'
EMAIL_HOST_PASSWORD = conf.get('email','password')
EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用

EMAIL_USE_TLS = False   #是否使用TLS安全传输协议

ERROR_FROM = 'tarena_feng@126.com'

#搜索
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.article.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'




import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/6'
CELERY_IMPORTS = ('apps.article.tasks', )
CELERY_TIMEZONE = TIME_ZONE
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERYD_MAX_TASKS_PER_CHILD = 5
CELERY_ENABLE_UTC = True



#CELERY_ENABLE_UTC=True
# 下面是定时任务的设置，我一共配置了三个定时任务.
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    u'每小时获取数据': {
        "task": "apps.article.tasks.getApi",
        #"schedule": crontab(minute='*/3',),
        "schedule": crontab(0,'*','*','*','*'),
        "args": (),
    },
    u'每周一进行数据库清理': {
        'task': 'apps.article.tasks.removeApi',
        'schedule': crontab(hour='*/9', minute='*/50', day_of_week='*/5'),
        "args": ()
    },
}

# SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 引擎
# SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
#
# SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
# SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径
# SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名
# SESSION_COOKIE_SECURE = False  # 是否Https传输cookie
# #SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 1800  # Session的cookie失效日期（2周）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = True  # 是否每次请求都保存Session，默认修改之后才保存
