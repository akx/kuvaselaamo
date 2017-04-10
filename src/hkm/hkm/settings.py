
# -*- coding: utf-8 -*-

from django.conf import settings

SAUCELABS_USERNAME = getattr(settings, 'SAUCELABS_USERNAME', '')
SAUCELABS_ACCESS_KEY = getattr(settings, 'SAUCELABS_ACCESS_KEY', '')

DEFAULT_LANGUAGE = settings.LANGUAGE_CODE

MY_DOMAIN = settings.HKM_MY_DOMAIN

CROPPED_IMAGES_DOWNLOAD_PATH = settings.HKM_CROPPED_IMAGES_DOWNLOAD_PATH

FEEDBACK_NOTIFICATION_EMAILS = settings.HKM_FEEDBACK_NOTIFICATION_EMAILS
FEEDBACK_FROM_EMAIL = settings.HKM_FEEDBACK_FROM_EMAIL

MY_DOMAIN = settings.HKM_MY_DOMAIN

#Paybyway
PBW_API_KEY = settings.HKM_PBW_API_KEY
PBW_SECRET_KEY = settings.HKM_PBW_SECRET_KEY

#Printmotor
PRINTMOTOR_USERNAME = settings.HKM_PRINTMOTOR_USERNAME
PRINTMOTOR_PASSWORD = settings.HKM_PRINTMOTOR_PASSWORD
PRINTMOTOR_API_KEY = settings.HKM_PRINTMOTOR_API_KEY

PRINTMOTOR_PRODUCT_NAMES = {
  '50 x 70 cm': 'api-poster-50x70',
  '70 x 50 cm': 'api-poster-70x50',
  'A4 Vaaka': 'api-poster-a4',
  'A4 Pysty': 'api-poster-a4',
}

# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2

