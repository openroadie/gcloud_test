gcloud beta compute --project=theopenroadproject instances create instance-2 --zone=us-west2-a --machine-type=c2-standard-16 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=637566993925-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --image=image-from-instance-1-ssh-working --image-project=theopenroadproject --boot-disk-size=10GB --boot-disk-type=pd-ssd --boot-disk-device-name=instance-2 --reservation-affinity=any