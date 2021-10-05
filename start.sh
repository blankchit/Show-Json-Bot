echo "Cloning Repo...."
git clone https://github.com/ZauteKm/Show-Json-Bot.git /Show-Json-Bot
cd /Show-Json-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
