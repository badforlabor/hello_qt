### 环境

1. 安装poetry，并设置：
   1. poetry config virtualenvs.in-project true
2. 每个项目，用poetry管理，第一次，需要初始化：
   1. poetry install --no-root
3. 用pycharm打开项目，即可。
4. 如果想直接运行某个python：
   1. 打开控制台
   2. poetry shell
   3. python xxx.py