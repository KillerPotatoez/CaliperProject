#local_settings.py :
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'Caliper',                      
        'USER': 'postgres',                     
        'PASSWORD': 'Caliper',                  
        'HOST': 'localhost',                      
        'PORT': '',                      
    }
}