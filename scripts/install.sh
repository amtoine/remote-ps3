#!/usr/bin/env bash

source config/install.sh
source scripts/colors.sh

if [ ! -d "$venv" ]; then
  echo "${cyan}$venv${end} is ${red}not installed${end}..."
  echo "${yellow}installing ${cyan}$venv${end}..."
  virtualenv "$venv"
  source "$venv/bin/activate"
  pip install -r requirements.txt
  pip install .
  echo "installation of ${cyan}$venv${end} is ${green}successful${end}!"
else
  echo "${cyan}$venv${end}is ${yellow}already installed${end}!"
fi

cat << EOF > "$exe"
#!/usr/bin/env bash
source $venv/bin/activate
python $lib/run --config $lib/config.json
EOF

chmod +x "$exe"
cp "$exe" "$bin" --verbose

if [ ! -d "$build" ]; then
  mkdir "$build"
fi
mv "$exe" "$build" --verbose

if [ ! -d "$lib" ]; then
  mkdir "$lib"
fi
cp scripts/run.py "$lib/run" --verbose
cp config/remote.json "$lib/config.json" --verbose
