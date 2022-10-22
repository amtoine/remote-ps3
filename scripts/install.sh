#!/usr/bin/env bash

source config/install.sh

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
python $path/scripts/remote.py --config $path/config/remote.json
EOF

chmod +x "$exe"
cp "$exe" "$bin" --verbose
if [ ! -d build ]; then
  mkdir build
fi
mv "$exe" build --verbose
