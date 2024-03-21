resource "aws_instance" "streamlit-server" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.ec2.id]
  subnet_id              = element(aws_subnet.public.*.id, 1)

  root_block_device {
    volume_size = 20
  }
#  connection {
#    type        = "ssh"
#    user        = "ubuntu"  # Replace with the appropriate username for your EC2 instance
#    private_key = file("~/.ssh/id_rsa")  # Replace with the path to your private key
#    host        = self.public_ip
#   }

#   provisioner "remote-exec" {
#    inline = [
#      "echo 'Hello from the remote instance'",
#      "sudo apt update -y",  # Update package lists (for ubuntu)
#      "sudo apt-get install -y python3-pip",  # Example package installation
#      "cd /home/ubuntu",
#      "git clone https://github.com/luisferico/thumbnail_gen.git",
#      "cd thumbnail_gen/streamlit_app",
#      "sudo pip3 install -r requirements.txt",
#      "sudo nohup streamlit run main.py & disown"
#    ]
#   }
  }