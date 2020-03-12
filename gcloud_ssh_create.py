import subprocess
import sys
import array as arr
def create_instance:
    #gcloud compute --project "foss-fpga-tools-ext-openroad" disks create "instance-1" --size "64" --zone "us-west2-a" --source-snapshot "snapshot-2" --type "pd-ssd"

    #gcloud beta compute --project=foss-fpga-tools-ext-openroad instances create instance-1 --zone=us-west2-a --machine-type=c2-standard-8 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=281156998478-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --disk=name=instance-1,device-name=instance-1,mode=rw,boot=yes,auto-delete=yes --reservation-affinity=any
    #gcloud compute disks snapshot instance-1 --project=foss-fpga-tools-ext-openroad --snapshot-names=snapshot-4 --zone=us-west2-a --storage-location=us
    #gcloud instances delete
    #gcloud beta compute disks create disk-1 --project=foss-fpga-tools-ext-openroad --type=pd-standard --size=64GB --zone=us-west2-a --source-snapshot=snapshot-3 --physical-block-size=4096    
    #gcloud beta compute --project=foss-fpga-tools-ext-openroad instances create instance-1 --zone=us-west2-a --machine-type=c2-standard-8 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=281156998478-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --disk=name=disk-1,device-name=disk-1,mode=rw,boot=yes --reservation-affinity=any
    #gcloud compute instances delete instance-1 --delete-disks=all --quiet
def get_external_ip_from_list_return_value(retval):
    inst_data = retval[1].split()
    external_ip = inst_data[4]
    return external_ip

def run_command_print_stdout(command):
    p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p1.stdout.readlines()
    return result

def run_command_remotely_ssh(user, host, keyfile, command):
    user_host=user+"@"+host
    ssh = subprocess.Popen(["ssh", "-oStrictHostKeyChecking=no", "-i", keyfile, user_host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        return error
    return result

inst = "instance-1"
zone = "us-west2-a"
print run_command_print_stdout(["gcloud", "compute", "instances", "list"])
print run_command_print_stdout(["gcloud", "compute", "instances", "start", "--zone", zone, inst])
retval_started = run_command_print_stdout(["gcloud", "compute", "instances", "list"])
ip_add = get_external_ip_from_list_return_value(retval_started)
result = run_command_remotely_ssh("tspyrou", ip_add, "~/.ssh/gcloud", "uname -a")
print "remote result=", result
run_command_print_stdout(["gcloud", "compute", "instances", "stop", "--zone", zone, inst])
print run_command_print_stdout(["gcloud", "compute", "instances", "list"])

# should have done this with google cloud run - for ephemeral things.
# Google cloud build, docker images etc, has docker container registry, private containers too
# Make machines ephemeral. For example run jenkins server at UCSD but executors in the cloud.
# Make deleting and stopping machines the same. Only stop is you want to keep data on the machine.


