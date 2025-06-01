# portfolio commands eg.:

python manage.py collectstatic
sudo systemctl daemon-reload
sudo systemctl restart portfolio.service
sudo systemctl status portfolio.service

sudo nginx -t
sudo systemctl restart nginx
sudo systemctl status nginx

python manage.py makemigrations
python manage.py migrate

sudo journalctl -u portfolio.service -f

source venv/bin/activate
export DATABASE_URL=postgresql://postgres:Toure7Medina@localhost:5432/portfolio
python manage.py runserver 0.0.0.0:8007

# CONNECT POSTGRES
sudo -i -u postgres
sudo nano /var/lib/pgsql/data/postgresql.conf

# systemd
sudo nano /etc/systemd/system/portfolio.service

# nginx
sudo nano /etc/nginx/sites-available/portfolio.conf

# CREATE SSL CERTIFICATE
sudo dnf install certbot python-certbot-nginx
sudo certbot --nginx

# link the configuration to enable it
sudo ln -s /etc/nginx/sites-available/portfolio.conf /etc/nginx/sites-enabled/portfolio.conf

sudo certbot certificates
sudo certbot --nginx -d portfolio.siisi.online -d www.portfolio.siisi.online

sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

sudo systemctl enable certbot.timer
sudo certbot renew --dry-run

# kill all port runing
sudo lsof -t -iTCP:80085 -sTCP:LISTEN | xargs sudo kill

# Docker 
docker --version
<!-- Build an image from Dockerfile in current dir -->
docker build -t portfolio:latest .
<!-- List local images -->
docker images
<!-- List all containers (running + stopped) -->
docker ps -a
<!-- Create & start container in detached mode -->
docker run -d --name web -p 8000:8005 portfolio:latest
<!-- View logs from a container -->
docker logs web
<!-- Start an interactive shell inside a running container -->
docker exec -it web bash
<!--Gracefully stop a running container -->
docker stop web
# Start DB + Django runserver
# Rebuild static assets & restart
<!-- prod -->
docker compose -f docker-compose.prod.yml -p portfolio_prod run portfolio python manage.py collectstatic
docker-compose -f docker-compose.prod.yml -p portfolio_prod down --volumes --remove-orphans
docker system prune -a --volumes 
docker-compose -f docker-compose.prod.yml -p portfolio_prod down -v
docker-compose -f docker-compose.prod.yml -p portfolio_prod up -d --build
docker-compose -f docker-compose.prod.yml -p portfolio_prod ps
docker-compose -f docker-compose.prod.yml -p portfolio_prod down
docker-compose -f docker-compose.prod.yml -p portfolio_prod up -d --remove-orphans
docker-compose -f docker-compose.prod.yml -p portfolio_prod logs -f nginx
docker-compose -f docker-compose.prod.yml -p portfolio_prod logs -f

<!-- dev -->
docker compose -f docker-compose.dev.yml -p portfolio_dev run portfolio python manage.py collectstatic
docker-compose -f docker-compose.dev.yml down --volumes --remove-orphans
docker system prune -a --volumes 
docker-compose -f docker-compose.dev.yml -p portfolio_dev down -v
docker-compose -f docker-compose.dev.yml -p portfolio_dev up -d --build --remove-orphans
docker-compose -f docker-compose.dev.yml -p portfolio_dev ps
docker-compose -f docker-compose.dev.yml -p portfolio_dev down
docker-compose -f docker-compose.dev.yml -p portfolio_dev up -d
docker-compose -f docker-compose.dev.yml -p portfolio_dev logs -f nginx
docker-compose -f docker-compose.dev.yml -p portfolio_dev logs -f

# Apply migrations or create superuser
<!-- prod -->
docker exec -it portfolio_prod-portfolio-1 python manage.py makemigrations
docker exec -it portfolio_prod-portfolio-1 python manage.py migrate
docker exec -it portfolio_prod-portfolio-1 python manage.py createsuperuser
# Shell
docker exec -it portfolio_prod-portfolio-1 python manage.py shell
<!-- dev -->
docker exec -it portfolio_dev-portfolio-1 python manage.py makemigrations
docker exec -it portfolio_dev-portfolio-1 python manage.py migrate
docker exec -it portfolio_dev-portfolio-1 python manage.py createsuperuser
# Shell
docker exec -it portfolio_dev-portfolio-1 python manage.py shell
