import os
import subprocess
import argparse
# 定义要执行的bash命令
# Splitting the provided command string into individual commands
cm = """
mkdir videos/
ls
echo "okkk"
echo $PATH
mkdir /home/runner/work/m3u8/m3u8/videos
echo $PATH
wget https://github.com/nilaoda/N_m3u8DL-RE/releases/download/v0.2.1-beta/N_m3u8DL-RE_Beta_linux-x64_20240828.tar.gz
tar -xvf N_m3u8DL-RE_Beta_linux-x64_20240828.tar.gz
chmod 777 N_m3u8DL-RE_Beta_linux-x64/N_m3u8DL-RE
N_m3u8DL-RE_Beta_linux-x64/N_m3u8DL-RE "【中文口譯直播】2024亞洲新媒體高峰會_11／12.m3u8" --auto-select TRUE --save-dir videos/ --log-level OFF --thread-count 16
N_m3u8DL-RE_Beta_linux-x64/N_m3u8DL-RE "【原聲原影版】2024亞洲新媒體高峰會_11／12 (1).m3u8" --auto-select TRUE --save-dir videos/ --log-level OFF --thread-count 16
"""

# Splitting the string into a list of commands
commands = cm.strip().split('\n')

# 执行每个命令
for command in commands:
    os.system(command)

parser = argparse.ArgumentParser(description='Process some integers.')
# 添加 --token 参数
parser.add_argument('--token', type=str, help='The token to be used')

# 解析命令行参数
args = parser.parse_args()

# 获取命令行传入的 token 参数值
args_token = args.token


subprocess.run(f'huggingface-cli login --token={args_token}', 
               shell=True)

from huggingface_hub import HfApi
from huggingface_hub import list_repo_files

api = HfApi()
model_repo_name = "haibaraconan/video"  # Format of Input  <Profile Name > / <Model Repo Name> 

#Create Repo in Hugging Face
folder_path = "videos/"
#Upload Model folder from Local to HuggingFace 
api.upload_folder(
    folder_path=folder_path,
    repo_id=model_repo_name,
    repo_type="dataset"
)
