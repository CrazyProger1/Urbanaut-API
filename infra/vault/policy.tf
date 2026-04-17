resource "vault_policy" "urbanaut_read" {
  name = "urbanaut-read"

  policy = <<EOT
path "secret/data/urbanaut" {
  capabilities = ["read"]
}
EOT
}

resource "vault_auth_backend" "kubernetes" {
  type = "kubernetes"
}

resource "vault_kubernetes_auth_backend_config" "config" {
  backend            = vault_auth_backend.kubernetes.path
  kubernetes_host    = "https://kubernetes.default.svc"
}

resource "vault_kubernetes_auth_backend_role" "urbanaut" {
  backend                          = vault_auth_backend.kubernetes.path
  role_name                        = "urbanaut"
  bound_service_account_names      = ["urbanaut"]
  bound_service_account_namespaces = ["urbanaut"]
  token_policies                   = [vault_policy.urbanaut_read.name]
  token_ttl                        = 3600
}