# log_config.py

import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义一个全局的 logger 对象
logger = logging.getLogger(__name__)

