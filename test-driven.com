server {
	listen 80;
	server_name www.test-driven.com;

	location / {
		proxy_pass http://localhost:8000;
	}
}
