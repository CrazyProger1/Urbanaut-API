variable "vault_address" {
  description = "Vault server address"
  default     = "http://127.0.0.1:8200"
}

variable "vault_token" {
  description = "Vault root token (dev mode)"
  sensitive   = true
}

variable "secret_key" {
  description = "Django SECRET_KEY"
  sensitive   = true
}

variable "otp_secret_key" {
  description = "Django OTP_SECRET_KEY"
  sensitive   = true
  default     = ""
}

variable "django_superuser_username" {
  description = "Django superuser username"
  default     = "admin"
}

variable "django_superuser_email" {
  description = "Django superuser email"
  default     = ""
}

variable "django_superuser_password" {
  description = "Django superuser password"
  sensitive   = true
}

variable "db_name" {
  description = "PostgreSQL database name"
  default     = "urbanautdb"
}

variable "db_user" {
  description = "PostgreSQL user"
  default     = "urbanaut"
}

variable "db_password" {
  description = "PostgreSQL password"
  sensitive   = true
}

variable "google_oauth_client_id" {
  description = "Google OAuth client ID"
  sensitive   = true
  default     = ""
}

variable "google_oauth_client_secret" {
  description = "Google OAuth client secret"
  sensitive   = true
  default     = ""
}

variable "google_gemini_api_key" {
  description = "Google Gemini API key"
  sensitive   = true
  default     = ""
}

variable "google_email_host_user" {
  description = "Google email host user"
  default     = ""
}

variable "google_email_host_password" {
  description = "Google email host password"
  sensitive   = true
  default     = ""
}

variable "telegram_bot_token" {
  description = "Telegram bot token"
  sensitive   = true
  default     = ""
}

variable "onesignal_app_id" {
  description = "OneSignal app ID"
  default     = ""
}

variable "onesignal_api_key" {
  description = "OneSignal API key"
  sensitive   = true
  default     = ""
}