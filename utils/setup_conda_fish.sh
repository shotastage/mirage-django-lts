#!/usr/bin/env bash

function env_in
{
    mkdir ./tmp_inst
    cd ./tmp_inst
}

function env_out
{
    cd ..
    rm -rf ./tmp_inst
}

function setup
{
    curl -O https://raw.githubusercontent.com/conda/conda/master/conda/shell/etc/fish/conf.d/conda.fish

}

env_in
setup
