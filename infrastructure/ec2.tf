resource "aws_key_pair" "example" {
  key_name   = var.key_name
  public_key = file("~/.ssh/id_rsa.pub")
}


resource "aws_instance" "streamlit-server" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.lb.id]
  subnet_id              = aws_subnet.public.id

  connection {
    type        = "ssh"
    user        = "ubuntu"  # Replace with the appropriate username for your EC2 instance
    private_key = file("~/.ssh/id_rsa")  # Replace with the path to your private key
    host        = self.public_ip
   }

   provisioner "remote-exec" {
    inline = [
      "echo 'Hello from the remote instance'",
      "sudo apt update -y",  # Update package lists (for ubuntu)
      "sudo apt-get install -y python3-pip",  # Example package installation
      "cd /home/ubuntu",
      "git clone https://github.com/luisferico/thumbnail_gen.git",
      "cd streamlit_app",
      "sudo pip3 install -r requirements.txt",
      "sudo nohup streamlit run app.py & disown",
    ]
   }
  }