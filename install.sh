#!/usr/bin/env bash

source config.sh

if [ ! -d "$venv" ]; then
  echo "not installed..."
  echo "installing..."
  virtualenv "$venv"
  source "$venv/bin/activate"
  pip install -r requirements.txt
  echo "installation done!"
else
  echo "already installed!"
fi

path=$(pwd)

cat << EOF > "$exe"
#!/usr/bin/env bash
source $venv/bin/activate
python $path/remote.py --config $path/remote.json
EOF

chmod +x "$exe"
cp "$exe" "$bin"
