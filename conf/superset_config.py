SECRET_KEY = "__SECRET_KEY__"
SQLALCHEMY_DATABASE_URI = "postgresql://__DB_USER__:__DB_PWD__@127.0.0.1/__DB_NAME__"

AUTH_TYPE = 2
AUTH_LDAP_SERVER = "ldap://127.0.0.1:389/"
AUTH_LDAP_USE_TLS = False

AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"
AUTH_LDAP_EMAIL_FIELD = "mail"

AUTH_LDAP_USERNAME_FORMAT = "uid=%s,ou=users,dc=yunohost,dc=org"
AUTH_LDAP_SEARCH = "ou=users,dc=yunohost,dc=org"
AUTH_LDAP_UID_FIELD = "uid"

AUTH_LDAP_GROUP_FIELD = "permission"
AUTH_ROLES_MAPPING = {
    "cn=__APP__.main,ou=permission,dc=yunohost,dc=org": ["Public"],
    "cn=__APP__.alpha,ou=permission,dc=yunohost,dc=org": ["Alpha"],
    "cn=__APP__.gamma,ou=permission,dc=yunohost,dc=org": ["Gamma"],
    "cn=__APP__.admin,ou=permission,dc=yunohost,dc=org": ["Admin"],
}
AUTH_ROLES_SYNC_AT_LOGIN = True

ENABLE_PROXY_FIX = True

DEFAULT_FEATURE_FLAGS = {
    "DASHBOARD_RBAC": True,
    "EMBEDDABLE_CHARTS": True,
}

ENABLE_CORS = True

HTTP_HEADERS = {}

TALISMAN_ENABLED = True

TALISMAN_CONFIG = {
    "content_security_policy": {
        "base-uri": ["'self'"],
        "default-src": ["'self'"],
        "img-src": [
            "'self'",
            "blob:",
            "data:",
            "https://apachesuperset.gateway.scarf.sh",
            "https://static.scarf.sh/",
        ],
        "worker-src": ["'self'", "blob:"],
        "connect-src": [
            "'self'",
            "https://api.mapbox.com",
            "https://events.mapbox.com",
        ],
        "object-src": "'none'",
        "style-src": [
            "'self'",
            "'unsafe-inline'",
        ],
        "script-src": ["'self'", "'strict-dynamic'"],
        "frame-ancestors": [
            "*.dataactivists.org",
            "localhost",
            "127.0.0.1",
        ],
    },
    "content_security_policy_nonce_in": ["script-src"],
    "force_https": False,
    "session_cookie_secure": False,
}
