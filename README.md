# Game "Breakout" for TRPP
Проект представляет собой реализацию классической аркадной игры Breakout на языке программирования Python с использованием библиотеки Pygame.

Для установки игры необходимо иметь Docker, и Х сервер

Для Windows:
https://sourceforge.net/projects/xming/
https://www.docker.com/products/docker-desktop/


После установки всего необходимого:

Запустить  Х-сервер (удостоверьтесь, что подключение доступно для всех клиентов)

Для установки игры необходимо открыть терминал в папке, где вы хотите хранить игру 

Ввести в терминал:
git clone https://github.com/iev-veta/game.git
cd game
docker build -t game .

Для запуска игры перейдите в папку game и выполните команду 
docker run game
