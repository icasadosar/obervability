resource "digitalocean_container_registry" "obs" {
  name                   = "obs"
  subscription_tier_slug = "starter"
  region                 = var.region
}