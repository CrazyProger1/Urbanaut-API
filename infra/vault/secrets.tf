resource "vault_mount" "kv" {
  path = "secret"
  type = "kv-v2"
}

resource "vault_kv_secret_v2" "urbanaut" {
  mount = vault_mount.kv.path
  name  = "urbanaut"

  data_json = jsonencode({
    SECRET_KEY                 = var.secret_key
    OTP_SECRET_KEY             = var.otp_secret_key
    DEBUG                      = "False"
    DJANGO_SETTINGS_MODULE     = "src.config.settings"
    LOG_LEVEL                  = "INFO"
    TIME_ZONE                  = "Europe/Kyiv"

    BASE_URL                   = "https://api.urbanaut.club"
    BASE_FRONTEND_URL          = "https://urbanaut.club"
    ALLOWED_HOSTS              = "api.urbanaut.club"
    CORS_ALLOWED_ORIGINS       = "https://urbanaut.club"
    CORS_ALLOW_ALL_ORIGINS     = "False"
    CSRF_TRUSTED_ORIGINS       = "https://api.urbanaut.club"

    CREATE_SUPERUSER           = "false"
    DJANGO_SUPERUSER_USERNAME  = var.django_superuser_username
    DJANGO_SUPERUSER_EMAIL     = var.django_superuser_email
    DJANGO_SUPERUSER_PASSWORD  = var.django_superuser_password

    DB_ENGINE                  = "django.contrib.gis.db.backends.postgis"
    DB_HOST                    = "postgres.urbanaut.svc.cluster.local"
    DB_PORT                    = "5432"
    DB_NAME                    = var.db_name
    DB_USER                    = var.db_user
    DB_PASSWORD                = var.db_password
    POSTGRES_DB                = var.db_name
    POSTGRES_USER              = var.db_user
    POSTGRES_PASSWORD          = var.db_password

    REDIS_HOST                 = "redis.urbanaut.svc.cluster.local"
    REDIS_PORT                 = "6379"

    ELASTICSEARCH_HOST         = "elasticsearch.urbanaut.svc.cluster.local"
    ELASTICSEARCH_PORT         = "9200"

    GOOGLE_OAUTH_CLIENT_ID     = var.google_oauth_client_id
    GOOGLE_OAUTH_CLIENT_SECRET = var.google_oauth_client_secret
    GOOGLE_GEMINI_API_KEY      = var.google_gemini_api_key
    GOOGLE_EMAIL_HOST_USER     = var.google_email_host_user
    GOOGLE_EMAIL_HOST_PASSWORD = var.google_email_host_password

    TELEGRAM_BOT_TOKEN         = var.telegram_bot_token
    ONESIGNAL_APP_ID           = var.onesignal_app_id
    ONESIGNAL_API_KEY          = var.onesignal_api_key
  })
}