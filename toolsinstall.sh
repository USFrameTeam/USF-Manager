echo "本程序将在当前目录安装并配置USFM所需要的环境和工具"
echo "正在配置python虚拟环境，这将会安装python3.10-venv"

read -p "输入继续(Y/n):" data
if [[ $data == "n" || $data == "N" ]]; then
    echo "已取消安装"
    exit 0
fi

sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate

echo "正在下载工具minecraft-nbt-editor"
pip install click>=8.0.0 colorama>=0.4.4 rich>=12.0.0