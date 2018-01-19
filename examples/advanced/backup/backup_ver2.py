import os
import time

# 1. 需要备份的文件与目录将被指定在一个列表中。
# Mac OS X 与 Linux 下：
source = ['/Users/support/Documents/projectRes/documents/notes']
# 注意：必须在字符串中使用双引号用以括起其中包含空格的名称。

# 2. 备份文件必须存储在一个主备份目录中
# Mac OS X 与 Linux 下：
target_dir = '/Users/support/Documents/projectRes/documents/backup'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    # 创建目录

# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的子目录名称。
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前事件作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名称格式
target = today + os.sep + now + '.zip'

# 如果子目录尚不存在，则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. 使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

"""
较 backup_ver1 改进的点：
    通过 os.path.exists 函数来检查主文件目录中是否已经存在了以当前日期作为名称的子目录。
    如果尚未存在，我们通过 os.mkdir 函数来创建一个。
"""