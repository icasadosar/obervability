# output "spaces" {
#   value = { for k, v in digitalocean_spaces_bucket.tf_state : k => v }
# }

# output "k8s" {
#   value     = { for k, v in digitalocean_kubernetes_cluster.workshop : k => v }

#   sensitive = true
# }

output "registry" {
  value = digitalocean_container_registry.obs
}