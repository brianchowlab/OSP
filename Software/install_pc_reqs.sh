#!/bin/bash
#conda update conda
conda create -n osp python=2.7 anaconda -y
conda install -n osp pyqt=4 -y
conda install -n osp -c anaconda numpy -y
conda install -n osp -c poehlmann python-seabreeze -y
conda install -n osp -c anaconda pyserial -y
conda install -n osp -c anaconda xlsxwriter -y
conda install -n osp -c conda-forge matplotlib -y
conda install -n osp -c anaconda git -y

