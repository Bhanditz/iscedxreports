from os import environ

from django.conf import settings

try:
    ENV_TOKENS = settings.ENV_TOKENS
    AUTH_TOKENS = settings.AUTH_TOKENS

    INTERSYSTEMS_REPORT_RECIPIENTS = ENV_TOKENS.get('INTERSYSTEMS_REPORT_RECIPIENTS', None)
    CMC_REPORT_RECIPIENTS = ENV_TOKENS.get('CMC_REPORT_RECIPIENTS', ('bryan@appsembler.com', ))
    VA_ENROLLMENT_REPORT_RECIPIENTS = ENV_TOKENS.get('VA_ENROLLMENT_REPORT_RECIPIENTS', ('bryan@appsembler.com', ))
    ISC_COURSE_PARTICIPATION_REPORT_RECIPIENTS = ENV_TOKENS.get('ISC_COURSE_PARTICIPATION_REPORT_RECIPIENTS', ('bryan@appsembler.com', ))
    ISC_COURSE_PARTICIPATION_BUCKET = ENV_TOKENS.get('ISC_COURSE_PARTICIPATION_BUCKET', None)
    ISC_COURSE_PARTICIPATION_S3_UPLOAD = ENV_TOKENS.get('ISC_COURSE_PARTICIPATION_S3_UPLOAD', False)
    ISC_COURSE_PARTICIPATION_STORE_LOCAL = ENV_TOKENS.get('ISC_COURSE_PARTICIPATION_STORE_LOCAL', False)
    ISC_COURSE_PARTICIPATION_LOCAL_STORAGE_DIR = ENV_TOKENS.get('ISC_COURSE_PARTICIPATION_LOCAL_STORAGE_DIR', '/tmp')
    ISC_S3_PATH_PREFIX = ENV_TOKENS.get('ISC_S3_PATH_PREFIX', '')
    CMC_COURSE_COMPLETION_BUCKET = ENV_TOKENS.get('CMC_COURSE_COMPLETION_BUCKET', None)
    CMC_COURSE_COMPLETION_S3_UPLOAD = ENV_TOKENS.get('CMC_COURSE_COMPLETION_S3_UPLOAD', False)
    CMC_COURSE_COMPLETION_STORE_LOCAL = ENV_TOKENS.get('CMC_COURSE_COMPLETION_STORE_LOCAL', False)
    CMC_COURSE_COMPLETION_LOCAL_STORAGE_DIR = ENV_TOKENS.get('CMC_COURSE_COMPLETION_LOCAL_STORAGE_DIR', '/tmp')
    CMC_S3_PATH_PREFIX = ENV_TOKENS.get('CMC_S3_PATH_PREFIX', '')

    AWS_ID = AUTH_TOKENS.get('AWS_ACCESS_KEY_ID', None)
    AWS_KEY = AUTH_TOKENS.get('AWS_SECRET_ACCESS_KEY', None)

except AttributeError:
    # these won't be available in test
    if environ.get('DJANGO_SETTINGS_MODULE') in (
            'lms.envs.acceptance', 'lms.envs.test',
            'cms.envs.acceptance', 'cms.envs.test'):
        pass
    else:
        raise
