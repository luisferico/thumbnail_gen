output "alb_hostname" {
  value = aws_alb.thumbnail.dns_name
}

output "streamlit-link" {
  value = "http://${aws_instance.streamlit-server.public_ip}"
}