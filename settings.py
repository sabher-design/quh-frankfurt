from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1/140,
    participation_fee=6.00, # in Euro
    doc=""
)

SESSION_CONFIGS = [
    # Algo Outsourcing
    dict(
        name='SH_ttc_labtest',
        display_name="SH_t",
        num_demo_participants=12,
        # app sequence session 1:
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17',
        'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8', 'part_II_survey_da']
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
POINTS_CUSTOM_NAME = 'Taler'
USE_POINTS = True
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2


environ['DATABASE_URL'] = 'postgresql://postgres:asdf@localhost/postgres'
DATABASE_URL = environ.get('DATABASE_URL')
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '4e0cd9nd3+-lh=zu1l^vota306m8%2l+#r7vdaph*11nuih33^'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
