output "aws_instance_public_ips" {
  value = [for instance in aws_instance.Server : instance.public_ip] # ใช้ for loop เพื่อดึง Public IP ของ Instances
}

output "lb_dns_name" {
  value = aws_lb.elb-webLB.dns_name
}
