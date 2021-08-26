sudo sysctl -w vm.max_map_count=262144
if ! command -v python3 &> /dev/null
then
    sudo apt-get update
    sudo apt-get install python3
    python3 -m pip install --upgrade pip
fi
python3 -m pip install -r ./requirements.txt
docker-compose down -v
file=".env"
if [ -f "$file" ] ; then
    rm "$file"
fi
cp .env.example .env
cd init
python3 initialise.py 
cd ..
sed -i '$d' .env
sed -i '$d' .env
value=$(<./init/login.txt)
echo "$value" | tee -a .env
docker-compose down
docker-compose up -d
rm ./init/login.txt
rm ./init/temp.txt
