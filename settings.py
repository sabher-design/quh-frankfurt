from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1,
    participation_fee=6.00, # in Euro
    doc=""
)

SESSION_CONFIGS = [
    dict(
        name='ttc_test_no_apps',
        display_name="ttc_test_no_apps",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'part_II_survey_ttc1']
    ),
    dict(
        name='da_test_no_apps',
        display_name="da_test_no_apps",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'part_II_survey_da1']
    ),
    dict(
        name='ttc_sequence_test',
        display_name="ttc_sequence_test",
        num_demo_participants=4,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc3', 'part_II_survey_ttc', 'payment_sequence1_ttc']
    ),
    dict(
        name='da_sequence_test',
        display_name="da_sequence_test",
        num_demo_participants=4,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda3', 'part_II_survey_da', 'payment_sequence1_da']
    ),
# app_sequence1 app_sequence=['SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17'
# 'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8']
# payoff round: 11 --> SHttc3
    dict(
        name='ttc_sequence1',
        display_name="ttc_sequence1",
        num_demo_participants=12,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9',
                      'SHttc5', 'SHttc13', 'SHttc17', 'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16',
                      'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8','part_II_survey_ttc', 'payment_sequence1_ttc']
    ),
    dict(
        name='da_sequence1',
        display_name="da_sequence1",
        num_demo_participants=12,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda11', 'SHda7', 'SHda1', 'SHda12', 'SHda19', 'SHda14', 'SHda9',
                      'SHda5', 'SHda13', 'SHda17',
                      'SHda3', 'SHda15', 'SHda20', 'SHda4', 'SHda10', 'SHda16', 'SHda18', 'SHda6', 'SHda2', 'SHda8',
                      'part_II_survey_da', 'payment_sequence1_da']
    ),
    dict(
        name='ttc_adv_sequence1',
        display_name="ttc_adv_sequence1",
        num_demo_participants=12,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc11_adv', 'SHttc7_adv', 'SHttc1_adv', 'SHttc12_adv',
                      'SHttc19_adv', 'SHttc14_adv', 'SHttc9_adv', 'SHttc5_adv', 'SHttc13_adv', 'SHttc17_adv',
                      'SHttc3_adv', 'SHttc15_adv', 'SHttc20_adv', 'SHttc4_adv', 'SHttc10_adv', 'SHttc16_adv', 'SHttc18_adv',
                      'SHttc6_adv', 'SHttc2_adv', 'SHttc8_adv', 'part_II_survey_ttc_adv', 'payment_sequence1_ttc_adv']
    ),
    dict(
        name='da_adv_sequence1',
        display_name="da_adv_sequence1",
        num_demo_participants=12,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda11_adv', 'SHda7_adv', 'SHda1_adv', 'SHda12_adv', 'SHda19_adv',
        'SHda14_adv', 'SHda9_adv', 'SHda5_adv', 'SHda13_adv', 'SHda17_adv', 'SHda3_adv', 'SHda15_adv', 'SHda20_adv',
        'SHda4_adv', 'SHda10_adv', 'SHda16_adv', 'SHda18_adv', 'SHda6_adv', 'SHda2_adv', 'SHda8_adv', 'part_II_survey_da_adv',
        'payment_sequence1_da_adv']
    ),
# app_sequence2 app_sequence=['SHttc7', 'SHttc12', 'SHttc19', 'SHttc15', 'SHttc9', 'SHttc5', 'SHttc4', 'SHttc6', 'SHttc20', 'SHttc16'
# 'SHttc11', 'SHttc1', 'SHttc17', 'SHttc13', 'SHttc2', 'SHttc3', 'SHttc14', 'SHttc8', 'SHttc10', 'SHttc18']
# payoff round: 11 --> SHttc11
    dict(
        name='ttc_sequence2',
        display_name="ttc_sequence2",
        num_demo_participants=16,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc7', 'SHttc12', 'SHttc19', 'SHttc15', 'SHttc9', 'SHttc5',
        'SHttc4', 'SHttc6', 'SHttc20', 'SHttc16', 'SHttc11', 'SHttc1', 'SHttc17', 'SHttc13', 'SHttc2', 'SHttc3', 'SHttc14',
        'SHttc8', 'SHttc10', 'SHttc18', 'part_II_survey_ttc']
    ),
    dict(
        name='da_sequence2',
        display_name="da_sequence2",
        num_demo_participants=12,
        expShortName='',
        expId='',
        sessId='',
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda7', 'SHda12', 'SHda19', 'SHda15', 'SHda9', 'SHda5', 'SHda4',
        'SHda6', 'SHda20', 'SHda16', 'SHda11', 'SHda1', 'SHda17', 'SHda13', 'SHda2', 'SHda3', 'SHda14', 'SHda8',
        'SHda10', 'SHda18', 'part_II_survey_da', 'payment_sequence2_da']
    ),
    dict(
        name='ttc_adv_sequence2',
        display_name="ttc_adv_sequence2",
        num_demo_participants=16,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc7_adv', 'SHttc12_adv', 'SHttc19_adv', 'SHttc15_adv',
        'SHttc9_adv', 'SHttc5_adv', 'SHttc4_adv', 'SHttc6_adv', 'SHttc20_adv', 'SHttc16_adv', 'SHttc11_adv', 'SHttc1_adv',
        'SHttc17_adv', 'SHttc13_adv', 'SHttc2_adv', 'SHttc3_adv', 'SHttc14_adv', 'SHttc8_adv', 'SHttc10_adv',
        'SHttc18_adv', 'part_II_survey_ttc']
    ),
    dict(
        name='da_adv_sequence2',
        display_name="da_adv_sequence2",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda7_adv', 'SHda12_adv', 'SHda19_adv', 'SHda15_adv', 'SHda9_adv',
        'SHda5_adv', 'SHda4_adv', 'SHda6_adv', 'SHda20_adv', 'SHda16_adv', 'SHda11_adv', 'SHda1_adv', 'SHda17_adv',
        'SHda13_adv', 'SHda2_adv', 'SHda3_adv', 'SHda14_adv', 'SHda8_adv', 'SHda10_adv', 'SHda18_adv', 'part_II_survey_da']
    ),
# app_sequence3 app_sequence=['SHttc20', 'SHttc9', 'SHttc7', 'SHttc16', 'SHttc13', 'SHttc3', 'SHttc4', 'SHttc5', 'SHttc12', 'SHttc15'
# 'SHttc18', 'SHttc10', 'SHttc11', 'SHttc19', 'SHttc14', 'SHttc2', 'SHttc8', 'SHttc17', 'SHttc1', 'SHttc6']
# payoff round: 11 --> SHttc18
    dict(
        name='ttc_sequence3',
        display_name="ttc_sequence3",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc20', 'SHttc9', 'SHttc7', 'SHttc16', 'SHttc13', 'SHttc3',
        'SHttc4', 'SHttc5', 'SHttc12', 'SHttc15', 'SHttc18', 'SHttc10', 'SHttc11', 'SHttc19', 'SHttc14', 'SHttc2', 'SHttc8',
        'SHttc17', 'SHttc1', 'SHttc6', 'part_II_survey_ttc']
    ),
    dict(
        name='da_sequence3',
        display_name="da_sequence3",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda20', 'SHda9', 'SHda7', 'SHda16', 'SHda13', 'SHda3', 'SHda4',
        'SHda5', 'SHda12', 'SHda15', 'SHda18', 'SHda10', 'SHda11', 'SHda19', 'SHda14', 'SHda2', 'SHda8', 'SHda17', 'SHda1',
        'SHda6', 'part_II_survey_da']
    ),
    dict(
        name='ttc_adv_sequence3',
        display_name="ttc_adv_sequence3",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc20_adv', 'SHttc9_adv', 'SHttc7_adv', 'SHttc16_adv',
        'SHttc13_adv', 'SHttc3_adv', 'SHttc4_adv', 'SHttc5_adv', 'SHttc12_adv', 'SHttc15_adv', 'SHttc18_adv', 'SHttc10_adv',
        'SHttc11_adv', 'SHttc19_adv', 'SHttc14_adv', 'SHttc2_adv', 'SHttc8_adv', 'SHttc17_adv', 'SHttc1_adv', 'SHttc6_adv',
        'part_II_survey_ttc']
    ),
    dict(
        name='da_adv_sequence3',
        display_name="da_adv_sequence3",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda20_adv', 'SHda9_adv', 'SHda7_adv', 'SHda16_adv', 'SHda13_adv',
        'SHda3_adv', 'SHda4_adv', 'SHda5_adv', 'SHda12_adv', 'SHda15_adv', 'SHda18_adv', 'SHda10_adv', 'SHda11_adv',
        'SHda19_adv', 'SHda14_adv', 'SHda2_adv', 'SHda8_adv', 'SHda17_adv', 'SHda1_adv', 'SHda6_adv', 'part_II_survey_da']
    ),
# app_sequence4 app_sequence=['SHttc5', 'SHttc2', 'SHttc8', 'SHttc1', 'SHttc19', 'SHttc11', 'SHttc16', 'SHttc12', 'SHttc10', 'SHttc14'
# 'SHttc9', 'SHttc18', 'SHttc7', 'SHttc13', 'SHttc15', 'SHttc20', 'SHttc3', 'SHttc4', 'SHttc6', 'SHttc17']
# payoff round: 11 --> SHttc9
    dict(
        name='ttc_sequence4',
        display_name="ttc_sequence4",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc5', 'SHttc2', 'SHttc8', 'SHttc1', 'SHttc19', 'SHttc11',
        'SHttc16', 'SHttc12', 'SHttc10', 'SHttc14', 'SHttc9', 'SHttc18', 'SHttc7', 'SHttc13', 'SHttc15', 'SHttc20',
        'SHttc3', 'SHttc4', 'SHttc6', 'SHttc17', 'part_II_survey_ttc']
    ),
    dict(
        name='da_sequence4',
        display_name="da_sequence4",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda5', 'SHda2', 'SHda8', 'SHda1', 'SHda19', 'SHda11', 'SHda16',
        'SHda12', 'SHda10', 'SHda14', 'SHda9', 'SHda18', 'SHda7', 'SHda13', 'SHda15', 'SHda20', 'SHda3', 'SHda4', 'SHda6',
        'SHda17', 'part_II_survey_da']
    ),
    dict(
        name='ttc_adv_sequence4',
        display_name="ttc_adv_sequence4",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc5_adv', 'SHttc2_adv', 'SHttc8_adv', 'SHttc1_adv', 'SHttc19_adv',
        'SHttc11_adv', 'SHttc16_adv', 'SHttc12_adv', 'SHttc10_adv', 'SHttc14_adv', 'SHttc9_adv', 'SHttc18_adv', 'SHttc7_adv',
        'SHttc13_adv', 'SHttc15_adv', 'SHttc20_adv', 'SHttc3_adv', 'SHttc4_adv', 'SHttc6_adv', 'SHttc17_adv', 'part_II_survey_ttc']
    ),
    dict(
        name='da_adv_sequence4',
        display_name="da_adv_sequence4",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda5_adv', 'SHda2_adv', 'SHda8_adv', 'SHda1_adv', 'SHda19_adv',
        'SHda11_adv', 'SHda16_adv', 'SHda12_adv', 'SHda10_adv', 'SHda14_adv', 'SHda9_adv', 'SHda18_adv', 'SHda7_adv',
        'SHda13_adv', 'SHda15_adv', 'SHda20_adv', 'SHda3_adv', 'SHda4_adv', 'SHda6_adv', 'SHda17_adv', 'part_II_survey_da']
    ),
# app_sequence5 app_sequence=['SHttc6', 'SHttc1', 'SHttc9', 'SHttc10', 'SHttc13', 'SHttc3', 'SHttc20', 'SHttc4', 'SHttc11', 'SHttc12'
# 'SHttc8', 'SHttc2', 'SHttc17', 'SHttc7', 'SHttc15', 'SHttc14', 'SHttc19', 'SHttc16', 'SHttc18', 'SHttc5']
# payoff round: 11 --> SHttc8
    dict(
        name='ttc_sequence5',
        display_name="ttc_sequence5",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc6', 'SHttc1', 'SHttc9', 'SHttc10', 'SHttc13', 'SHttc3',
        'SHttc20', 'SHttc4', 'SHttc11', 'SHttc12', 'SHttc8', 'SHttc2', 'SHttc17', 'SHttc7', 'SHttc15', 'SHttc14',
        'SHttc19', 'SHttc16', 'SHttc18', 'SHttc5', 'part_II_survey_ttc']
    ),
    dict(
        name='da_sequence5',
        display_name="da_sequence5",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda6', 'SHda1', 'SHda9', 'SHda10', 'SHda13', 'SHda3', 'SHda20',
        'SHda4', 'SHda11', 'SHda12', 'SHda8', 'SHda2', 'SHda17', 'SHda7', 'SHda15', 'SHda14', 'SHda19', 'SHda16',
        'SHda18', 'SHda5', 'part_II_survey_da']
    ),
    dict(
        name='ttc_adv_sequence5',
        display_name="ttc_adv_sequence5",
        num_demo_participants=12,
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc6_adv', 'SHttc1_adv', 'SHttc9_adv', 'SHttc10_adv',
        'SHttc13_adv', 'SHttc3_adv', 'SHttc20_adv', 'SHttc4_adv', 'SHttc11_adv', 'SHttc12_adv', 'SHttc8_adv', 'SHttc2_adv',
        'SHttc17_adv', 'SHttc7_adv', 'SHttc15_adv', 'SHttc14_adv', 'SHttc19_adv', 'SHttc16_adv', 'SHttc18_adv', 'SHttc5_adv',
        'part_II_survey_ttc']
    ),
    dict(
        name='da_adv_sequence5',
        display_name="da_adv_sequence5",
        num_demo_participants=12,
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda6_adv', 'SHda1_adv', 'SHda9_adv', 'SHda10_adv', 'SHda13_adv',
        'SHda3_adv', 'SHda20_adv', 'SHda4_adv', 'SHda11_adv', 'SHda12_adv', 'SHda8_adv', 'SHda2_adv', 'SHda17_adv',
        'SHda7_adv', 'SHda15_adv', 'SHda14_adv', 'SHda19_adv', 'SHda16_adv', 'SHda18_adv', 'SHda5_adv', 'part_II_survey_da']
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
POINTS_CUSTOM_NAME = 'ECU'
USE_POINTS = True
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2

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
