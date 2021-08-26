sudo sysctl -w vm.max_map_count=262144
file=".env"
if [ -f "$file" ] ; then
    rm "$file"
fi
python -m pip install -r ./requirements.txt
rm ./instances.yml
cp ./inst_test.yml ./instances.yml
cp .env.example .env
cd init
python initialise.py 
cd ..
sed -i '$d' .env
sed -i '$d' .env
value=$(<./init/login.txt)
echo "$value" | tee -a .env
docker-compose down
docker-compose up -d
rm ./init/login.txt
rm ./init/temp.txt