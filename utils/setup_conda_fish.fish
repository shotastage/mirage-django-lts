#!/usr/bin/env fish

function env_in
    mkdir ./tmp_inst
    cd ./tmp_inst
end

function env_out
    cd ..
    rm -rf ./tmp_inst
end

function setup
    curl -O https://raw.githubusercontent.com/conda/conda/master/conda/shell/etc/fish/conf.d/conda.fish
end

function install
    mv conda.fish (conda info --root)/etc/fish/conf.d/conda.fish
end

env_in
setup
install
echo "Please add this configuration to config.fish"
echo "source (conda info --root)/etc/fish/conf.d/conda.fish"
env_out
exit 0
